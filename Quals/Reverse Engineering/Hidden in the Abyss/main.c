#include <stdio.h>
#include <unistd.h>
#include <string.h>

#include <dirent.h>
#include <dlfcn.h>
#include <fcntl.h>
#include <link.h>
#include <libgen.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/ptrace.h>
#include <openssl/md5.h>

#ifdef __LP64__
#define Elf_Ehdr Elf64_Ehdr
#define Elf_Shdr Elf64_Shdr
#define Elf_Sym  Elf64_Sym
#else
#define Elf_Ehdr Elf32_Ehdr
#define Elf_Shdr Elf32_Shdr
#define Elf_Sym  Elf32_Sym
#endif

const char *fake_flag = "FLAG: aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1DaV96YWQzOVVodyZsaXN0PVJEQ2lfemFkMzlVaHcmdD0xNXM=";

const char *flags[] = {
    "3d137ff4afbdf0b6afbfa059c81ece9b",
    "7521e341d48b08f214d1dac0738f16d0",
    "21017490f1e4e968f513520349816008",
    "c26841cc98f760f636f2c4d9d827e18c",
    "ad46789f9ffd7e66fe565d594802dcfc",
    "c26841cc98f760f636f2c4d9d827e18c",
    "c2212457b76a1819d17e3f2a976ff78a",
    "605446531ca5a2370658803cdf07b59f",
    "aaec1d22915a22823a4c3f7bc703c9d8",
    "ad46789f9ffd7e66fe565d594802dcfc",
    "e94656b6137dd01f26085f984afe853e",
    "23006ec47629c459550c9d9508b7a41b",
    "e64574a1d280db82707a389ccd89cbd5",
    "ad46789f9ffd7e66fe565d594802dcfc",
    "23006ec47629c459550c9d9508b7a41b",
    "69171c9442ce2032a1a52868f05f9d1c",
    "b94857f6a905ccd028329b0a8324ac4c",
    "da190e616797844b591057d0190e7728",
    "da190e616797844b591057d0190e7728",
    "3fab7a2f9df80382ef2ec5b4e78cbcce",
    "1a36313b7ed15ba14e0acb4da569b8b7",
    "23006ec47629c459550c9d9508b7a41b",
    "92ebcae27b5395a18af07a7e07265cf7",
    "7ecc92917e9c4556cc19f457ddc41af8",
    "e94656b6137dd01f26085f984afe853e",
    "3fab7a2f9df80382ef2ec5b4e78cbcce",
    "132cd3b981019b59dc42653eea0b34b4",
    "23006ec47629c459550c9d9508b7a41b",
    "c2212457b76a1819d17e3f2a976ff78a",
    "33b3102b6558811a7b7629a1e8e59bd2",
    "33b3102b6558811a7b7629a1e8e59bd2",
    "fc5940aadeacd5e9079c50e8dd481bbc"
};

const char *md5_str(const char *str) {
    static char buf[33];
    unsigned char digest[16];
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, str, strlen(str));
    MD5_Final(digest, &ctx);
    for (int i = 0; i < 16; i++) {
        sprintf(buf + i * 2, "%02x", digest[i]);
    }
    return buf;
}

const char *md5_data(uint8_t *data, size_t len) {
    static char buf[33];
    unsigned char digest[16];
    MD5_CTX ctx;
    MD5_Init(&ctx);
    MD5_Update(&ctx, data, len);
    MD5_Final(digest, &ctx);
    for (int i = 0; i < 16; i++) {
        sprintf(buf + i * 2, "%02x", digest[i]);
    }
    return buf;
}

const char *reverse_string(const char* str) {
    static char buf[100];
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        buf[i] = str[len - i - 1];
    }
    buf[len] = '\0';
    return buf;
}

__attribute__((section(".encrypted"))) int process_flag(const char *flag) {
    if (strlen(flag) != 32) {
        return 0;
    }

    for (int i = 0; i < 32; i++) {
        char c[2];
        c[0] = flag[i];
        c[1] = '\0';

        if (strcmp(reverse_string(md5_str(c)), flags[i]) != 0) {
            return 0;
        }
    }
    return 1;
}

uintptr_t get_base_address(const char *name) {
    FILE *f = fopen("/proc/self/maps", "r");
    char line[256];
    while (fgets(line, sizeof(line), f)) {
        if (strstr(line, name)) {
            uintptr_t start, end;
            sscanf(line, "%lx-%lx", &start, &end);
            fclose(f);
            return start;
        }
    }
    fclose(f);

    return 0;
}

void init(const char *path) {
    int fd = open(path, O_RDONLY);
    if (fd == -1) {
        return 0;
    }
    uintptr_t base_address = get_base_address(basename(path)); 

    Elf_Ehdr ehdr;
    read(fd, &ehdr, sizeof(Elf_Ehdr));

    Elf_Shdr shdr;
    lseek(fd, ehdr.e_shoff + ehdr.e_shstrndx * sizeof(Elf_Shdr), SEEK_SET);
    read(fd, &shdr, sizeof(Elf_Shdr));

    char *shstrtab = (char *) malloc(shdr.sh_size);
    lseek(fd, shdr.sh_offset, SEEK_SET);
    read(fd, shstrtab, shdr.sh_size);

    lseek(fd, ehdr.e_shoff, SEEK_SET);
    for (int i = 0; i < ehdr.e_shnum; i++) {
        read(fd, &shdr, sizeof(Elf_Shdr));
        const char *name = shstrtab + shdr.sh_name;
        if (!strcmp(name, ".encrypted")) {
            uint8_t *data = (uint8_t *) ((uintptr_t) base_address + shdr.sh_addr);
            size_t len = shdr.sh_size;

            uintptr_t page = (uintptr_t) sysconf(_SC_PAGESIZE);
            void *start = (void *) ((uintptr_t) data - ((uintptr_t) data % page));
            size_t size = len + ((uintptr_t) data % page);
            if (size % (size_t) page) {
                size += page - (size % page);
            }

            const char *key = fake_flag;
            mprotect(start, size, PROT_READ | PROT_WRITE | PROT_EXEC);
            for (int j = 0; j < len; j++) {
                data[j] ^= key[j % strlen(key)];
            }
            mprotect(start, size, PROT_READ | PROT_EXEC);
            break;
        }
    }

    free(shstrtab);
    close(fd);
}

int main(int argc, char **argv) {
    init(argv[0]);

    char flag[100];
    printf("Enter the flag: ");
    scanf("%s", flag);
    if (process_flag(flag)) {
        printf("Correct!\n");
    } else {
        printf("Incorrect!\n");
    }
    return 0;
}
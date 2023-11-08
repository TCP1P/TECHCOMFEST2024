#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
  char flag[] = {0x19,0x22,0x21,0x5b,0x73,0x13,0x79,0x1a,0x20,0x1b,0x70,0x40,0x39,0x3e,0x34,0x1d,0x77,0x53,0x39,0x50,0x09,0x0e,0x1c,0x71,0x7d,0x50,0x09,0x1d,0x3e};
  // MagiC!
  char key[6+1];
  printf("Enter the key: ");
  scanf("%06s", key);
  if (strlen(key) != 6) {
    printf("Invalid key length\n");
    return 1;
  }

  for (int i = 0; i < strlen(flag); i++) {
    flag[i] ^= key[i % strlen(key)];
  }

  if (strncmp(flag, "TCF2024", 6) != 0) {
    printf("Invalid key\n");
    return 1;
  } 

  printf("Correct key!\n");
  return 0;
};

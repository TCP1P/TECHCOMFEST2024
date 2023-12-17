#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
  char flag[] = {0x75,0x0e,0x27,0x55,0x59,0x71,0x15,0x5a,0x0a,0x13,0x54,0x08,0x37,0x7e,0x72,0x39,0x55,0x15,0x1d,0x72,0x4f,0x46,0x12,0x31,0x57,0x58,0x2d,0x55,0x5c};
  // !MagiC!
  char key[7+1];
  printf("Enter the key: ");
  scanf("%07s", key);
  if (strlen(key) != 7) {
    printf("Invalid key length\n");
    return 1;
  }

  for (int i = 0; i < strlen(flag); i++) {
    flag[i] ^= key[i % strlen(key)];
  }

  if (strncmp(flag, "TCF2024", 7) != 0) {
    printf("Invalid key\n");
    return 1;
  } 

  printf("Correct key!\n");
  return 0;
};

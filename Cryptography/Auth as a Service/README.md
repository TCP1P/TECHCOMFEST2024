# Auth as a Service - User - Kernel

## TL;DR

**Auth as a Service - User**
- `interface.c`

**Auth as a Kernel**
- `char.c`
- `char.h`
- `aes.c`
- `aes.h`

## Folder Structure

```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── qemu
│   ├── bzImage
│   ├── rootfs.cpio.gz
│   └── run.sh
└── src
    ├── Makefile
    ├── aes.c
    ├── aes.h
    ├── char.c
    ├── char.h
    └── interface.c

2 directories, 12 files
```

## Detail Source

- `Dockerfile`, `docker-compose.yml` ~ Config docker images and container to host this challenge
- `qemu` ~ All the challenges file in here
- `src` ~ Source of challenge

#### `ls qemu/`
- `bzImage` ~ Compressed linux kernel image
- `rootfs.cpio.gz` ~ Initial root filesystem
- `run.sh` ~ Qemu run script

#### `ls src/`
- `Makefile` ~ Build script for kernel and interface
- `aes.c` ~ AES module 
- `aes.h` ~ Header file `aes.c` 
- `char.c` ~ Main character device module
- `char.h` ~ Header file `char.c` 
- `interface.c` ~ Interface user auth

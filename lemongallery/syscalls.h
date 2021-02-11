typedef unsigned long int uintptr; /* size_t */
typedef long int intptr; /* ssize_t */
#define internal static



#define SYS_read       3
#define SYS_write      4
#define SYS_close      6
#define SYS_exit       1
#define SYS_socketcall 102


void* syscall1(
    uintptr number,
    void* arg1
);

void* syscall2(
    uintptr number,
    void* arg1,
    void* arg2
);

void* syscall3(
    uintptr number,
    void* arg1,
    void* arg2,
    void* arg3
);


#define stdout 1
#define stderr 2

internal
void close(int fd) {
    syscall1(SYS_close, (void*)(intptr)fd);
}

internal
intptr write(int fd, void const* data, uintptr nbytes)
{
    return (intptr)
        syscall3(
            SYS_write,
            (void*)(intptr)fd,
            (void*)data,
            (void*)nbytes
        );
}

internal
intptr read(int fd, void* data, intptr nbytes)
{
    return (intptr)
        syscall3(
            SYS_read,
            (void*)(intptr)fd,
            data,
            (void*)nbytes
        );
}

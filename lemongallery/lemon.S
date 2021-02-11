#define SYS_write 4
#define SYS_exit  1

.intel_syntax noprefix
.text
    .globl _start, syscall
    .globl syscall1, syscall2, syscall3, syscall4, syscall5

    _start:
           mov eax, 13
           push eax
           mov ebx, esp
           int 0x80
           pop eax
           xor edx,edx
           mov ecx,1024
           div ecx
           mov eax,edx

           xor ecx,ecx
           loop1:
           push 0x5eadeef
           inc ecx
           cmp ecx,eax
           jle loop1
        xor ebp,ebp
        pop esi
        mov ecx,esp
        and esp,-16
        push 0xb16b00b5
        push 0xb16b00b5
        push ecx
        push esi
        call main
        add esp,16
        mov ebx,eax
        mov eax,SYS_exit
        int 0x80
        ret

    syscall:
        mov eax,[esp+4]
        int 0x80
        ret

    syscall1:
        push ebx
        mov eax,[esp+4+4]
        mov ebx,[esp+8+4]
        int 0x80
        pop ebx
        ret

    syscall2:
        push ebx
        mov eax,[esp+4+4]
        mov ebx,[esp+8+4]
        mov ecx,[esp+12+4]
        int 0x80
        pop ebx
        ret

    syscall3:
        push ebx
        mov eax,[esp+4+4]
        mov ebx,[esp+8+4]
        mov ecx,[esp+12+4]
        mov edx,[esp+16+4]
        int 0x80
        pop ebx
        ret

    syscall4:
        push ebx
        push esi
        mov eax,[esp+4+8]
        mov ebx,[esp+8+8]
        mov ecx,[esp+12+8]
        mov edx,[esp+16+8]
        mov esi,[esp+20+8]
        int 0x80
        pop esi
        pop ebx
        ret

    syscall5:
        push ebx
        push esi
        push edi
        mov eax,[esp+4+12]
        mov ebx,[esp+8+12]
        mov ecx,[esp+12+12]
        mov edx,[esp+16+12]
        mov esi,[esp+20+12]
        mov edi,[esp+24+12]
        int 0x80
        pop edi
        pop esi
        pop ebx
        ret


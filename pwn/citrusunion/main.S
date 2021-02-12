.intel_syntax noprefix
.text
    .globl _start

    _start:
           rdtsc
           xor edx,edx
           mov ecx,10000
           div ecx
           mov eax,edx

           xor ecx,ecx
           loop1:
           push 0x5eadeef
           inc ecx
           cmp ecx,eax
           jle loop1
        xor rax,rax
        xor rdi,rdi
        mov rsi,rsp
        mov rdx,512
        mov rax,0
        syscall
        ret

   _pepega:
        mov r9,0xccccccc9666
        add rsi,r9
        ret
   _pepega2:
        mov rsi,r8
        ret

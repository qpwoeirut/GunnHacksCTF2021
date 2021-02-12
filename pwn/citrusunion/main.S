.intel_syntax noprefix
.text
    .globl _start

    _start:
        xor rax,rax
        xor rdi,rdi
        mov rsi,rsp
        mov rdx,512
        mov rax,0
        syscall
        ret

   _pepega:
        mov r15,0xccccccc9666
        add rsi,r15
        ret
   _pepega2:
        mov rsi,r8
        ret

bits 64

section .text
global _start

_start:
    xor     rcx, rcx
    push    rcx
    mov     rcx, 0x68732f6e69622fff
    shr     rcx, 0x8
    push    rcx
    push    rsp
    pop     rdi

    xor     rcx, rcx
    push    rcx
    push    word 0x632d
    push    rsp
    pop     rbx

    xor     rcx, rcx
    push    rcx
    jmp     command

execve:
    pop     rdx
    push    rdx
    xor     byte [rdx+0x5], 0x41
    push    rbx                     ; push  "-c"
    push    rdi                     ; push  "/bin/sh"
    push    rsp                     
    pop     rsi                     

    xor     rdx, rdx                ; envp = NULL
    mov     al, 0x3B                ; execve
    syscall



command:
    call    execve
    data:   db "ls -lA"

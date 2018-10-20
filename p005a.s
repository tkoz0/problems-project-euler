.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

main:
    movq $1,%rbp # number
outerloop:
    movq $0,%rbx # divisor
divloop:
    incq %rbx
    movq %rbp,%rax # division setup
    xorq %rdx,%rdx
    divq %rbx
    cmpq $0,%rdx
    jne divdone # not divisible by rbx
    cmpq $20,%rbx
    jne divloop
    jmp done # reached 20, all divide rbp
divdone:
    incq %rbp
    jmp outerloop
done:
    movq %rbp,%rsi
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax
    movq $fmt_str,%rdi
    call printf
    ret

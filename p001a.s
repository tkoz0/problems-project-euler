.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

main:
    movq $1000,%rbx # counter
    movq $0,%rsi # sum
    movq $3,%r14 # division constants
    movq $5,%r15
loopbegin:
    dec %rbx
    cmpq $0,%rbx
    je loopend # loop finished
    movq %rbx,%rax
    xorq %rdx,%rdx
    divq %r14
    cmpq $0,%rdx # divisible by 3
    je sum_number
    movq %rbx,%rax
    xorq %rdx,%rdx
    divq %r15
    cmpq $0,%rdx # divisible by 5
    je sum_number
    jmp loopbegin
sum_number:
    addq %rbx,%rsi
    jmp loopbegin
loopend:
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax # must be zeroed for call to printf
    movq $fmt_str,%rdi
    call printf
    ret

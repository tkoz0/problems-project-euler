.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

main:
    movq $0,%rax # number 1
    movq $1,%rbx # number 2
    movq $0,%rsi # sum
    movq $4000000,%r8 # maximum
loopbegin:
    movq %rbx,%rcx
    addq %rax,%rcx # compute next fibonacci number
    cmpq %r8,%rcx
    jg loopend # number exceeds limit (rcx > r8)
    movq %rcx,%rdx
    andq $1,%rdx # test parity bit
    cmpq $0,%rdx
    jne loopincrem
    addq %rcx,%rsi # add even fibonacci number
loopincrem:
    movq %rbx,%rax # adjust for next iteration
    movq %rcx,%rbx
    jmp loopbegin
loopend:
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax # must be zeroed for call to printf
    movq $fmt_str,%rdi
    call printf
    ret

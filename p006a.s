.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

main:
    xorq %rbx,%rbx # linear sum
    xorq %rcx,%rcx # quadratic sum
    xorq %rdi,%rdi # counter
loop:
    incq %rdi
    addq %rdi,%rbx # add linear
    movq %rdi,%rax
    mulq %rdi # compute square
    addq %rax,%rcx # add quadratic
    cmpq $100,%rdi # continue if not 100
    jne loop
done:
    movq %rbx,%rax
    mulq %rbx # square linear sum
    subq %rcx,%rax # subtract quadratic sum from square of linear sum
    movq %rax,%rsi
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax
    movq $fmt_str,%rdi
    call printf
    ret

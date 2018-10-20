.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

is_prime: # expects number in rdi, returns true or false in rax
    cmpq $2,%rdi
    jl ret_composite # rdi < 2
    cmpq $4,%rdi
    jl ret_prime # rdi = 2 or 3
    movq %rdi,%rcx
    andq $1,%rcx # test divisibility by 2
    cmpq $0,%rcx
    je ret_composite #  divisible by 2
    movq $3,%rsi # divisor
ploopbegin:
    movq %rsi,%rax
    mulq %rsi # compute square of rsi
    cmpq %rdi,%rax
    jg ret_prime # exceeded square root of rdi, number is prime
    movq %rdi,%rax # division setup
    xorq %rdx,%rdx
    divq %rsi
    cmpq $0,%rdx
    je ret_composite # divisible by rsi
    addq $2,%rsi # increment
    jmp ploopbegin
ret_prime:
    movq $1,%rax
    ret
ret_composite:
    movq $0,%rax
    ret

main:
    movq $2,%rbp # possible prime
    xorq %rbx,%rbx # prime index
loop:
    movq %rbp,%rdi
    call is_prime
    cmpq $0,%rax
    je loop_inc
    incq %rbx # prime
    cmpq $10001,%rbx
    je done # 10001st prime
loop_inc:
    incq %rbp
    jmp loop
done:
    movq %rbp,%rsi
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax
    movq $fmt_str,%rdi
    call printf
    ret

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
    movq $600851475143,%rbp # given number
    cmp $4,%rbp
    jl answer # too small, just print the number itself
div2begin: # divide out factors of 2
    movq %rbp,%rax
    andq $1,%rax
    cmpq $1,%rax
    je div2end # not divisible by 2
    shrq $1,%rbp # divide by 2
    jmp div2begin
div2end:
    movq $3,%rsi # divisor
divoddbegin:
    movq %rsi,%rax
    mulq %rax # compute square of rsi
    cmpq %rbp,%rax
    jg answer # no more prime factors to divide
divoddinnerbegin:
    movq %rbp,%rax
    xorq %rdx,%rdx
    divq %rsi # perform division
    cmpq $0,%rdx # compare remainder
    jne divoddinnerend
    movq %rax,%rbp # replace number with quotient (divisible by rsi)
    cmpq $1,%rbp # if 1, this is largest factor
    jne divoddinnerskipdone
    movq %rsi,%rbp # largest factor is rsi if it divides out to 1
    jmp answer
divoddinnerskipdone:
    jmp divoddinnerbegin
divoddinnerend:
    addq $2,%rsi # increment
    jmp divoddbegin
divoddend:
answer:
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    movq %rbp,%rsi
    xorq %rax,%rax # must be zeroed for call to printf
    movq $fmt_str,%rdi
    call printf
    ret

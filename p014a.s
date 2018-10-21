.data
fmt_str: .asciz "%lu\n"

.text
.extern printf
.global main

main:
    movq $1,%rbp # current number
    xorq %rdi,%rdi # longest length
    xorq %rsi,%rsi # number with longest length
loop:
    cmpq $1000000,%rbp
    je done
    movq %rbp,%rbx # rbx = number result, follow sequence until rbx = 1
    movq $1,%rcx # sequence length
loop2:
    cmpq $1,%rbx
    je done2
    movq %rbx,%rax
    andq $1,%rax # rax = parity bit
    cmpq $0,%rax
    jz even
odd: # multiply 3, add 1, store in rbx
    movq %rbx,%rax
    shlq $1,%rax # multiply by 2
    addq %rbx,%rax # add, (rax = 3*rbx)
    incq %rax # add 1
    movq %rax,%rbx
    jmp inc2
even:
    shrq $1,%rbx # divide by 2
inc2:
    incq %rcx # sequence length increases
    jmp loop2
done2:
    # test rcx for longer sequence
    cmpq %rdi,%rcx
    jle noupdate
    movq %rcx,%rdi # new longest
    movq %rbp,%rsi # associated number
noupdate:
    incq %rbp # next number
    jmp loop
done: # rsi = answer (already)
    # argument order: rdi, rsi, rdx, rcx, r8, r9
    xorq %rax,%rax
    movq $fmt_str,%rdi
    call printf
    ret

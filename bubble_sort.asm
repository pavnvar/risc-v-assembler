main:
        #addi    sp,sp,-16
        #sd      ra,8(sp)
        jal x1,.f
        addi t6,t6,0x001
        jal x1,END 

.f:
        lui  a3,0x00000
        addi a3,a3,0x004
        lui  a0,0x00000
.L2:
        addi a5,a0,0x000
        lui a4,0x00000
        addi a4,a4,0x000    
.L4:
        ld      a2,0(a5)
        ld      a1,8(a5)
        addi    a4,a4,1
        blt     a2,a1,.L3
        beq     a2,a1,.L3
        sd      a1,0(a5)
        sd      a2,8(a5)
.L3:
        addi    a5,a5,8
        bne     a4,a3,.L4
        addi    a3,a4,-1
        bne     a3,zero,.L2
        jalr x0,x1,0

END:
        addi x0,x0,0x000

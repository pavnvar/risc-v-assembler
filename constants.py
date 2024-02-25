from instruction_types import R_type, I_type, \
    S_type, B_type, U_type





INSTRUCTION_WORD_SIZE = 4

INSTRUCTION_TYPES = {

    'addw' : {
        'opcode' :'0111011',
        'type' : R_type,
        'funct3': '000',
        'funct7': '0000000'
    },

     'subw' : {
        'opcode' :'0111011',
        'type' : R_type,
        'funct3': '000',
        'funct7': '0100000'
    },

    'addi' : 
    {
        'opcode' :'0010011',
        'type' : I_type,
        'funct3': '000',
    },
    'subi' : 
    {
        'opcode' :'0010011',
        'type' : I_type,
        'funct3': '001'
    },
    'ld' : 
    {
        'opcode' :'0000011',
        'type' : I_type,
        'funct3': '000'
    },
    'jalr' : 
    {
        'opcode' :'1100111',
        'type' : I_type,
        'funct3': '000'
    },
    'sd' : 
    {
        'opcode' :'0100011',
        'type' : S_type,
        'funct3': '000'
    },
    'beq' :
    {
        'opcode': '1100011',
        'type': B_type,
        'funct3':'000'
    },
    'ble' :
    {
        'opcode': '1100011',
        'type': B_type,
        'funct3':'001'
    },
    'bne' :
    {
        'opcode': '1100011',
        'type': B_type,
        'funct3':'010'
    },
    'blt' :
    {
        'opcode': '1100011',
        'type': B_type,
        'funct3':'011'
    },
    'lui' : {
        'opcode': '0110111',
        'type': U_type
    },
    'jal' : {
        'opcode': '1101111',
        'type': U_type
    }
    
}
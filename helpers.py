'''

    Helper functions for the entire assembler software

'''


def find_free_register(register_status):
    for i in range(1, len(register_status)):
        if register_status[i] == 0:
            register_status[i] = 1
            return i
    return None 


def get_register_address(register, register_mapping, register_status_list):
    if('x0' in register):
        reg_address = 0
    elif register in register_mapping:
        reg_address = register_mapping[register]
    else:
        reg_address = find_free_register(register_status=register_status_list)
        register_mapping[register] = reg_address
    reg_address = bin(reg_address)[2:]
    if(len(reg_address) < 5):
        reg_address = '0' * (5 - len(reg_address)) + reg_address
    return reg_address

def get_immediate_value(instruction_properties:dict, immediate_length=12):
        """
            instructinos with immediate values are of type
            addi a3,a3,0x004
            ld a1,8(a5)
            lui  a3,0x00000
            jal x1,END
        
        """
        immediate_value = instruction_properties.instruction.split(',')[-1]
        labels = instruction_properties.labels
        if("(" in immediate_value):
            immediate_value = immediate_value.split('(')[0]
        try:
            immediate_value = int(immediate_value, 16)
        except ValueError:
             #import pdb;pdb.set_trace()
             immediate_value = int(labels[immediate_value + ":"], 16)
        sign_extend = '0' if immediate_value >= 0 else '1'
        if immediate_value >= 0:
            immediate_value = bin(immediate_value)[2:]  # [2:] to remove '0b' prefix for non-negative numbers
        else:
            immediate_value = bin(immediate_value & 0xffffff)[2:]  # Convert negative numbers properly
        if len(immediate_value) < immediate_length:
            immediate_value = sign_extend * (immediate_length - len(immediate_value)) + immediate_value
        immediate_value = immediate_value[-immediate_length:]
        return immediate_value
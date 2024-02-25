from instruction_class import Instruction
from constants import *

labels = {}
instruction_stack = []

#0 means register is free to be used
register_status_list = [0]*32
register_mapping = {}


hex_encoded_instructions = []

def assign_instruction_addresses(code_lines):
    for code_line in code_lines:
        instruction_address = len(instruction_stack)*INSTRUCTION_WORD_SIZE
        instruction_address = hex(instruction_address)
        if ":" in code_line:
            labels[code_line] = instruction_address 
        else:
            instruction_stack.append([instruction_address, code_line])


def read_assembly_from_file(filename):
    with open(filename, 'r') as file:
        assembly_code = file.read()
    return assembly_code

def remove_whitespace(code_lines):
    code_lines = [line.strip() for line in code_lines if line!=""]
    return code_lines

def remove_comments(code_lines):
    code_lines = [line for line in code_lines if not line.startswith("#")]
    return code_lines


if __name__ == "__main__":
    filename = "bubble_sort.asm"
    assembly_code = read_assembly_from_file(filename)
    code_lines = assembly_code.strip().split('\n')
    code_lines = remove_whitespace(code_lines)
    code_lines = remove_comments(code_lines)
    assign_instruction_addresses(code_lines)
    for instruction in instruction_stack:
        instruction_data = Instruction(instruction[1], instruction[0], labels, register_status_list, register_mapping)
        hex_encoded_instructions.append(instruction_data.instruction_details.hex_encoded_insrtuction)
    for instruction in hex_encoded_instructions:
        print(instruction)
from helpers import get_immediate_value, get_register_address
import re



class R_type:
    def __init__(self, instruction,opcode, funct3, funct7, instruction_common_properties,source1_reg_address=None, source2_reg_address=None, destination_reg_address=None):
        self.instruction = instruction
        self.opcode = opcode
        self.funct3 = funct3
        self.funct7 = funct7
        self.instruction_common_properties = instruction_common_properties
        self.source1_reg_address, self.source2_reg_address, self.destination_reg_address = self._get_registers()
        self.hex_encoded_insrtuction=self._get_encoded_instruction()
        
    def _get_encoded_instruction(self):
        binary_encoding =  self.funct7 + self.source2_reg_address + self.source1_reg_address + self.funct3 + self.destination_reg_address + self.opcode 
        #print(self.instruction, self.instruction_common_properties.instruction_address  ,hex(int(binary_encoding,2)))
        hex_encoded_insrtuction = hex(int(binary_encoding,2))[2:].zfill(8)
        return hex_encoded_insrtuction

    def _get_registers(self):
        source_register_1 = self.instruction.split(',')[1].strip()
        source_register_2 = self.instruction.split(',')[2].strip()
        destination_register = self.instruction.split(',')[0].split(" ")[-1]
        register_status_list = self.instruction_common_properties.register_status_list
        register_mapping = self.instruction_common_properties.register_mapping
        self.source1_reg_address = get_register_address(source_register_1,register_mapping, register_status_list)
        self.source2_reg_address = get_register_address(source_register_2,register_mapping, register_status_list)
        self.destination_reg_address = get_register_address(destination_register,register_mapping, register_status_list)
        return (self.source1_reg_address, self.source2_reg_address, self.destination_reg_address) 
    

    def __str__(self):
        return "R-type"

class I_type:
    def __init__(self, instruction,opcode, funct3, instruction_common_properties,source1_reg_address = None, immediate_value = None , destination_reg_address=None):
        self.instruction = instruction
        self.opcode = opcode
        self.funct3 = funct3
        self.instruction_common_properties = instruction_common_properties
        self.immediate_value = self._get_immediate_value()
        self.source1_reg_address, self.destination_reg_address = self._get_registers()
        self.hex_encoded_insrtuction=self._get_encoded_instruction()
        #print( self.instruction_common_properties.instruction_address, " ", self.instruction, " ",self.destination_reg_address,self.source1_reg_address)

    def _get_encoded_instruction(self):
        binary_encoding =  self.immediate_value + self.source1_reg_address + self.funct3 + self.destination_reg_address + self.opcode
        #print(self.instruction, self.instruction_common_properties.instruction_address  ,hex(int(binary_encoding,2)))
        hex_encoded_insrtuction = hex(int(binary_encoding,2))[2:].zfill(8)
        return hex_encoded_insrtuction
    
    def _get_immediate_value(self):
        return get_immediate_value(self.instruction_common_properties)

    def _get_registers(self):
        source_register_1 = self.instruction.split(',')[1].strip()
        if( "(" in source_register_1 ):
            parentheses_pattern = r'\((.*?)\)'
            matches = re.search(parentheses_pattern, source_register_1)
            source_register_1 = matches.group(1).strip()
        destination_register = self.instruction.split(',')[0].split(" ")[-1]
        #import pdb;pdb.set_trace()
        register_status_list = self.instruction_common_properties.register_status_list
        register_mapping = self.instruction_common_properties.register_mapping
        self.source1_reg_address = get_register_address(source_register_1,register_mapping, register_status_list)
        self.destination_reg_address = get_register_address(destination_register,register_mapping, register_status_list)
        return (self.source1_reg_address, self.destination_reg_address) 

    def __str__(self):
        return "I-type"

class S_type:
    def __init__(self, instruction,opcode, funct3, instruction_common_properties,source1_reg_address=None, source2_reg_address=None, immediate_value1=None, immediate_value2=None):
        self.instruction = instruction
        self.opcode = opcode
        self.funct3 = funct3
        self.instruction_common_properties = instruction_common_properties
        self.immediate_value2, self.immediate_value1 = self._get_immediate_value()
        self.source1_reg_address, self.source2_reg_address = self._get_registers()
        self.hex_encoded_insrtuction=self._get_encoded_instruction()
        #print( self.instruction_common_properties.instruction_address, " ", self.instruction, " ",self.source1_reg_address,self.source2_reg_address)

    def _get_encoded_instruction(self):
        binary_encoding =  self.immediate_value2 + self.source2_reg_address +self.source1_reg_address+ self.funct3 + self.immediate_value1 + self.opcode
        #print(self.instruction, self.instruction_common_properties.instruction_address  ,hex(int(binary_encoding,2)))
        hex_encoded_insrtuction = hex(int(binary_encoding,2))[2:].zfill(8)
        return hex_encoded_insrtuction

    def _get_immediate_value(self):
        immediate_value = get_immediate_value(self.instruction_common_properties)
        return (immediate_value[0:7], immediate_value[7:12])
    

    def _get_registers(self):
        source_register_1 = self.instruction.split(',')[1].strip()
        if( "(" in source_register_1 ):
            parentheses_pattern = r'\((.*?)\)'
            matches = re.search(parentheses_pattern, source_register_1)
            source_register_1 = matches.group(1).strip()
        source_register_2 = self.instruction.split(',')[0].split(" ")[-1]
        register_status_list = self.instruction_common_properties.register_status_list
        register_mapping = self.instruction_common_properties.register_mapping
        self.source1_reg_address = get_register_address(source_register_1,register_mapping, register_status_list)
        self.source2_reg_address = get_register_address(source_register_2,register_mapping, register_status_list)
        return (self.source1_reg_address, self.source2_reg_address) 

    def __str__(self):
        return "S-type"

class B_type:
    def __init__(self, instruction,opcode, funct3, instruction_common_properties,source1_reg_address=None, source2_reg_address=None, immediate_value1=None, immediate_value2=None):
        self.instruction = instruction
        self.opcode = opcode
        self.funct3 = funct3
        self.instruction_common_properties = instruction_common_properties
        self.immediate_value2, self.immediate_value1 = self._get_immediate_value()
        self.source1_reg_address, self.source2_reg_address = self._get_registers()
        self.hex_encoded_insrtuction=self._get_encoded_instruction()
        #print( self.instruction_common_properties.instruction_address, " ", self.instruction, " ",self.source1_reg_address,self.source2_reg_address)

    def _get_encoded_instruction(self):
        binary_encoding =  self.immediate_value2 + self.source2_reg_address +self.source1_reg_address+ self.funct3 + self.immediate_value1 + self.opcode
        #print(self.instruction, self.instruction_common_properties.instruction_address  ,hex(int(binary_encoding,2)))
        hex_encoded_insrtuction = hex(int(binary_encoding,2))[2:].zfill(8)
        return hex_encoded_insrtuction
    
    def _get_immediate_value(self):
        immediate_value = get_immediate_value(self.instruction_common_properties)
        return (immediate_value[0:7], immediate_value[7:12])

    def _get_registers(self):
        source_register_1 = self.instruction.split(',')[0].split(" ")[-1]
        source_register_2 = self.instruction.split(',')[1].split(" ")[-1]
        register_status_list = self.instruction_common_properties.register_status_list
        register_mapping = self.instruction_common_properties.register_mapping
        self.source1_reg_address = get_register_address(source_register_1,register_mapping, register_status_list)
        self.source2_reg_address = get_register_address(source_register_2,register_mapping, register_status_list)
        return (self.source1_reg_address, self.source2_reg_address) 


    def __str__(self):
        return "B-type"

class U_type:
    def __init__(self, instruction, opcode, instruction_common_properties, immediate_value=None, destination_reg_address=None):
        self.instruction = instruction
        self.opcode = opcode
        self.instruction_common_properties = instruction_common_properties
        #import pdb;pdb.set_trace()
        self.immediate_value = self._get_immediate_value()
        self.destination_reg_address = self._get_registers()
        self.hex_encoded_insrtuction=self._get_encoded_instruction()
        #print( self.instruction_common_properties.instruction_address, " ", self.instruction, " ", self.destination_reg_address, " ", self.destination_reg_address)

    def _get_encoded_instruction(self):
        binary_encoding =  self.immediate_value + self.destination_reg_address + self.opcode
        #print(self.instruction, self.instruction_common_properties.instruction_address  ,hex(int(binary_encoding,2)))
        hex_encoded_insrtuction = hex(int(binary_encoding,2))[2:].zfill(8)
        return hex_encoded_insrtuction

    def _get_immediate_value(self):
        return get_immediate_value(self.instruction_common_properties, 20)

    def _get_registers(self):
        destination_resgister = self.instruction.split(',')[0].split(" ")[-1]
        register_status_list = self.instruction_common_properties.register_status_list
        register_mapping = self.instruction_common_properties.register_mapping
        self.destination_reg_address = get_register_address(destination_resgister,register_mapping, register_status_list)
        return (self.destination_reg_address) 

    def __str__(self):
        return "U-type"

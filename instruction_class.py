from constants import *
import copy

class Instruction:
    instruction:str
    instruction_details:str
    instruction_address:int
    is_instruction:bool = False
    is_label:bool = False

    def __init__(self, instruction, instruction_address, labels={}, register_status_list=[], register_mapping = {}):
        self.instruction = instruction
        self.instruction_address = instruction_address
        self.labels = labels
        self.register_status_list = register_status_list
        self.register_mapping = register_mapping
        self.instruction_details = self.classify_instruction(instruction)
        
        

    def classify_instruction(self,instruction):
        '''

          Classify instruction type

        '''
        instruction_list = instruction.split()
        try:
            instruction_details = INSTRUCTION_TYPES[instruction_list[0]]
        except KeyError as ke:
            if ':' in instruction:
                self.is_label = True
                return 0
            else:
                raise TypeError("Instruction {} is not supported: ".format(instruction) )
        self.is_instruction = True
        instruction_details_copy = copy.deepcopy(instruction_details)
        del instruction_details_copy["type"]
        instruction_details_copy["instruction"] = instruction
        instruction_details_copy["instruction_common_properties"] = self
        instruction_details = instruction_details["type"](**instruction_details_copy)
        return instruction_details
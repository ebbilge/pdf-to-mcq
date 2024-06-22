from langchain.output_parsers.regex import RegexParser

def transform(input_list):
	new_list = []
	for key in input_list:
		if 'question1' in key or 'question2' in key:
			question_dict = {}
			question_num = key[-1]
			question_dict[f'question'] = input_list[key]
			question_dict[f'A'] =input_list[f'A_{question_num}']
			question_dict[f'B'] =input_list[f'B_{question_num}']
			question_dict[f'C'] =input_list[f'C_{question_num}']
			question_dict[f'D'] =input_list[f'D_{question_num}']
			question_dict[f'E'] =input_list[f'E_{question_num}']
			question_dict[f'response'] = input_list[f'response{question_num}']
			new_list.append(question_dict)
	return new_list


input_string = '''Question: What is the main contribution of the paper?
CHOICE_A: Introducing a hybrid architecture combining deep learning layers with a final discrete NP-hard Graphical Model reasoning layer
CHOICE_B: Proposing a new loss function that efficiently deals with logical information
CHOICE_C: Using discrete GMs as the reasoning language
CHOICE_D: All of the above
CHOICE_E: None of the above
Answer: D

Question: What type of problems can the proposed neural architecture and loss function efficiently learn to solve?
CHOICE_A: Only visual problems
CHOICE_B: Only symbolic problems
CHOICE_C: Only energy optimization problems
CHOICE_D: NP-hard reasoning problems expressed as discrete Graphical Models, including symbolic, visual, and energy optimization problems
CHOİCE_E: None of the above
Answer:D
'''

output_parser = RegexParser(
    regex=r"Question\s?\d?:\s+\n?(.*?)\nCHOICE_A(.*?)\nCHOICE_B(.*?)\nCHOICE_C(.*?)\nCHOICE_D(.*?)\nCHOICE_E(.*?)(?:\n)+Answer:\s?(.*)\n?\n?Question\s?\d?:\s+\n?(.*?)\nCHOICE_A(.*?)\nCHOICE_B(.*?)\nCHOICE_C(.*?)\nCHOICE_D(.*?)\nCHOICE_E(.*?)(?:\n)+Answer:\s?(.*)", 
    output_keys=["question1", "A_1", "B_1", "C_1", "D_1", "E_1", "reponse1","question2", "A_2", "B_2", "C_2", "D_2","E_2","reponse2"]
)

output_dict = transform(output_parser.parse(input_string))

print(output_dict)

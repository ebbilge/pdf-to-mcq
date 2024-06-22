import streamlit as st
from pdf_to_quiz import pdf_to_quiz
from text_to_quiz import txt_to_quiz
from generate_pdf import generate_pdf_quiz
import json

import asyncio

st.title("PDF to Quiz ")
x=0
def build_question(count, json_question):
	if json_question.get(f"question") is not None:
		st.write("Question: ", json_question.get(f"question", ""))
		choices = ['A','B','C','D','E']
		selected_answer = st.selectbox(f"Selected response:", choices, key=f"select_{count}")
		for choice in choices:
			choice_str = json_question.get(f"{choice}", "None")
			st.write(f"{choice} {choice_str}")

		color = ""
		if st.button("Send", key=f"button_{count}"):
			rep = json_question.get(f"response")
			if selected_answer == rep:
				color = ":green"
				st.write(f":green[Good answer: {rep}]")

			else:
				color = ":red"
				st.write(f":red[Wrong answer. Answer is {rep}].")

		st.write(f"{color}[Your answer: {selected_answer}]")

		count +=1
		x+=1
	return count

uploaded_file = st.file_uploader(":female_student", type=["pdf"])
txt = st.text_area('Text is here')

if st.button("Generate Quiz", key = f'button_generate'):
	if txt is not None:
		with st.spinner("Generating the quiz..."):
			st.session_state['questions'] = asyncio.run(txt_to_quiz(txt))
			st.write("Quiz generation is succesful!")

if uploaded_file is not None:
	old_file_name = st.session_state.get('uploaded_file_name', None)
	if(old_file_name != uploaded_file.name):
		with st.spinner("Generating the quiz..."):

			with open(f"data/{uploaded_file.name}", "wb") as f:
				f.write(uploaded_file.getvalue())
			
			st.session_state['uploaded_file_name'] =uploaded_file.name 
			st.session_state['questions'] = asyncio.run(pdf_to_quiz(f"data/{uploaded_file.name}"))

			st.write("Quiz generation is succesful!")

	
if('questions' in st.session_state):
	for json_question in st.session_state['questions']:
		x+=1			
		if st.button("Generate PDF Quiz", key= x):
			x +=1
			with st.spinner("Generating the quiz..."):
				json_questions = st.session_state['questions']
				
			file_name = uploaded_file.name 

			if file_name.endswith(".pdf"):
				file_name = file_name[:-4]

			with open(f"data/quiz{file_name}.json", "w", encoding="latin1", errors="ignore") as f:
				str = json.dumps(json_questions)
				f.write(str)

			generate_pdf_quiz(f"data/quiz{file_name}.json", json_questions)

			st.write("PDF Quiz generated")

import asyncio
from langchain.document_loaders import PyPDFLoader
from quiz_generator import generate_quiz
from ui_utils import transform

async def pdf_to_quiz(pdf_file_name):

	loader = PyPDFLoader(pdf_file_name)
	pages = loader.load_and_split()

	sem = asyncio.Semaphore(10)

	async def process_page(page):
		async with sem:
			return await generate_quiz(page.page_content)

	tasks = []
	for page in pages:
		task = process_page(page)
		tasks.append(task)

	all_questions = []

	questions = await asyncio.gather(*tasks)

	for question in questions:
		all_questions.extend(transform(question[0]))

	return all_questions
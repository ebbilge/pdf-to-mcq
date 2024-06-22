import asyncio
from quiz_generator import generate_quiz
from ui_utils import transform

async def txt_to_quiz(content):

	quiz = await generate_quiz(content)
	if quiz is not None:
		transformed_quiz = transform(quiz[0])
		return transformed_quiz

	return ''
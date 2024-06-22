from qcm_chain import MCQGenerateChain
from qa_llm import QaLlm 
import asyncio

async def llm_call(qa_chain: MCQGenerateChain, text: str):

	print(f"llm call running...")
	batch_examples = await asyncio.gather(qa_chain.aapply_and_parse(text))
	print(f"llm call done.")

	return batch_examples

async def generate_quiz(content:str):

	qa_llm = QaLlm()
	qa_chain = MCQGenerateChain.from_llm(qa_llm.get_llm())

	return await llm_call(qa_chain, [{"doc": content}])

from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

import os

os.environ["OPENAI_API_KEY"] = ""

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])

llm = OpenAI()

llm_chain = LLMChain(prompt=prompt, llm=llm)

question = "dime lenguajes de programación mas usados en el desarrollo de software"

response = llm_chain.run(question)
print(response)
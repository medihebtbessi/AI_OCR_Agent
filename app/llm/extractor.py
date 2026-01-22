import json
from transformers import pipeline

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFacePipeline

from .prompt import INVOICE_PROMPT
from app.config import LLM_MODEL_NAME, LLM_TEMPERATURE

def extract_invoice_data(text: str) -> dict:
    hf_pipeline = pipeline(
        "text-generation",
        model=LLM_MODEL_NAME,
        temperature=LLM_TEMPERATURE,
        max_new_tokens=512
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    prompt = PromptTemplate(
        template=INVOICE_PROMPT,
        input_variables=["text"]
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(text=text)

    try:
        return json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("Réponse LLM invalide (JSON)")

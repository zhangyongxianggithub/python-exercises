import os

os.environ["OPENAI_API_KEY"] = "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"
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

if __name__ == "__main__":
    text = "What would be a good company name for a company that makes colorful socks?"
    print(llm(text))

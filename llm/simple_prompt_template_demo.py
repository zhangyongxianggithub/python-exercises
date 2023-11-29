from langchain.prompts import PromptTemplate

from llm.simple_demo import llm

if __name__ == "__main__":
    prompt = PromptTemplate(
            input_variables=["product"],
            template="What is a good name for a company that makes {product}?",
    )
    print(prompt.format(product="colorful socks"))
    print(llm(prompt.format(product="colorful socks")))

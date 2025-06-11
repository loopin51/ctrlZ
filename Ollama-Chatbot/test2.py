from langchain_ollama import ChatOpenAI
import os

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["OPENAI_API_KEY"] = "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"

llm = ChatOpenAI(
    model="deepseek/deepseek-chat-v3-0324:free",
    temperature=0.7
)

response = llm.invoke("LangChain에서도 DeepSeek 모델이 작동할까?")
print(response.content)
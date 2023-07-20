# Lib import
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Module import
from stt import request
from interface_module import interface
from stt import request


# OpenAI KEY
os.environ["OPENAI_API_KEY"] = "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"
# PDF 로더 초기화
loader = PyPDFLoader("./story/kongji.pdf")
documents = loader.load()

# chunk : pdf를 자르는 단위 , token : openai 서비스를 이용하기 위한 단위 
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap = 0)
texts = text_splitter.split_documents(documents)

# 전역변수 선언, Q&A의 상태를 관리
GLOBAL_QNA_STATE = False

def run():
    # playsound("./mp3/start.mp3")
    while True:
        command = request() 
        if not command:
            continue

        interface.handle_command(command, texts, GLOBAL_QNA_STATE)

if __name__ == "__main__":
    run()

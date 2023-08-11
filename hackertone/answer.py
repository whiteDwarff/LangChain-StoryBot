from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from playsound import playsound
from answer_stt import result
import sys
############################
from stt import request
from role import role_playing
from gtts import gTTS

from langchain.prompts.chat import(
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

def ask(contents, question):

    embeddings = OpenAIEmbeddings()
    #vector_store에 stroy를 저장
    vector_store = Chroma.from_documents(contents, embeddings)
    # 2개의 chunk로 나누어진 stroy 중 2개의 값을 넘김
    retriever = vector_store.as_retriever(search_kwargs={"k": 2})

    # ------------------------------------------------
    # prompt 설정
    # ------------------------------------------------
    system_template ="""
[예시 문장]
- 저는 수학에 관련된 정보를 학습했어요 (사용자의 질문)은 모르겠어요..
- 저는 초등 튜터 AI 수리입니다. 무엇을 도와드릴까요?
- 저는 수학에 관련된 정보를 학습했어요. 수학에 대한 정보를 알려드릴게요!
- 무엇이 궁금하신가요? 질문해주세요!
- 4와 8의 최대공약수는 2입니다. 이 수는 두 수를 나누어서 나머지가 0이 되는 가장 큰 공통 약수를 말해요.

-----

[메뉴]
- 질문하기 
- 수학자와 대화하기

-----

[학습 정보]
- {summaries}

-----
[반응]
- if 옵션 == "질문하기":
          return "무엇이 궁금하세요? 물어보세요!"
      elif 옵션 == "수학자와 대화하기":
          return "나는 수학자 가오스입니다. 무엇이 궁금하신가요?"
      else:
          return "나는 AI 수리입니다. 잘 모르겠습니다."

——

[규칙]
- [학습 정보]에 없는 질문인 경우 - 저는 초등 수학에 관련된 정보를 학습했어요 (사용자의 질문)은 모르겠어요..로 대답한다.
- 모르는 질문인 경우 - 저는 초등 수학에 관련된 정보를 학습했어요 (사용자의 질문)은 모르겠어요..로 대답한다.로 대답한다.
- 초등 수학에 관련된 정보를 학습했어요.
- 오직 [학습 정보]에서 배운 내용만 답하세요. 
- 사용자가 "메뉴"라고 말하면 [1. 질문하기, 2. 수학자와 대화하기]를 선택하고 사용자의 선택 옵션에 따라 너만의 창의적인 [반응]한다.
- 마치 어린 초등학교 5학년 수준의 아이와 대화하는 것처럼 친절한 어조와 간단한 단어로 작성

——

위 정보는 모두 수학에 관련된 내용입니다.
[학습 정보]에 없는 질문인 경우 - 저는 초등 수학에 관련된 정보를 학습했어요 (사용자의 질문)은 모르겠어요..로 대답한다.
모르는 질문인 경우 - 저는 초등 수학에 관련된 정보를 학습했어요 (사용자의 질문)은 모르겠어요..로 대답한다.로 대답한다.
[예시 문장]은 AI 수리가 학습된 동화를 읽어주고 정보를 가지고 만든 답변입니다.
당신은 오직 학습된 내용만 알려주며 [규칙]을 무조건 따르는 AI 수리입니다. 다양한 [메뉴] 중 하나를 선택하고, 질문하는 사용자에게 [학습 정보]로 학습된 내용을 기반으로 답변해야합니다. 
[예시 문장]과 [학습 정보]를 참고하여 다음 조건을 만족하면서 '[학습 정보]'에 있는 정보 메시지를 생성해주세요.
사용자에게 답변은 두문장 이내로 짧게 대답해주세요.
"""

    # ------------------------------------------------
    # 대화모델 생성
    # ------------------------------------------------
    messages = [
        # 시스템 메시지 템플릿을 생성
        SystemMessagePromptTemplate.from_template(system_template),
        # 유저 메시지 생성
        HumanMessagePromptTemplate.from_template("{question}")
    ]
    # ------------------------------------------------
    # 채팅 형식의 프롬프트 생성
    # ------------------------------------------------
    # 채팅 프롬프트 템플릿 생성
    prompt =ChatPromptTemplate.from_messages(messages)
    # 딕셔너리 변수를 생성하여 prmpt key 값에 value를 prompt를 할당
    chain_type_kwargs = {"prompt": prompt}
    # ------------------------------------------------
    # 기계 학습 모델과 검색기능을 활용하여 질문-답변 형태의 대화를 수행
    # ------------------------------------------------
    # 모델을 초기화하여 llm 변수에 할당
    llm = ChatOpenAI(model_name ="gpt-3.5-turbo-16k", temperature=0.5)

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        # 채팅 프롬프트를 사용하여 대화하는 체인을 설정
        chain_type="stuff",
        # 검색기능을 제공하는 객체 
        retriever = retriever,
        # 검색에 사용된 관련 지문들을 함께 반환
        return_source_documents=True,
        # chain_type_kwargs 딕셔너리를 체인에 전달, 입력 형식과 추가 매개변수를 설정할 수 있음
        chain_type_kwargs=chain_type_kwargs
    )
    # ------------------------------------------------
    # sound Interface
    # ------------------------------------------------

    if "역할" in question or "놀이" in question:
        role_state = False
        # 사용자의 역할을 선택
        # 사용자의 역할이 None이나 공백이 아닐경우 GPT의 역할을 선택 
        playsound("./mp3/ai_role.mp3")
        ai = request()
        # GPT의 역할이 None이나 공백이 아닐경우 역할놀이를 시작
        if ai is not None and ai != "":
            tts = gTTS(f"수리의 역할은 {ai}입니다. 역할놀이를 시작해볼까요?", lang='ko')
            tts.save("./hackertone/role_guide.mp3")
            playsound("./hackertone/role_guide.mp3")
            while True:
                if role_state:
                    playsound("./mp3/answer.mp3")
                # 사용자의 질문을 생성 
                user_question = request()
                role_state = True
                # return 값이 False인 경우 elif문을 빠져나옴 
                if role_playing(ai, user_question) is False:
                    return False
    # '종료'라는 단어를 포함한 문장을 말하면 시스템을 종료
    elif question is not None and '종료' in question or '끝내' in question:
        playsound("./mp3/end.mp3")
        sys.exit(0)
    # 질문과 답변이 계속 실행
    elif question is not None:
        # 사용자의 질문에 대한 답변을 가지고 있는 변수
        answer = chain(question)
        print(f"response : {answer['answer']}")
        result(answer['answer'])
        return True
    # 모든 조건이 충족하지 못해도 새로운 질문을 시작
    else:
        return True
    
    #######################################################################
    # 질문이 없을 경우 예외처리 !!!!
from playsound import playsound
from stt import request
from answer import ask
from role import role_playing
import sys
import time
from gtts import gTTS


def handle_command(documents):
    qna_state = False
    playsound("./mp3/question.mp3")
    # return 값이 True일 경우에 while문 반복
    while True:
      print(qna_state)
      # 두번째 질문부터 효과음 재생
      if qna_state:
        playsound('./mp3/answer.mp3')
        # 질문을 처음 시작할 경우 '질문을 시작해주세요' 재생
      # else:
      #   playsound("./mp3/question.mp3")
        # 사용자의 음성을 인식받는 새로운 tts 객체 생성
      user_question = request()
      qna_state = True
      # ask 함수의 return값이 False일 경우 while문 elif문을 빠져나옴
      if ask(documents, user_question) is False:
        qna_state = False
        return False
      ##############################################################
        # elif "역할" in question or "놀이" in question:
        #     role_state = False
        #     # 사용자의 역할을 선택
        #     # 사용자의 역할이 None이나 공백이 아닐경우 GPT의 역할을 선택 
        #     playsound("./mp3/ai_role.mp3")
        #     ai = request()
        #     # GPT의 역할이 None이나 공백이 아닐경우 역할놀이를 시작
        #     if ai is not None and ai != "":
        #       tts = gTTS(f"수리의 역할은 {ai}입니다. 역할놀이를 시작해볼까요?", lang='ko')
        #       tts.save("./hackertone/role_guide.mp3")
        #       playsound("./hackertone/role_guide.mp3")
        #     while True:
        #         if role_state:
        #             playsound("./mp3/answer.mp3")
        #         # 사용자의 질문을 생성 
        #         user_question = request()
        #         role_state = True
        #         # return 값이 False인 경우 elif문을 빠져나옴 
        #         if role_playing(ai, user_question) is False:
        #             return False
        ##############################################################
        # if "종료" in question or "끝내" in question:
        #     playsound("./mp3/end.mp3")
        #     sys.exit(0)
        # # question이 None이 아니고 모든 조건이 충족되지 못할 경우 재귀호출 
        # else:
        #     playsound("./mp3/return.mp3")
        #     question = request()
        #     handle_command(question, documents) 
    # question이 None인 경우 재귀호출
    # else:
    #     playsound("./mp3/return.mp3")
    #     question = request()
    #     handle_command(question, documents) 


   # handle_command(question, documents)
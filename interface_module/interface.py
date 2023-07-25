from playsound import playsound
from stt import request
from qna_module import answer
from tts_module import story
from role_module import role_main
from role_module import role
import sys
import time
from gtts import gTTS



def handle_command(question, documents, qna_state):

    if question is not None:
        if "동화" in question or "읽기" in question or "읽어" in question:
            playsound("./mp3/ready.mp3")
            time.sleep(1)
            # speak 함수의 return값이 False일 경우 if문을 빠져나옴
            if story.speak() is False:
                return False
        elif "질문" in question or "큐앤" in question:
            # return 값이 True일 경우에 while문 반복
            while True:
                # 질문을 처음 시작할 경우 '질문을 시작해주세요' 재생
                if qna_state:
                    playsound('./mp3/answer.mp3')
                # 두번째 질문부터 효과음 재생
                else:
                    playsound("./mp3/question.mp3")
                # 사용자의 음성을 인식받는 새로운 tts 객체 생성
                user_question = request()
                qna_state = True
                # ask 함수의 return값이 False일 경우 while문 elif문을 빠져나옴
                if answer.ask(documents, user_question) is False:
                    qna_state = False
                    return False
        ##############################################################
        elif "역할" in question or "놀이" in question:
            playsound("./mp3/user_role.mp3")
            while True:
                user_role = request()
                if user_role is not None and user_role is not "":
                    playsound("./mp3/ai_role.mp3")
                    ai_role = request()
                    if user_role is not None and user_role is not "" and ai_role is not None and user_role is not "":
                        tts = gTTS(f"사용자의 역할은 {user_role}이고 토리의 역할은 {ai_role}입니다. 역할놀이를 시작해볼까요?", lang='ko')
                        tts.save("./mp3/role_guide.mp3")
                        playsound("./mp3/role_guide.mp3")
                        user_question = request()
                if role_main.ask(user_role, ai_role, user_question) is False:
                    return False
        ##############################################################
        elif "종료" in question or "끝내" in question:
            playsound("./mp3/end.mp3")
            sys.exit(0)
        # question이 None이 아니고 모든 조건이 충족되지 못할 경우 재귀호출 
        else:
            playsound("./mp3/return.mp3")
            question = request()
            handle_command(question, documents, qna_state) 
    # question이 None인 경우 재귀호출
    else:
        playsound("./mp3/return.mp3")
        question = request()
        handle_command(question, documents, qna_state) 


    handle_command(question, documents, qna_state)

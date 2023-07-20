from playsound import playsound
from stt import request
from qna_module import answer
from tts_module import story
import sys
import time


def handle_command(question, documents, qna_state):

    if question is not None:
        if "읽어" in question:
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

from playsound import playsound
from qna_module import answer_stt
import sys



def ask(user_role, ai_role, question):


  # ------------------------------------------------
  # sound Interface
  # ------------------------------------------------
  # '뒤로'라는 단어를 포함한 문장을 말하면 메뉴선택 화면으로 이동
  if question is not None and '뒤로' in question or '메뉴' in question:
    return False
    # '종료'라는 단어를 포함한 문장을 말하면 시스템을 종료
  elif question is not None and '종료' in question or '끝내' in question:
    playsound("./mp3/end.mp3")
    sys.exit(0)
    # 질문과 답변이 계속 실행
  elif question is not None:
    # 사용자의 질문에 대한 답변을 가지고 있는 변수
    # answer = chain(question)
    # answer_stt.result(answer['answer'])
    return True
    # 모든 조건이 충족하지 못해도 새로운 질문을 시작
  else:
    return True
    

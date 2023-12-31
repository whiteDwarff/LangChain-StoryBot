# 1. 팀 소개

---

**팀명 : 뉴런스(Neurons)**

[팀 명단](https://www.notion.so/80e5d9fb15ef43e2a9f5c9e0b0b9ba8e?pvs=21)

# 2. 작품 개요

---

> **작품명**
> 

**LangChain을 활용한 ChatGPT 기반 수학 튜터**

> **한줄 소개**
> 

AI **ChatGPT** 기반 튜터는 **수학 PDF 학습**을 통해 아이들의 이해력과 지식을 높이며 **수학자와의 대화**로 창의적 사고를 촉진하는 중요한 교육 도구로 아이들의 미래를 발전시키는 역할을 합니다.

> **개발 동기**
> 

AI 튜터는 **아이들과 이야기**를 나누는 데 있어 매우 유용한 도구입니다. 

**수학 PDF를 학습**하여 아이들의 **이해력**을 높이고,  **지식**을 확장하는 데 도움이 될 수 있습니다. 

**다양한 PDF 학습을 통해 수학뿐 아니라 다양한 과목으로 확대, 교육적 가치 제공**

이러한 AI 튜터는 아이들의 교육에 기여하고,, 창의적인 사고를 발전시킬 수 있습니다. 

아이들의 미래를 위한 중요한 발판이 되기위해 AI 튜터 서비스를 개발하였습니다.

> **사용 방법**
> 

(1) 인베딩 되어있는 젯슨나노를 구동한다.

(2) 음성을 활용해 원하는 질문을 한다. 

예) 정수는 짝수와 홀수로 나뉘는 이유가 무엇인가요?

(3) 학습된 AI가 사용자의 질문에 알맞는 대답을 한다. 

예) 정수는 2로 나누어 떨어지는 수와 떨어지지 않는 수로 나눌 수 있기 때문입니다.

(4) 질문을 반복하거나 수학자와 역할놀이를 한다.

예) 역할놀이 할래!

(5) 학습된 수학자와 대화한다. 

예) 넌 누구야?

(6) 학습된 수학자가 답변한다.

예) 난 수학자 가우스야! 무엇을 도와줄까? 재밌는 얘기 해줄까?

(7) 종료한다.

# 3. 세부 내용

**사용기술, 구현방안 등 작품에 대한 자세한 사항을 자유롭게 알려주세요.**

---

무언가를 배울 때 항상 따라다니는 책. 

저희는 **교과서(책) 중심의 공부가아닌** AI와 함께 **자기주도적 공부**를 할 수 있도록 도움을 주기위한 솔루션인            AI 튜터는 학습 내용을 이해하고 소화하는 과정에서 상호작용하며, 문제 해결 능력을 향상시키고 실생활에 적용할 수 있는 실용적인 지식을 강조합니다. 

이를 통해 학생들은 더욱 주도적으로 학습하며, 지식을 이해하고 활용할 수 있는 능력을 발전시킬 수 있습니다.

- **사용 기술 :**
    - Jetson Nano
    - LangChain
    - ChromaDB
    - ChatGPT
    - Python
    - Text-to-Speech
    - Speech-to-Text

- **준비물 :**
    - Jetson Nano
    - BredBoard
    - LED
    - 저항
    - 점퍼 케이블
    - 모니터
    - 마우스
    - 키보드

- **구현 과정 :**
    1. 학습 PDF 데이터 만들기
    2. 학습 PDF 데이터에 맞는 프롬프트 엔지니어링
    3. 파이썬에서 LangChain과 ChromaDB를 통한 PDF 데이터 학습하기 (LLM, OpenAI)
    4. 사용자 기능에 맞는 로직 구현하기
    5. 파이썬 코드 모듈화 및 통합하기
    6. Jetson Nano 환경설정 및 가상환경 구축하기
    7. Jetson Nano에 파이썬, 렝체인 코드 임베딩하기
    8. 테스트
    9. 하드웨어 제품으로 연결하기
    10. Jetson Nano 구동으로 제품 작동

# 4. 기대 효과

**작품을 통해 얻을 수 이점, 발전 방향성 등을 알려주세요.**

---

**이점**

1. **자기주도적 학습 강화**: 기존의 교과서 중심 학습보다 더욱 자기주도적인 학습 경험을 제공
2. **상호작용적 학습**: 상호작용은 학습 동기를 높이고 지루함을 줄여주어 지식 습득을 더욱 효과적으로!
3. **창의적 사고 촉진**: 수학자와의 대화와 역할놀이를 함으로써 수학에 대한 개념을 게임이나 이야기를 통해 접근하게 한다.
4. **문제 해결 능력 강화**: 문제 해결 시나리오를 통해 어린이들은 현실 세계의 문제를 수학적으로 분석하고 해결하는 능력을 키울 수 있습니다.
5. **높은 동기부여**: 대화, 해결 과정에서의 성취감, 창의적 역할놀이 등이 어린이들에게 지식 습득에 대한 즐거움과 동기부여를 한다.

**차별화** 

렝체인을 활용해 인공지능의 고질적인 **Hallucination(환각)** 문제 최소화

PDF로 원하는 학습 데이터를 만들어 학습시켜 더욱 다양한 분야에서 활용가능한 범용성

아이들을  대상으로 보이스컨트롤에 집중한 서비스 기획

**향후 계획** 

상호작용할 수 있는 교육 환경 교육으로 수학 뿐 아니라 다양한 과목으로 확대**,** 교육적 가치 제공
미국**,** 한국**..** 이미 시작된 태블릿 교육 환경을 따라가 AI수리를 발전시킬 것

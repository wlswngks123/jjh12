# setting
커스텀 Dockerfile, requirements.txt 설정 확인

# testing
터미널 열고 streamlit hello 입력

# 패키지 추가 설치
버전에 맞는 pypi 검색 후, requirements.txt에 추가
(ex) pandas==2.2.3
텍스트 파일 저장 후
pip install -r requirements.txt

# Custom Chatbot Guide
## base 버전 실행: 기본 템플릿 제작
streamlit run custom_chatbot/st_chatbot_ver0_base.py
## session: 대화 기록이 남도록 세션 조정 
streamlit run custom_chatbot/st_chatbot_ver1_session.py
## history: 대화 요약 기억(Memory) 기능 추가
streamlit run custom_chatbot/st_chatbot_ver2_history.py
## add_func: ChatGPT Temperature 조정 슬라이더, 답변 스타일
streamlit run custom_chatbot/st_chatbot_ver3_add_func.py
## RAG: 사용자 업로드 파일에 대한 RAG / 추천 질문까지 추가
streamlit run custom_chatbot/st_chatbot_ver4_RAG2.py

## 강의 실습
기능 추가 예시 리스트
1. 소스 코드의 프롬프트 엔지니어링 수행 및, 헤더, 타이틀 등 텍스트나 레이아웃 등 전반적인 서비스 커스텀 수행
2. 대화 기록 저장 기능 추가 (excel, txt 확장자)
3. 이전 대화 내용이나 추천 질문에 따라 챗봇이 대화를 유도하거나 다음 질문을 제안할 수 있도록 기능 추가


# Auto_QnA Guide
## base 버전 실행: 템플릿 제작
streamlit run Auto_QnA/st_QnA_ver0_base.py
## Layout: 레이아웃 스마트폰 채팅처럼 구현
streamlit run Auto_QnA/st_QnA_ver1_layout.py
## History: 대화 기록 세션, 메모리 구현되도록 개발
streamlit run Auto_QnA/st_QnA_ver2_history.py
## Multiple RAG: 백엔드에서 다중 문서 업로드 가능하도록 LangChain 기능 개발
streamlit run Auto_QnA/st_QnA_ver3_multi_RAG.py
## Question_REC: Vector Store로 등록된 문서에 대한 추천 질문 생성 / 간단한 프롬프트 수정으로 다음 추천 질문 생성
streamlit run Auto_QnA/st_QnA_ver4_Qustion_REC2.py

## 강의 실습
1. 소스 코드의 프롬프트 엔지니어링 수행 및, 헤더, 타이틀 등 텍스트나 레이아웃 등 전반적인 서비스 커스텀 수행
2. 자동 언어 전환 기능: 고객이 질문을 작성할 때 사용하는 언어를 자동으로 감지해, 그 언어에 맞춰 AI가 응답하도록 하여 여러 언어를 자연스럽게 지원
3. 고객 만족도 평가 기능: 응답 후에 고객이 해당 답변에 만족했는지 평가할 수 있는 기능을 추가해, 평가 결과를 반영하여 모델의 응답 품질을 개선하는 데 활용
4. 고객 감정 분석 기능: 고객의 메시지에서 감정을 분석해 기쁨, 화남, 슬픔 등의 감정을 인식하도록 하여, 고객 만족도 평가 없이도 반응을 수집할 수 있도록 구현, 백엔드에서 로그 txt 형태나, csv 파일로 반응이 저장되도록 구성


# Blog_Bot Guide
## base 버전 실행: 템플릿 제작
streamlit run Blog_Bot/st_Blog_ver0_base.py
## add_func: 블로그 좌측 사이드바에 다양한 기능 추가
streamlit run Blog_Bot/st_Blog_ver1_add_func.py
## SEO: 블로그 사이드바에 SEO 관련 기능 추가 (프롬프트 엔지니어링 기능)
streamlit run Blog_Bot/st_Blog_ver2_SEO.py
## Translation: 블로그 작성 후 다중 언어로 번역하는 기능 추가
streamlit run Blog_Bot/st_Blog_ver3_Translation.py
## Translation: 블로그 작성 후 SEO 피드백 기능 추가
streamlit run Blog_Bot/st_Blog_ver4_SEO2.py
## 강의 실습
1. 소스 코드의 프롬프트 엔지니어링 수행 및, 헤더, 타이틀 등 텍스트나 레이아웃 등 전반적인 서비스 커스텀 및 보완 수행
2. 블로그 포스트 편집 기능: 생성된 블로그 포스트를 텍스트 에디터에 불러와서 사용자가 직접 수정할 수 있도록 하는 기능을 추가
3. 자동 키워드 생성 및 삽입: SEO를 강화하기 위해, 주제에 따라 관련된 키워드를 AI 모델에 요청해 자동으로 추천하고, 해당 키워드를 블로그 포스트의 적절한 위치에 배치하는 기능을 추가
4. 표 자동 생성: 블로그 내용에서 표가 추가될 파트가 있으면 추가하는 프롬프트 및 streamlit 웹 구현



!export OPENAI_API_KEY=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

y


conda install -c conda-forge faiss-cpu pypdf

import streamlit as st
from groq import Groq
st.set_page_config(page_title="PLACEMENT PREPARATION",page_icon="😍",layout="centered")
st.title("AI_INTERVIEW_ASSISTANT")
st.caption("Practice and prepare for placement")
st.caption("Launched by Harshitha K T")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except(Keyerror, FileNotFound):
  st.error("API Key is missing.Add it in advanced settings")
  st.stop()
role=st.selectbox('Job Title',['Machine learning engineer','Deveops engineer','Prompt engineer','Senior software engineer','Others'])
if role=="Others":
  st.text_input("Enter you job title","XXXXXX")
model=st.selectbox('Model',['openai/gpt-oss-120b', 'openai/gpt-oss-safeguard-20b'])
level=st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])
mode=st.radio('Activity',['Generate questions','Generate code questions','Evaluate answers','Improve answers'])
if mode=='Generate questions':
  count=st.slider("Number of questions",1,10,5)
elif mode=='Generate code questions':
  topic=st.selectbox('Topics',['sql','Aiml','Python','Dsa','C++','C','Java','PHP','DevOps','Web development','Cyber security'])
  count=st.slider("Number of Questions",1,10,5)
else:
  question=st.text_area('Enter Interview Question here')
  answer=st.text_area('Enter your answer',height=160)
if st.button("Generate AI response",type="primary"):
if mode=['Evaluate answers','Improve answers'] and (not question.strip()) or (not answer.strip())
  st.warning("Please enter question and answer")
  st.stop()

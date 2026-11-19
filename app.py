import streamlit as st
from groq import Groq
st.set_page_config(page_title="Placement Practice",page_icon='🥰',layout="centered")
st.title("AI Interview Assistant")
st.caption("Practice and Prepare for our Interview")
try:
  client=Groq(api_key=st.secrets["GROQ_API_KEY"])
except(Keyerror,FileNotFound):
  st.error("API key is missing.Add it in advanced settings")
  st.stop() 
role=st.selectbox('Job Title',['Machine Learning Engineer','Senior Software Engineer','Devops Engineer','Data Analyst','other'])
if role=="other":
  st.text_input('Enter you Job Title','XXXXXXX')
  model=st.selectbox('Model',['openai/gpt-oss-20b','qwen/qwen3.8-27b'])
  level=st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])  
  mode = st.radio('Activity',['Generate Questions','Generate Code','Evaluate Answers','Improve Answers'])
if mode=='Generate Questions':
  count=st.slider("Number of Questions",1,10,5)
elif mode=='Generate Code Questions':
  topic=st.selectbox('Topics',['SQL','AIML','Python','DSA','C/C++','Java','Cyber Security','Web Developer'])
  count=st.slider("Number of Questions",1,10,5)
else:
  question=st.text_area('Enter Interview Questions here')
  answer=st.text_area('Enter your answer',height=160)




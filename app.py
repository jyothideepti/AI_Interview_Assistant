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
role=st.selectbox('Job Title',['Machine Learning Enginerr','Senior Software Enginerr','Devops Engineer','Data Analyst','other'])
if role=="other":
  st.text_input('Enter you Job Title','XXXXXXX')
  model=st.selectbox('Model',['openai/gpt-oss-20b','qwen/qwen3.8-27b'])
  level=st.selectbox('Difficulty',['Beginner','Intermediate','Advanced'])  
  mode = st.radio('Activity',['Generate Questions','Generate Code','Evaluate Answers','Improve Answers'])

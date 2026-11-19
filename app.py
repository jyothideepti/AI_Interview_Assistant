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
  gen_model=st.selectbox('Model',['openai/gpt-oss-120b', 'openai/gpt-oss-safeguard-20b'])
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
if st.button('Generate AI response', type="primary"):
  if mode in ['Evaluate Answers','Improve Answers'] and (not question.strip() or not answer.strip()):
    st.warning("Please enter question and answer")
    st.stop()
    topics = "Topics is " + topic + "Difficulty is " + level
  if mode == "Generate Questions":
    task = "Generate " + str(count) + " Frequently asked Interview Questions 3 theory and 2 Scenario Questions. Do not give answers. Give Hints"
  elif mode == 'Generate Code Questions':
    task = "Generate " +  str(count) + " Frequency asked coding questions on topic "+topic+" and give hints to solve them. Be accurate"
  elif mode == "Evaluate Answers":
    task="Questions:" + question + "My Answer : " +answer+ " Evaluate answer based on concept,relavent,communication and length of answer"
  elif mode == "Improve Answer":  
    task="Questions " +question+"My answers"+answer+ " Improve answer based on choice of words,key words,accuracy,concept,relevant,better explanation and choice of words"
    background = "Job role : " +role+ " Difficulty level "+level
with st.spinner("Generating your answer..."):
try:
    response=client.chat.completions.create(
    model=gen_model,
    messages=[{"role":"system","content":"You are an expert technical interviewer"},
                {"role":"user",
                "content":background+task}],
    temperature=0.7,
    max_tokens=2000)
    output = response.choices[0].message.content
    st.subheder("AI Response ")
    st.markdown(output)
    st.download_button("Download Response", output, file_name = "Interview_Response.txt", mime = 'text/plain')
  except Exception as e:
    st.error ("API connection was unsuccessful: ",e)
    st.info  ("Please check your API Key and rate limits")
    st.caption("Powered by Streamlit.io and GitHub.Using LLM API")
    

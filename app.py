import streamlit as st
from rag_engine import load_base, ask_rag
st.set_page_config(page_title = "SIET_Chatbot", layout = "centered")
st.title("Shridevi Institute of Engineering and Technology - ChatBot")
st.caption("Ask anything about college information...")
st.caption("Created by Rashmitha")

mykey = st.secrets("GROQ_API_KEY")

@st.cache_resource #deconstructs already loaded data
def intiate_rag()
return load_base("01.College_Information.pdf")

index, embed_model, chunks = intiate_rag()

if"chat_hist" not in st.session_state:  #load and display vhat histroy
  st.session_state.chat_hist = []

for qa in st.session.chat_hist:  #qa here is question and answer
  with st.chat_message(qa["role"]):
    st.write(qa["content"])

question = st.chat_input("Ask anything about SIET college....")

if question:
  st.session_state.chat_hist.append(
    ("role" :"user" , content = question))      #append is used to add the question in the list i.e., chat history is the list.
with st.chat_message("user")
  st.write(question)

with st.chat_message("assistant")
 with st.spinner("Asking RAG for for answer...")
   answer = ask_rag (question, embed_model, chunks, index, api_key = mykey, num_chunks)
   st.write(answer)

if st.button("Clear chat")
  st.session_state.chat_hist = []
  st.rerun()
    

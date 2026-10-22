import streamlit as st
from ollama import chat
from pypdf import PdfReader
st.set_page_config(
    page_title="AI Study Buddy",
    page_icon="🎓",
    layout="wide"
)
st.title("AI Study Buddy") #App title
st.write("Your personal AI study companion")

if "history" not in st.session_state: #create memory for chat history
    st.session_state["history"] = []
with st.sidebar:
    st.title("🎓 Study Buddy")
    st.write("Your AI learning assistant")
    uploaded_file = st.file_uploader(
    "Upload your lecture notes",
    type=["pdf"]
    )
    if uploaded_file is not None:
        reader = PdfReader(uploaded_file)

        text = ""

        for page in reader.pages:
                text += page.extract_text() or ""

        st.write(text[:500])
    if uploaded_file is not None:
        st.success("PDF uploaded successfully!")
        st.write(uploaded_file.name)
    

    if st.button("➕ New Chat"):
        st.session_state["history"] = []
        st.rerun()
for message in st.session_state["history"]: #read old chats
    with st.chat_message(message["role"]):
        st.write(message["content"])
question= st.chat_input("Ask a question: ") # space to write a question
if question: #save the question
    st.session_state["history"].append({"role":"user","content":question})
with st.chat_message("user"): #show the question
    st.write(question)
# Get the AI's response
rep = chat(
        model="qwen3:4b",
        messages=st.session_state["history"]
    )
answer=rep.message.content
with st.chat_message("assistant"): #show the answer
    st.write(answer)
st.session_state["history"].append({ # save the answer
        "role": "assistant",
        "content": answer
    })
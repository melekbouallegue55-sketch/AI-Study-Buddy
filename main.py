from ollama import chat
history=[]
while True:
    question=input("Ask a question: ")
    if question.lower() in ["exit","stop","quit"]:
        break
    history.append({"role":"user","content":question})
    rep=chat(
        model="qwen3:4b",
        messages=history
    )
    answer=rep.message.content
    print("AI:",answer)
    history.append({"role":"assistant","content":answer})
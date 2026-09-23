import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
        "role":"system",
        "content":"Give the answer in 2 lines.Iam a teacher of  5 years old kid"
        },
        {
            "role":"user",
            "content":"Explain ai"
        }
    ]
)
print(response["message"]["content"])
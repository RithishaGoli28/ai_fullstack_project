import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Give Defination of ai in 3 lines,and main 3 types of ai"
        }
    ]
)
print(response["message"]["content"])
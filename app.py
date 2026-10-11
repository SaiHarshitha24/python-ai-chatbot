
import ollama

print("🤖 My AI Chatbot")
print("Type 'exit' to stop chatting.")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("Bot:", response.message.content)

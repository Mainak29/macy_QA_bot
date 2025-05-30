from qa_bot import ask_question

while True:
    user_input = input("Hi, I am Macy. \n Ask your question (or 'exit'): ")
    if user_input.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    answer = ask_question(user_input)
    print("\nMacy :->   ", answer)

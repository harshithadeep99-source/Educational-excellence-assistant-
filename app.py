# Educational Excellence Assistant Chatbot

def chatbot():
    print("===================================")
    print(" Educational Excellence Assistant ")
    print("===================================")
    print("Type 'exit' to quit.\n")

    while True:
        user = input("You: ").lower()

        if user == "exit":
            print("Bot: Thank you! Have a great day.")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you with your studies?")

        elif "course" in user:
            print("Bot: We offer guidance on Engineering, Science, Mathematics, and Programming courses.")

        elif "exam" in user:
            print("Bot: Create a study schedule, revise important topics, and solve previous year question papers.")

        elif "study tips" in user:
            print("Bot: Study regularly, take short breaks, make notes, and practice problems daily.")

        elif "attendance" in user:
            print("Bot: Maintain at least 75% attendance for better academic performance.")

        elif "programming" in user:
            print("Bot: Learn Python, C, Java, and Data Structures through regular practice.")

        elif "vtu" in user:
            print("Bot: VTU students should focus on syllabus-based preparation and previous year papers.")

        elif "help" in user:
            print("Bot: Ask me about courses, exams, study tips, attendance, VTU, or programming.")

        else:
            print("Bot: Sorry, I didn't understand. Please ask an education-related question.")

# Run chatbot
chatbot()

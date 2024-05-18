questions = [
    {
        "Prompt": "The “Father of Artificial Intelligence” is:",
        "Options": ["A. John McCarthy", "B. Alen Turing", "C. Charles Babbage", "D. None of the Abovea"],
        "Answer": "A"
     },
    {
        "Prompt": "Which of the following is not an application of artificial intelligence?",
        "Options": ["A. Computer Vision", "B. NLP", "C. Database Management System", "D. Digital Assstants"],
        "Answer": "C"
     },
    {
        "Prompt": "Which of the following are informed search methods?",
        "Options": ["A. Best Fist Search", "B. A* Search", "C. Memory Bound Huristic Search", "D. All of the Above"],
        "Answer": "D"
     },
    {
        "Prompt": "The correct ways to solve a problem of state-space search are?",
        "Options": ["A. Forward for the initial State", "B. Backword from the goal", "C. Both A and B", "D. None of the Above"],
        "Answer": "C"
     }
]
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["Prompt"])
        for option in question["Options"]:
            print(option)
        answer = input("Enter your Answer (A, B, C or D): ").upper()
        if answer == question["Answer"]:
            print("Correct!\n ")
            score += 1
        else: 
            print("Wrong! The correct answer was", question["Answer"], "\n")

    print(f"You got {score} out of {len(questions)} Questions correct!")

run_quiz(questions)

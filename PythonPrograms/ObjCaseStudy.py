userslist = [
    {'uname':'Sowmya','upwd':'sowmya','secq':'what is your pet name: ','seca':"chotu"},
    {'uname':'Sowmith','upwd':'sowmith','secq':'what is your school name: ','seca':"srkr"}
]
def UserSignUp():
    user = {}
    user['uname'] = input("Enter User Name: \n")
    user['upwd'] = input("Enter Password: \n")
    user['sq'] = input("Enter security question: \n")
    user['sa'] = input("Enter security answer: \n")
    userslist.append(user)
    
def subMenu():
    questions = [
        {
            "question": "1) What is the capital of France?",
            "option1": "Berlin",
            "option2": "Madrid",
            "option3": "Paris",
            "option4": "Rome",
            "answer": "Paris"
        },
        {
            "question": "2) Which planet is known as the Red Planet?",
            "option1": "Earth",
            "option2": "Mars",
            "option3": "Jupiter",
            "option4": "Venus",
            "answer": "Mars"
        },
        {
            "question": "3) What is the largest mammal in the world?",
            "option1": "Elephant",
            "option2": "Blue Whale",
            "option3": "Great White Shark",
            "option4": "Giraffe",
            "answer": "Blue Whale"
        },
        {
            "question": "4) Which element has the chemical symbol O?",
            "option1": "Gold",
            "option2": "Oxygen",
            "option3": "Silver",
            "option4": "Hydrogen",
            "answer": "Oxygen"
        },
        {
            "question": "5) In which year did World War II end?",
            "option1": "1941",
            "option2": "1943",
            "option3": "1945",
            "option4": "1947",
            "answer": "1945"
        },
        {
            "question": "6) What is the square root of 64?",
            "option1": "6",
            "option2": "7",
            "option3": "8",
            "option4": "9",
            "answer": "8"
        },
        {
            "question": "7) What is the smallest prime number?",
            "option1": "1",
            "option2": "2",
            "option3": "3",
            "option4": "5",
            "answer": "2"
        },
        {
            "question": "8) What is the powerhouse of the cell?",
            "option1": "Nucleus",
            "option2": "Mitochondria",
            "option3": "Ribosome",
            "option4": "Golgi apparatus",
            "answer": "Mitochondria"
        },
        {
            "question": "9) Which language is primarily spoken in Brazil?",
            "option1": "Spanish",
            "option2": "French",
            "option3": "Portuguese",
            "option4": "English",
            "answer": "Portuguese"
        },
        {
            "question": "10) What is the chemical formula for water?",
            "option1": "H2O",
            "option2": "CO2",
            "option3": "O2",
            "option4": "NaCl",
            "answer": "H2O"
        }
    ]
    score = 0
    for q in questions:
        print(q['question'],q['option1'],q['option2'],q['option3'],q['option4'],sep='\n')
        ans = input("Enter your answer: \n")
        if ans == q['answer']:
            score += 1
        print("=======================")
    print("The correct answes are: ")
    for q in questions:
        print(q['answer'],end='\n===\n')
    return score

def UserSignIn():
    name = input("Enter User Name: \n")
    pwd = input("Enter Password: \n")
    x = 1
    y = 1
    for user in userslist:
        if user['uname'] == name and user['upwd'] == pwd:
            score = subMenu()
            user['score'] = score
            print(f"the score of {user['uname']} is {score}")
            x = 0
            y = 0
            break
        if user['uname'] == name and user['upwd'] != pwd:
            x = 0
        if user['uname'] != name and user['upwd'] == pwd:
            y = 0
    if x == 1 and y == 1:
        print("Invalid User name and password")
    elif x == 0 and y == 1:
        print("Invalid password")
    elif x == 1 and y == 0:
        print("Invalid username")

while True:
    print("Main Menu:\n")
    print("==================\n")
    print("1) User SignUp\n2) User SignIn\n3) Exit\n")
    n = int(input("Enter Choice: \n"))
    if n == 1:
        UserSignUp()
    elif n == 2:
        UserSignIn()
    elif n == 3:
        print("Exit\n")
        break
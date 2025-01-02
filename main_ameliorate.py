
"""
def ask_question(question_title, ans1, ans2, ans3, ans4, correct_answer):
    global score
    print(question_title)
    print("a-",ans1)
    print("b-",ans2)
    print("c-",ans3)
    print("d-",ans4)
    answer = input("T'as réponse : ")
    if answer == correct_answer:
        print("Bonne réponse, félicitations !")
        score += 1
    else:
        print(f"Mauvaise réponse, la bonne réponse était {correct_answer} !")


score = 0
ask_question("Quel est la capital du Mali?","Bamako", "Kidal", "Tombouctou", "Tombouctou", "a")
ask_question("Quel est la capital de l'Italie?","Milan", "Naples", "Rome", "Florence", "c")
ask_question("Quel est la capital du Japon?","Nagoya", "Kyoto ", "Osaka", "Tokyo", "d")
ask_question("Quel est la capital du Cameroun?","Douala", "Yaoundé", "Garoua", "Bamenda", "b")

print(f"Ton score est {score}")
"""
def ask_question(question):
    question_title = question[0]
    choice = question[1]
    correct_answer = question[2]
    global score
    print(question_title)
    print("a-",choice[0])
    print("b-",choice[1])
    print("c-",choice[2])
    print("d-",choice[3])
    answer = input("Ta réponse : ")
    if answer.lower() == correct_answer.lower():
        print("Bonne réponse, félicitations !")
        score += 1
    else:
        print(f"Mauvaise réponse, la bonne réponse était {correct_answer} !")



question0 = ("Quel est la capital du Mali?",("Bamako", "Kidal", "Tombouctou", "Segou"), "Bamako")
question1 = ("Quel est la capital de l'Italie?",("Milan", "Naples", "Rome", "Florence"), "Rome")
question2 = ("Quel est la capital du Japon?",("Nagoya", "Kyoto", "Osaka", "Tokyo"), "Tokyo")

score = 0

ask_question(question0)
ask_question(question1)
ask_question(question2)

print(f"Ton score est {score}")
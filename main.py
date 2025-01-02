

def ask_question(question, ans1, ans2, ans3, ans4, correct_answer):
    global score
    print(question)
    print("a-",ans1)
    print("b-",ans2)
    print("c-",ans3)
    print("d-",ans4)
    answer = input("Ta réponse : ")
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
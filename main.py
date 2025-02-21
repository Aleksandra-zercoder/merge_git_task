def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.lower()


if __name__ == '__main__':
    print("Grammar Exercise: Subject-Verb Agreement")
    print("Fill in the blank:")
    print("She ______ to school every day. (go/goes)")

    answer = input("Your answer: ")
    if check_answer(answer, "goes"):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is 'goes'.")


def ask_question(question, correct_answer):
    print("\n" + question)
    user_answer = input("Your answer: ")
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect. The correct answer is:", correct_answer)
        return 0


if __name__ == '__main__':
    score = 0
    total = 0

    print("English Grammar Exercises")
    print("=========================")

    # Упражнение 1: согласование подлежащего и сказуемого
    q1 = ("1. Fill in the blank: She ______ to school every day. (go/goes)")
    score += ask_question(q1, "goes")
    total += 1

    # Упражнение 2: времена глаголов
    q2 = ("2. Choose the correct tense: I ______ (to be) happy yesterday. (am/was)")
    score += ask_question(q2, "was")
    total += 1

    # Упражнение 3: использование артиклей
    q3 = ("3. Fill in the blank: I saw ______ elephant at the zoo. (a/an)")
    score += ask_question(q3, "an")
    total += 1

    print(f"\nYour total score: {score} out of {total}")


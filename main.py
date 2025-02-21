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

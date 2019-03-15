#jessica Weinburger
import sys
def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Error. IOError", e)
        input("\n\nPress the enter key to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

##file = open_file("test_file.txt", "w")
##file.write("this/ is a/ Test")
##file.close()
##
##file = open_file("test_file.txt", "r")
##line = next_line(file)
##print(line)

def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answer = [ ]
    for i in range(4):
        answers = next_line(the_file)
        answer.append(answers)
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answer, correct, explanation

##the_file = open_file("final.txt", "r")
##category, question, answer, correct, explanation = next_block(the_file)
##print(category)
##print(question)
##print(answer)
##print(correct)
##print(explanation)

def welcome(title):
    print("Welcome to Trivia Challenge")
    print(title)

def main():
    the_file = open_file("trivia1.txt", "r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answer, correct, explanation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(answer[i])
        answer = input("1, 2, 3, 4")
        if answer == correct:
            print("Congrats")
            score += 1
        else:
            print("Your answer was Incorrect")
        print(explanation)
        print(score)
        category, question, answer, correct, explanation = next_block(the_file)
    print("That is the end")
    print(score)
    input(the_file.close())

main()

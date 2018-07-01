from graph_func import gender_graphing
# from overall_survey import ques_to_question
from collections import defaultdict


def graph_string(question, people):
    f = open('results/strings/' + question + '.txt', 'w')
    # ques_to_question = ques_to_question()
    f.write("question: " + question + '\n\n')
    string_value = defaultdict(int)
    for person in people:
        value = getattr(person, question)
        if value != "":
            string_value[value] += 1

    for key in string_value.keys():
        f.write(str(key) + ": " + str(string_value[key]))
        f.write('\n')
    f.close()


def long_text(question, people):
    f = open('results/strings/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')
    for person in people:
        value = getattr(person, question)
        if value != "":
            f.write(value)
            f.write('\n')
            f.write('\n')

    f.close()


def graph_num(question, focus_var, people):
    # tbh the only question we care about in this function is university_gpa_TEXT
    f = open('results/numbers/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')

    different_responses = []

    for person in people:
        value = getattr(person, question)
        if value == "":
            pass
        elif value.isdigit() and int(value) < 5:
            different_responses.append(int(value))
        elif value.replace('.', '', 1).isdigit() and float(value) < 5:
            different_responses.append(float(value))

    different_responses.sort()

    for response in different_responses:
        f.write(str(response))
        f.write('\n')
    f.close()


def mult_choice(question, focus_var, options, people):
    if focus_var == 'gender':
        gender_graphing(question, options, people)
    #  elif # think about graduation date, major, age, etc

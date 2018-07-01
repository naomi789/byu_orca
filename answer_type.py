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
        f.write(str(key) + str(string_value[key]))
        f.write('\n')
    f.close()


def graph_int(question, var, people):
    print("graph int axis")


def graph_double(question, var, people):
    print("graph double axis")


def mult_choice(question, focus_var, options, people):
    if focus_var == 'gender':
        gender_graphing(question, options, people)
    #  elif # think about graduation date, major, age, etc

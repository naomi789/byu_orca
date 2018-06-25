from collections import namedtuple, defaultdict
import csv
from itertools import zip_longest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from answer_type import graph_string, graph_int, graph_double, graph_likert, graph_list
from constants import question_shorthand, question_string, answer_type, agreement, comfort, certainty, frequency, frequency_class, frequency_TA
from graph_func import ques_to_answer, gender_graphing, makeBoxWhisker, values_per_gender, bar_graph
import pprint


plt.style.use('seaborn-deep')

ques_to_question = []

Person = namedtuple('Person', question_shorthand)


def run_overall():
    with open('ORCA_overall_CS_edited.csv', 'r') as file:
        return list(csv.reader(file, delimiter=','))


def ques_to_question():
    if len(question_shorthand) is not len(question_string):
        print(len(question_shorthand))
        print(len(question_string))
        print("mapping SHORTHAND questions to question error")
        exit(1)
    else:
        ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
        return ques_to_question


def parse_data(data):
    all_people = list(map(lambda line: Person(*line), data))
    all_students = []
    for person in all_people: # filters out all responses where there is no gender
        if getattr(person, 'gender') is not '':
            all_students.append(person)
    return all_students


def pick_graphing_style(ques_text_ans, people):
    # decide what we're looking at
    focus_var = ['gender'] # ['gender', 'gradu_year', 'cs_not_major']  # maybe GPA, too?
    likert_questions = ['certainty', 'agreement', 'frequency', 'frequency_TA', 'frequency_class', 'comfort']

    for var in focus_var:
        #  actually pick how to graph it
        for question in question_shorthand:
            # if ques_text_ans[question] == 'string':
            #     graph_string(question, var, people)
            # elif ques_text_ans[question] == 'int':
            #     graph_int(question, var, people)
            # elif ques_text_ans[question] == 'double':
            #     graph_double(question, var, people)
            # elif ques_text_ans[question] == 'list':
            #     graph_list(question, var, people)
            # el
            if ques_text_ans[question] in likert_questions:
                graph_likert(question, var, ques_text_ans[question], people)





data = run_overall()
ques_to_question = ques_to_question()
data = data[2:]  # deletes the question text and shorthand from the dataset

people = parse_data(data)

ques_ans = ques_to_answer()
pick_graphing_style(ques_ans, people)


#  xvalueQuesText = ['\n'.join(wrap(l, 18)) for l in xvalueQuesText]
# ^^ if things are too long
# https://github.com/byuhci/vat_analyzer/blob/master/subjectiveAnswers.py
# options = defaultdict(set)  # holds no duplicates

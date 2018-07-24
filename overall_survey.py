from collections import namedtuple, defaultdict
import csv
from itertools import zip_longest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from answer_type import mult_choice, graph_string, graph_num, long_text
from constants import BYU_question_shorthand, BYU_question_string, do_not_graph
    # , answer_type, agreement, comfort, certainty, frequency, frequency_class, frequency_TA
from list_constants import likert_question_answer_types, list_question_answer_types
from graph_func import ques_to_answer\
    # , gender_graphing, makeBoxWhisker, values_per_a_and_b, bar_graph
import os
    # import pprint

plt.style.use('seaborn-deep')

Person = namedtuple('Person', BYU_question_shorthand)


def run_overall(file_name):
    print(os.path.dirname(os.path.realpath(__file__)))
    print(file_name)
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=','))


def ques_to_question():
    if len(BYU_question_shorthand) is not len(BYU_question_string):
        print(len(BYU_question_shorthand))
        print(len(BYU_question_string))
        print("mapping SHORTHAND questions to question error")
        exit(1)
    else:
        return dict(zip_longest(BYU_question_shorthand, BYU_question_string[:len(BYU_question_shorthand)]))


def parse_overall_data(data):
    all_people = list(map(lambda line: Person(*line), data))
    all_students = []
    for person in all_people:  # filters out all responses where there is no gender
        if getattr(person, 'gender') is not '':
            all_students.append(person)
        #  todo: should also check that other values are not '' # ['gender', 'gradu_year', 'cs_not_major']  # maybe GPA, too?
    return all_students


def pick_graphing_style(ques_text_ans, people):
    possible_focus_var = ['university_program', 'university_graduation_year', 'university_major', 'gender']  # maybe GPA, too?

    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:
            print("focus_var: " + focus_var + " question number: " + str(counter))
            print('question: ' + question)
            counter += 1
            answer_type = ques_text_ans[question]
            print('answer_type: ' + answer_type)
            if question in ['describe_positive_experience', 'describe_negative_experience', 'suggestion_improve_institution']:
                long_text(question, people)
            elif ques_text_ans[question] == 'string':
                graph_string(question, people)
            elif ques_text_ans[question] == 'int' or ques_text_ans[question] == 'double':
                graph_num(question, focus_var, people)
                temp = 'trash'
            elif answer_type in likert_question_answer_types:
                mult_choice(question, focus_var, ques_text_ans[question], people, answer_type)
            elif answer_type in list_question_answer_types:
                mult_choice(question, focus_var, ques_text_ans[question], people, answer_type)
            elif answer_type in do_not_graph:
                pass
            else:
                print("question: " + question + " ques_text_ans[question]: " + answer_type)


data = run_overall('raw_overall_survey/overall_data_prepped_BYU.csv')  # ./fake_data/ORCA_overall_CS_edited.csv
ques_to_question = ques_to_question()
data = data[2:]  # deletes the question text and shorthand from the dataset

people = parse_overall_data(data)

ques_ans = ques_to_answer() # this thing
pick_graphing_style(ques_ans, people)

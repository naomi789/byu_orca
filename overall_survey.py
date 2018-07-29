from collections import namedtuple, defaultdict
import csv
from itertools import zip_longest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from answer_type import mult_choice, graph_string, graph_num, long_text, compare_confidence_GPA
from graph_func import call_respective_graphing_functions, filter_and_graph
from constants import BYU_question_shorthand, BYU_question_string, do_not_graph
# , answer_type, agreement, comfort, certainty, frequency, frequency_class, frequency_TA
from list_constants import likert_question_answer_types, list_question_answer_types
import os
from data_structures import ques_ans

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
    counter = 0
    for person in all_people:  # filters out all responses where there is no gender
        counter += 1
        if getattr(person, 'gender') is not '':
            all_students.append(person)
        #  todo: should also check that other values are not '' # ['gender', 'gradu_year', 'cs_not_major']  # maybe GPA, too?
    print('there were ' + str(counter) + ' participants.')
    return all_students


# need to refactor 'ques_text_ans' the obj that contains ques : ans_type
def pick_graphing_style(ques_ans, people):
    possible_focus_var = ['gender', 'university_program', 'university_graduation_year', 'university_major']  # maybe GPA, too?
    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:
            answer_type = ques_ans[question]

            if question == 'people_sexist_jokes_gender':
                current_bug = 23

            print('\nfocus_var: ' + focus_var + " question number: " + str(counter))
            print('question: ' + question)
            counter += 1
            print('answer_type: ' + answer_type)

            if question in ['describe_positive_experience', 'describe_negative_experience',
                            'suggestion_improve_institution']:
                long_text(question, people)
            elif answer_type == 'string':
                graph_string(question, people)
            elif answer_type == 'int' or answer_type == 'double':
                graph_num(question, focus_var, people)
            elif answer_type in likert_question_answer_types:
                categories = mult_choice(focus_var)
                list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question,
                                                                                               answer_type, people,
                                                                                               focus_var, categories)
                call_respective_graphing_functions(question, focus_var, answer_type, list_all_answers_per_category,
                                                   answer_to_count_per_category, categories)



data = run_overall('raw_overall_survey/overall_data_prepped_BYU.csv')  # ./fake_data/ORCA_overall_CS_edited.csv
ques_to_question = ques_to_question()
data = data[2:]  # deletes the question text and shorthand from the dataset

people = parse_overall_data(data)

# ques_ans = ques_to_answer() # this thing is the root of most evil
# print(ques_ans)

# the one that actually does stuff
# pick_graphing_style(ques_ans, people)

# some other random graphs
compare_confidence_GPA(people, 'gender')



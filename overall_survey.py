from collections import namedtuple
import csv
from itertools import zip_longest
import matplotlib.pyplot as plt
from answer_type import mult_choice, graph_string, graph_num, long_text, compare_confidence_GPA, \
    associate_with_professors, time_confidence
from graph_func import call_respective_graphing_functions, filter_and_graph
from constants import BYU_question_shorthand, BYU_question_string
from list_constants import likert_question_answer_types, list_question_answer_types, confidence_measurement, long_feedback
import os
from data_structures import ques_ans
import logging


plt.style.use('seaborn-deep')

Person = namedtuple('Person', BYU_question_shorthand)


def run_overall(file_name):
    print(os.path.dirname(os.path.realpath(__file__)))
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=','))


def ques_to_question():
    if len(BYU_question_shorthand) is not len(BYU_question_string):
        for long_ques, short_ques in zip(BYU_question_string, BYU_question_shorthand):
            if long_ques == 'If members of the CS department (students/TAs/professors/etc) make negative comments about your appearance what do they comment about? (select all that apply)':
                pass
            print(long_ques)
            print(short_ques)
            print('\n')
        print(str(len(BYU_question_shorthand)) + str(BYU_question_shorthand))
        print(str(len(BYU_question_string)) + str(BYU_question_string))
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


def assorted_special_graphs(people):
    compare_confidence_GPA(people, 'gender')

    for type_of_feedback in ['describe_positive_experience', 'describe_negative_experience']:
        associate_with_professors(people, type_of_feedback)


def pick_graphing_style(people):
    possible_focus_var = ['university_graduation_year', 'gender', 'university_program', 'university_major']
    # ,'major_and_gender', 'university_graduation_year_and_gender']  # maybe GPA, too?
    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:
            answer_type = ques_ans[question]

            print('\nfocus_var: ' + focus_var + " question number: " + str(counter))
            print('question: ' + question)
            counter += 1
            print('answer_type: ' + answer_type)

            if question in long_feedback:
                long_text(question, people)
            elif answer_type == 'string':
                graph_string(question, people)
            elif answer_type == 'int' or answer_type == 'double':
                graph_num(question, focus_var, people)
            elif answer_type in likert_question_answer_types or answer_type in list_question_answer_types:
                category_names = mult_choice(focus_var)
                list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, answer_type,
                                                                                               people, focus_var,
                                                                                               category_names)
                call_respective_graphing_functions(question, focus_var, answer_type, list_all_answers_per_category,
                                                   answer_to_count_per_category, category_names)

                if question in confidence_measurement and focus_var == 'university_graduation_year':
                    time_confidence(question, focus_var, answer_to_count_per_category, list_all_answers_per_category,
                                    category_names)


# if __name__ == "__main__":  # needed if I decide to include this file elsewhere
# logging.basicConfig(level=logging.DEBUG)  # or 'INFO', 'WARNING', 'ERROR', 'CRITICIAL'
# logging.info('asdf')

data = run_overall('raw_overall_survey/overall_data_prepped_BYU.csv')  # ./fake_data/ORCA_overall_CS_edited.csv
ques_to_question = ques_to_question()

print(ques_to_question)

data = data[2:]  # deletes the question text and shorthand from the dataset

people = parse_overall_data(data)

# the one that actually does stuff
pick_graphing_style(people)

# does other graphs
assorted_special_graphs(people)



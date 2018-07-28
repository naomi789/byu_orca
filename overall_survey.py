from collections import namedtuple, defaultdict
import csv
from itertools import zip_longest
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from answer_type import mult_choice, graph_string, graph_num, long_text, compare_confidence_GPA
from constants import BYU_question_shorthand, BYU_question_string, do_not_graph
# , answer_type, agreement, comfort, certainty, frequency, frequency_class, frequency_TA
from list_constants import likert_question_answer_types, list_question_answer_types
from graph_func import ques_to_answer \
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
    counter = 0
    for person in all_people:  # filters out all responses where there is no gender
        counter += 1
        if getattr(person, 'gender') is not '':
            all_students.append(person)
        #  todo: should also check that other values are not '' # ['gender', 'gradu_year', 'cs_not_major']  # maybe GPA, too?
    print('there were ' + str(counter) + ' participants.')
    return all_students


# need to refactor 'ques_text_ans' the obj that contains ques : ans_type
def pick_graphing_style(ques_text_ans, people):
    possible_focus_var = ['gender', 'university_program', 'university_graduation_year', 'university_major']  # maybe GPA, too?
    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:
            answer_type = ques_text_ans[question]

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

# ques_ans = ques_to_answer() # this thing is the root of most evil
# print(ques_ans)
temp = {'duration_seconds': 'int', 'Location_Latitude': 'double', 'LocationLongitude': 'double',
        'consent_current': 'string', 'consent_future': 'string', 'email': 'string', 'gender': 'string',
        'gender_other': 'race', 'race': 'int', 'age': 'string', 'university_program': 'double',
        'university_major': 'string', 'university_minor': 'string', 'university_courses_fall': 'courses',
        'university_graduation_year': 'string', 'university_gpa': 'string', 'university_gpa_TEXT': 'double',
        'received_internship_offer': 'yes_no', 'extracurriculars': 'extracurriculars', 'major_pros': 'encouragement',
        'major_pros_TEXT': 'string', 'major_cons': 'barriers', 'major_cons_TEXT': 'string',
        'confidence_graduate_gpa': 'agreement', 'confidence_prepared_courses': 'agreement',
        'confidence_percentile': 'percentile', 'participation_questions_comfortable_NONCS': 'comfort',
        'participation_absent_frequency': 'frequency_absent',
        'participation_questions_ask_frequency': 'frequency_class', 'participation_questions_comfortable': 'comfort',
        'participation_not_questions_frequency': 'frequency_class', 'participation_absent_why': 'miss_class',
        'participation_MORE_comfortable': 'increase_comfort', 'participation_LESS_comfortable': 'decrease_comfort',
        'participation_not_reasons': 'participate_decrease', 'participation_questions_ask_ignored': 'frequency_class',
        'participation_group_project_role': 'responsibilities', 'professors_ask_advice': 'frequency',
        'professors_encouraged_you': 'professor_encouragement', 'participation_TA_session': 'frequency_TA',
        'participation_TA_ask_questions': 'frequency', 'participation_talk_peers': 'frequency',
        'courses_professors_engaging': 'agreement', 'professors_represent_diversity': 'agreement',
        'role_models_same_gender': 'agreement', 'participation_peers_help_you': 'frequency',
        'participation_peers_you_serve': 'frequency', 'participation_clubs': 'meetings_clubs',
        'participation_friends_CS_students': 'percentage', 'friends_CS_students_want_more': 'agreement',
        'scholarship': 'scholarships', 'extracurricular_plans_before_graduation': 'involvement',
        'frequency_balance_career_parenthood': 'frequency', 'professors_declare_parent': 'frequency',
        'professors_declare_full_time': 'frequency', 'department_sexist_you': 'certainty',
        'department_sexist_others': 'certainty', 'department_success_because_gender': 'certainty',
        'department_appearance': 'frequency', 'department_appearance_comments': 'appearance_comments',
        'complaints_how': 'certainty', 'complaints_concequences': 'certainty',
        'complaints_concequences_fear': 'certainty', 'peer_mistreated_react': 'sexism_response',
        'people_surprise_major': 'agreement', 'people_sexist_jokes_gender': 'frequency',
        'highest_standard': 'student_groups_standards', 'peer_sexism_ignoring_suggestion': 'frequency',
        'friends_other_gender': 'agreement', 'intelligence_fixed': 'agreement', 'intelligence_malleable': 'agreement',
        'failure_lazy': 'agreement', 'failure_environment': 'agreement', 'failure_ability': 'agreement',
        'describe_positive_experience': 'string', 'describe_negative_experience': 'string',
        'suggestion_improve_institution': 'string'}


# the one that actually does stuff
# pick_graphing_style(temp, people)

# some other random graphs
compare_confidence_GPA(people, 'gender', ['Male', 'Female'])


from collections import namedtuple
import csv
from itertools import zip_longest
import matplotlib.pyplot as plt
from language_processing import graph_string, long_text
from answer_type import mult_choice, graph_num, compare_confidence_GPA, time_confidence
from graph_func import call_respective_graphing_functions, filter_and_graph, pie_chart
from constants import BYU_question_shorthand, BYU_question_string
from list_constants import likert_question_answer_types, list_question_answer_types, confidence_measurement, long_feedback, race
from language_processing import associate_with_professors
from collections import defaultdict
import os
from data_structures import ques_ans
import logging


plt.style.use('seaborn-deep')

Person = namedtuple('Person', BYU_question_shorthand)


def run_overall(file_name):
    logging.info(os.path.dirname(os.path.realpath(__file__)))
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=','))


def ques_to_question():
    if len(BYU_question_shorthand) is not len(BYU_question_string):
        logging.critical(str(len(BYU_question_shorthand)) + str(BYU_question_shorthand))
        logging.critical(str(len(BYU_question_string)) + str(BYU_question_string))
        logging.critical('mapping SHORTHAND questions to question error')
        exit(1)
    else:
        return dict(zip_longest(BYU_question_shorthand, BYU_question_string[:len(BYU_question_shorthand)]))


def parse_overall_data(data):
    return list(map(lambda line: Person(*line), data))


def encouragement_or_barriers(question, focus_var, answer_to_count_per_category, list_all_answers_per_category, category_names):
    print('question: ' + question)
    print('focus var: ' + focus_var)
    print('var, mean: ' + category_names[0] + ', mean: ' + category_names[1])

    category_counts = list(map(len, list_all_answers_per_category))

    sum_0 = category_counts[0]
    sum_1 = category_counts[1]

    for cat_0_keys, cat_1_keys, in zip(answer_to_count_per_category[0], answer_to_count_per_category[1]):
        print(cat_0_keys + ', ' + str((answer_to_count_per_category[0][cat_0_keys]/sum_0)) + ', ' + str((answer_to_count_per_category[1][cat_1_keys]/sum_1)) + ',')

def assorted_special_graphs(people):
    compare_confidence_GPA(people, 'gender')

    for type_of_feedback in ['describe_positive_experience', 'describe_negative_experience']:
        associate_with_professors(people, type_of_feedback)

    # pie chart of races
    var = 'race'
    choice_to_answer = calculate_one_chart(people, var)
    assert choice_to_answer
    pie_chart(var, choice_to_answer)

    # pie chart of what non-CS majors there were
    var = 'university_major'
    choice_to_answer = calculate_one_chart(people, var)
    assert choice_to_answer
    pie_chart('university_major', choice_to_answer)


def calculate_one_chart(people, attribute):
    choice_to_answer = {}
    for person in people:
        this_var = getattr(person, attribute)
        if not choice_to_answer.keys().__contains__(this_var):
            choice_to_answer[this_var] = 0
        else:
            choice_to_answer[this_var] += 1


def pick_graphing_style(people):
    possible_focus_var = ['university_major', 'university_graduation_year', 'gender', 'university_program']
    # TODO: add functionality for: 'major_and_gender', 'university_graduation_year_and_gender']  # maybe GPA, too?
    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:
            if question == 'participation_TA_ask_questions':
                print('participation_TA_ask_questions')

            answer_type = ques_ans[question]

            logging.info('\nfocus_var: ' + focus_var + " question number: " + str(counter))
            logging.info('question: ' + question)
            logging.info('answer_type: ' + answer_type)

            counter += 1

            if question in long_feedback:
                long_text(question, people)
            elif answer_type == 'string':
                graph_string(question, people)
            elif answer_type == 'int' or answer_type == 'double':
                graph_num(question, focus_var, people)
            elif answer_type in likert_question_answer_types + list_question_answer_types:
                category_names = mult_choice(focus_var)
                list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, answer_type,
                                                                                               people, focus_var,
                                                                                               category_names)
                call_respective_graphing_functions(question, focus_var, answer_type, list_all_answers_per_category,
                                                   answer_to_count_per_category, category_names)

                if question in confidence_measurement and focus_var == 'university_graduation_year':
                    time_confidence(question, focus_var, answer_to_count_per_category, list_all_answers_per_category,
                                    category_names)

                # Women and Men Engineering Students: Anticipation of Family and Work Roles
                if question in ['major_pros', 'major_cons']:
                    encouragement_or_barriers(question, focus_var, answer_to_count_per_category, list_all_answers_per_category,
                                    category_names)



# if __name__ == "__main__":  # needed if I decide to include this file elsewhere
logging.basicConfig(level=logging.INFO)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICIAL'


data = run_overall('raw_overall_survey/overall_data_prepped_BYU.csv')  # ./fake_data/ORCA_overall_CS_edited.csv
# ques_to_question = ques_to_question() # not using yet, but would be good to add to graphs, eventually

data = data[2:]  # deletes the question text and shorthand from the dataset

people = parse_overall_data(data)

# will not be needed again unless the questions change for UVA version
# short_to_long = {}
# for short, long in zip(BYU_question_shorthand, BYU_question_string):
#     short_to_long[short] = long
#
# print(short_to_long)

# does other graphs
assorted_special_graphs(people)

# the one that actually does stuff
pick_graphing_style(people)




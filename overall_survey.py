from collections import namedtuple
import csv
from itertools import zip_longest
import matplotlib.pyplot as plt
from language_processing import graph_string, long_text, find_common_words
from answer_type import mult_choice, graph_num, compare_confidence_GPA
from graph_func import call_respective_graphing_functions, filter_and_graph, pie_chart
from data_structures import BYU_question_shorthand, BYU_question_string, likert_question_answer_types, list_question_answer_types, confidence_measurement, \
    long_feedback, race
from language_processing import associate_with_professors
import os
from data_structures import ques_ans
import logging

plt.style.use('seaborn-deep')

Person = namedtuple('Person', BYU_question_shorthand)


def run_overall(file_name):
    logging.info(os.path.dirname(os.path.realpath(__file__)))
    with open(file_name, 'r', encoding='utf-8') as file:
        return list(csv.reader(file, delimiter=','))


def parse_overall_data(data):
    return list(map(lambda line: Person(*line), data))


def ques_to_question():
    if len(BYU_question_shorthand) is not len(BYU_question_string):
        logging.critical(str(len(BYU_question_shorthand)) + str(BYU_question_shorthand))
        logging.critical(str(len(BYU_question_string)) + str(BYU_question_string))
        logging.critical('mapping SHORTHAND questions to question error')
        exit(1)
    else:
        return dict(zip_longest(BYU_question_shorthand, BYU_question_string[:len(BYU_question_shorthand)]))


def encouragement_or_barriers(question, focus_var, answer_to_count_per_category, list_all_answers_per_category,
                              category_names):
    print('question: ' + question)
    print('focus var: ' + focus_var)
    print('var, mean: ' + category_names[0] + ', mean: ' + category_names[1])

    category_counts = list(map(len, list_all_answers_per_category))

    sum_0 = category_counts[0]
    sum_1 = category_counts[1]

    for cat_0_keys, cat_1_keys, in zip(answer_to_count_per_category[0], answer_to_count_per_category[1]):
        print(cat_0_keys + ', ' + str((answer_to_count_per_category[0][cat_0_keys] / sum_0)) + ', ' + str(
            (answer_to_count_per_category[1][cat_1_keys] / sum_1)) + ',')


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
    pie_chart(var, choice_to_answer)

    # pie chart of what genders there were
    var = 'gender'
    choice_to_answer = calculate_one_chart(people, var)
    assert choice_to_answer
    pie_chart(var, choice_to_answer)

    # print out the stats of who responded v. who was invited to take the survey
    response_rate(people)

    # see how common different words are in free response
    find_common_words(people)


def response_rate(people):
    # these are magic numbers given to me by BYU
    female = 427
    male = 2163
    CS_major = 1125
    CS_minor = 259
    other_program = 1231
    doctorate = 31
    master = 79
    post_bac = 8
    undergraduate = 2473

    responses_female, responses_male, responses_other_gender = gender_responses(people)
    responses_CS_major, responses_CS_minor, responses_other_program = program_responses(people)
    responses_doctorate, responses_master, responses_other, responses_undergrad = degree_responses(people)
    responses_freshmen, responses_sophomores, responses_juniors, responses_seniors = gradu_date_responses(people)

    f = open('results_at_BYU/overall/response_rate.txt', 'w')
    total_invited = female + male
    total_participated = responses_male + responses_female + responses_other_gender
    f.write(str(total_invited) + ' students were invited to take this survey, ' + str(
        total_participated) + ' took it (' + str((total_participated/total_invited)*100) + '%)\n')
    f.write('responses//those invited to take it (response rates for particular categories): \n')
    f.write('Female students: ' + str(100*responses_female / female) + '%\n')
    f.write('Male students: ' + str(100*responses_male / male) + '%\n')
    f.write('Other/Prefer not to say: [none were registered with non-binary/other genders]\n')
    f.write('CS majors: ' + str(100*responses_CS_major / CS_major) + '%\n')
    f.write('CS minors: ' + str(100*responses_CS_minor / CS_minor) + '%\n')
    f.write('Non-CS-major, non-CS-minor students: ' + str(100*responses_other_program / other_program) + '%\n')
    f.write('Undergraduates: ' + str(100*responses_undergrad/undergraduate) + '%\n')
    f.write('Masters: ' + str(100*responses_master / master) + '%\n')
    f.write('PhD: ' + str(100*responses_doctorate / doctorate) + '%\n')
    f.write('Freshmen: ' + str(responses_freshmen) + ' responses\n')
    f.write('Sophomores: ' + str(responses_sophomores) + ' responses\n')
    f.write('Juniors: ' + str(responses_juniors) + ' responses\n')
    f.write('Seniors: ' + str(responses_seniors) + ' responses\n')
    f.close()

def gradu_date_responses(people):
    responses_freshmen = 0
    responses_sophomores = 0
    responses_juniors = 0
    responses_seniors = 0
    for person in people:
        gradu_year = getattr(person, 'university_graduation_year')
        if gradu_year == '2021 or later':
            responses_freshmen += 1
        elif gradu_year == '2020':
            responses_sophomores += 1
        elif gradu_year == '2019':
            responses_juniors += 1
        elif gradu_year == '2018':
            responses_seniors += 1
        elif gradu_year == '':
            pass
        else:
            assert(False)

    return responses_freshmen, responses_sophomores, responses_juniors, responses_seniors


def degree_responses(people):
    responses_doctorate = 0
    responses_master = 0
    responses_other = 0
    responses_undergrad = 0
    # degree_pursuing = ['Undergraduate', 'Masters', 'PhD', 'Not currently pursuing a degree']

    for person in people:
        university_program = getattr(person, 'university_program')
        if university_program == 'Undergraduate':
            responses_undergrad += 1
        elif university_program == 'Masters':
            responses_master += 1
        elif university_program == 'PhD':
            responses_doctorate += 1
        else:
            responses_other += 1

    return responses_doctorate, responses_master, responses_other, responses_undergrad


def gender_responses(people):
    responses_female = 0
    responses_male = 0
    responses_other_gender = 0
    for person in people:
        this_person = getattr(person, 'gender')
        if this_person == 'Female':
            responses_female += 1
        elif this_person == 'Male':
            responses_male += 1
        else:
            responses_other_gender += 1 
    return responses_female, responses_male, responses_other_gender


def program_responses(people):
    responses_CS_major = 0
    responses_CS_minor = 0
    responses_other_program = 0
    for person in people:
        major = getattr(person, 'university_major')
        minor = getattr(person, 'university_minor')
        if major == 'Computer Science':
            responses_CS_major += 1
        elif minor == 'Computer Science':
            responses_CS_minor += 1
        else:
            responses_other_program += 1
    return responses_CS_major, responses_CS_minor, responses_other_program


def calculate_one_chart(people, attribute):
    choice_to_answer = {}
    for person in people:
        this_var = getattr(person, attribute)
        if not choice_to_answer.keys().__contains__(this_var):
            choice_to_answer[this_var] = 0
        else:
            choice_to_answer[this_var] += 1
    return choice_to_answer


def pick_graphing_style(people):
    possible_focus_var = ['university_major', 'university_graduation_year', 'gender', 'university_program']
    for focus_var in possible_focus_var:
        counter = 1
        for question in BYU_question_shorthand:

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
                    # time_confidence(question, focus_var, answer_to_count_per_category, list_all_answers_per_category,
                    #                 category_names)
                    pass
                    # TODO CHECK AND SEE HOW BAD ME DELETING THAT WAS
                # Women and Men Engineering Students: Anticipation of Family and Work Roles
                if question in ['major_pros', 'major_cons']:
                    encouragement_or_barriers(question, focus_var, answer_to_count_per_category,
                                              list_all_answers_per_category,
                                              category_names)


# if __name__ == "__main__":  # needed if I decide to include this file elsewhere
logging.basicConfig(level=logging.INFO)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICIAL'

data = run_overall('raw_overall_survey/overall_data_prepped_BYU.csv')  # ./fake_data/ORCA_overall_CS_edited.csv
# ques_to_question = ques_to_question() # not using yet, but would be good to add to graphs, eventually

people = parse_overall_data(data[2:])  # deletes the question text and shorthand from the dataset

# will not be needed again unless the questions change for UVA version
# short_to_long = {}
# for short, long in zip(BYU_question_shorthand, BYU_question_string):
#     short_to_long[short] = long

# the one that actually does stuff
pick_graphing_style(people)

# does other graphs
assorted_special_graphs(people)
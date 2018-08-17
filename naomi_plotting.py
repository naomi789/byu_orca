import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from language_processing import *
from other_constants import *
import logging
import sys


def get_question_df(df, question, keep_cols, get_answers=True):
    # find expected answer types
    expected_answers = question_number_to_expected_answer[question]

    # Get a copy of the data we need
    question_df = df[keep_cols + [question]].copy()

    # Replace nans with "unanswered"
    question_df[question].fillna('Unanswered', inplace=True)

    answers_set = set()
    for row in question_df[question]:
        for item in row.split(','):
            answers_set.add(item.strip())

    question_df = pd.concat([question_df, question_df[question].str.get_dummies(sep=',')], axis=1)

    for answer in expected_answers:
        if answer not in answers_set:
            question_df[answer] = 0

        question_df.rename(columns={col: col.strip() for col in question_df.columns},
                           inplace=True)

    return question_df, list(answers_set)


def sorted_answers(question_options):
    answer = answer_dict_switcher.get(question_options, 'error')
    if answer == 'error':
        raise Exception('answer type is unknown in sorted_answers()\'s switcher')
    return answer


def make_graphs(df):
    global temp
    is_likert_stacked_vertical_transposed = False
    counter_likert = 0
    counter_non = 0
    gender_options = ['Male', 'Female']
    for comparison_point in FOCUS_VARS:
        shorthand_var = ques_num_to_shorthand[comparison_point]
        print('COMPARISON POINT ' + comparison_point + ' SHORT ' + shorthand_var)
        keep_cols = [GENDER, comparison_point]

        for question in MANY_CHOICES_QUESTIONS + ONE_CHOICE_QUESTIONS:
            question_df, answers = get_question_df(df, question, keep_cols)
            if question in ONE_CHOICE_QUESTIONS:
                is_likert_stacked_vertical_transposed = True
                question_df = question_df[question_df[question] != 'Unanswered']

            shorthand_question = ques_num_to_shorthand[question]
            print('question', question, 'short', shorthand_question, 'is_likert_stacked_vertical_transposed',
                  is_likert_stacked_vertical_transposed)

            agg_t, counts, columns_for_var = filter_data(question_df, comparison_point, question, answers, keep_cols)
            transposed = agg_t / counts

            if is_likert_stacked_vertical_transposed:
                question_options = ques_ans[shorthand_question.lower()]
                print(question_options)

                correct_order = answer_dict_switcher.get(question_options, 'error')

                new_df = transposed.transpose()
                ax = new_df[correct_order].plot(kind='barh', stacked=is_likert_stacked_vertical_transposed)
                labels = [x[:40] for x in agg_t.transpose().index]
                # if 'Unanswered' in labels: labels.remove('Unanswered')
                # TODO fix that
                counter_likert += 1
            else:
                ax = transposed.plot(kind='barh', stacked=is_likert_stacked_vertical_transposed)
                labels = [x[:40] for x in agg_t.index]
                counter_non += 1


            # TODO: have the labels be in a logical order (same as above)

            ax.set_yticklabels(labels)
            plt.xlim(0, 1)
            real_title = '\n'.join(ques_num_to_long[question][i:i + 60] for i in range(0, len(ques_num_to_long[question]), 60))
            plt.title(real_title)
            # plt.tight_layout() # debug this...

            if is_likert_stacked_vertical_transposed:
                os.makedirs(f'panda_BYU_results/{shorthand_var}/likert_bar_graphs', exist_ok=True)
                file_name = f'panda_BYU_results/{shorthand_var}/likert_bar_graphs/{shorthand_question}.png'
            else:
                os.makedirs(f'panda_BYU_results/{shorthand_var}/stacked_bar_graphs', exist_ok=True)
                file_name = f'panda_BYU_results/{shorthand_var}/stacked_bar_graphs/{shorthand_question}.png'
            plt.savefig(file_name)

        # for debugging purposes
        print('counter_likert', counter_likert, 'len(ONE_CHOICE_QUESTIONS)', len(ONE_CHOICE_QUESTIONS))
        print('counter_non', counter_non, 'len(MANY_CHOICES_QUESTIONS)', len(MANY_CHOICES_QUESTIONS))


def filter_data(question_df, comparison_point, question, answers, keep_cols):
    if comparison_point == MAJOR:
        question_df['binary_CS'] = ['CS' if x else 'non_CS' for x in question_df[MAJOR] == 'Computer Science']
        agg = question_df[keep_cols + ['binary_CS'] + answers]
        agg = agg.groupby([GENDER, 'binary_CS']).aggregate(sum)
        columns_for_var = 'binary_CS'

    else:
        expected_answer_types = question_number_to_expected_answer[question]
        wanted_ones = keep_cols + expected_answer_types
        agg = question_df[wanted_ones].groupby(keep_cols).aggregate(sum)
        columns_for_var = comparison_point

    agg_t = agg.transpose()
    cat1 = agg_t.columns.levels[0]
    cat2 = agg_t.columns.levels[1]
    counts = np.array(
        [len(question_df[(question_df[GENDER] == x) & (question_df[columns_for_var] == y)]) for x in cat1 for y in
         cat2])

    return agg_t, counts, columns_for_var


def gender_response_calulator(df):
    responses_female = df[GENDER].value_counts()['Female']
    responses_male = df[GENDER].value_counts()['Male']
    responses_other_gender = 0  # set at zero because there were five responses for prefer not/other/etc and... privacy
    return responses_female, responses_male, responses_other_gender


def program_response_calculator(df):
    responses_CS_major = df[MAJOR].value_counts()['Computer Science']
    responses_CS_minor = df[MINOR].value_counts()['Computer Science']
    responses_other_program = df.shape[0] - responses_CS_major - responses_CS_minor
    return responses_CS_major, responses_CS_minor, responses_other_program


def degree_response_calculator(df):
    responses_doctorate = df[PROGRAM].value_counts()['PhD']
    responses_master = df[PROGRAM].value_counts()['Masters']
    responses_undergrad = df[PROGRAM].value_counts()['Undergraduate']
    responses_other = df[PROGRAM].value_counts()['Not currently pursuing a degree']
    return responses_doctorate, responses_master, responses_other, responses_undergrad


def gradu_date_response_calculator(df):
    responses_freshmen = df[GRAD_YEAR].value_counts()['2021 or later']
    responses_sophomores = df[GRAD_YEAR].value_counts()['2020']
    responses_juniors = df[GRAD_YEAR].value_counts()['2019']
    responses_seniors = df[GRAD_YEAR].value_counts()['2018']
    return responses_freshmen, responses_sophomores, responses_juniors, responses_seniors


def response_rate_calculator(df, num_responses):
    # gender # major # minor # program
    responses_female, responses_male, responses_other_gender = gender_response_calulator(df)
    responses_CS_major, responses_CS_minor, responses_other_program = program_response_calculator(df)
    responses_doctorate, responses_master, responses_other, responses_undergrad = degree_response_calculator(df)
    responses_freshmen, responses_sophomores, responses_juniors, responses_seniors = gradu_date_response_calculator(df)

    f = open('panda_BYU_results/response_rate.txt', 'w')
    total_invited = FEMALE_COUNT + MALE_COUNT
    total_participated = responses_male + responses_female + responses_other_gender

    f.write('\nOVERALL: \n')
    f.write(str(total_invited) + ' students were invited to take this survey, ' + '\n' +
            str(num_responses) + ' students "responded" (ie, at least opened the survey)' + '\n' +
            str(total_participated) + ' took it (' + str((total_participated / total_invited) * 100) + '%)\n')
    f.write('responses//those invited to take it (response rates for particular categories): \n')
    f.write('\nGENDER: \n')
    f.write('Female students: ' + str(100 * responses_female / FEMALE_COUNT) + '%\n')
    f.write('Male students: ' + str(100 * responses_male / MALE_COUNT) + '%\n')
    f.write('Other/Prefer not to say: [none were registered with non-binary/other genders]\n')

    f.write('\nMAJORS: \n')
    f.write('CS majors: ' + str(100 * responses_CS_major / CS_MAJOR_COUNT) + '%\n')
    f.write('CS minors: ' + str(100 * responses_CS_minor / CS_MINOR_COUNT) + '%\n')
    f.write('Non-CS-major, non-CS-minor students: ' + str(100 * responses_other_program / OTHER_MAJOR_COUNT) + '%\n')

    f.write('\nDEGREE: \n')
    f.write('Undergraduates: ' + str(100 * responses_undergrad / UNDERGRADUATE_COUNT) + '%\n')
    f.write('Masters: ' + str(100 * responses_master / MASTER_COUNT) + '%\n')
    f.write('PhD: ' + str(100 * responses_doctorate / DOCTORATE_COUNT) + '%\n')

    f.write('\nCLASS STANDING: \n')
    f.write('Freshmen: ' + str(responses_freshmen) + ' responses\n')
    f.write('Sophomores: ' + str(responses_sophomores) + ' responses\n')
    f.write('Juniors: ' + str(responses_juniors) + ' responses\n')
    f.write('Seniors: ' + str(responses_seniors) + ' responses\n')
    f.close()


def new_num_histogram(df, title, var):
    # TODO trash the data for people who said their GPA > 4
    cleaned = pd.to_numeric(df[var], errors='coerce')
    cleaned.dropna().hist(bins=50)
    plt.title(title)
    plt.savefig(f'panda_BYU_results/overall/{title}.png')
    plt.clf()



def assorted_special_graphs(df):
    # histogram of ages
    # title = 'ages'
    # df = df.sort_values(AGE)
    # clean_ages = pd.to_numeric(df[AGE], errors='coerce')
    # clean_ages = clean_ages.sort_values(AGE)
    # clean_ages = clean_ages.value_counts()
    # clean_ages.dropna().plot.bar(y='AGE')
    # plt.title(title)
    # plt.savefig(f'panda_BYU_results/overall/{title}.png')
    # plt.clf()

    # histogram of GPA
    title = 'GPA'
    var = GPA
    new_num_histogram(df, title, var)


    # pie chart of races
    title = 'race'
    var = RACE
    new_pie_chart(df, title, var)

    # pie chart of what non-CS majors there were
    title = 'majors'
    var = MAJOR
    new_pie_chart(df, title, var)

    # pie chart of what non-CS majors there were
    title = 'minors'
    var = MINOR
    new_pie_chart(df, title, var)

    # pie chart of what genders there were
    title = 'gender'
    var = GENDER
    new_pie_chart(df, title, var)

    # pie chart of what PROGRAMS there were
    title = 'program'
    var = PROGRAM
    new_pie_chart(df, title, var)


    # see how common different words are in free response; which professors' names come up more
    split_on_var = GENDER
    for pos_neg_sug in TEXT_ANSWERS:
        find_common_words(df, pos_neg_sug, split_on_var)
        associate_with_professors(df, pos_neg_sug)


    # compare_confidence_GPA(people, 'gender')

def new_pie_chart(df, title, var):
    # TODO: wouldn't it be interesting if I made the actual one on the same sheet, to better compare
    df[var].value_counts().sort_values(ascending=False).plot(kind='pie', autopct='%.1f%%', )
    plt.axis('equal')
    plt.title(title)
    plt.savefig(f'panda_BYU_results/overall/{title}.png')
    plt.clf()


def main():
    logging.basicConfig(level=logging.INFO)  # 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICIAL'
    nltk.download('stopwords')
    df = pd.read_csv('raw_overall_survey/use-this.csv')
    num_responses = df.shape[0]
    df.dropna(subset=[RACE, GENDER, PROGRAM, MAJOR, GRAD_YEAR],
              inplace=True)  # tosses if participants didn't answer these
    df = df[(df[GENDER] == 'Male') | (df[GENDER] == 'Female')]

    # print out the stats of who responded v. who was invited to take the survey
    response_rate_calculator(df, num_responses)

    assorted_special_graphs(df)

    make_graphs(df)


print(len(question_shorthand ))
print(len(ques_text))
main()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from new_constants import *
from language_processing import *
from graph_func import pie_chart
from answer_type import compare_confidence_GPA
from overall_survey import response_rate, calculate_one_chart

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



def many_option_graphing(df): # this does all the '% of focus_var gave this answer # all be bar graphs
    gender_options = ['Male', 'Female']
    for var in FOCUS_VARS:
        shorthand_var = ques_num_to_shorthand[var]
        print('var', var, 'short', shorthand_var)
        keep_cols = [var,  GENDER]

        for question in MANY_CHOICES_QUESTIONS:
            shorthand_question = ques_num_to_shorthand[question]
            print('question', question, 'short', shorthand_question)
            question_df, answers = get_question_df(df, question, keep_cols)

            DF = question_df

            if var == MAJOR:
                question_df['binary_CS'] = ['CS' if x else 'non_CS' for x in question_df[MAJOR]=='Computer Science']
                agg = question_df[keep_cols + ['binary_CS'] + answers].groupby([GENDER, 'binary_CS']).aggregate(sum)
                columns_for_var = 'binary_CS'
            else:
                expected_answer_types = ques_ans[question]
                possible_answers = sorted_answers(expected_answer_types)
                agg = question_df[keep_cols + answers].groupby(keep_cols).aggregate(sum)
                columns_for_var = 'idk' # TODO

            agg_t = agg.transpose()
            # CS = ['CS', 'non_CS']
            cat1 = agg_t.columns.levels[0]
            cat2 = agg_t.columns.levels[1]
            counts = np.array([len(DF[(DF[GENDER] == x) & (DF[columns_for_var] == y)]) for x in cat1 for y in cat2])


            ax = (agg_t / (counts)).plot(kind='barh', stacked=False)

            labels = [x[:40] for x in agg_t.index]
            ax.set_yticklabels(labels)
            plt.xlim(0,1)
            plt.title(shorthand_question)
            plt.tight_layout()
            plt.savefig(f'panda_BYU_results/{shorthand_var}/{shorthand_question}.png')


def one_option_graph():
    # these will all be STACKED bar graphs
    # for question in ONE_CHOICE_QUESTIONS:
    for var in FOCUS_VARS:
        print('var', var)
        keep_cols = [var,  GENDER]

        for question in MANY_CHOICES_QUESTIONS:
            print('question', question)
            question_df, answers = get_question_df(df, question, keep_cols)
            DF = question_df

def prep_for_pie(df, attribute):
    choice_to_answer = {}
    for person in people:
        this_var = getattr(person, attribute)
        if not choice_to_answer.keys().__contains__(this_var):
            choice_to_answer[this_var] = 0
        else:
            choice_to_answer[this_var] += 1
    return choice_to_answer


def assorted_special_graphs(df, people):
    compare_confidence_GPA(people, 'gender')

    for type_of_feedback in ['describe_positive_experience', 'describe_negative_experience']:
        associate_with_professors(people, type_of_feedback)

    # pie chart of races
    var = 'race'
    choice_to_answer = prep_for_pie(people, var)
    assert choice_to_answer
    pie_chart(var, choice_to_answer)

    # pie chart of what non-CS majors there were
    var = 'university_major'
    choice_to_answer = prep_for_pie(people, var)
    assert choice_to_answer
    pie_chart(var, choice_to_answer)

    # pie chart of what genders there were
    var = 'gender'
    choice_to_answer = prep_for_pie(people, var)
    assert choice_to_answer
    pie_chart(var, choice_to_answer)

    # print out the stats of who responded v. who was invited to take the survey
    response_rate(people)

    # see how common different words are in free response
    find_common_words(people)







def main():
    df = pd.read_csv('raw_overall_survey/byu_for_pandas_strings_stephen_fixed.csv')
    df.dropna(subset=[RACE, GENDER, PROGRAM, MAJOR, GRAD_YEAR], inplace=True)  # tosses if participants didn't answer these
    df = df[(df[GENDER] == 'Male') | (df[GENDER] == 'Female')]
    many_option_graphing(df)
    # assorted_special_graphs(df)


main()
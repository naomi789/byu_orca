import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from new_constants import *
# from data_structures import question_number_to_expected_answer


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


def many_option_graphing(df):
    # this does all the '% of focus_var gave this answer'
    # in other words, these will all be bar graphs
    for var in FOCUS_VARS:
        print('var', var)
        keep_cols = [var,  GENDER]

        for question in MANY_CHOICES_QUESTIONS:
            print('question', question)
            question_df, answers = get_question_df(df, question, keep_cols)

            DF = question_df

            if var == MAJOR:
                question_df['binary_CS'] = ['CS' if x else 'non_CS' for x in question_df[MAJOR]=='Computer Science']
                agg = question_df[keep_cols + ['binary_CS'] + answers].groupby([GENDER, 'binary_CS']).aggregate(sum)
            else:
                agg = question_df[keep_cols + answers].groupby(keep_cols).aggregate(sum)

            gender_options = ['Male', 'Female']
            CS = ['CS', 'non_CS']

            agg_t = agg.transpose()
            cat1 = agg_t.columns.levels[0]
            cat2 = agg_t.columns.levels[1]
            counts = np.array([len(DF[(DF[GENDER]==x) & (DF['binary_CS']==y)]) for x in cat1 for y in cat2])

            ax = (agg_t / (counts)).plot(kind='barh', stacked=False)

            labels = [x[:30] for x in agg_t.index]
            ax.set_yticklabels(labels)

            plt.title(question)
            plt.tight_layout()

            plt.savefig(f'panda_BYU_results/{var}/{question}.png')
            # {var}/
            question_df.to_csv('practice_df.csv')

def one_option_graph():
    # these will all be STACKED bar graphs
    # for question in ONE_CHOICE_QUESTIONS:
    pass


df = pd.read_csv('raw_overall_survey/byu_for_pandas_strings_stephen_fixed.csv')
df.dropna(subset=[RACE, GENDER, PROGRAM, MAJOR, GRAD_YEAR], inplace=True)  # tosses if participants didn't answer these
df = df[(df[GENDER] == 'Male') | (df[GENDER] == 'Female')]
many_option_graphing(df)

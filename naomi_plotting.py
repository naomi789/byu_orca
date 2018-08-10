import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
from new_constants import *
from data_structures import question_number_to_expected_answer


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

    # TODO check and see if that works
    for answer in expected_answers:
        if answer not in answers_set:
            question_df[answer] = 0
            print(answer)

    print({col: col.strip() for col in question_df.columns})
    question_df.rename(columns={col: col.strip() for col in question_df.columns},
                       inplace=True)

    return question_df, list(answers_set)


def graph_data(df):
    # this does all the '% of focus_var gave this answer'
    # in other words, these will all be bar graphs
    for var in FOCUS_VARS:
        keep_cols = [var,  GENDER]

        for question in TEMP_MANY_CHOICES:
            question_df, answers = get_question_df(df, question, keep_cols)

            if question == MAJOR_PROS:
                global THING
                THING = question_df
                global ANSWERS
                ANSWERS = answers


            agg = question_df[keep_cols + answers].groupby(keep_cols).aggregate(sum)
            agg_t = agg.transpose()
            (agg_t / (agg_t.sum(axis=0))).plot.bar(stacked=False)
            plt.savefig(f'panda_BYU/{question}.png')

            question_df.to_csv('practice_df.csv')

    # these will all be STACKED bar graphs
    # for question in ONE_CHOICE_QUESTIONS:


df = pd.read_csv('raw_overall_survey/byu_for_pandas_strings_stephen_fixed.csv')
df.dropna(subset=[RACE, GENDER, PROGRAM, MAJOR, GRAD_YEAR], inplace=True)  # tosses if participants didn't answer these

graph_data(df)



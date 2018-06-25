import numpy as np
import matplotlib.pyplot as plt
from constants import question_shorthand, question_string, answer_type, agreement, comfort, certainty, frequency, \
    frequency_class, frequency_TA
from itertools import zip_longest
from textwrap import wrap


def gender_graphing(question, type_likert, people):
    men = []
    women = []
    other = []

    for person in people:
        if getattr(person, 'gender') == 'Male':
            men.append(getattr(person, question))
        elif getattr(person, 'gender') == 'Female':
            women.append(getattr(person, question))
        elif getattr(person, 'gender') == 'Other' or getattr(person, 'gender') == 'Prefer not to say':
            other.append(getattr(person, question))
        else:
            print("error: " + str(getattr(person, 'gender')))

    #  returns dict, sorted. Key = choices, value = count
    men_graphable, other_graphable, women_graphable = values_per_gender(men, other, women, type_likert)

    #  decide and call preferred graph here
    bar_graph(question, men_graphable, other_graphable, women_graphable)
    pie_chart(question, men_graphable, other_graphable, women_graphable)


def values_per_gender(men, other_prefer_not, women, type_likert):
    men_graphable = dict.fromkeys(sorted_answers(type_likert), 0)
    other_graphable = dict.fromkeys(sorted_answers(type_likert), 0)
    women_graphable = dict.fromkeys(sorted_answers(type_likert), 0)
    #
    for answer in men:
        if men_graphable.__contains__(answer):
            men_graphable[answer] += 1
        else:
            men_graphable[answer] = 1
    for answer in women:
        if women_graphable.__contains__(answer):
            women_graphable[answer] += 1
        else:
            women_graphable[answer] = 1
    for answer in other_prefer_not:
        if other_graphable.__contains__(answer):
            other_graphable[answer] += 1
        else:
            other_graphable[answer] = 1
    return men_graphable, other_graphable, women_graphable


def sorted_answers(type):
    switcher = {
        'agreement': agreement,
        'frequency': frequency,
        'frequency_TA': frequency_TA,
        'frequency_class': frequency_class,
        'comfort': comfort,
        'certainty': certainty
    }
    return switcher.get(type, 'other_answer_types')


def ques_to_answer():
    if len(question_shorthand) is not len(answer_type):
        print("mapping questions to answer error")
        exit(1)
    else:
        translate_questions = dict(zip_longest(question_shorthand, answer_type[:len(question_shorthand)]))
    return translate_questions


def bar_graph(question, men, other_prefer_not, women):
    ques_ans = ques_to_answer()
    x_values = sorted_answers(ques_ans[question])  # possible answers
    men_vals = men.values()
    women_vals = women.values()

    ind = np.arange(len(men_vals))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, men_vals, width,
                    color='cornflowerblue', label='Men')
    rects2 = ax.bar(ind + width / 2, women_vals, width,
                    color='hotpink', label='Women')
    # rects3 = ax.bar(ind + width / 2, other_prefer_not, width,
    #                 color='lime', label='other_p_not')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')

    #  todo I need help wrapping my long strings to short ones
    print(question)
    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    print(longhand)
    title = ['\n'.join(wrap(l, 18)) for l in longhand]
    print(title)
    ax.set_title(question)  # eventually switch that to longhand

    ax.set_xticks(np.arange(len(x_values)))  # ind)
    ax.set_xticklabels(x_values)
    ax.legend()

    plt.savefig('results/by_gender/bar_graph/' + question + '.pdf')


def makeBoxWhisker(question, men, other_prefer_not, women):
    plt.figure()
    # plt.title(ques_to_question['confidence_graduate_gpa'] + str(datetime.now().time()))
    # plt.xlabel('gender')
    # plt.ylabel('answers')
    # trash_numbers = [1, 3, 4, 5, 6, 7, 8, 0, 4, 3, 2, 1]
    # plt.boxplot(trash_numbers, 0, 'gD')
    plt.savefig('results/trash/trash.pdf')


def pie_chart(question, men, other_prefer_not, women):
    #  clear the plot bc something is getting really mixed up

    ques_ans = ques_to_answer()
    x_values = sorted_answers(ques_ans[question])  # possible answers

    men_vals = men.values()
    women_vals = women.values()

    if len(men_vals) != len(x_values):
        temp_vals = len(men_vals)
        temp_x = len(x_values)
        print('HELP')
    plt.pie(men_vals, explode=None, labels=x_values, colors=None)
    plt.savefig('results/pie_chart/' + question + '.pdf')

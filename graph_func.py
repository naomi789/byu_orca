import numpy as np
import matplotlib.pyplot as plt
from constants import question_shorthand, question_string, answer_type, agreement, comfort, certainty, frequency, frequency_class, frequency_TA
from itertools import zip_longest

def makeBoxWhisker(men, women):
    plt.figure()
    # plt.title(ques_to_question['confidence_graduate_gpa'] + str(datetime.now().time()))
    # plt.xlabel('gender')
    # plt.ylabel('answers')
    # trash_numbers = [1, 3, 4, 5, 6, 7, 8, 0, 4, 3, 2, 1]
    # plt.boxplot(trash_numbers, 0, 'gD')
    plt.savefig('results/trash/trash.pdf')


def makePieChart(men, women, question):
    print(men)
    keys = dict.fromkeys(men, 0)
    # values =
    print(keys)
    plt.pyplot.pie(keys, explode=None, labels=None, colors=None)


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
    men_graphable, other_graphable, women_graphable = values_per(men, other, women)

    #  decide and call preferred graph here
    anotherBarGraph('confidence_graduate_gpa', men_graphable, other_graphable, women_graphable)


def values_per(men, other_prefer_not, women):
    # men_graphable = defaultdict(set)
    # women_graphable = defaultdict(set)
    # other_graphable = defaultdict(set)
    men_graphable = dict.fromkeys(agreement, 0)
    other_graphable = dict.fromkeys(agreement, 0)
    women_graphable = dict.fromkeys(agreement, 0)
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



def makeBarGraph(men, women):
    plt.figure()

    plt.savefig('results/trash/trash.pdf')

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

def anotherBarGraph(question, men, other_prefer_not, women):
    ques_ans = ques_to_answer()
    x_values = sorted_answers(ques_ans[question])  # possible answers
    men_means = men.values()
    women_means = women.values()
    # men_means = (20, 35, 30, 35, 27)
    # women_means = (25, 32, 34, 20, 25)
    print(men.values())
    print(women.values())
    # men_means = men.values()
    # women_means = women.values()

    ind = np.arange(len(men_means))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, men_means, width,
                    color='cornflowerblue', label='Men')
    rects2 = ax.bar(ind + width / 2, women_means, width,
                    color='hotpink', label='Women')
    # rects3 = ax.bar(ind + width / 2, other_prefer_not, width,
    #                 color='lime', label='other_p_not')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')
    ax.set_title(question)
    ax.set_xticks(np.arange(len(x_values))) # ind)
    # ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5')) # x_values
    ax.set_xticklabels(x_values)
    ax.legend()

    plt.savefig('results/by_gender/' + question + '.pdf')
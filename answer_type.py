from collections import defaultdict
from scipy.stats import mannwhitneyu
import numpy as np
import matplotlib.pyplot as plt
from data_structures import ques_ans, gender_colors, staff_names, professor_names
from graph_func import make_box_and_whisker, convert_into_numbers
import logging


def graph_num(question, focus_var, people):
    logging.info("graph numbers")
    number_questions = ['university_gpa_TEXT', 'confidence_percentile']
    if question not in number_questions:
        return

    if focus_var == 'gender':
        gender_graph_num(question, people, focus_var, 'Male', 'Female')

    elif focus_var == 'university_program':
        gender_graph_num(question, people, focus_var, 'Undergraduate', 'not')

    elif focus_var == 'university_major':
        gender_graph_num(question, people, focus_var, 'Computer Science', 'not')

    elif focus_var == 'university_graduation_year':
        pass


def gender_graph_num(question, people, focus_var, a, b):
    # if question == 'confidence_percentile':
    #     current_bug = 23
    logging.info("graph gender number")
    f = open('results_at_BYU/' + focus_var + '/numbers/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')

    option_a = []
    option_b = []
    other_prefer_not = []

    if b == 'not':
        b_is_not_a = True
    else:
        b_is_not_a = False

    for person in people:
        value = getattr(person, question)
        focus_attribute = getattr(person, focus_var)
        if value == "":
            continue
        elif value.isdigit():  # and int(value) < 5:
            if focus_attribute == a:
                option_a.append(int(value))
            elif b_is_not_a:
                option_b.append(int(value))
            elif focus_attribute == b:
                option_b.append(int(value))

        elif value.replace('.', '', 1).isdigit():  # and float(value) < 5:
            if focus_attribute == a:
                option_a.append(float(value))
            elif b_is_not_a:
                option_b.append(float(value))
            elif focus_attribute == b:
                option_b.append(float(value))
        else:
            other_prefer_not.append(value)
    gender_graph_num_stats(question, focus_var, a, b, option_a, option_b)


def gender_graph_num_stats(question, focus_var, a, b, option_a, option_b):
    option_a.sort()
    option_b.sort()

    if len(option_a) < 1 or len(option_b) < 1:
        return  # because we can't compare the data

    f = open('results_at_BYU/' + focus_var + '/numbers/' + question + '.txt', 'w')
    f.write("focus_var: " + focus_var + '\n')
    f.write("question: " + question + '\n\n')

    f.write("option_a: " + a + ": " + str(option_a) + '\n')
    f.write("option_b: " + b + ": " + str(option_b) + '\n\n')

    f.write("avg " + a + " GPA: " + str(sum(option_a) / len(option_a)) + '\n')
    f.write("avg " + b + " GPA: " + str(sum(option_b) / len(option_b)) + '\n')

    f.write("mann whitney option_a v. option_b: " + str(mannwhitneyu(option_a, option_b)) + '\n')
    # no ttests because unequal numbers of option_a and option_b

    # anova tests take a bit more work
    # moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)', data=data).fit()
    # table = sm.stats.anova_lm(moore_lm, typ=2)  # Type 2 ANOVA DataFrame
    # f.write("ANOVA: " + str(table))

    f.close()
    # make_box_and_whisker(question, option_a, option_b, focus_var, a, b)


def mult_choice(focus_var):
    if focus_var == 'gender':
        categories = ['Male', 'Female']
    elif focus_var == 'university_program':
        categories = ['Undergraduate', 'Masters', 'PhD',
                      'Not currently pursuing a degree']  # ['Undergraduate', 'Not undergrads']
    elif focus_var == 'university_major':
        categories = ['Computer Science', 'Not CS majors']
    elif focus_var == 'university_graduation_year':
        categories = ['2021 or later', '2020', '2019', '2018']
    # elif focus_var == 'major_and_gender':
    #     pass

    return categories


def compare_confidence_GPA(people, focus_var):
    question = 'confidence_percentile'
    answer_type = ques_ans[question]
    categories = mult_choice(focus_var)
    title = question + '\nfocus_var: ' + focus_var

    categorized_responses = defaultdict(list)
    for person in people:
        this_category = getattr(person, focus_var)
        y_percentile = getattr(person, 'confidence_percentile')
        x_gpa = getattr(person, 'university_gpa_TEXT')

        if x_gpa == '' or y_percentile == '':  # or x_gpa > 4:
            continue
        else:
            x_gpa = float(x_gpa)
            y_percentile = float(y_percentile)

        if x_gpa > 4:
            continue

        categorized_responses[this_category].append((x_gpa, y_percentile))

    fig, ax = plt.subplots()
    ax.set_title(title)

    counter = 0
    for category in categorized_responses.keys():
        option_a = categorized_responses[category]
        x, y = map(list, zip(*option_a))
        ax.plot(x, y, 'o', label=category, color=gender_colors[counter])
        fit = np.polyfit(x, y, 1)
        fit_fn = np.poly1d(fit)
        plt.plot(x, fit_fn(x), color=gender_colors[counter])  # label=category + ' linear regression')
        counter += 1

    plt.xlim(0, 4.5)
    plt.xticks([.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
    plt.ylim(0, 110)
    plt.yticks([num for num in range(0, 101) if num % 10 == 0])

    plt.legend()  # loc="upper right")

    plt.savefig('results_at_BYU/' + focus_var + '/' + question + '.pdf')

    for category in categorized_responses.keys():
        option_a = categorized_responses[category]
        x, y = map(list, zip(*option_a))
        make_box_and_whisker(category + ' GPA', x, focus_var, categories)
        make_box_and_whisker(category + ' percentile', y, focus_var, categories)

# def time_confidence(question, focus_var, answer_to_count_per_category, list_all_answers_per_category, category_names):
#     category_counts = list(map(len, list_all_answers_per_category))
#
#     fig, ax = plt.subplots(figsize=(8.5, 11))
#     ax.set_title("Default")
#
#     for one_name, one_category_and_their_answers, count in zip(category_names, answer_to_count_per_category, category_counts):
#         # note that max ignores '' if that was a thing
#         responses_as_numbers, min, max = convert_into_numbers(one_category_and_their_answers)
#         y_axis = sum(responses_as_numbers) / len(responses_as_numbers)
#         x_axis = one_name
#         ax.plot(x_axis, y_axis, 'o-')
#
#     plt.savefig('results_at_BYU/' + focus_var + '/bar_graph_' + question + '.pdf')

import numpy as np
import matplotlib.pyplot as plt
from constants import question_shorthand, question_string, answer_type, agreement, comfort, certainty, frequency, \
    frequency_class, frequency_TA, color_options
from list_constants import responsibilities, professor_encouragement, meetings_clubs, percentage, scholarships, yes_no, \
    involvement, appearance_comments, sexism_response, student_groups_standards, majors_minors, graduation_year, \
    extracurriculars, encouragement, barriers, likert_question_answer_types, list_question_answer_types
from itertools import zip_longest
from textwrap import wrap


def gender_graphing(question, options, people):
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
    men_graphable, other_graphable, women_graphable = values_per_gender(men, other, women, options)

    #  decide and call preferred graph here
    bar_graph(question, men_graphable, other_graphable, women_graphable)
    pie_chart(question, men_graphable, other_graphable, women_graphable)


def filter_for_gender(unsorted_one_gender_answers, answer_count_dictionary):
    for answer in unsorted_one_gender_answers:
        answer_count_dictionary[answer] += 1
    return answer_count_dictionary


def deconstruct_answers_filter(unsorted_one_gender_answers, answer_count_dictionary):
    for all_selected in unsorted_one_gender_answers:
        # answer_count_dictionary[all_selected] += 1
        # split answer on comma here
        # split_all_selected = all_selected.split(',')
        split_all_selected = [split_all_selected.strip() for split_all_selected in all_selected.split(',')]
        # [x.strip() for x in my_string.split(',')]
        for each_answer in split_all_selected:
            answer_count_dictionary[each_answer] += 1
    return answer_count_dictionary


def values_per_gender(men, other_prefer_not, women, options):
    men_graphable = dict.fromkeys(sorted_answers(options), 0)
    other_graphable = dict.fromkeys(sorted_answers(options), 0)
    women_graphable = dict.fromkeys(sorted_answers(options), 0)

    if options in likert_question_answer_types:
        men_graphable = filter_for_gender(men, men_graphable)
        women_graphable = filter_for_gender(women, women_graphable)
        other_graphable = filter_for_gender(other_prefer_not, other_graphable)
    elif options in list_question_answer_types:
        men_graphable = deconstruct_answers_filter(men, men_graphable)
        women_graphable = deconstruct_answers_filter(women, women_graphable)
        other_graphable = deconstruct_answers_filter(other_prefer_not, other_graphable)
    return men_graphable, other_graphable, women_graphable


def sorted_answers(question_options):
    switcher = {
        'agreement': agreement,
        'frequency': frequency,
        'frequency_TA': frequency_TA,
        'frequency_class': frequency_class,
        'comfort': comfort,
        'certainty': certainty,
        'majors_minors': majors_minors,
        'graduation_year': graduation_year,
        'extracurriculars': extracurriculars,
        'encouragement': encouragement,
        'barriers': barriers,
        'responsibilities': responsibilities,
        'professor_encouragement': professor_encouragement,
        'meetings_clubs': meetings_clubs,
        'percentage': percentage,
        'scholarships': scholarships,
        'yes_no': yes_no,
        'involvement': involvement,
        'appearance_comments': appearance_comments,
        'sexism_response': sexism_response,
        'student_groups_standards': student_groups_standards
    }
    return switcher.get(question_options, 'other_answer_types')


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
    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    title = '\n'.join(longhand[i:i+60] for i in range(0, len(longhand), 60))
    ax.set_title(title)

    ax.set_xticks(np.arange(len(x_values)))  # ind)
    ax.set_xticklabels(x_values)
    ax.legend()

    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results/by_gender/bar_graph/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results/by_gender/bar_graph/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results/by_gender/bar_graph/error/' + question + '.pdf'
    plt.savefig(file_destination)


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

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    pie_1 = axes[0].pie(men_vals, explode=None, labels=x_values, colors=color_options)
    axes[0].set_title('Male')
    # Make both axes equal, so that the chart is round
    axes[0].axis('equal')
    pie_2 = axes[1].pie(women_vals, explode=None, labels=x_values, colors=color_options)
    axes[1].set_title('Female')
    axes[1].axis('equal')

    plt.subplots_adjust(wspace=1)

    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    title = '\n'.join(longhand[i:i+60] for i in range(0, len(longhand), 60))
    plt.suptitle(title)

    temp = ques_ans[question]
    other_temp = list_question_answer_types
    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results/by_gender/pie_chart/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results/by_gender/pie_chart/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results/by_gender/pie_chart/error/' + question + '.pdf'
    plt.savefig(file_destination)


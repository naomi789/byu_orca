import numpy as np
import matplotlib.pyplot as plt
from constants import agreement, frequency, frequency_typo, frequency_TA, frequency_TA_typo, frequency_class, \
    frequency_class_typo, comfort, certainty, color_options, long_colors

from list_constants import responsibilities, professor_encouragement, meetings_clubs, percentage, scholarships, \
    yes_no, involvement, appearance_comments, sexism_response, student_groups_standards, majors_minors, \
    graduation_year, extracurriculars, encouragement, barriers, likert_question_answer_types, \
    list_question_answer_types, frequency_absent
from data_structures import ques_ans, short_to_long
from itertools import zip_longest
import scipy.stats
from scipy.stats import mannwhitneyu

import logging



def filter_and_graph(question, options, people, focus_var, category_names):
    if question == 'participation_questions_ask_frequency':
        temp = 23
    num_categories = len(category_names)
    categorized_responses = np.empty([num_categories, 0]).tolist()
    answer_type = ques_ans[question]
    for person in people:
        focus_var_person = getattr(person, focus_var)
        if focus_var_person == "":
            continue
        if focus_var == 'university_major':
            if focus_var_person == 'Computer Science':
                value = getattr(person, question)

                # this means likert responses can't be 'none of the above'
                if value is not '' or answer_type not in likert_question_answer_types:
                    categorized_responses[0].append(value)
            else:
                value = getattr(person, question)
                if value is not '':
                    categorized_responses[1].append(value)

        else:  # elif focus_var == "university_graduation_year":
            for category in zip(category_names, categorized_responses):
                if focus_var_person == category[0]:
                    value = getattr(person, question)

                    # if answer_type in likert_question_answer_types:
                    #     pass

                    # this means likert responses can't be 'none of the above'
                    if value is not '' or answer_type not in likert_question_answer_types:
                        category[1].append(value)

    graphable_options = values(categorized_responses, options)

    return categorized_responses, graphable_options


def call_respective_graphing_functions(question, focus_var, answer_type, list_all_answers_per_category,
                                       answer_to_count_per_category, category_names):
    category_counts = list(map(len, list_all_answers_per_category))

    #  decide and call preferred graph here
    # bar_graph(question, focus_var, option_a_graphable, option_b_graphable, len(list_all_answers_from_people_in_category_a), len(list_all_answers_from_people_in_category_b), a, b)
    # pie_chart(question, focus_var, option_a_graphable, option_b_graphable, len(list_all_answers_from_people_in_category_a), len(list_all_answers_from_people_in_category_b), a, b)

    if answer_type in list_question_answer_types:
        percent_per_factor(question, focus_var, answer_to_count_per_category, category_counts, category_names)
    elif answer_type in likert_question_answer_types:
        likert_percents(question, focus_var, answer_to_count_per_category, category_counts, category_names)
        likert_statistics(question, focus_var, answer_to_count_per_category, category_names)


def convert_into_numbers(option_and_count_dict):
    static_list = list(option_and_count_dict.items())
    responses_as_numbers = []
    counter = len(option_and_count_dict) - 1  # this will put '' at being 0, if it exists, so no effect!!
    # however... if there isn't a zero, this will be a problem
    # TODO QUICK FIX THIS
    for key in option_and_count_dict.keys():
        if key != "":
            for num in range(0, option_and_count_dict[key]):
                responses_as_numbers.append(counter)
        counter -= 1
    max = static_list[0][0]
    min = static_list[-1][0]
    if max == '':
        max = static_list[-2][0]

    return responses_as_numbers, min, max


def filter_for_a_and_b(unsorted_one_option_answers, answer_count_dictionary):
    for answer in unsorted_one_option_answers:
        answer_count_dictionary[answer] += 1
    return answer_count_dictionary


def deconstruct_answers_filter(unsorted_one_gender_answers, answer_count_dictionary):
    for all_selected in unsorted_one_gender_answers:
        split_all_selected = [split_all_selected.strip() for split_all_selected in all_selected.split(',')]
        for each_answer in split_all_selected:
            answer_count_dictionary[each_answer] += 1
    return answer_count_dictionary


def values(option_list, options):
    # todo the problem is here # CURRENT BUG
    # I'm getting an array of chars instead of a list of ~5 strings
    temp = sorted_answers(options)
    dict_of_answers_per_focus_var = [dict.fromkeys(sorted_answers(options), 0) for _ in option_list]
    bar = zip(option_list, dict_of_answers_per_focus_var)

    if options in likert_question_answer_types:
        ret = map(lambda x: filter_for_a_and_b(x[0], x[1]), bar)
    elif options in list_question_answer_types:
        ret = map(lambda x: deconstruct_answers_filter(x[0], x[1]), bar)

    return list(ret)


def sorted_answers(question_options):
    switcher = {
        'agreement': agreement,
        'frequency': frequency,
        'frequency_typo': frequency_typo,
        'frequency_TA': frequency_TA,
        'frequency_TA_typo': frequency_TA_typo,
        'frequency_class': frequency_class,
        'frequency_class_typo': frequency_class_typo,
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
        'student_groups_standards': student_groups_standards,
        'frequency_absent': frequency_absent,
    }
    answer = switcher.get(question_options, 'error')
    if answer == 'error':
        raise Exception('answer type is unknown in sorted_answers()\'s switcher')
    return answer


def bar_graph(question, focus_var, option_a, option_b, count_option_a_responses, count_option_b_responses, a, b):
    file_destination, x_values = get_file_location(question, focus_var, 'bar_graph')

    option_a_vals = option_a.values()
    option_b_vals = option_b.values()

    ind = np.arange(len(option_a_vals))  # the x locations for the groups
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width / 2, option_a_vals, width,
                    color='cornflowerblue', label=a)
    rects2 = ax.bar(ind + width / 2, option_b_vals, width,
                    color='hotpink', label=b)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Scores')

    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    title = '\n'.join(longhand[i:i + 60] for i in range(0, len(longhand), 60))
    ax.set_title(title)

    ax.set_xticks(np.arange(len(x_values)))
    ax.set_xticklabels(x_values)
    ax.legend()  #

    plt.savefig(file_destination)


def calc_percent(options_to_answers, total_responses):
    ordered_list = []
    for key in options_to_answers.keys():
        # TODO: why did I do this if?
        if total_responses == 0:
            ordered_list.append(0)
        else:
            ordered_list.append(int(options_to_answers[key]) / total_responses)
    return ordered_list


def likert_percents(question, focus_var, answer_to_count_per_category, category_counts, category_names):
    if question == 'participation_TA_ask_questions':
        print('participation_TA_ask_questions')
    logging.info("select one only graph")
    num_categories = len(answer_to_count_per_category)
    assert (num_categories == len(answer_to_count_per_category) and
            num_categories == len(category_counts) and
            num_categories == len(category_names))

    plt.figure()
    longhand = short_to_long[question]
    real_title = '\n'.join(longhand[i:i + 60] for i in range(0, len(longhand), 60))

    title = 'question: ' + real_title + '\n'
    # title += 'focus_var: ' + focus_var + '\n'
    categories = list(zip(category_counts, category_names))

    # TODO: can I get these questions on the legend instead of in the title hashtag readability
    for category in categories:
        title += str(category[1]) + ' (' + str(category[0]) + ') '
    plt.suptitle(title)

    ind = [x for x, _ in enumerate(answer_to_count_per_category)]

    possible_responses = answer_to_count_per_category[0].keys()
    for category in answer_to_count_per_category:
        assert (category.keys() == possible_responses)

    all_bars = []

    categories = list(zip(answer_to_count_per_category, category_counts))
    for response in possible_responses:
        set_of_responses = []
        for category in categories:
            if category[1] == 0:
                set_of_responses.append(0)
            else:
                set_of_responses.append(category[0][response] / category[1])

        all_bars.append(set_of_responses)

    counter = 0
    used_bars = [0 for _ in range(num_categories)]

    responses = list(zip(all_bars, possible_responses))
    for response in responses:
        plt.bar(ind, response[0], width=.8, label=response[1], color=color_options[counter], bottom=used_bars)  # temp
        used_bars = [x + y for x, y in zip(used_bars, response[0])]

        counter += 1

    plt.xticks(ind, category_names)
    plt.ylim(ymax=1)
    plt.ylabel("Percent of Likert Responses")
    # plt.legend(loc="upper right")

    ax = plt.gca()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1], title='Line', loc='upper right')

    plt.savefig('results_at_BYU/' + focus_var + '/likert_percents/' + question + '.pdf')


def likert_statistics(question, focus_var, answer_to_count_per_category, categories):
    option_a_graphable = answer_to_count_per_category[0]
    option_b_graphable = answer_to_count_per_category[1]

    f = open('results_at_BYU/' + focus_var + '/likert_stats/' + question + '.txt', 'w')
    option_a_countable, min, max = convert_into_numbers(option_a_graphable)
    option_b_countable, min, max = convert_into_numbers(option_b_graphable)

    f.write("question: " + question + '\n')
    f.write("dict: " + str(option_a_graphable) + '\n')
    f.write("dict: " + str(option_b_graphable) + '\n')
    f.write('\n')

    f.write("option_a, " + categories[0] + " wilcoxon: " + str(scipy.stats.wilcoxon(option_a_countable)) + '\n')
    f.write("option_b, " + categories[1] + " wilcoxon: " + str(scipy.stats.wilcoxon(option_b_countable)) + '\n')
    f.write('\n')

    f.write('\n' + categories[0] + ' ' + str(np.mean(option_a_countable)))
    f.write('\n' + categories[1] + ' ' + str(np.mean(option_b_countable)))
    f.write('\n\n')

    f.write('on a scale where the min was: ' + min + ' ' + str(1) + '\n')
    f.write('ACTUALLY HELP I JUST REALIZED THE WHOLE "NO RESPONSE" THING IS A PROBLEM HERE AND MY STATS ARE INVALID')
    f.write('and the max was: ' + max + ' ' + str(len(answer_to_count_per_category[0].keys())))
    f.write('\n\n')

    f.write(
        "mann whitney " + categories[0] + " v. " + categories[1] + ": " + str(
            mannwhitneyu(option_a_countable, option_b_countable)) + '\n')
    f.write('\n')

    # f.write(anova()) # https://plot.ly/python/anova/
    # f.write('\n')

    # f.write("ttest related option_a v. option_b: " + str(scipy.stats.ttest_rel(option_a_countable, option_b_countable)) + '\n')
    # f.write("ttest independent option_a v. option_b: " + str(scipy.stats.ttest_ind(option_a_countable, option_b_countable)) + '\n')
    f.write('\n')

    f.close()


def percent_per_factor(question, focus_var, answer_to_count_per_category, category_counts, category_names):
    if question == 'participation_group_project_role':
        pass
    logging.info("select all that apply graph")
    num_categories = len(answer_to_count_per_category)

    assert (num_categories == len(answer_to_count_per_category) and
            num_categories == len(category_counts) and
            num_categories == len(category_names))

    # start graphing:
    plt.figure()

    plt.rcdefaults()
    fig, axes = plt.subplots(figsize=(11, 8.5))

    bar_width = .1
    counter = 0

    for category_name, dict_ans_count, count in zip(category_names, answer_to_count_per_category, category_counts):
        possible_answers = dict_ans_count.keys()
        index = np.arange(len(possible_answers))
        axes.set_yticks(index + bar_width / 2)
        axes.set_yticklabels(possible_answers)

        category_performance = calc_percent(dict_ans_count, count)

        answers_with_new_lines = []
        for answer in possible_answers:
            if len(answer) > 40:
                # answer = '\n'.join(answer[i:i + 30] for i in range(0, len(answer), 30))
                answer = answer[:40]
            answers_with_new_lines.append(answer)


        axes.barh(index + bar_width * counter, category_performance, bar_width, tick_label=answers_with_new_lines,
                  label=category_name)  # color=color_a,
        axes.set_yticks(index)
        axes.set_yticklabels(answers_with_new_lines) # possible_answers
        axes.set_xlim(0, 1)

        counter += 1

    axes.legend()
    plt.title(short_to_long[question])
    plt.tight_layout()
    plt.savefig('results_at_BYU/' + focus_var + '/percent_per_factor/' + question + '.pdf')


def make_box_and_whisker(question, list_options, focus_var, names_of_options):
    option_a = list_options
    a = names_of_options

    plt.figure()
    plt.suptitle(question)  # ques_to_question['confidence_graduate_gpa'] + str(datetime.now().time()))

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 6), sharey=True)

    axes[0].boxplot(option_a)
    axes[0].set_title(a)

    plt.savefig('results_at_BYU/' + focus_var + '/box_and_whisker/' + question + '.pdf')


def get_file_location(question, focus_var, graph_type):
    x_values = sorted_answers(ques_ans[question])  # possible answers

    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results_at_BYU/' + focus_var + '/' + graph_type + '/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results_at_BYU/' + focus_var + '/' + graph_type + '/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results_at_BYU/' + focus_var + '/' + graph_type + '/error/' + question + '.pdf'

    return file_destination, x_values


def pie_chart(question, choice_to_answer):
    fig, axes = plt.subplots()

    plt.axis("equal")

    sum_answers = 0
    for val in choice_to_answer:
        sum_answers += int(choice_to_answer[val])

    axes.set_title(question)
    # for choice in choice_to_answer:
    #     val = choice_to_answer[choice]
    #     wedges, texts, autotexts = axes.pie(val, explode=None, labels=None, autopct='%1.1f%%', colors=long_colors)

    print(type(choice_to_answer))
    keys = choice_to_answer.keys()
    values = choice_to_answer.values()

    wedges, texts, autotexts = axes.pie(values, explode=None, labels=None, autopct='%1.1f%%', colors=long_colors)

    # handles, labels
    plt.legend(wedges, keys, title="Legend", loc="lower center", bbox_to_anchor=(1, 0, 0.5, 1))

    plt.savefig('results_at_BYU/overall/' + question + '.pdf')


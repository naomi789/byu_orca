import numpy as np
import matplotlib.pyplot as plt
from constants import question_shorthand, answer_type, question_string, agreement, frequency, frequency_TA, \
    frequency_class, comfort, certainty, color_options, long_colors

from list_constants import responsibilities, professor_encouragement, meetings_clubs, percentage, scholarships, \
    yes_no, involvement, appearance_comments, sexism_response, student_groups_standards, majors_minors, \
    graduation_year, extracurriculars, encouragement, barriers, likert_question_answer_types, list_question_answer_types
from itertools import zip_longest
from textwrap import wrap
import scipy.stats
from scipy.stats import mannwhitneyu


def filter_and_graph(question, options, people, answer_type, focus_var, category_names):
    a=category_names[0]
    b=category_names[1]

    num_categories = len(category_names)
    categorized_responses = np.empty([num_categories, 0]).tolist()
    for person in people:
        focus_var_person = getattr(person, focus_var)
        if focus_var_person == "":
            continue
        if focus_var == "university_graduation_year":
            for category in zip(category_names, categorized_responses):
                if focus_var_person == category[0]:
                    category[1].append(getattr(person, question))
        else:
            if focus_var_person == a:
                categorized_responses[0].append(getattr(person, question))
            else:  # elif focus_var_person[:4] == 'Not ':
                categorized_responses[1].append(getattr(person, question))
    option_a=categorized_responses[0]
    option_b=categorized_responses[1]

    graphable_options = values(categorized_responses, options)
    option_a_graphable = graphable_options[0]
    option_b_graphable = graphable_options[1]

    #  decide and call preferred graph here
    #bar_graph(question, focus_var, option_a_graphable, option_b_graphable, len(option_a), len(option_b), a, b)
    #pie_chart(question, focus_var, option_a_graphable, option_b_graphable, len(option_a), len(option_b), a, b)

    if answer_type in list_question_answer_types:
        percent_per_factor(question, focus_var, option_a_graphable, option_b_graphable, len(option_a), len(option_b), a,
                           b)
    elif answer_type in likert_question_answer_types:
        category_counts=list(map(len, categorized_responses))
        likert_percents(question, focus_var, graphable_options, category_counts, category_names)

    elif answer_type in likert_question_answer_types:
        f = open('results/' + focus_var + '/likert_stats/' + question + '.txt', 'w')
        option_a_countable = convert_into_numbers(option_a_graphable)
        option_b_countable = convert_into_numbers(option_b_graphable)

        f.write("question: " + question + '\n')
        f.write("dict: " + str(option_a_graphable) + '\n')
        f.write("dict: " + str(option_b_graphable) + '\n')
        f.write('\n')

        f.write("option_a, " + a + " wilcoxon: " + str(scipy.stats.wilcoxon(option_a_countable)) + '\n')
        f.write("option_b, " + b + " wilcoxon: " + str(scipy.stats.wilcoxon(option_b_countable)) + '\n')
        f.write('\n')

        f.write(
            "mann whitney " + a + " v. " + b + ": " + str(mannwhitneyu(option_a_countable, option_b_countable)) + '\n')
        f.write('\n')

        # f.write(anova()) # https://plot.ly/python/anova/
        # f.write('\n')

        # f.write("ttest related option_a v. option_b: " + str(scipy.stats.ttest_rel(option_a_countable, option_b_countable)) + '\n')
        # f.write("ttest independent option_a v. option_b: " + str(scipy.stats.ttest_ind(option_a_countable, option_b_countable)) + '\n')
        f.write('\n')

        f.close()


def convert_into_numbers(option_and_count_dict):
    responses_as_numbers = []
    counter = 1
    for key in option_and_count_dict.keys():
        if key != "":
            for num in range(0, option_and_count_dict[key]):
                responses_as_numbers.append(counter)
        counter = counter + 1
    return responses_as_numbers


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


#def values_per_a_and_b(option_a, option_b, options):
#    option_a_graphable = dict.fromkeys(sorted_answers(options), 0)
#    option_b_graphable = dict.fromkeys(sorted_answers(options), 0)
#
#    if options in likert_question_answer_types:
#        option_a_graphable = filter_for_a_and_b(option_a, option_a_graphable)
#        option_b_graphable = filter_for_a_and_b(option_b, option_b_graphable)
#    elif options in list_question_answer_types:
#        option_a_graphable = deconstruct_answers_filter(option_a, option_a_graphable)
#        option_b_graphable = deconstruct_answers_filter(option_b, option_b_graphable)
#
#    return option_a_graphable, option_b_graphable

def values(option_list, options):
    foo = [dict.fromkeys(sorted_answers(options), 0) for _ in option_list]
    bar = zip(option_list, foo)

    if options in likert_question_answer_types:
        ret = map(lambda x: filter_for_a_and_b(x[0], x[1]), bar)
    elif options in list_question_answer_types:
        ret = map(lambda x: deconstruct_answers_filter(x[0], x[1]), bar)

    return list(ret)

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
    # rects3 = ax.bar(ind + width / 2, other_prefer_not, width,
    #                 color='lime', label='other_p_not')

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
        if total_responses == 0:
            ordered_list.append(0)
        else:
            ordered_list.append(int(options_to_answers[key]) / total_responses)
    return ordered_list


def likert_percents(question, focus_var, category_values, category_counts, category_names):
    num_categories=len(category_values)
    assert(num_categories == len(category_values) and
           num_categories == len(category_counts) and
           num_categories == len(category_names))
    plt.figure()
    title='question: ' + question + '\n'
    title+= 'focus_var: ' + focus_var + '\n'
    categories=list(zip(category_counts, category_names))
    for category in categories:
        title+=str(category[1]) + ' (' + str(category[0]) + ')\n'
    plt.suptitle(title)

    ind = [x for x, _ in enumerate(category_values)]

    possible_responses=category_values[0].keys()
    for category in category_values:
            assert(category.keys() == possible_responses)

    all_bars = []

    categories=list(zip(category_values, category_counts))
    for response in possible_responses:
        set_of_responses=[]
        for category in categories:
            if category[1] == 0:
                set_of_responses.append(0)
            else:
                set_of_responses.append(category[0][response] / category[1])

        all_bars.append(set_of_responses)

    counter = 0
    used_bars = [0 for _ in range(num_categories)]

    responses=list(zip(all_bars, possible_responses))
    for response in responses:
        plt.bar(ind, response[0], width=.8, label=response[1], color=color_options[counter], bottom=used_bars) # temp
        used_bars = [x + y for x, y in zip(used_bars, response[0])]

        counter += 1

    plt.xticks(ind, category_names)
    plt.ylim(ymax=1)
    plt.ylabel("Percent of Likert Responses")
    plt.legend(loc="upper right")

    plt.savefig('results/' + focus_var + '/likert_percents/' + question + '.pdf')


def percent_per_factor(question, focus_var, option_a, option_b, count_option_a_responses, count_option_b_responses, a,
                       b):
    plt.figure()
    plt.suptitle(question)

    plt.rcdefaults()
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8.5, 11))
    possible_answers = option_a.keys()
    y_pos = np.arange(len(possible_answers))

    axes[0].set_yticks(y_pos)
    axes[0].set_yticklabels(possible_answers)

    option_a_performance = calc_percent(option_a, count_option_a_responses)
    option_b_performance = calc_percent(option_b, count_option_b_responses)

    if a == 'Male':
        color_a = 'deepskyblue'
        color_b = 'hotpink'
    else:
        color_a = 'orange'
        color_b = 'navy'
    axes[0].barh(y_pos, option_a_performance, align='center', color=color_a, tick_label=possible_answers)
    axes[0].set_yticks(y_pos)
    axes[0].set_yticklabels(possible_answers)
    axes[0].set_xlim(0, 1)

    plt.xlabel(b)
    axes[1].barh(y_pos, option_b_performance, align='center', color=color_b, tick_label=possible_answers)
    axes[1].set_yticks(y_pos)
    axes[1].set_yticklabels(possible_answers)
    axes[1].set_xlim(0, 1)

    plt.tight_layout()
    plt.savefig('results/' + focus_var + '/percent_per_factor/' + question + '.pdf')


def make_box_and_whisker(question, option_a, option_b, focus_var, a, b):
    plt.figure()
    plt.suptitle(question)  # ques_to_question['confidence_graduate_gpa'] + str(datetime.now().time()))

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 6), sharey=True)

    axes[0].boxplot(option_a)
    axes[0].set_title(a)

    axes[1].boxplot(option_b)
    axes[1].set_title(b)

    plt.savefig('results/' + focus_var + '/box_and_whisker/' + question + '.pdf')


def get_file_location(question, focus_var, graph_type):
    ques_ans = ques_to_answer()
    x_values = sorted_answers(ques_ans[question])  # possible answers

    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results/' + focus_var + '/' + graph_type + '/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results/' + focus_var + '/' + graph_type + '/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results/' + focus_var + '/' + graph_type + '/error/' + question + '.pdf'

    return file_destination, x_values


def pie_chart(question, focus_var, option_a, option_b, count_option_a_responses, count_option_b_responses, a, b):
    file_destination, x_values = get_file_location(question, focus_var, 'pie_chart')

    option_a_vals = option_a.values()
    option_b_vals = option_b.values()

    num_plots = len(x_values)
    fig, axes = plt.subplots(nrows=1, ncols=2)  # figsize=(8, 4))

    axes[0].set_title(a + " " + str(count_option_a_responses))
    axes[0].axis('equal')
    wedges, texts, autotexts = axes[0].pie(option_a_vals, explode=None, labels=None, autopct='%1.1f%%',
                                           colors=long_colors)  # colors=color_options,

    axes[1].set_title(b + " " + str(count_option_b_responses))
    axes[1].axis('equal')
    pie_2 = axes[1].pie(option_b_vals, explode=None, labels=None, autopct='%1.1f%%', colors=long_colors)

    plt.subplots_adjust(wspace=1)

    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    title = '\n'.join(longhand[i:i + 60] for i in range(0, len(longhand), 60))
    plt.suptitle(title)

    plt.legend(wedges, x_values, title="Legend", loc="lower center",
               bbox_to_anchor=(1, 0, 0.5, 1))  # lower right # best # center right

    plt.savefig(file_destination)

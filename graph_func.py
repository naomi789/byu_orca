import numpy as np
import matplotlib.pyplot as plt
from constants import question_shorthand, question_string, answer_type, agreement, comfort, certainty, frequency, \
    frequency_class, frequency_TA, color_options, long_colors
from list_constants import responsibilities, professor_encouragement, meetings_clubs, percentage, scholarships, yes_no, \
    involvement, appearance_comments, sexism_response, student_groups_standards, majors_minors, graduation_year, \
    extracurriculars, encouragement, barriers, likert_question_answer_types, list_question_answer_types
from itertools import zip_longest
from textwrap import wrap
import scipy.stats
from scipy.stats import mannwhitneyu


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

    ques_ans = ques_to_answer()
    answer_type = ques_ans[question]

    if answer_type in likert_question_answer_types:
        f = open('results/by_gender/likert_stats/' + question + '.txt', 'w')
        men_countable = convert_into_numbers(men_graphable)
        women_countable = convert_into_numbers(women_graphable)

        f.write("question: " + question + '\n')
        # f.write("men: " + str(men_countable) + '\n')
        f.write("dict: " + str(men_graphable) + '\n')
        # f.write("women: " + str(women_countable) + '\n')
        f.write("dict: " + str(women_graphable) + '\n')
        f.write('\n')

        # TODO: get all of these lists of strings into actual numbers
        f.write("men, wilcoxon: " + str(scipy.stats.wilcoxon(men_countable)) + '\n')
        f.write("women, wilcoxon: " + str(scipy.stats.wilcoxon(women_countable)) + '\n')
        f.write('\n')

        f.write("mann whitney men v. women: " + str(mannwhitneyu(men_countable, women_countable)) + '\n')
        f.write('\n')

        # f.write(anova()) # https://plot.ly/python/anova/
        # f.write('\n')

        # f.write("ttest related men v. women: " + str(scipy.stats.ttest_rel(men_countable, women_countable)) + '\n')
        # f.write("ttest independent men v. women: " + str(scipy.stats.ttest_ind(men_countable, women_countable)) + '\n')
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


def filter_for_gender(unsorted_one_gender_answers, answer_count_dictionary):
    for answer in unsorted_one_gender_answers:
        answer_count_dictionary[answer] += 1
    return answer_count_dictionary


def deconstruct_answers_filter(unsorted_one_gender_answers, answer_count_dictionary):
    for all_selected in unsorted_one_gender_answers:
        split_all_selected = [split_all_selected.strip() for split_all_selected in all_selected.split(',')]
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

    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results/by_gender/bar_graph/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results/by_gender/bar_graph/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results/by_gender/bar_graph/error/' + question + '.pdf'

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
    title = '\n'.join(longhand[i:i + 60] for i in range(0, len(longhand), 60))
    ax.set_title(title)

    ax.set_xticks(np.arange(len(x_values)))
    ax.set_xticklabels(x_values)
    ax.legend()  #

    plt.savefig(file_destination)


def make_box_and_whisker(question, men, women):
    plt.figure()
    plt.suptitle(question)  # ques_to_question['confidence_graduate_gpa'] + str(datetime.now().time()))

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 6), sharey=True)

    axes[0].boxplot(men)
    axes[0].set_title('men')

    axes[1].boxplot(women)
    axes[1].set_title('women')

    plt.savefig('results/by_gender/box_and_whisker/' + question + '.pdf')


def get_file_location(question):
    ques_ans = ques_to_answer()
    x_values = sorted_answers(ques_ans[question])  # possible answers

    if ques_ans[question] in list_question_answer_types:
        file_destination = 'results/by_gender/pie_chart/select_all/' + question + '.pdf'
    elif ques_ans[question] in likert_question_answer_types:
        file_destination = 'results/by_gender/pie_chart/mult_choice/' + question + '.pdf'
    else:
        file_destination = 'results/by_gender/pie_chart/error/' + question + '.pdf'

    return file_destination, x_values


def pie_chart(question, men, other_prefer_not, women):
    file_destination, x_values = get_file_location(question)

    men_vals = men.values()
    women_vals = women.values()

    num_plots = len(x_values)
    fig, axes = plt.subplots(nrows=1, ncols=2)  # figsize=(8, 4))

    # colormap = plt.cm.gist_ncar # .set_prop_cycle
    # plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])
    # below should have a better answer than the commented out code
    # https: // stackoverflow.com / questions / 8389636 / creating - over - 20 - unique - legend - colors - using - matplotlib
    axes[0].set_title('Male')
    axes[0].axis('equal')
    wedges, texts, autotexts = axes[0].pie(men_vals, explode=None, labels=None, autopct='%1.1f%%', colors=long_colors) # colors=color_options,

    axes[1].set_title('Female')
    axes[1].axis('equal')
    pie_2 = axes[1].pie(women_vals, explode=None, labels=None, autopct='%1.1f%%', colors=long_colors) # colors=color_options,

    plt.subplots_adjust(wspace=1)

    ques_to_question = dict(zip_longest(question_shorthand, question_string[:len(question_shorthand)]))
    longhand = ques_to_question[question]
    title = '\n'.join(longhand[i:i + 60] for i in range(0, len(longhand), 60))
    plt.suptitle(title)

    plt.legend(wedges, x_values, title="Legend", loc="bottom", bbox_to_anchor=(1, 0, 0.5, 1))  # lower right # best # center right

    plt.savefig(file_destination)

from graph_func import filter_and_graph, make_box_and_whisker, call_respective_graphing_functions
# from overall_survey import ques_to_question
from collections import defaultdict
from scipy.stats import mannwhitneyu


# import statsmodels.api as sm




def graph_string(question, people):
    print("graph string")
    f = open('results_at_BYU/strings/' + question + '.txt', 'w', encoding='utf-8')
    # ques_to_question = ques_to_question()
    f.write("question: " + question + '\n\n')
    string_value = defaultdict(int)
    for person in people:
        value = getattr(person, question)
        if value != "":
            string_value[value] += 1

    for key in string_value.keys():
        f.write(str(key) + ": " + str(string_value[key]))
        f.write('\n')
    f.close()


def long_text(question, people):
    print("graph long text")
    f = open('results_at_BYU/strings/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')
    for person in people:
        value = getattr(person, question)
        if value != "":
            f.write(value)
            f.write('\n')
            f.write('\n')

    f.close()


def graph_num(question, focus_var, people):
    print("graph numbers")
    number_questions = ['university_gpa_TEXT', 'confidence_percentile']
    if question not in number_questions :
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
    print("graph gender number")
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
        elif value.isdigit() and int(value) < 5:
            if focus_attribute == a:
                option_a.append(int(value))
            elif b_is_not_a:
                option_b.append(int(value))
            elif focus_attribute == b:
                option_b.append(int(value))

        elif value.replace('.', '', 1).isdigit() and float(value) < 5:
            if focus_attribute == a:
                option_a.append(float(value))
            elif b_is_not_a:
                option_b.append(float(value))
            elif focus_attribute == b:
                option_b.append(float(value))
        else:
            other_prefer_not.append(value)
    gender_graph_num_stats(question, people, focus_var, a, b, option_a, option_b)


def gender_graph_num_stats(question, people, focus_var, a, b, option_a, option_b):
    option_a.sort()
    option_b.sort()

    # # todo: delete this it was just for debugging
    # print('a: ' + a)
    # print('b: ' + b)
    # print('option_a: ' + str(option_a))
    # print('option_b: ' + str(option_b))
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


def mult_choice(question, focus_var, possible_answers, people, answer_type):
    variables = []
    if focus_var == 'gender':
        categories = ['Male', 'Female']
        option_a_graphable, option_b_graphable, list_all_answers_from_people_in_category_a, list_all_answers_from_people_in_category_b, list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, possible_answers, people, answer_type, focus_var, categories)

    elif focus_var == 'university_program':
        categories = ['Undergraduate', 'Not undergrads']
        option_a_graphable, option_b_graphable, list_all_answers_from_people_in_category_a, list_all_answers_from_people_in_category_b, list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, possible_answers, people, answer_type, focus_var, categories)

    elif focus_var == 'university_major':
        categories = ['Computer Science', 'Not CS majors']
        option_a_graphable, option_b_graphable, list_all_answers_from_people_in_category_a, list_all_answers_from_people_in_category_b, list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, possible_answers, people, answer_type, focus_var, categories)

    elif focus_var == 'university_graduation_year':
        categories = ['2018', '2019', '2020', '2021 or later']
        option_a_graphable, option_b_graphable, list_all_answers_from_people_in_category_a, list_all_answers_from_people_in_category_b, list_all_answers_per_category, answer_to_count_per_category = filter_and_graph(question, possible_answers, people, answer_type, focus_var, categories)

    call_respective_graphing_functions(question, focus_var, possible_answers, people, answer_type, option_a_graphable, option_b_graphable, list_all_answers_from_people_in_category_a, list_all_answers_from_people_in_category_b, list_all_answers_per_category, answer_to_count_per_category, categories)





def compare_confidence_GPA(people, focus_var, a, b):
    question = 'compare confidence to GPA'
    print(question)
    f = open('results_at_BYU/' + focus_var + '/numbers/' + question + '.txt', 'w')
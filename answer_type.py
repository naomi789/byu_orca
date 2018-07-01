from graph_func import gender_graphing, make_box_and_whisker
# from overall_survey import ques_to_question
from collections import defaultdict
from scipy.stats import mannwhitneyu
# import statsmodels.api as sm



def graph_string(question, people):
    f = open('results/strings/' + question + '.txt', 'w')
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
    f = open('results/strings/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')
    for person in people:
        value = getattr(person, question)
        if value != "":
            f.write(value)
            f.write('\n')
            f.write('\n')

    f.close()


def graph_num(question, focus_var, people):
    if question != 'university_gpa_TEXT':
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
    f = open('results/' + focus_var + '/numbers/' + question + '.txt', 'w')
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

    option_a.sort()
    option_b.sort()

    f = open('results/' + focus_var + '/numbers/' + question + '.txt', 'w')
    f.write("focus_var: " + focus_var + '\n')
    f.write("question: " + question + '\n\n')

    f.write("option_a: " + str(option_a) + '\n')
    f.write("option_b: " + str(option_b) + '\n\n')

    f.write("avg " + a + " GPA: " + str(sum(option_a)/len(option_a)) + '\n')
    f.write("avg " + b + " GPA: " + str(sum(option_b)/len(option_b)) + '\n')


    f.write("mann whitney option_a v. option_b: " + str(mannwhitneyu(option_a, option_b)) + '\n')
    # no ttests because unequal numbers of option_a and option_b

    # anova tests take a bit more work
    # moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)', data=data).fit()
    # table = sm.stats.anova_lm(moore_lm, typ=2)  # Type 2 ANOVA DataFrame
    # f.write("ANOVA: " + str(table))

    f.close()
    make_box_and_whisker(question, option_a, option_b, focus_var)

def mult_choice(question, focus_var, options, people, answer_type):
    if focus_var == 'gender':
        gender_graphing(question, options, people, answer_type)
    #  elif # think about graduation date, major, age, etc

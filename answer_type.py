from graph_func import gender_graphing, make_box_and_whisker
# from overall_survey import ques_to_question
from collections import defaultdict
from scipy.stats import mannwhitneyu
# import statsmodels.api as sm



def graph_string(question, people):
    f = open('results/by_gender/strings/' + question + '.txt', 'w')
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
    f = open('results/by_gender/strings/' + question + '.txt', 'w')
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

    f = open('results/by_gender/numbers/' + question + '.txt', 'w')
    f.write("question: " + question + '\n\n')
    if focus_var == 'gender':
        men = []
        women = []
        other_prefer_not = []

        for person in people:
            value = getattr(person, question)
            gender = getattr(person, 'gender')
            if value == "":
                continue
            elif value.isdigit() and int(value) < 5:
                if gender == 'Male':
                    men.append(int(value))
                elif gender == 'Female':
                    women.append(int(value))

            elif value.replace('.', '', 1).isdigit() and float(value) < 5:
                if gender == 'Male':
                    men.append(float(value))
                elif gender == 'Female':
                    women.append(float(value))
            else:
                other_prefer_not.append(value)

        men.sort()
        women.sort()

        f = open('results/by_gender/numbers/' + question + '.txt', 'w')
        f.write("question: " + question + '\n\n')

        f.write("men: " + str(men) + '\n')
        f.write("women: " + str(women) + '\n\n')

        f.write("avg male GPA: " + str(sum(men)/len(men)) + '\n')
        f.write("avg female GPA: " + str(sum(women)/len(women)) + '\n')


        f.write("mann whitney men v. women: " + str(mannwhitneyu(men, women)) + '\n')
        # no ttests because unequal numbers of men and women

        # anova tests take a bit more work
        # moore_lm = ols('conformity ~ C(fcategory, Sum)*C(partner_status, Sum)', data=data).fit()
        # table = sm.stats.anova_lm(moore_lm, typ=2)  # Type 2 ANOVA DataFrame
        # f.write("ANOVA: " + str(table))

        f.close()
        make_box_and_whisker(question, men, women)

def mult_choice(question, focus_var, options, people, answer_type):
    if focus_var == 'gender':
        gender_graphing(question, options, people, answer_type)
    #  elif # think about graduation date, major, age, etc

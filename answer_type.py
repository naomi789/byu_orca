from graph_func import gender_graphing

def graph_string(question, var, people):
    print("graph string axis")


def graph_int(question, var, people):
    print("graph int axis")


def graph_double(question, var, people):
    print("graph double axis")


def mult_choice(question, focus_var, options, people):
    if focus_var == 'gender':
        gender_graphing(question, options, people)
    #  elif # think about graduation date, major, age, etc

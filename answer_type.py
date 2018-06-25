from graph_func import gender_graphing

def graph_string(question, var, people):
    print("graph string axis")


def graph_int(question, var, people):
    print("graph int axis")


def graph_double(question, var, people):
    print("graph double axis")


def graph_list(question, var, people):
    print("graph list axis")


def graph_likert(question, var, type_likert, people):
    if var == 'gender':
        gender_graphing(question, type_likert, people)
    #  elif #
    # print("question type is: " + type_likert)

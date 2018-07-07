from overall_survey import run_overall

def main():
    import_data()


def import_data():
    data = run_overall('confidence_preliminary.csv')
    data = data[2:]  # deletes the question text and shorthand from the dataset

    # all_people = list(map(lambda line: Person(*line), data))
    # all_students = []
    # for person in all_people:  # filters out all responses where there is no gender
    #     if getattr(person, 'gender') is not '':
    #         all_students.append(person)
    #     #  todo: should also check that other values are not '' # ['gender', 'gradu_year', 'cs_not_major']  # maybe GPA, too?
    # return all_students
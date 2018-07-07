from overall_survey import run_overall
from data_structures import confident_person

def main():
    all_students_whole_semester = import_data()


def import_data():
    # first survey # raw_first_confidence_survey/confidence_preliminary.csv
    data = run_overall('raw_first_confidence_survey/confidence_preliminary.csv')
    data = data[2:]  # deletes the question text and shorthand from the dataset

    all_raw_preliminary_students = list(map(lambda line: confident_person(*line), data))
    preliminary_students = []
    for person in all_raw_preliminary_students:  # filters out all responses where there is no gender
        if getattr(person, 'gender') is not '':
            preliminary_students.append(person)


    # middle surveys # raw_middle_confidence_survery/raw_middle.csv


    # final_sruveys # raw_final_confidence_survey/final_raw.csv

    final_data = run_overall('raw_final_confidence_survey/confidence_final.csv')
    data = data[:2]
    all_raw_final_students = [] # list(map(lambda line: confident_person(*line), data))
    final_students = []

    all_students_whole_semester = []

    return all_students_whole_semester

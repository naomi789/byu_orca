from overall_survey import run_overall
from data_structures import first_confident_person, middle_confidence_person, last_confidence_person

def main():
    all_students_whole_semester = import_data()


def one_source(file, tuple_results):
    # first survey  # raw_first_confidence_survey/confidence_preliminary.csv
    data = run_overall(file)
    data = data[2:]  # deletes the question text and shorthand from the dataset

    processed = list(map(lambda line: tuple_results(*line), data))
    answer = []
    for person in processed:  # filters out all responses where there is no gender
        if getattr(person, 'gender') is not '':
            answer.append(person)

    return answer

def import_data():
    # first survey # raw_first_confidence_survey/confidence_preliminary.csv
    first_survey = one_source('raw_first_confidence_survey/confidence_preliminary.csv', first_confident_person)

    # middle surveys # raw_middle_confidence_survery/raw_middle.csv
    # for file in folder:
    middle_survey = one_source('raw_middle_confidence_survery/raw_middle.csv', middle_confidence_person)

    # final_surveys # raw_final_confidence_survey/final_raw.csv
    final_survey = one_source('raw_final_confidence_survey/confidence_final.csv', last_confidence_person)




    all_students_whole_semester = []
    return all_students_whole_semester

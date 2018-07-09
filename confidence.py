from overall_survey import run_overall
from data_structures import first_confident_person, middle_confidence_person, last_confidence_person


def main():
    pass


def one_source(file, tuple_for_results):
    # first survey  # raw_first_confidence_survey/confidence_preliminary.csv
    data = run_overall(file)
    data = data[2:]  # deletes the question text and shorthand from the dataset

    processed = list(map(lambda line: tuple_for_results(*line), data))
    answer = []  # TODO: make this into a dictionary; map + key
    for person in processed:  #  filters out all responses where there is no gender
        if getattr(person, 'gender') is not '':
            answer.append(person)
            #  save the 'identifier' as a key with person as a value

    return answer


def import_data():
    # first survey # raw_first_confidence_survey/confidence_preliminary.csv
    first_survey = one_source('raw_first_confidence_survey/confidence_preliminary.csv', first_confident_person)

    # middle surveys # raw_middle_confidence_survery/raw_middle.csv
    all_middle_results = []
    for file in ['raw_middle_confidence_survery/raw_middle.csv']:
        middle_survey = one_source(file, middle_confidence_person)
        all_middle_results.append(middle_survey)

    # final_surveys # raw_final_confidence_survey/final_raw.csv
    final_survey = one_source('raw_final_confidence_survey/confidence_final.csv', last_confidence_person)

    return first_survey, all_middle_results, final_survey


def unite_into_people(first_survey, all_middle_results, final_survey):
    for person_id in first_survey.keys():
        getattr(first_survey[person_id], 'identifier')
        getattr(all_middle_results[person_id], 'identifier')  # TODO: people filled this out like seven times. Hopefully.
        getattr(last_confidence_person[person_id], 'identifier') # TODO: what about the flakes who didn't fill out more?
        # TODO: ideally, we can connect this to the original survey as well
    pass


first_survey, all_middle_results, final_survey = import_data()
unite_into_people(first_survey, all_middle_results, final_survey)
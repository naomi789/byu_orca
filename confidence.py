from overall_survey import run_overall
from data_structures import first_confident_person, middle_confidence_person, last_confidence_person

def main():
    first_survey, all_middle_results, final_survey = import_data()

    # graph all confidence points across time, one line per CLASS (expect: see differences) (do I care about professor differences? no?)
    # graph all confidence points across time, one line per GENDER (expect: women are lower than men)
    # graph all confidence points across time, one line per FINAL GRADE (positive slope if good grade, zero/negative/shaky for bad grades)
    # graph all confidence points across time, one line per FINAL GRADE PER GENDER (women need a higher grade to see an uptick in confidence)
    # graph all confidence points across time, one line per class per gender (women dislike 142 and 235 more)
    # graph all confidence points across time (expect: if confidence fell more than X points, they are no longer CS majors)
    # compare overall GPA to confidence levels (each metric) (expect: correlation. ofc.)
    # compare overall GPA to confidence levels (each metric) PER GENDER (expect: given X gpa, women have lower confidence than men)
    # compare each confidence metric to the other (what is/is not consistent)

    # expect: non majors who grow in confidence are more likely to switch to CS
    # expect: CS majors who's confidence falls are more likely to leave CS
    # expect: if I asked about age, expect younger students to have weaker study habits --> less confidence EXCEPT UW paper questions
    # expect: sooner graduation date --> more confidence in intro CS courses? or less bc they've been nurveous and procrastinating?
    # expect: upperclassmen to feel more prepared before the semester. Have more confidence in graduating. )

def one_source(file, tuple_for_results):
    # first survey  # raw_first_confidence_survey/confidence_preliminary.csv
    data = run_overall(file)
    data = data[2:]  # deletes the question text and shorthand from the dataset

    processed = list(map(lambda line: tuple_for_results(*line), data))
    answer = []  # make this into a dictionary
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

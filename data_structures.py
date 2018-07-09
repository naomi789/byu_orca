from collections import namedtuple

first_confidence_survey = ['date', 'identifier', 'gender', 'gender_other', 'gpa', 'major', 'graduating_year', 'confidence_prepared',
                           'confidence_ability', 'confidence_general_classes', 'confidence_major',
                           'confidence_get_degree', 'confidence_percentile']

first_confident_person = namedtuple('Confident_person', first_confidence_survey)

middle_confidence_survey = ['date', 'identifier', 'confidence_general_classes', 'confidence_major_classes',
                            'confidence_excel_graduate', 'confidence_get_degree', 'confidence_percentile']

middle_confidence_person = namedtuple('middle_confident_person', middle_confidence_survey)

last_confidence_survey = ['date', 'identifier', 'confidence_general_classes', 'confidence_major_classes', 'confidence_excel_graduate',
                          'confidence_get_degree', 'confidence_career', 'confidence_percentile', '1_grade', '1_class',
                          '2_grade', '2_class', '3_grade', '3_class', '4_grade', '4_class']

last_confidence_person = namedtuple('last_confidence_person', last_confidence_survey)


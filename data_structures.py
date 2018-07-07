from collections import namedtuple

first_confidence_survey = ['email', 'gender', 'gender_other', 'gpa', 'major', 'graduating_year', 'confidence_prepared',
                           'confidence_ability', 'confidence_general_classes', 'confidence_major',
                           'confidence_get_degree', 'confidence_percentile']

first_confident_person = namedtuple('Confident_person', first_confidence_survey)

middle_confidence_survey = ['identifier', 'confidence_general_classes', 'confidence_major', 'confidence_get_degree',
                            'confidence_percentile']

middle_confidence_person = namedtuple('middle_confident_person', middle_confidence_survey)

last_confidence_survey = ['identifier', 'confidence_general_classes', 'confidence_major', 'confidence_get_degree',
                          'confidence_get_degree', 'confidence_career', 'confidence_percentile', '1_class', '1_grade',
                          '2_class', '2_grade', '3_class', '3_grade', '4_class', '4_grade']

last_confidence_person = namedtuple('last_confidence_person', last_confidence_survey)

full_semester_of_data = []

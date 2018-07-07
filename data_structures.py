from collections import namedtuple

confidence_survey = ['email','gender', 'gender_other', 'gpa', 'major', 'graduating_year', 'confidence_prepared', 'confidence_ability', 'confidence_general_classes', 'confidence_major', 'confidence_get_degree', 'confidence_percentile']

confident_person = namedtuple('Confident_person', confidence_survey)

full_semester_of_data = []
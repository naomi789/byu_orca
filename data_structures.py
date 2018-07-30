from collections import namedtuple

first_confidence_survey = ['date', 'identifier', 'gender', 'gender_other', 'gpa', 'major', 'graduating_year', 'confidence_prepared',
                           'confidence_ability', 'confidence_general_classes', 'confidence_major',
                           'confidence_get_degree', 'confidence_percentile']

first_confident_person = namedtuple('Confident_person', first_confidence_survey)

middle_confidence_survey = ['date', 'identifier', 'confidence_general_classes', 'confidence_major_classes',
                            'confidence_excel_graduate', 'confidence_get_degree', 'confidence_percentile']

middle_confidence_person = namedtuple('middle_confident_person', middle_confidence_survey)
#
# last_confidence_survey = ['date', 'identifier', 'confidence_general_classes', 'confidence_major_classes', 'confidence_excel_graduate',
#                           'confidence_get_degree', 'confidence_career', 'confidence_percentile', '1_grade', '1_class',
#                           '2_grade', '2_class', '3_grade', '3_class', '4_grade', '4_class']

# last_confidence_person = namedtuple('last_confidence_person', last_confidence_survey)

ques_ans = {'duration_seconds': 'int', 'Location_Latitude': 'double', 'LocationLongitude': 'double',
        'consent_current': 'string', 'consent_future': 'string', 'email': 'string', 'gender': 'string',
        'gender_other': 'race', 'race': 'int', 'age': 'string', 'university_program': 'double',
        'university_major': 'string', 'university_minor': 'string', 'university_courses_fall': 'courses',
        'university_graduation_year': 'string', 'university_gpa': 'string', 'university_gpa_TEXT': 'double',
        'received_internship_offer': 'yes_no', 'extracurriculars': 'extracurriculars', 'major_pros': 'encouragement',
        'major_pros_TEXT': 'string', 'major_cons': 'barriers', 'major_cons_TEXT': 'string',
        'confidence_graduate_gpa': 'agreement', 'confidence_prepared_courses': 'agreement',
        'confidence_percentile': 'double', 'participation_questions_comfortable_NONCS': 'comfort',
        'participation_absent_frequency': 'frequency_absent',
        'participation_questions_ask_frequency': 'frequency_class_typo', 'participation_questions_comfortable': 'comfort',
        'participation_not_questions_frequency': 'frequency_class', 'participation_absent_why': 'miss_class',
        'participation_MORE_comfortable': 'increase_comfort', 'participation_LESS_comfortable': 'decrease_comfort',
        'participation_not_reasons': 'participate_decrease', 'participation_questions_ask_ignored': 'frequency_class_typo',
        'participation_group_project_role': 'responsibilities', 'professors_ask_advice': 'frequency_typo',
        'professors_encouraged_you': 'professor_encouragement', 'participation_TA_session': 'frequency_TA_typo',
        'participation_TA_ask_questions': 'frequency_typo', 'participation_talk_peers': 'frequency',
        'courses_professors_engaging': 'agreement', 'professors_represent_diversity': 'agreement',
        'role_models_same_gender': 'agreement', 'participation_peers_help_you': 'frequency_typo',
        'participation_peers_you_serve': 'frequency_typo', 'participation_clubs': 'meetings_clubs',
        'participation_friends_CS_students': 'percentage', 'friends_CS_students_want_more': 'agreement',
        'scholarship': 'scholarships', 'extracurricular_plans_before_graduation': 'involvement',
        'frequency_balance_career_parenthood': 'frequency', 'professors_declare_parent': 'frequency_typo',
        'professors_declare_full_time': 'frequency_typo', 'department_sexist_you': 'certainty',
        'department_sexist_others': 'certainty', 'department_success_because_gender': 'certainty',
        'department_appearance': 'frequency_typo', 'department_appearance_comments': 'appearance_comments',
        'complaints_how': 'certainty', 'complaints_concequences': 'certainty',
        'complaints_concequences_fear': 'certainty', 'peer_mistreated_react': 'sexism_response',
        'people_surprise_major': 'agreement', 'people_sexist_jokes_gender': 'frequency_typo',
        'highest_standard': 'student_groups_standards', 'peer_sexism_ignoring_suggestion': 'frequency_typo',
        'friends_other_gender': 'agreement', 'intelligence_fixed': 'agreement', 'intelligence_malleable': 'agreement',
        'failure_lazy': 'agreement', 'failure_environment': 'agreement', 'failure_ability': 'agreement',
        'describe_positive_experience': 'string', 'describe_negative_experience': 'string',
        'suggestion_improve_institution': 'string'}
from data_structures import *

AGE = 'Q80'
RACE = 'Q81'
GENDER = 'Q3'
PROGRAM = 'Q4'
MAJOR = 'Q5'
MINOR = 'Q6'
FALL_COURSES = 'Q7'
GRAD_YEAR = 'Q73'
GPA = 'Q74_2_TEXT'
INTERNSHIP_OFFER = 'Q50'
EXTRACURRICULARS = 'Q8'
MAJOR_PROS = 'Q10'
MAJOR_PROS_CLASS = 'Q10_21_TEXT	'
MAJOR_CONS = 'Q11'
MAJOR_CONS_CLASS = 'Q11_14_TEXT'
CONFIDENCE_GRAD_GPA = 'Q68'  # other bug
CONFIDENCE_PREPARED_COURSES = 'Q88'
CONFIDENCE_PERCENTILE_PEERS = 'Q93'
COURSES_QUESTION_COMFORT = 'Q86'
COURSES_ABSENT_FREQUENCY = 'Q84'
PARTICIPATION_QUESTIONS_ASK_FREQUENCY = 'Q16'
COURSES_ASKING_QUESTIONS_COMFORT = 'Q15'
PARTICIPATION_NOT_QUESTIONS_FREQUENCY = 'Q90'
PARTICIPATION_ABSENT_WHY = 'Q83'
PARTICIPATION_MORE_COMFORTABLE = 'Q91'
PARTICIPATION_LESS_COMFORTABLE = 'Q85'
PARTICIPATION_NOT_REASONS = 'Q92'
PARTICIPATION_QUESTIONS_ASK_IGNORED = 'Q57'
PARTICIPATION_GROUP_PROJECT_ROLE = 'Q46'
PROFESSORS_ASK_ADVICE = 'Q18'
PROFESSORS_ENCOURAGED_YOU = 'Q19'
PARTICIPATION_TA_SESSION = 'Q21'
PARTICIPATION_TA_ASK_QUESTIONS = 'Q22'
PARTICIPATION_TALK_PEERS = 'Q52'
COURSES_PROFESSORS_ENGAGING = 'Q20'
PROFESSORS_REPRESENT_DIVERSITY = 'Q59'
ROLE_MODELS_SAME_GENDER = 'Q63'
PARTICIPATION_PEERS_HELP_YOU = 'Q26'
PARTICIPATION_PEERS_YOU_SERVE = 'Q25'
PARTICIPATION_CLUBS = 'Q27'
PARTICIPATION_FRIENDS_CS_STUDENTS = 'Q28'
FRIENDS_CS_STUDENTS_WANT_MORE = 'Q82'
SCHOLARSHIP = 'Q48'
EXTRACURRICULAR_PLANS_BEFORE_GRADUATION = 'Q9'
FREQUENCY_BALANCE_CAREER_PARENTHOOD = 'Q32'
PROFESSORS_DECLARE_PARENT = 'Q31'
PROFESSORS_DECLARE_FULL_TIME = 'Q30'
DEPARTMENT_SEXIST_YOU = 'Q41'
DEPARTMENT_SEXIST_OTHERS = 'Q42'
# Q35
DEPARTMENT_APPEARANCE = 'Q62'
DEPARTMENT_APPEARANCE_COMMENTS = 'Q61'
COMPLAINTS_HOW = 'Q38'
COMPLAINTS_CONCEQUENCES = 'Q39'
COMPLAINTS_CONCEQUENCES_FEAR = 'Q40'
PEER_MISTREATED_REACT = 'Q51'
PEOPLE_SURPRISE_MAJOR = 'Q60'
PEOPLE_SEXIST_JOKES_GENDER = 'Q58'
HIGHEST_STANDARD = 'Q160'  # TODO NOTE
PEER_SEXISM_IGNORING_SUGGESTION = 'Q161'  # TODO NOTE
FRIENDS_OTHER_GENDER = 'Q56'
INTELLIGENCE_FIXED = 'Q75'
INTELLIGENCE_MALLEABLE = 'Q76'
FAILURE_LAZY = 'Q77'
FAILURE_ENVIRONMENT = 'Q78'
FAILURE_ABILITY = 'Q79'
DESCRIBE_NEGATIVE_EXPERIENCE = 'Q67'
DESCRIBE_POSITIVE_EXPERIENCE = 'Q168'
SUGGESTION_IMPROVE_INSTITUTION = 'Q54'
UNIVERSITY_COURSES_FALL = 'Q7'
PARTICIPATION_QUESTIONS_COMFORTABLE_NONCS = 'Q86'  # TODO
PARTICIPATION_QUESTIONS_COMFORTABLE = 'Q15'  # TODO

# count of how many people were invited to take this survey
FEMALE_COUNT = 427
MALE_COUNT = 2163
CS_MAJOR_COUNT = 1125
CS_MINOR_COUNT = 259
OTHER_MAJOR_COUNT = 1231
DOCTORATE_COUNT = 31
MASTER_COUNT = 79
POST_BAC_COUNT = 8
UNDERGRADUATE_COUNT = 2473

question_number_to_expected_answer = {
    'Q8': extracurriculars,
    'Q10': encouragement,  # MAJOR_PROS
    'Q11': barriers,  # MAJOR_CONS
    'Q68': agreement,  # CONFIDENCE_PREPARED_COURSES
    'Q88': agreement,  # CONFIDENCE_PERCENTILE_PEERS
    'Q84': frequency_absent,  # COURSES_ABSENT_FREQUENCY
    'Q16': frequency_class,  # PARTICIPATION_QUESTIONS_ASK_FREQUENCY
    'Q15': comfort,  # COURSES_ASKING_QUESTIONS_COMFORT
    'Q90': frequency_class,  # PARTICIPATION_NOT_QUESTIONS_FREQUENCY
    'Q83': miss_class,  # PARTICIPATION_ABSENT_WHY
    'Q91': increase_comfort,  # PARTICIPATION_MORE_COMFORTABLE
    'Q85': decrease_comfort,  # PARTICIPATION_LESS_COMFORTABLE
    'Q92': not_participate_reasons,  # PARTICIPATION_NOT_REASONS
    'Q57': frequency_class,  # PARTICIPATION_QUESTIONS_ASK_IGNORED
    'Q46': responsibilities,  # PARTICIPATION_GROUP_PROJECT_ROLE
    'Q18': frequency,  # PROFESSORS_ASK_ADVICE
    'Q19': professor_encouragement,  # PROFESSORS_ENCOURAGED_YOU
    'Q21': frequency_TA,  # PARTICIPATION_TA_SESSION
    'Q22': frequency,  # PARTICIPATION_TA_ASK_QUESTIONS
    'Q52': frequency,  # PARTICIPATION_TALK_PEERS
    'Q20': agreement,  # COURSES_PROFESSORS_ENGAGING
    'Q59': agreement,  # PROFESSORS_REPRESENT_DIVERSITY
    'Q63': agreement,  # ROLE_MODELS_SAME_GENDER
    'Q26': frequency,  # PARTICIPATION_PEERS_HELP_YOU
    'Q25': frequency,  # PARTICIPATION_PEERS_YOU_SERVE
    'Q27': meetings_clubs,  # PARTICIPATION_CLUBS
    'Q28': percentage,  # PARTICIPATION_FRIENDS_CS_STUDENTS
    'Q82': agreement,  # FRIENDS_CS_STUDENTS_WANT_MORE
    'Q48': scholarships,  # SCHOLARSHIP
    'Q9': involvement,  # EXTRACURRICULAR_PLANS_BEFORE_GRADUATION
    'Q32': frequency,  # FREQUENCY_BALANCE_CAREER_PARENTHOOD
    'Q31': frequency,  # PROFESSORS_DECLARE_PARENT
    'Q30': frequency,  # PROFESSORS_DECLARE_FULL_TIME
    'Q41': certainty,  # DEPARTMENT_SEXIST_YOU
    'Q42': certainty,  # DEPARTMENT_SEXIST_OTHERS
    # Q35 # Has a member of the CS department (students, TAs, professors, etc) ever told you that you earned a good grade, got a job, internship, or scholarship offer because of your gender?
    'Q62': frequency,  # DEPARTMENT_APPEARANCE
    'Q61': appearance_comments,  # DEPARTMENT_APPEARANCE_COMMENTS # because of this
    'Q38': certainty,  # COMPLAINTS_HOW
    'Q39': certainty,  # COMPLAINTS_CONCEQUENCES
    'Q40': certainty,  # COMPLAINTS_CONCEQUENCES_FEAR
    'Q51': sexism_response,  # PEER_MISTREATED_REACT
    'Q60': agreement,  # PEOPLE_SURPRISE_MAJOR # because of this
    'Q58': frequency,  # PEOPLE_SEXIST_JOKES_GENDER
    'Q160': student_groups_standards,  # HIGHEST_STANDARD #  TODO IMPORTANT THIS WAS EDITED
    'Q161': frequency,  # PEER_SEXISM_IGNORING_SUGGESTION  # TODO IMPORTANT THIS WAS EDITED
    'Q56': agreement,  # FRIENDS_OTHER_GENDER
    'Q75': agreement,  # INTELLIGENCE_FIXED
    'Q76': agreement,  # INTELLIGENCE_MALLEABLE
    'Q77': agreement,  # FAILURE_LAZY
    'Q78': agreement,  # FAILURE_ENVIRONMENT
    'Q79': agreement,  # FAILURE_ABILITY
    'Q50': yes_no,  # RECEIVED_INTERNSHIP_OFFER
    'Q7': byu_courses,  # UNIVERSITY_COURSES_FALL
    'Q86': comfort,  # COURSES_ASKING_QUESTIONS_COMFORT
}

answer_dict_switcher = {
    'agreement': agreement,
    'frequency': frequency,
    # 'frequency_typo': frequency_typo,
    'frequency_TA': frequency_TA,
    # 'frequency_TA_typo': frequency_TA_typo,
    'frequency_class': frequency_class,
    # 'frequency_class_typo': frequency_class_typo,
    'comfort': comfort,
    'certainty': certainty,
    'majors_minors': majors_minors,
    'graduation_year': graduation_year,
    'extracurriculars': extracurriculars,
    'encouragement': encouragement,
    'barriers': barriers,
    'responsibilities': responsibilities,
    'professor_encouragement': professor_encouragement,
    'meetings_clubs': meetings_clubs,
    'percentage': percentage,
    'scholarships': scholarships,
    'yes_no': yes_no,
    'involvement': involvement,
    'appearance_comments': appearance_comments,
    'sexism_response': sexism_response,
    'student_groups_standards': student_groups_standards,
    'frequency_absent': frequency_absent,
    'miss_class': miss_class,
    'increase_comfort': increase_comfort,
    'decrease_comfort': decrease_comfort,
    'participate_decrease': participate_decrease,
}

ques_num = [
    # 'StartDate', 'EndDate', 'Status', 'IPAddress', 'Progress', 'Duration (in seconds)', 'Finished',
    # 'RecordedDate', 'ResponseId', 'RecipientLastName', 'RecipientFirstName', 'RecipientEmail',
    # 'ExternalReference', 'LocationLatitude', 'LocationLongitude', 'DistributionChannel', 'UserLanguage',
    'Q70', 'Q89', 'Q89_1_TEXT', 'Q3', 'Q3_3_TEXT', 'Q81', 'Q80', 'Q4', 'Q5', 'Q6', 'Q7', 'Q73', 'Q74', 'Q74_2_TEXT',
    'Q50', 'Q8', 'Q10', 'Q10_21_TEXT', 'Q11', 'Q11_14_TEXT', 'Q68', 'Q88', 'Q93', 'Q86', 'Q84', 'Q16', 'Q15',
    'Q90', 'Q83', 'Q91', 'Q85', 'Q92', 'Q57', 'Q46', 'Q18', 'Q19', 'Q21', 'Q22', 'Q52', 'Q20', 'Q59', 'Q63',
    'Q26', 'Q25', 'Q27', 'Q28', 'Q82', 'Q48', 'Q9', 'Q32', 'Q31', 'Q30', 'Q41', 'Q42', 'Q35', 'Q62', 'Q61',
    'Q38', 'Q39', 'Q40', 'Q51', 'Q60', 'Q58', 'Q160', 'Q161', 'Q56', 'Q75', 'Q76', 'Q77', 'Q78', 'Q79', 'Q168',
    'Q67', 'Q54']

ques_text = [
    # 'Start Date', 'End Date', 'Response Type', 'IP Address', 'Progress', 'Duration (in seconds)', 'Finished',
    # 'Recorded Date', 'Response ID', 'Recipient Last Name', 'Recipient First Name', 'Recipient Email',
    # 'External Data Reference', 'Location Latitude', 'Location Longitude', 'Distribution Channel',
    # 'User Language',
    'Please read the entire text above before selecting an answer below.',
    'Are you willing to participate more in this study of students at BYU? - Selected Choice',
    'Are you willing to participate more in this study of students at BYU? - Yes - please enter your email address here - Text',
    'What gender do you identify with? - Selected Choice', 'What gender do you identify with? - Other - Text',
    'What is your race/ethnicity (select all that apply)?', 'How old are you?',
    'What degree are you currently pursuing?', 'What is your intended major?',
    'What is your minor/secondary major?',
    'What CS courses will you enroll in during the fall semester of 2018? (select all that apply)',
    'When do you anticipate graduating?', 'What is your current GPA at this university? - Selected Choice',
    'What is your current GPA at this university? - My current overall GPA is: - Text',
    'Have you ever been offered a CS-related internship?',
    'What extracurriculars have you pursued in high school or college? (select all that apply)',
    'What factors influenced your decision to pick your major? (select all that apply) - Selected Choice',
    'What factors influenced your decision to pick your major? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
    'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Selected Choice',
    'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
    'How much do you agree with the following statement: I am confident in my ability to graduate with a 3.0 or higher major GPA (your major GPA does not include AP/IB credits or general education/GE classes).',
    'How much do you agree with the following statement: I am prepared for my CS course(s) next semester.',
    'With respect to your peers in your major what percentile would you rank yourself at? Please enter a number between 0 and 100.',
    'How comfortable are you asking questions in your non-CS courses?',
    'How often are you absent from your CS class(es)?',
    'On average how often do you ask questions in CS courses?',
    'How comfortable are you asking questions in your CS courses?',
    'Aside from asking questions, how often do you participate (answer questions/talk in discussions/etc) in CS courses?',
    'When you miss a CS class, what is most often the reason why? (only select one)',
    'What helps you feel MORE COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
    'When do you feel LESS COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
    'Why do you not participate (aside from asking questions: answering questions/participating in discussions/etc) more in your CS course(s)?',
    'How often do you raise your hand in a CS class but never get called on?',
    'In group projects for CS courses which tasks do you typically take responsibility for? (select all that apply)',
    'How often do you discuss your academic performance or career plans with a professor or faculty member? (during office hours or in other one-on-one situations)',
    'Has as a CS professor ever invited you, personally, to consider any of the following? (select all that apply)',
    'How often do you go to TA-led help sessions for CS courses?',
    'How often to you visit the CS TAs to ask questions?',
    'How often do you talk with other students (not TAs) while in the CS TA cubicals or CS labs?',
    'How strongly do you agree with the statement: CS professors and CS courses are engaging.',
    'How strongly do you agree with the statement: I feel that the CS professors adequately represent the diverse backgrounds, views, demographics, and perspectives of students in CS courses.',
    'Do you feel like you have role models of the same gender as you who do CS?',
    'How often have you asked another student (not a TA for the course) to help you understand CS course material?',
    'How often have you mentored any students in the CS major or CS courses this semester? (assisted them with labs, homework, or given internship/job or graduate school advice)',
    'Do you attend meetings/events for any of the following? (select all that apply)',
    'What percentage of your friends are taking classes in the CS department?',
    'How much do you agree with the following statement: I want to make more friends in the CS major.',
    'Have you been the recipient of an academic scholarship? (select all that apply)',
    'Which of the following have you done, or do you plan to do before you graduate? (select all that apply)',
    'How often do members of the CS department (students, TAs, professors, etc) ask you about your plans to balance a career and parenthood?',
    'How often do members of the CS department (students, TAs, professors, etc) tell you that you should be a stay-at-home parent?',
    'How often do members of the CS department (students, TAs, professors, etc) tell you that you should pursue a full-time career?',
    'Do you feel like a member of the CS department (students, TAs, professors, etc) has treated you differently than your peers of the opposite gender?',
    'Are you aware of CS classmates who believe they have been treated differently by members of the CS department (students, TAs, professors, etc) because of their gender?',
    'Has a member of the CS department (students, TAs, professors, etc)ever told you that you earned a good grade, got a job, internship, or scholarship offer because of your gender?',
    'How often do you get negative comments about your appearance or attire from members of the CS department (students, TAs, professors, etc)?',
    'If members of the CS department (students, TAs, professors, etc) make negative comments about your appearance, what do they comment about? (select all that apply)',
    'Do you know how to file complaints for being treated differently because of your gender in the CS department?',
    'Do you know what happens if a complaint is filed against a member of the CS department who is accused of being sexist?',
    'Would you personally be worried about retribution if you filed a complaint about someone treating you or a peer differently because of your/their gender?',
    'If you saw a peer treat someone differently because of their gender (through words, actions, etc), would you say or do something? (select all that apply)',
    'How much do you agree with the following statement:When you tell people what your major is, they often express surprise (You don\'t look/act like a ____ major", Why are you majoring in ____?)?',
    'How often do you hear people in the CS department make sexist remarks or jokes about your gender?',
    'Do you feel that some students are held to a higher standard than other students in the CS department? If so, please select all groups that apply.',
    'How often, within the CS department, do you make a suggestion that was not considered until another person makes the same suggestion?',
    'Do you feel like you can have non-romantic friends of the opposite gender?',
    'How strongly do you agree with the statement: Intelligence is a fixed trait; you are born with the talents that you have and nothing you do can change them.',
    'How strongly do you agree with the statement: Intelligence is a malleable quality, if you work hard and practice you will improve.',
    'How strongly do you agree with the statement: Failure or a lack of achievement is due to insufficient effort.',
    'How strongly do you agree with the statement: Failure or a lack of achievement is due to personal or environmental obstacles.',
    'How strongly do you agree with the statement: Failure or a lack of achievement is due to a lack of ability.',
    'Are there any positive experiences or interactions that you had with members of the CS department that you would like to share?',
    'Are there any negative experiences or interactions that you had with members of the CS department that you would like to share?',
    "What one change would you most like to see implemented to improve students' experiences at this institution?"]

question_shorthand = ['CONSENT_CURRENT', 'CONSENT_FUTURE', 'EMAIL', 'GENDER', 'GENDER_OTHER', 'RACE', 'AGE',
                      'UNIVERSITY_PROGRAM', 'UNIVERSITY_MAJOR', 'UNIVERSITY_MINOR', 'UNIVERSITY_COURSES_FALL',
                      'UNIVERSITY_GRADUATION_YEAR', 'UNIVERSITY_GPA', 'UNIVERSITY_GPA_TEXT',
                      'RECEIVED_INTERNSHIP_OFFER', 'EXTRACURRICULARS', 'MAJOR_PROS', 'MAJOR_PROS_TEXT', 'MAJOR_CONS',
                      'MAJOR_CONS_TEXT', 'CONFIDENCE_GRADUATE_GPA', 'CONFIDENCE_PREPARED_COURSES',
                      'CONFIDENCE_PERCENTILE', 'PARTICIPATION_QUESTIONS_COMFORTABLE_NONCS',
                      'PARTICIPATION_ABSENT_FREQUENCY', 'PARTICIPATION_QUESTIONS_ASK_FREQUENCY',
                      'PARTICIPATION_QUESTIONS_COMFORTABLE', 'PARTICIPATION_NOT_QUESTIONS_FREQUENCY',
                      'PARTICIPATION_ABSENT_WHY', 'PARTICIPATION_MORE_COMFORTABLE', 'PARTICIPATION_LESS_COMFORTABLE',
                      'PARTICIPATION_NOT_REASONS', 'PARTICIPATION_QUESTIONS_ASK_IGNORED',
                      'PARTICIPATION_GROUP_PROJECT_ROLE', 'PROFESSORS_ASK_ADVICE', 'PROFESSORS_ENCOURAGED_YOU',
                      'PARTICIPATION_TA_SESSION', 'PARTICIPATION_TA_ASK_QUESTIONS', 'PARTICIPATION_TALK_PEERS',
                      'COURSES_PROFESSORS_ENGAGING', 'PROFESSORS_REPRESENT_DIVERSITY', 'ROLE_MODELS_SAME_GENDER',
                      'PARTICIPATION_PEERS_HELP_YOU', 'PARTICIPATION_PEERS_YOU_SERVE', 'PARTICIPATION_CLUBS',
                      'PARTICIPATION_FRIENDS_CS_STUDENTS', 'FRIENDS_CS_STUDENTS_WANT_MORE', 'SCHOLARSHIP',
                      'EXTRACURRICULAR_PLANS_BEFORE_GRADUATION', 'FREQUENCY_BALANCE_CAREER_PARENTHOOD',
                      'PROFESSORS_DECLARE_PARENT', 'PROFESSORS_DECLARE_FULL_TIME', 'DEPARTMENT_SEXIST_YOU',
                      'DEPARTMENT_SEXIST_OTHERS', 'DEPARTMENT_SUCCESS_BECAUSE_GENDER', 'DEPARTMENT_APPEARANCE',
                      'DEPARTMENT_APPEARANCE_COMMENTS', 'COMPLAINTS_HOW', 'COMPLAINTS_CONCEQUENCES',
                      'COMPLAINTS_CONCEQUENCES_FEAR', 'PEER_MISTREATED_REACT', 'PEOPLE_SURPRISE_MAJOR',
                      'PEOPLE_SEXIST_JOKES_GENDER', 'HIGHEST_STANDARD', 'PEER_SEXISM_IGNORING_SUGGESTION',
                      'FRIENDS_OTHER_GENDER', 'INTELLIGENCE_FIXED', 'INTELLIGENCE_MALLEABLE', 'FAILURE_LAZY',
                      'FAILURE_ENVIRONMENT', 'FAILURE_ABILITY', 'DESCRIBE_POSITIVE_EXPERIENCE',
                      'DESCRIBE_NEGATIVE_EXPERIENCE', 'SUGGESTION_IMPROVE_INSTITUTION']

ques_num_to_shorthand = {'Q70': 'CONSENT_CURRENT', 'Q89': 'CONSENT_FUTURE', 'Q89_1_TEXT': 'EMAIL', 'Q3': 'GENDER',
                         'Q3_3_TEXT': 'GENDER_OTHER', 'Q81': 'RACE', 'Q80': 'AGE', 'Q4': 'UNIVERSITY_PROGRAM',
                         'Q5': 'UNIVERSITY_MAJOR', 'Q6': 'UNIVERSITY_MINOR', 'Q7': 'UNIVERSITY_COURSES_FALL',
                         'Q73': 'UNIVERSITY_GRADUATION_YEAR', 'Q74': 'UNIVERSITY_GPA',
                         'Q74_2_TEXT': 'UNIVERSITY_GPA_TEXT', 'Q50': 'RECEIVED_INTERNSHIP_OFFER',
                         'Q8': 'EXTRACURRICULARS', 'Q10': 'MAJOR_PROS', 'Q10_21_TEXT': 'MAJOR_PROS_TEXT',
                         'Q11': 'MAJOR_CONS', 'Q11_14_TEXT': 'MAJOR_CONS_TEXT', 'Q68': 'DESCRIBE_POSITIVE_EXPERIENCE',
                         'Q88': 'CONFIDENCE_PREPARED_COURSES', 'Q93': 'CONFIDENCE_PERCENTILE',
                         'Q86': 'PARTICIPATION_QUESTIONS_COMFORTABLE_NONCS', 'Q84': 'PARTICIPATION_ABSENT_FREQUENCY',
                         'Q16': 'PARTICIPATION_QUESTIONS_ASK_FREQUENCY', 'Q15': 'PARTICIPATION_QUESTIONS_COMFORTABLE',
                         'Q90': 'PARTICIPATION_NOT_QUESTIONS_FREQUENCY', 'Q83': 'PARTICIPATION_ABSENT_WHY',
                         'Q91': 'PARTICIPATION_MORE_COMFORTABLE', 'Q85': 'PARTICIPATION_LESS_COMFORTABLE',
                         'Q92': 'PARTICIPATION_NOT_REASONS', 'Q57': 'PARTICIPATION_QUESTIONS_ASK_IGNORED',
                         'Q46': 'PARTICIPATION_GROUP_PROJECT_ROLE', 'Q18': 'PROFESSORS_ASK_ADVICE',
                         'Q19': 'PROFESSORS_ENCOURAGED_YOU', 'Q21': 'PARTICIPATION_TA_SESSION',
                         'Q22': 'PARTICIPATION_TA_ASK_QUESTIONS', 'Q52': 'PARTICIPATION_TALK_PEERS',
                         'Q20': 'COURSES_PROFESSORS_ENGAGING', 'Q59': 'PROFESSORS_REPRESENT_DIVERSITY',
                         'Q63': 'ROLE_MODELS_SAME_GENDER', 'Q26': 'PARTICIPATION_PEERS_HELP_YOU',
                         'Q25': 'PARTICIPATION_PEERS_YOU_SERVE', 'Q27': 'PARTICIPATION_CLUBS',
                         'Q28': 'PARTICIPATION_FRIENDS_CS_STUDENTS', 'Q82': 'FRIENDS_CS_STUDENTS_WANT_MORE',
                         'Q48': 'SCHOLARSHIP', 'Q9': 'EXTRACURRICULAR_PLANS_BEFORE_GRADUATION',
                         'Q32': 'FREQUENCY_BALANCE_CAREER_PARENTHOOD', 'Q31': 'PROFESSORS_DECLARE_PARENT',
                         'Q30': 'PROFESSORS_DECLARE_FULL_TIME', 'Q41': 'DEPARTMENT_SEXIST_YOU',
                         'Q42': 'DEPARTMENT_SEXIST_OTHERS', 'Q35': 'DEPARTMENT_SUCCESS_BECAUSE_GENDER',
                         'Q62': 'DEPARTMENT_APPEARANCE', 'Q161': 'PEER_SEXISM_IGNORING_SUGGESTION',
                         'Q61': 'DEPARTMENT_APPEARANCE_COMMENTS', 'Q60': 'PEOPLE_SURPRISE_MAJOR',
                         'Q38': 'COMPLAINTS_HOW', 'Q39': 'COMPLAINTS_CONCEQUENCES',
                         'Q40': 'COMPLAINTS_CONCEQUENCES_FEAR', 'Q51': 'PEER_MISTREATED_REACT',
                         'Q160': 'HIGHEST_STANDARD', 'Q58': 'PEOPLE_SEXIST_JOKES_GENDER', 'Q56': 'FRIENDS_OTHER_GENDER',
                         'Q75': 'INTELLIGENCE_FIXED', 'Q76': 'INTELLIGENCE_MALLEABLE', 'Q77': 'FAILURE_LAZY',
                         'Q78': 'FAILURE_ENVIRONMENT', 'Q79': 'FAILURE_ABILITY', 'Q67': 'DESCRIBE_NEGATIVE_EXPERIENCE',
                         'Q54': 'SUGGESTION_IMPROVE_INSTITUTION', 'Q168': 'CONFIDENCE_GRAD_GPA'}

ques_shorthand_to_long = {'CONSENT_CURRENT': 'Please read the entire text above before selecting an answer below.',
                          'CONSENT_FUTURE': 'Are you willing to participate more in this study of students at BYU? - Selected Choice',
                          'EMAIL': 'Are you willing to participate more in this study of students at BYU? - Yes - please enter your email address here - Text',
                          'GENDER': 'What gender do you identify with? - Selected Choice',
                          'GENDER_OTHER': 'What gender do you identify with? - Other - Text',
                          'RACE': 'What is your race/ethnicity (select all that apply)?', 'AGE': 'How old are you?',
                          'UNIVERSITY_PROGRAM': 'What degree are you currently pursuing?',
                          'UNIVERSITY_MAJOR': 'What is your intended major?',
                          'UNIVERSITY_MINOR': 'What is your minor/secondary major?',
                          'UNIVERSITY_COURSES_FALL': 'What CS courses will you enroll in during the fall semester of 2018? (select all that apply)',
                          'UNIVERSITY_GRADUATION_YEAR': 'When do you anticipate graduating?',
                          'UNIVERSITY_GPA': 'What is your current GPA at this university? - Selected Choice',
                          'UNIVERSITY_GPA_TEXT': 'What is your current GPA at this university? - My current overall GPA is: - Text',
                          'RECEIVED_INTERNSHIP_OFFER': 'Have you ever been offered a CS-related internship?',
                          'EXTRACURRICULARS': 'What extracurriculars have you pursued in high school or college? (select all that apply)',
                          'MAJOR_PROS': 'What factors influenced your decision to pick your major? (select all that apply) - Selected Choice',
                          'MAJOR_PROS_TEXT': 'What factors influenced your decision to pick your major? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                          'MAJOR_CONS': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Selected Choice',
                          'MAJOR_CONS_TEXT': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                          'CONFIDENCE_GRADUATE_GPA': 'How much do you agree with the following statement: I am confident in my ability to graduate with a 3.0 or higher major GPA (your major GPA does not include AP/IB credits or general education/GE classes).',
                          'CONFIDENCE_PREPARED_COURSES': 'How much do you agree with the following statement: I am prepared for my CS course(s) next semester.',
                          'CONFIDENCE_PERCENTILE': 'With respect to your peers in your major what percentile would you rank yourself at? Please enter a number between 0 and 100.',
                          'PARTICIPATION_QUESTIONS_COMFORTABLE_NONCS': 'How comfortable are you asking questions in your non-CS courses?',
                          'PARTICIPATION_ABSENT_FREQUENCY': 'How often are you absent from your CS class(es)?',
                          'PARTICIPATION_QUESTIONS_ASK_FREQUENCY': 'On average how often do you ask questions in CS courses?',
                          'PARTICIPATION_QUESTIONS_COMFORTABLE': 'How comfortable are you asking questions in your CS courses?',
                          'PARTICIPATION_NOT_QUESTIONS_FREQUENCY': 'Aside from asking questions, how often do you participate (answer questions/talk in discussions/etc) in CS courses?',
                          'PARTICIPATION_ABSENT_WHY': 'When you miss a CS class, what is most often the reason why? (only select one)',
                          'PARTICIPATION_MORE_COMFORTABLE': 'What helps you feel MORE COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                          'PARTICIPATION_LESS_COMFORTABLE': 'When do you feel LESS COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                          'PARTICIPATION_NOT_REASONS': 'Why do you not participate (aside from asking questions: answering questions/participating in discussions/etc) more in your CS course(s)?',
                          'PARTICIPATION_QUESTIONS_ASK_IGNORED': 'How often do you raise your hand in a CS class but never get called on?',
                          'PARTICIPATION_GROUP_PROJECT_ROLE': 'In group projects for CS courses which tasks do you typically take responsibility for? (select all that apply)',
                          'PROFESSORS_ASK_ADVICE': 'How often do you discuss your academic performance or career plans with a professor or faculty member? (during office hours or in other one-on-one situations)',
                          'PROFESSORS_ENCOURAGED_YOU': 'Has as a CS professor ever invited you, personally, to consider any of the following? (select all that apply)',
                          'PARTICIPATION_TA_SESSION': 'How often do you go to TA-led help sessions for CS courses?',
                          'PARTICIPATION_TA_ASK_QUESTIONS': 'How often to you visit the CS TAs to ask questions?',
                          'PARTICIPATION_TALK_PEERS': 'How often do you talk with other students (not TAs) while in the CS TA cubicals or CS labs?',
                          'COURSES_PROFESSORS_ENGAGING': 'How strongly do you agree with the statement: CS professors and CS courses are engaging.',
                          'PROFESSORS_REPRESENT_DIVERSITY': 'How strongly do you agree with the statement: I feel that the CS professors adequately represent the diverse backgrounds, views, demographics, and perspectives of students in CS courses.',
                          'ROLE_MODELS_SAME_GENDER': 'Do you feel like you have role models of the same gender as you who do CS?',
                          'PARTICIPATION_PEERS_HELP_YOU': 'How often have you asked another student (not a TA for the course) to help you understand CS course material?',
                          'PARTICIPATION_PEERS_YOU_SERVE': 'How often have you mentored any students in the CS major or CS courses this semester? (assisted them with labs, homework, or given internship/job or graduate school advice)',
                          'PARTICIPATION_CLUBS': 'Do you attend meetings/events for any of the following? (select all that apply)',
                          'PARTICIPATION_FRIENDS_CS_STUDENTS': 'What percentage of your friends are taking classes in the CS department?',
                          'FRIENDS_CS_STUDENTS_WANT_MORE': 'How much do you agree with the following statement: I want to make more friends in the CS major.',
                          'SCHOLARSHIP': 'Have you been the recipient of an academic scholarship? (select all that apply)',
                          'EXTRACURRICULAR_PLANS_BEFORE_GRADUATION': 'Which of the following have you done, or do you plan to do before you graduate? (select all that apply)',
                          'FREQUENCY_BALANCE_CAREER_PARENTHOOD': 'How often do members of the CS department (students, TAs, professors, etc) ask you about your plans to balance a career and parenthood?',
                          'PROFESSORS_DECLARE_PARENT': 'How often do members of the CS department (students, TAs, professors, etc) tell you that you should be a stay-at-home parent?',
                          'PROFESSORS_DECLARE_FULL_TIME': 'How often do members of the CS department (students, TAs, professors, etc) tell you that you should pursue a full-time career?',
                          'DEPARTMENT_SEXIST_YOU': 'Do you feel like a member of the CS department (students, TAs, professors, etc) has treated you differently than your peers of the opposite gender?',
                          'DEPARTMENT_SEXIST_OTHERS': 'Are you aware of CS classmates who believe they have been treated differently by members of the CS department (students, TAs, professors, etc) because of their gender?',
                          'DEPARTMENT_SUCCESS_BECAUSE_GENDER': 'Has a member of the CS department (students, TAs, professors, etc)ever told you that you earned a good grade, got a job, internship, or scholarship offer because of your gender?',
                          'DEPARTMENT_APPEARANCE': 'How often do you get negative comments about your appearance or attire from members of the CS department (students, TAs, professors, etc)?',
                          'DEPARTMENT_APPEARANCE_COMMENTS': 'If members of the CS department (students, TAs, professors, etc) make negative comments about your appearance, what do they comment about? (select all that apply)',
                          'COMPLAINTS_HOW': 'Do you know how to file complaints for being treated differently because of your gender in the CS department?',
                          'COMPLAINTS_CONCEQUENCES': 'Do you know what happens if a complaint is filed against a member of the CS department who is accused of being sexist?',
                          'COMPLAINTS_CONCEQUENCES_FEAR': 'Would you personally be worried about retribution if you filed a complaint about someone treating you or a peer differently because of your/their gender?',
                          'PEER_MISTREATED_REACT': 'If you saw a peer treat someone differently because of their gender (through words, actions, etc), would you say or do something? (select all that apply)',
                          'PEOPLE_SURPRISE_MAJOR': 'How much do you agree with the following statement:When you tell people what your major is, they often express surprise (You don\'t look/act like a ____ major", Why are you majoring in ____?)?',
                          'PEOPLE_SEXIST_JOKES_GENDER': 'How often do you hear people in the CS department make sexist remarks or jokes about your gender?',
                          'HIGHEST_STANDARD': 'Do you feel that some students are held to a higher standard than other students in the CS department? If so, please select all groups that apply.',
                          'PEER_SEXISM_IGNORING_SUGGESTION': 'How often, within the CS department, do you make a suggestion that was not considered until another person makes the same suggestion?',
                          'FRIENDS_OTHER_GENDER': 'Do you feel like you can have non-romantic friends of the opposite gender?',
                          'INTELLIGENCE_FIXED': 'How strongly do you agree with the statement: Intelligence is a fixed trait; you are born with the talents that you have and nothing you do can change them.',
                          'INTELLIGENCE_MALLEABLE': 'How strongly do you agree with the statement: Intelligence is a malleable quality, if you work hard and practice you will improve.',
                          'FAILURE_LAZY': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to insufficient effort.',
                          'FAILURE_ENVIRONMENT': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to personal or environmental obstacles.',
                          'FAILURE_ABILITY': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to a lack of ability.',
                          'DESCRIBE_POSITIVE_EXPERIENCE': 'Are there any positive experiences or interactions that you had with members of the CS department that you would like to share?',
                          'DESCRIBE_NEGATIVE_EXPERIENCE': 'Are there any negative experiences or interactions that you had with members of the CS department that you would like to share?',
                          'SUGGESTION_IMPROVE_INSTITUTION': "What one change would you most like to see implemented to improve students' experiences at this institution?"}

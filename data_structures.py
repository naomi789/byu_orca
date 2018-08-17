
ques_ans = {'duration_seconds': 'int', 'Location_Latitude': 'double', 'LocationLongitude': 'double',
            'consent_current': 'string', 'consent_future': 'string', 'email': 'string', 'gender': 'string',
            'gender_other': 'string', 'race': 'race', 'age': 'int', 'university_program': 'string',
            'university_major': 'string', 'university_minor': 'string', 'university_courses_fall': 'courses',
            'university_graduation_year': 'string', 'university_gpa': 'string', 'university_gpa_TEXT': 'double',
            'received_internship_offer': 'yes_no', 'extracurriculars': 'extracurriculars',
            'major_pros': 'encouragement',
            'major_pros_TEXT': 'string', 'major_cons': 'barriers', 'major_cons_TEXT': 'string',
            'confidence_graduate_gpa': 'agreement', 'confidence_prepared_courses': 'agreement',
            'confidence_percentile': 'double', 'participation_questions_comfortable_NONCS': 'comfort',
            'participation_absent_frequency': 'frequency_absent',
            'participation_questions_ask_frequency': 'frequency_class_typo',
            'participation_questions_comfortable': 'comfort',
            'participation_not_questions_frequency': 'frequency_class', 'participation_absent_why': 'miss_class',
            'participation_MORE_comfortable': 'increase_comfort', 'participation_LESS_comfortable': 'decrease_comfort',
            'participation_not_reasons': 'participate_decrease',
            'participation_questions_ask_ignored': 'frequency_class',  # _typo
            'participation_group_project_role': 'responsibilities', 'professors_ask_advice': 'frequency',  # _typo
            'professors_encouraged_you': 'professor_encouragement', 'participation_TA_session': 'frequency_TA',  # _typo
            'participation_TA_ask_questions': 'frequency_typo', 'participation_talk_peers': 'frequency',
            'courses_professors_engaging': 'agreement', 'professors_represent_diversity': 'agreement',
            'role_models_same_gender': 'agreement', 'participation_peers_help_you': 'frequency_typo',
            'participation_peers_you_serve': 'frequency_typo', 'participation_clubs': 'meetings_clubs',
            'participation_friends_CS_students': 'percentage', 'friends_CS_students_want_more': 'agreement',
            'scholarship': 'scholarships', 'extracurricular_plans_before_graduation': 'involvement',
            'frequency_balance_career_parenthood': 'frequency', 'professors_declare_parent': 'frequency',  # _typo
            'professors_declare_full_time': 'frequency',  # _typo
            'department_sexist_you': 'certainty',
            'department_sexist_others': 'certainty', 'department_success_because_gender': 'certainty',
            'department_appearance': 'frequency',  # _typo
            'department_appearance_comments': 'appearance_comments',
            'complaints_how': 'certainty', 'complaints_concequences': 'certainty',
            'complaints_concequences_fear': 'certainty', 'peer_mistreated_react': 'sexism_response',
            'people_surprise_major': 'agreement', 'people_sexist_jokes_gender': 'frequency',  # _typo
            'highest_standard': 'student_groups_standards', 'peer_sexism_ignoring_suggestion': 'frequency',  # _typo
            'friends_other_gender': 'agreement', 'intelligence_fixed': 'agreement',
            'intelligence_malleable': 'agreement',
            'failure_lazy': 'agreement', 'failure_environment': 'agreement', 'failure_ability': 'agreement',
            'describe_positive_experience': 'string', 'describe_negative_experience': 'string',
            'suggestion_improve_institution': 'string'}

ques_num_to_long = {'Q70': 'Please read the entire text above before selecting an answer below.',
                    'Q89': 'Are you willing to participate more in this study of students at BYU? - Selected Choice',
                    'Q89_1_TEXT': 'Are you willing to participate more in this study of students at BYU? - Yes - please enter your email address here - Text',
                    'Q3': 'What gender do you identify with? - Selected Choice',
                    'Q3_3_TEXT': 'What gender do you identify with? - Other - Text',
                    'Q81': 'What is your race/ethnicity (select all that apply)?', 'Q80': 'How old are you?',
                    'Q4': 'What degree are you currently pursuing?', 'Q5': 'What is your intended major?',
                    'Q6': 'What is your minor/secondary major?',
                    'Q7': 'What CS courses will you enroll in during the fall semester of 2018? (select all that apply)',
                    'Q73': 'When do you anticipate graduating?',
                    'Q74': 'What is your current GPA at this university? - Selected Choice',
                    'Q74_2_TEXT': 'What is your current GPA at this university? - My current overall GPA is: - Text',
                    'Q50': 'Have you ever been offered a CS-related internship?',
                    'Q8': 'What extracurriculars have you pursued in high school or college? (select all that apply)',
                    'Q10': 'What factors influenced your decision to pick your major? (select all that apply) - Selected Choice',
                    'Q10_21_TEXT': 'What factors influenced your decision to pick your major? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                    'Q11': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Selected Choice',
                    'Q11_14_TEXT': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                    'Q68': 'How much do you agree with the following statement: I am confident in my ability to graduate with a 3.0 or higher major GPA (your major GPA does not include AP/IB credits or general education/GE classes).',
                    'Q88': 'How much do you agree with the following statement: I am prepared for my CS course(s) next semester.',
                    'Q93': 'With respect to your peers in your major what percentile would you rank yourself at? Please enter a number between 0 and 100.',
                    'Q86': 'How comfortable are you asking questions in your non-CS courses?',
                    'Q84': 'How often are you absent from your CS class(es)?',
                    'Q16': 'On average how often do you ask questions in CS courses?',
                    'Q15': 'How comfortable are you asking questions in your CS courses?',
                    'Q90': 'Aside from asking questions, how often do you participate (answer questions/talk in discussions/etc) in CS courses?',
                    'Q83': 'When you miss a CS class, what is most often the reason why? (only select one)',
                    'Q91': 'What helps you feel MORE COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                    'Q85': 'When do you feel LESS COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                    'Q92': 'Why do you not participate (aside from asking questions: answering questions/participating in discussions/etc) more in your CS course(s)?',
                    'Q57': 'How often do you raise your hand in a CS class but never get called on?',
                    'Q46': 'In group projects for CS courses which tasks do you typically take responsibility for? (select all that apply)',
                    'Q18': 'How often do you discuss your academic performance or career plans with a professor or faculty member? (during office hours or in other one-on-one situations)',
                    'Q19': 'Has as a CS professor ever invited you, personally, to consider any of the following? (select all that apply)',
                    'Q21': 'How often do you go to TA-led help sessions for CS courses?',
                    'Q22': 'How often to you visit the CS TAs to ask questions?',
                    'Q52': 'How often do you talk with other students (not TAs) while in the CS TA cubicals or CS labs?',
                    'Q20': 'How strongly do you agree with the statement: CS professors and CS courses are engaging.',
                    'Q59': 'How strongly do you agree with the statement: I feel that the CS professors adequately represent the diverse backgrounds, views, demographics, and perspectives of students in CS courses.',
                    'Q63': 'Do you feel like you have role models of the same gender as you who do CS?',
                    'Q26': 'How often have you asked another student (not a TA for the course) to help you understand CS course material?',
                    'Q25': 'How often have you mentored any students in the CS major or CS courses this semester? (assisted them with labs, homework, or given internship/job or graduate school advice)',
                    'Q27': 'Do you attend meetings/events for any of the following? (select all that apply)',
                    'Q28': 'What percentage of your friends are taking classes in the CS department?',
                    'Q82': 'How much do you agree with the following statement: I want to make more friends in the CS major.',
                    'Q48': 'Have you been the recipient of an academic scholarship? (select all that apply)',
                    'Q9': 'Which of the following have you done, or do you plan to do before you graduate? (select all that apply)',
                    'Q32': 'How often do members of the CS department (students, TAs, professors, etc) ask you about your plans to balance a career and parenthood?',
                    'Q31': 'How often do members of the CS department (students, TAs, professors, etc) tell you that you should be a stay-at-home parent?',
                    'Q30': 'How often do members of the CS department (students, TAs, professors, etc) tell you that you should pursue a full-time career?',
                    'Q41': 'Do you feel like a member of the CS department (students, TAs, professors, etc) has treated you differently than your peers of the opposite gender?',
                    'Q42': 'Are you aware of CS classmates who believe they have been treated differently by members of the CS department (students, TAs, professors, etc) because of their gender?',
                    'Q35': 'Has a member of the CS department (students, TAs, professors, etc)ever told you that you earned a good grade, got a job, internship, or scholarship offer because of your gender?',
                    'Q62': 'How often do you get negative comments about your appearance or attire from members of the CS department (students, TAs, professors, etc)?',
                    'Q61': 'If members of the CS department (students, TAs, professors, etc) make negative comments about your appearance, what do they comment about? (select all that apply)',
                    'Q38': 'Do you know how to file complaints for being treated differently because of your gender in the CS department?',
                    'Q39': 'Do you know what happens if a complaint is filed against a member of the CS department who is accused of being sexist?',
                    'Q40': 'Would you personally be worried about retribution if you filed a complaint about someone treating you or a peer differently because of your/their gender?',
                    'Q51': 'If you saw a peer treat someone differently because of their gender (through words, actions, etc), would you say or do something? (select all that apply)',
                    'Q60': 'How much do you agree with the following statement:When you tell people what your major is, they often express surprise (You don\'t look/act like a ____ major", Why are you majoring in ____?)?',
                    'Q58': 'How often do you hear people in the CS department make sexist remarks or jokes about your gender?',
                    'Q160': 'Do you feel that some students are held to a higher standard than other students in the CS department? If so, please select all groups that apply.',
                    'Q161': 'How often, within the CS department, do you make a suggestion that was not considered until another person makes the same suggestion?',
                    'Q56': 'Do you feel like you can have non-romantic friends of the opposite gender?',
                    'Q75': 'How strongly do you agree with the statement: Intelligence is a fixed trait; you are born with the talents that you have and nothing you do can change them.',
                    'Q76': 'How strongly do you agree with the statement: Intelligence is a malleable quality, if you work hard and practice you will improve.',
                    'Q77': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to insufficient effort.',
                    'Q78': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to personal or environmental obstacles.',
                    'Q79': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to a lack of ability.',
                    'Q168': 'Are there any positive experiences or interactions that you had with members of the CS department that you would like to share?',
                    'Q67': 'Are there any negative experiences or interactions that you had with members of the CS department that you would like to share?',
                    'Q54': "What one change would you most like to see implemented to improve students' experiences at this institution?"}

short_to_long = {'duration_seconds': 'How long between opening and submitting survey?', 'Location_Latitude': 'latitude',
                 'LocationLongitude': 'longitude',
                 'consent_current': 'Please read the entire text above before selecting an answer below.',
                 'consent_future': 'Are you willing to participate more in this study of students at BYU? - Selected Choice',
                 'email': 'Are you willing to participate more in this study of students at BYU? - Yes - please enter your email address here - Text',
                 'gender': 'What gender do you identify with? - Selected Choice',
                 'gender_other': 'What gender do you identify with? - Other - Text',
                 'race': 'What is your race/ethnicity (select all that apply)?', 'age': 'How old are you?',
                 'university_program': 'What degree are you currently pursuing?',
                 'university_major': 'What is your intended major?',
                 'university_minor': 'What is your minor/secondary major?',
                 'university_courses_fall': 'What CS courses will you enroll in during the fall semester of 2018? (select all that apply)',
                 'university_graduation_year': 'When do you anticipate graduating?',
                 'university_gpa': 'What is your current GPA at this university? - Selected Choice',
                 'university_gpa_TEXT': 'What is your current GPA at this university? - My current overall GPA is: - Text',
                 'received_internship_offer': 'Have you ever been offered a CS-related internship?',
                 'extracurriculars': 'What extracurriculars have you pursued in high school or college? (select all that apply)',
                 'major_pros': 'What factors influenced your decision to pick your major? (select all that apply) - Selected Choice',
                 'major_pros_TEXT': 'What factors influenced your decision to pick your major? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                 'major_cons': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Selected Choice',
                 'major_cons_TEXT': 'What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Specific BYU courses or labs (list courses here please) - Text',
                 'confidence_graduate_gpa': 'How much do you agree with the following statement: I am confident in my ability to graduate with a 3.0 or higher major GPA (your major GPA does not include AP/IB credits or general education/GE classes).',
                 'confidence_prepared_courses': 'How much do you agree with the following statement: I am prepared for my CS course(s) next semester.',
                 'confidence_percentile': 'With respect to your peers in your major, what percentile would you rank yourself at? Please enter a number between 0 and 100.',
                 'participation_questions_comfortable_NONCS': 'How comfortable are you asking questions in your non-CS courses?',
                 'participation_absent_frequency': 'How often are you absent from your CS class(es)?',
                 'participation_questions_ask_frequency': 'On average how often do you ask questions in CS courses?',
                 'participation_questions_comfortable': 'How comfortable are you asking questions in your CS courses?',
                 'participation_not_questions_frequency': 'Aside from asking questions how often do you participate (answer questions/talk in discussions/etc) in CS courses?',
                 'participation_absent_why': 'When you miss a CS class what is most often the reason why? (only select one)',
                 'participation_MORE_comfortable': 'What helps you feel MORE COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                 'participation_LESS_comfortable': 'When do you feel LESS COMFORTABLE asking questions in your CS course(s)? (select all that apply)',
                 'participation_not_reasons': 'Why do you not participate (aside from asking questions: answering questions/participating in discussions/etc) more in your CS course(s)?',
                 'participation_questions_ask_ignored': 'How often do you raise your hand in a CS class but never get called on?',
                 'participation_group_project_role': 'In group projects for CS courses which tasks do you typically take responsibility for? (select all that apply)',
                 'professors_ask_advice': 'How often do you discuss your academic performance or career plans with a professor or faculty member? (during office hours or in other one-on-one situations)',
                 'professors_encouraged_you': 'Has as a CS professor ever invited you  personally to consider any of the following? (select all that apply)',
                 'participation_TA_session': 'How often do you go to TA-led help sessions for CS courses?',
                 'participation_TA_ask_questions': 'How often to you visit the CS TAs to ask questions?',
                 'participation_talk_peers': 'How often do you talk with other students (not TAs) while in the CS TA cubicals or CS labs?',
                 'courses_professors_engaging': 'How strongly do you agree with the statement: CS professors and CS courses are engaging.',
                 'professors_represent_diversity': 'How strongly do you agree with the statement: I feel that the CS professors adequately represent the diverse backgrounds/views/demographics/perspectives of students in CS courses.',
                 'role_models_same_gender': 'Do you feel like you have role models of the same gender as you who do CS?',
                 'participation_peers_help_you': 'How often have you asked another student (not a TA for the course) to help you understand CS course material?',
                 'participation_peers_you_serve': 'How often have you mentored any students in the CS major or CS courses this semester? (assisted them with labs/homework/or given internship/job or graduate school advice)',
                 'participation_clubs': 'Do you attend meetings/events for any of the following? (select all that apply)',
                 'participation_friends_CS_students': 'What percentage of your friends are taking classes in the CS department?',
                 'friends_CS_students_want_more': 'How much do you agree with the following statement: I want to make more friends in the CS major.',
                 'scholarship': 'Have you been the recipient of an academic scholarship? (select all that apply)',
                 'extracurricular_plans_before_graduation': 'Which of the following have you done or do you plan to do before you graduate? (select all that apply)',
                 'frequency_balance_career_parenthood': 'How often do members of the CS department (students/TAs/professors/etc) ask you about your plans to balance a career and parenthood?',
                 'professors_declare_parent': 'How often do members of the CS department (students/TAs/professors/etc) tell you that you should be a stay-at-home parent?',
                 'professors_declare_full_time': 'How often do members of the CS department (students/TAs/professors/etc) tell you that you should pursue a full-time career?',
                 'department_sexist_you': 'Do you feel like a member of the CS department (students/TAs/professors/etc) has treated you differently than your peers of the opposite gender?',
                 'department_sexist_others': 'Are you aware of CS classmates who believe they have been treated differently by members of the CS department (students/TAs/professors/etc) because of their gender?',
                 'department_success_because_gender': 'Has a member of the CS department (students/TAs/professors/etc)you ever been told that you earned a good grade/got a job/internship/or scholarship offer because of your gender?',
                 'department_appearance': 'How often do you get negative comments about your appearance or attire from members of the CS department (students/TAs/professors/etc)?',
                 'department_appearance_comments': 'If members of the CS department (students/TAs/professors/etc) make negative comments about your appearance what do they comment about? (select all that apply)',
                 'complaints_how': 'Do you know how to file complaints for being treated differently because of your gender in the CS department?',
                 'complaints_concequences': 'Do you know what happens if a complaint is filed against a member of the CS department who is accused of being sexist?',
                 'complaints_concequences_fear': 'Would you personally be worried about retribution if you filed a complaint about someone treating you or a peer differently because of your/their gender?',
                 'peer_mistreated_react': 'If you saw a peer treat someone differently because of their gender (through words/actions/etc) would you say or do something? (select all that apply)',
                 'people_surprise_major': 'When you tell people what your major is how often do they express surprise (You dont look/act like a ____ major/Why are you majoring in ____?)?',
                 'people_sexist_jokes_gender': 'How often do you hear people in the CS department make sexist remarks or jokes about your gender?',
                 'highest_standard': 'Do you feel that some students are held to a higher standard than other students in the CS department? If so please select all groups that apply.',
                 'peer_sexism_ignoring_suggestion': 'How often within the CS department do you make a suggestion that was not considered until another person makes the same suggestion?',
                 'friends_other_gender': 'Do you feel like you can have non-romantic friends of the opposite gender?',
                 'intelligence_fixed': 'How strongly do you agree with the statement: Intelligence is a fixed trait; you are born with the talents that you have and nothing you do can change them.',
                 'intelligence_malleable': 'How strongly do you agree with the statement: Intelligence is a malleable quality if you work hard and practice you will improve.',
                 'failure_lazy': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to insufficient effort.',
                 'failure_environment': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to personal or environmental obstacles.',
                 'failure_ability': 'How strongly do you agree with the statement: Failure or a lack of achievement is due to a lack of ability.',
                 'describe_positive_experience': 'Are there any positive experiences or interactions that you had with members of the CS department that you would like to share?',
                 'describe_negative_experience': 'Are there any negative experiences or interactions that you had with members of the CS department that you would like to share?',
                 'suggestion_improve_institution': "What one change would you most like to see implemented to improve students' experiences at this institution?"}

majors_minors = ['Computer Science', 'Computer Engineering', 'Information Systems', 'Information Technology',
                 'Electrical Engineering', 'Civil Engineering', 'Mechanical Engineering', 'Statistics', 'Mathematics',
                 'ACME', 'Undeclared', 'Undeclared/none', 'Other']

graduation_year = ['2018', '2019', '2020', '2021 or later']

extracurriculars = ['JV/varsity or other sports', 'Thespian/acting clubs', 'Orchestra/band/choir/music',
                    'Robotics/computer or other STEM clubs', 'Speech/debate',
                    'Student government or political groups and clubs', 'Other', 'None']

encouragement = ['Mother\'s encouragement', 'Father\'s encouragement', "Other family member's encouragement",
                 'Teacher\'s encouragement', 'Contact with or mentoring from a graduate',
                 'Lure of a high income', 'Scholarship/financial aid offered for the major',
                 'Desire to have a job that others respect', 'Desire to do something to contribute to society',
                 'Desire to meet people with similar interests',
                 'Career will give opportunity to combine work and family needs',
                 'Appeal of doing something to contribute to science', 'Job openings available',
                 'Job security and permanence',
                 'Advancement opportunities', 'Career possibilities fit interests',
                 'Career possibilities will give freedom to make own decisions', 'Teaching quality',
                 'Mentoring or friendship from students', 'Participation in conference or event',
                 'Specific BYU courses or labs (list courses here please)', 'None of the above']

barriers = ['There are no barriers', 'Coursework too difficult', 'The coursework is too removed from real problems',
            'Feeling as if I don\'t fit in', 'Need to balance parenting and career after having children',
            'Need to balance relationships and career after marriage', 'No mentor',
            'Not certain of steps needed to succeed', 'Not clear on my goals for the future',
            'Not enough confidence in my ability to succeed', 'Not enough financial support to finish college',
            'Not enough time to take other courses', 'Parents are encouraging other paths',
            'Sacrifice too much free time', 'Specific BYU courses or labs (list courses here please)', 'Other barriers',
            '']

responsibilities = [
    'Writing or creating materials (designed user interface/created poster or visual aid/wrote reports or essays/etc)',
    'Managerial (group leader/presentation/etc)',
    'Support tasks (schedule meetings/email professor/scribe or notetaker/other errands)',
    'Technical (coding/math/etc)']

professor_encouragement = ['Join the computer science major', 'Continue in the CS major', 'Apply for a scholarship',
                           'Apply for internship', 'Apply for part-time/full-time job',
                           'Apply for a research position (either on or off campus)', 'Grad school',
                           'Leadership position']
meetings_clubs = ['ACM (Association of Computing Machinery)',
                  'CS Colloquiums',
                  'YHacks (ethical hacking)',
                  'Linux Club (Linux operating system club)',
                  'WiCS (Women in Computer Science)',
                  'WIT (Women in Technology)',
                  'Visiting companies\' tech talks',
                  'Dev Club (Developer\'s club)',
                  'Visiting companies\' tech talks']

percentage = ['0 - 20%', '21 - 40%', '41 - 60%', '61 - 80%', '81 - 100%']

scholarships = ['Minority based (race/gender/etc)',
                'Academic path based (specific to your major/department/field/etc)',
                'Need based (financial aid/FAFSA/pell grant/etc)', 'Other qualifications',
                'I have never received a scholarship']

yes_no = ['Yes', 'No']

involvement = ['Internship', 'Study abroad', 'Research', 'Capstone project', 'Leadership role in club or at work']

appearance_comments = ['Too formal', 'Too casual', 'Workplace appropriateness/modesty',
                       'Facial hair or hair color/length/style', 'Body type or weight',
                       'I never receive negative comments']

sexism_response = ['I would say something during the event', 'I would speak to the victim after the event',
                   'I would speak to the perpetrator after the event', 'I would probably not say anything',
                   'I would report this to the department if this happened at school',
                   'I would report this to my boss if this happened at work',
                   'I would report this to a professor if this happened at school',
                   '']

student_groups_standards = ['Male students', 'Female students', 'Non-binary students',
                            'All students are held to an equal standard']

race = ['White', 'Hispanic or Latino', 'Asian/Pacific Islander', 'Black or African American',
        'Native American or American Indian', 'Other', 'Prefer not to say']

degree_pursuing = ['Undergraduate', 'Masters', 'PhD', 'Not currently pursuing a degree']

age = ['18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31-39', '40-49', '50-59',
       '60 or older', 'Prefer not to say']

byu_courses = ['CS 142', 'CS 224', 'CS 235', 'CS 236', 'CS 240', 'CS 252', 'CS 260', 'CS 312', 'CS 324', 'CS 340',
               'CS 404', 'Other 300 or 400 level courses', 'Other 500 or 600 level courses',
               'I will not take any CS courses Fall 2018']

frequency_absent = ['I never miss class', 'I miss class once or twice a semester', 'I miss once or twice a month',
                    'I miss once a week', 'I go sometimes', 'I never go to class']

miss_class_reasons = ['Physical or mental health issues (flu/cold/depression/anxiety/etc)', 'Work commitments',
                      'Family commitments', 'Other commitments (club events/religious activities/etc)',
                      'To study or do homework for that CS class', 'To study or do homework for other courses',
                      'Class is too hard/confusing', 'Class is too easy/boring',
                      'On accident (I overslept, lost track of time, was running late, etc)',
                      'Time of day/day of week (I hate Monday 8am classes, etc)',
                      'I don\'t like the subject of the class',
                      'I don\'t like the professor/the way they teach/the environment or culture of the class']

likert_question_answer_types = ['certainty', 'agreement', 'frequency', 'frequency_typo', 'frequency_absent',
                                'not_participate_reasons',
                                'frequency_TA', 'frequency_TA_typo', 'frequency_class', 'frequency_class_typo',
                                'comfort', 'miss_class_reasons']

more_comfortable = ['Feeling like I am on a similar academic level to my peers', 'Feeling like I won’t be judged',
                    'Knowing my peers in the class', 'Not knowing my peers in the class/feeling anonymous',
                    'Peers asking more questions', 'Having a good grade in the class',
                    'Feeling like the professor wants students to ask questions', 'Knowing the professor',
                    'Larger class size/more students', 'Smaller class size/fewer students']

not_participate_reasons = ['I already participate enough/too much', 'The CS class is too large/has too many students',
                           'The CS class is too small/has too few students', 'I don’t know my peers in the class',
                           'I do know my peers in the class', 'I don’t have questions to ask',
                           'I am not prepared for class/don’t have anything to add', 'I am not called on',
                           'I am worried my answer is wrong/comment is irrelevant/etc']

less_comfortable = ['I DO feel comfortable asking questions in my CS course(s)', 'Larger class size/more students',
                    'Smaller class size/fewer students', 'Knowing my peers in the class',
                    'Not knowing my peers in the class/feeling anonymous',
                    'I’m worried the professor won’t answer my question (at all/clearly/succinctly/correctly/etc)',
                    'I don’t think the professor wants me to ask questions', 'I’m worried it’s a dumb question',
                    'I’m worried someone else already asked the question', 'I think I ask too many questions',
                    'If other students don’t ask questions', 'I feel like I can figure out the answer own my own',
                    'I don\'t want to take time out of class']

list_question_answer_types = ['responsibilities', 'professor_encouragement', 'meetings_clubs', 'percentage',
                              'scholarships', 'yes_no', 'involvement', 'appearance_comments', 'sexism_response',
                              'student_groups_standards', 'majors_minors', 'graduation_year', 'extracurriculars',
                              'encouragement', 'barriers', 'more_comfortable', 'less_comfortable', 'increase_comfort',
                              'decrease_comfort', 'miss_class', 'participate_decrease']
# from above, TODO, not sure if 'miss_class', 'participate_decrease' should really be in list...

professor_names = ['brent adams', 'cory barker', 'mark clement', 'jacob crandall', 'casey deccio', 'parris egbert',
                   'ryan farrell', 'kelly flanagan', 'christophe giraud-carrier', 'michael goodrich', 'seth holladay',
                   'frank jones', 'michael jones', 'mike jones', 'tony martinez', 'eric mercer', 'bryan morse',
                   'dennis ng', 'ken rodham', 'paul roper', 'kent seamons', 'kevin seppi', 'quinn snell', 'dan ventura',
                   'sean warnick', 'david wingate', 'scott woodfield', 'daniel zappala']

staff_names = ['gordon billings', 'jennifer bonnett', 'lynette nelson', 'erin rowan', 'greg corlett', 'klark walker',
               'angela jones', 'other angela']

confidence_measurement = ['confidence_prepared_courses', 'confidence_graduate_gpa']

long_feedback = ['describe_positive_experience', 'describe_negative_experience', 'suggestion_improve_institution']

question_shorthand = ['duration_seconds', 'Location_Latitude', 'LocationLongitude', 'university', 'current_internship',
                      'gender', 'gender_other', 'university_program', 'university_gpa', 'university_gpa_TEXT',
                      'university_major', 'university_minor', 'university_graduation_year', 'extracurriculars',
                      'major_pros', 'major_pros_TEXT', 'major_cons', 'major_cons_TEXT', 'confidence_graduate_gpa',
                      'participation_questions_comfortable', 'participation_questions_ask_frequency',
                      'participation_questions_ask_ignored', 'participation_group_project_role',
                      'professors_ask_advice',
                      'professors_encouraged_you', 'participation_TA_session', 'participation_TA_ask_questions',
                      'participation_talk_peers', 'courses_professors_engaging', 'professors_represent_diversity',
                      'role_models_same_gender', 'participation_peers_help_you', 'participation_peers_you_serve',
                      'participation_clubs', 'participation_friends_CS_students', 'scholarship',
                      'received_internship_offer', 'extracurricular_plans_before_graduation',
                      'frequency_balance_career_parenthood', 'professors_declare_parent',
                      'professors_declare_full_time',
                      'department_sexist_you', 'department_sexist_others', 'department_success_because_gender',
                      'department_appearance', 'department_appearance_comments', 'complaints_how',
                      'complaints_concequences', 'complaints_concequences_fear', 'peer_mistreated_react',
                      'people_surprise_major', 'people_sexist_jokes_gender', 'highest_standard',
                      'peer_sexism_ignoring_suggestion', 'friends_other_gender', 'intelligence_fixed',
                      'intelligence_malleable', 'failure_lazy', 'failure_environment', 'failure_ability',
                      'describe_positive_experience', 'describe_negative_experience', 'suggestion_improve_institution']

BYU_question_shorthand = ['duration_seconds', 'Location_Latitude', 'LocationLongitude', 'consent_current',
                          'consent_future', 'email', 'gender', 'gender_other', 'race', 'age', 'university_program',
                          'university_major', 'university_minor', 'university_courses_fall',
                          'university_graduation_year', 'university_gpa', 'university_gpa_TEXT',
                          'received_internship_offer', 'extracurriculars', 'major_pros', 'major_pros_TEXT',
                          'major_cons', 'major_cons_TEXT', 'confidence_graduate_gpa', 'confidence_prepared_courses',
                          'confidence_percentile',
                          'participation_questions_comfortable_NONCS', 'participation_absent_frequency',
                          'participation_questions_ask_frequency', 'participation_questions_comfortable',
                          'participation_not_questions_frequency', 'participation_absent_why',
                          'participation_MORE_comfortable', 'participation_LESS_comfortable',
                          'participation_not_reasons', 'participation_questions_ask_ignored',
                          'participation_group_project_role', 'professors_ask_advice', 'professors_encouraged_you',
                          'participation_TA_session', 'participation_TA_ask_questions', 'participation_talk_peers',
                          'courses_professors_engaging', 'professors_represent_diversity', 'role_models_same_gender',
                          'participation_peers_help_you', 'participation_peers_you_serve', 'participation_clubs',
                          'participation_friends_CS_students', 'friends_CS_students_want_more', 'scholarship',
                          'extracurricular_plans_before_graduation', 'frequency_balance_career_parenthood',
                          'professors_declare_parent', 'professors_declare_full_time', 'department_sexist_you',
                          'department_sexist_others', 'department_success_because_gender', 'department_appearance',
                          'department_appearance_comments', 'complaints_how', 'complaints_concequences',
                          'complaints_concequences_fear', 'peer_mistreated_react', 'people_surprise_major',
                          'people_sexist_jokes_gender', 'highest_standard', 'peer_sexism_ignoring_suggestion',
                          'friends_other_gender', 'intelligence_fixed', 'intelligence_malleable', 'failure_lazy',
                          'failure_environment', 'failure_ability', 'describe_positive_experience',
                          'describe_negative_experience', 'suggestion_improve_institution']

answer_type = ["int", "double", "double", "string", "string", "string", "string", "string", "string", "double",
               "string", "string", "string", "extracurriculars", "encouragement", "string", "barriers", "string",
               "agreement", "comfort",
               "frequency_class", "frequency_class", "responsibilities", "frequency", "professor_encouragement",
               "frequency_TA", "frequency", "frequency",
               "agreement", "agreement", "agreement", "frequency", "frequency", "meetings_clubs", "percentage",
               "scholarships", "yes_no",
               "involvement", "frequency", "frequency", "frequency", "certainty", "certainty", "certainty", "frequency",
               "appearance_comments", "certainty", "certainty", "certainty", "sexism_response", "agreement",
               "frequency", "student_groups_standards", "frequency",
               "agreement", "agreement", "agreement", "agreement", "agreement", "agreement", "string", "string",
               "string"]

question_string = ["duration_seconds", "Location_Latitude", "LocationLongitude", "What university are you attending?",
                   "What company are you interning with this summer?",
                   "What gender do you identify with? - Selected Choice",
                   "What gender do you identify with? - Other - Text",
                   "What degree are you currently pursuing?",
                   "What is your current GPA at this university? - Selected Choice",
                   "What is your current GPA at this university? - My current overall GPA is: - Text",
                   "What is your intended major?", "What is your minor/secondary major?",
                   "When do you anticipate graduating?",
                   "What extracurriculars have you pursued in high school or college? (select all that apply)",
                   "What factors influenced your decision to pick your major? (select all that apply) - Selected Choice",
                   "What factors influenced your decision to pick your major? (select all that apply) - Specific BYU courses or labs (if so which ones) - Text",
                   "What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Selected Choice",
                   "What do you perceive as being a barrier to your completion of this major and your career in this field? (select all that apply) - Specific BYU courses or labs (if so which ones) - Text",
                   "How much do you agree with the following statement: I am confident in my ability to graduate with a 3.0 or higher major GPA (your major GPA does not include AP credits or general education/GE classes).",
                   "How comfortable are you asking questions in your CS courses?",
                   "On average how often do you ask questions in CS courses?",
                   "How often do you raise your hand in class but never get called on?",
                   "In group projects for CS courses which tasks do you typically take responsibility for? (select all that apply)",
                   "How often do you discuss your academic performance or career plans with a professor or faculty member? (during office hours or in other one-on-one situations)",
                   "Has as a CS professor ever invited you personally to consider any of the following? (select all that apply)",
                   "whhooops",
                   "How often to you visit the TAs to ask questions?",
                   "How often do you talk with other students (not TAs) while in the TA cubicals or CS labs?",
                   "How strongly do you agree with the statement: CS professors and CS courses are engaging.",
                   "How strongly do you agree with the statement: I feel that the CS professors adequately represent the diverse backgrounds views demographics and perspectives of students in CS courses.",
                   "Do you feel like you have role models of the same gender as you who do CS?",
                   "How often have you asked another student (not a TA for the course) to help you understand course material?",
                   "How often have you mentored any students in the CS major or CS courses this semester? (assisted them with labs homework or given internship/job or graduate school advice)",
                   "Do you attend meetings/events for any of the following? (select all that apply)",
                   "What percentage of your friends are taking classes in the CS department?",
                   "Have you been the recipient of an academic scholarship? (select all that apply)",
                   "Have you ever been offered a CS-related internship?",
                   "Which of the following have you done or do you plan to do before you graduate? (select all that apply)",
                   "How often do members of the CS department (students TAs professors etc) ask you about your plans to balance a career and parenthood?",
                   "How often do members of the CS department (students TAs professors etc) tell you that you should be a stay-at-home parent?",
                   "How often do members of the CS department (students TAs professors etc) tell you that you should pursue a full-time career?",
                   "Do you feel like a member of the CS department (students TAs professors etc) has treated you differently than your peers of the opposite gender?",
                   "Are you aware of CS classmates who believe they have been treated differently by members of the CS department (students TAs professors etc) because of their gender?",
                   "Has a member of the CS department (students TAs professors etc) you ever been told that you earned a good grade got a job internship or scholarship offer because of your gender?",
                   "How often do you get negative comments about your appearance or attire from members of the CS department (students TAs  professors etc)?",
                   "If members of the CS department (students TAs professors etc) make negative comments about your appearance what do they comment about? (select all that apply)",
                   "Do you know how to file complaints for being treated differently because of your gender in the CS department?",
                   "Do you know what happens if a complaint is filed against a member of the CS department who is accused of being sexist?",
                   "Would you personally be worried about retribution if you filed a complaint about someone treating you or a peer differently because of your/their gender?",
                   "If you saw a peer treat someone differently because of their gender (through words actions etc) would you say or do something? (select all that apply)",
                   "When you tell people what your major is how often do they express surprise (You don_t look/act like a ____ major, Why are you majoring in ____?",
                   "How often are you subjected to sexist remarks or jokes about your gender?",
                   "Do you feel that some students are held to a higher standard than other students? If so please select all groups that apply.",
                   "How often do you make a suggestion that was not considered until another student of the opposite gender makes the same suggestion?",
                   "Do you feel like you can have non-romantic friends of the opposite gender?",
                   "How strongly do you agree with the statement: Intelligence is a fixed trait; you are born with the talents that you have and nothing you do can change them.",
                   "How strongly do you agree with the statement: Intelligence is a malleable quality if you work hard and practice you will improve.",
                   "How strongly do you agree with the statement: Failure or a lack of achievement is due to insufficient effort.",
                   "How strongly do you agree with the statement: Failure or a lack of achievement is due to personal or environmental obstacles.",
                   "How strongly do you agree with the statement: Failure or a lack of achievement is due to a lack of ability.",
                   "Are there any positive experiences or interactions that you had with members of the CS department that you would like to share?",
                   "Are there any negative experiences or interactions that you had with members of the CS department that you would like to share?",
                   "What one change would you most like to see implemented that would improve the educational experience at this institution?"]

agreement = ['Strongly agree',
             'Agree',
             'Somewhat agree',
             'Neither agree nor disagree',
             'Somewhat disagree',
             'Disagree',
             'Strongly disagree']

frequency = ['Never', 'Once or twice a semester', 'Once a month', 'Once a week', 'Daily']

frequency_typo = ['Never', 'Once or twice a semester', 'Once a month', 'Once a week ', 'Daily']

frequency_TA = ['Never my classes do not have help session', 'Never I don\'t go to help sessions',
                'Once or twice a semester',
                'Once a month',
                'Once a week',
                'Daily']

frequency_TA_typo = ['Never my classes do not have help session', 'Never I don\'t go to help sessions',
                     'Once or twice a semester',
                     'Once a month',
                     'Once a week ',
                     'Daily']

frequency_class_typo = ['Never', 'Once or twice a semester', 'Once a month', 'Once a week ', 'Daily']

frequency_class = ['Never', 'Once or twice a semester', 'Once a month', 'Once a week', 'Daily']

comfort = ['Extremely comfortable', 'Moderately comfortable',
           'Slightly comfortable', 'Neither comfortable nor uncomfortable',
           'Slightly uncomfortable',
           'Moderately uncomfortable',
           'Extremely uncomfortable']

certainty = ['Definitely yes', 'Probably yes',
             'Might or might not',
             'Probably not',
             'Definitely not']

color_options = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'black']

gender_colors = ['deepskyblue', 'hotpink', 'purple', 'green', 'black']

long_colors = ['palevioletred', 'navy', 'm', 'royalblue', 'g', 'purple', 'seagreen', 'blueviolet', 'forestgreen',
               'salmon', 'dodgerblue', 'mediumvioletred', 'aqua', 'firebrick', 'mediumaquamarine', 'goldenrod',
               'darkred', 'sandybrown', 'grey', 'silver', 'orange', 'coral']

consent_current = ['Yes I am over 18 and agree to participate in this study.', 'No I am under 18',
                   'No I do not consent to participate in this study']

consent_future = ['Yes - please enter your email address here', 'No']

miss_class = ['Physical or mental health issues (flu/cold/depression/anxiety/etc)', 'Work commitments',
              'Family commitments', 'Other commitments (club events/religious activities/etc)',
              'To study or do homework for that CS class', 'To study or do homework for other courses',
              'Class is too hard/confusing', 'Class is too easy/boring',
              'On accident (I overslept, lost track of time, was running late, etc)',
              'Time of day/day of week (I hate Monday 8am classes, etc)', 'I don\'t like the subject of the class',
              'I don\'t like the professor/the way they teach/the environment or culture of the class']

increase_comfort = ['Feeling like I am on a similar academic level to my peers', 'Feeling like I won’t be judged',
                    'Knowing my peers in the class', 'Not knowing my peers in the class/feeling anonymous',
                    'Peers asking more questions', 'Having a good grade in the class',
                    'Feeling like the professor wants students to ask questions',
                    'Knowing the professor', 'Larger class size/more students', 'Smaller class size/fewer students']

decrease_comfort = ['I DO feel comfortable asking questions in my CS course(s)', 'Larger class size/more students',
                    'Smaller class size/fewer students', 'Knowing my peers in the class',
                    'Not knowing my peers in the class/feeling anonymous',
                    'I’m worried the professor won’t answer my question (at all/clearly/succinctly/correctly/etc)',
                    'I don’t think the professor wants me to ask questions', 'I’m worried it’s a dumb question',
                    'I’m worried someone else already asked the question', 'I think I ask too many questions',
                    'If other students don’t ask questions', 'I feel like I can figure out the answer own my own',
                    'I don’t want to take time out of class']

participate_decrease = ['I already participate enough/too much', 'The CS class is too large/has too many students',
                        'The CS class is too small/has too few students', 'I don’t know my peers in the class',
                        'I do know my peers in the class', 'I don’t have questions to ask',
                        'I am not prepared for class/don’t have anything to add', 'I am not called on',
                        'I am worried my answer is wrong/comment is irrelevant/etc']

do_not_graph = [consent_current, consent_future]

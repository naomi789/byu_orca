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

answer_type = ["int", "double", "double", "string", "string", "string", "string", "string", "string", "double",
               "string", "string", "string", "list", "list", "string", "list", "list", "agreement", "comfort",
               "frequency_class", "frequency", "list", "frequency", "list", "frequency", "frequency", "frequency",
               "agreement", "agreement", "agreement", "frequency", "frequency", "list", "string", "list", "bool",
               "list", "frequency", "frequency", "frequency", "agreement", "certainty", "certainty", "frequency",
               "list", "certainty", "certainty", "certainty", "list", "agreement", "frequency", "list", "frequency",
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

frequency_TA = ['Never, my classes do not have help session', 'Never, I don\'t go to help sessions',
                'Once or twice a semester',
                'Once a month',
                'Once a week',
                'Daily']

frequency_class = ['Never, because I never go to class', 'Never, but I do attend class', 'Once or twice a semester',
                   'Once a month', 'Once a week', 'Daily']

comfort = ['Extremely comfortable', 'Moderately comfortable',
           'Slightly comfortable', 'Neither comfortable nor uncomfortable',
           'Slightly uncomfortable',
           'Moderately uncomfortable',
           'Extremely uncomfortable']

certainty = ['Definitely yes', 'Probably yes',
             'Might or might not',
             'Probably not',
             'Definitely not']
from new_constants import *

# commenting this out in order to facilitate debugging
FOCUS_VARS = [MAJOR, PROGRAM, GRAD_YEAR]
# GENDER IS NOT INCLUDED BECAUSE WE USE GENDER FOR EVERYTHING
# [AGE, RACE, GENDER, PROGRAM, MAJOR, MINOR, GRAD_YEAR, GPA]
ONE_CHOICE_QUESTIONS = [INTERNSHIP_OFFER, CONFIDENCE_PREPARED_COURSES, CONFIDENCE_PREPARED_COURSES,
                        PARTICIPATION_QUESTIONS_ASK_FREQUENCY,
                        COURSES_ASKING_QUESTIONS_COMFORT, PARTICIPATION_NOT_QUESTIONS_FREQUENCY,
                        PARTICIPATION_ABSENT_WHY, PARTICIPATION_NOT_REASONS, PARTICIPATION_QUESTIONS_ASK_IGNORED,
                        PROFESSORS_ASK_ADVICE, PARTICIPATION_TA_ASK_QUESTIONS, PARTICIPATION_TALK_PEERS,
                        COURSES_PROFESSORS_ENGAGING, PROFESSORS_REPRESENT_DIVERSITY, ROLE_MODELS_SAME_GENDER,
                        PARTICIPATION_PEERS_HELP_YOU, PARTICIPATION_PEERS_YOU_SERVE, PARTICIPATION_FRIENDS_CS_STUDENTS,
                        FRIENDS_CS_STUDENTS_WANT_MORE, FREQUENCY_BALANCE_CAREER_PARENTHOOD, PROFESSORS_DECLARE_PARENT,
                        PROFESSORS_DECLARE_FULL_TIME, DEPARTMENT_SEXIST_YOU, DEPARTMENT_SEXIST_OTHERS,
                        DEPARTMENT_APPEARANCE, COMPLAINTS_HOW, COMPLAINTS_CONCEQUENCES, COMPLAINTS_CONCEQUENCES_FEAR,
                        PEOPLE_SURPRISE_MAJOR, PEOPLE_SEXIST_JOKES_GENDER, PEER_SEXISM_IGNORING_SUGGESTION,
                        INTELLIGENCE_FIXED, FAILURE_ABILITY, FAILURE_ENVIRONMENT, FAILURE_LAZY, FRIENDS_OTHER_GENDER,
                        INTELLIGENCE_MALLEABLE, COURSES_ABSENT_FREQUENCY, PARTICIPATION_TA_SESSION, ]
    # CONFIDENCE_GRAD_GPA, (should be in the above list)

PRO_CON_STRINGS = [MAJOR_CONS_CLASS, MAJOR_CONS_CLASS]

TEXT_ANSWERS = [DESCRIBE_POSITIVE_EXPERIENCE, DESCRIBE_NEGATIVE_EXPERIENCE, SUGGESTION_IMPROVE_INSTITUTION]

NUMBER_ANSWERS = [GPA, CONFIDENCE_PERCENTILE_PEERS, AGE]

UNSURE = [UNIVERSITY_COURSES_FALL, FALL_COURSES] # a duplicate

# does not belong here: PARTICIPATION_ABSENT_WHY, PARTICIPATION_FRIENDS_CS_STUDENTS, PARTICIPATION_NOT_REASONS
MANY_CHOICES_QUESTIONS = [MAJOR_PROS, MAJOR_CONS, EXTRACURRICULARS, PARTICIPATION_MORE_COMFORTABLE,
                          PARTICIPATION_LESS_COMFORTABLE, PARTICIPATION_GROUP_PROJECT_ROLE, PROFESSORS_ENCOURAGED_YOU,
                          PARTICIPATION_CLUBS, EXTRACURRICULAR_PLANS_BEFORE_GRADUATION, DEPARTMENT_APPEARANCE_COMMENTS,
                          PEER_MISTREATED_REACT, HIGHEST_STANDARD, SCHOLARSHIP]

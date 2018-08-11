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
CONFIDENCE_GRAD_GPA = 'Q68'
CONFIDENCE_PREPARED_COURSES = 'Q88'
CONFIDENCE_PERCENTILE_PEERS = 'Q93'
COURSES_QUESTION_COMFORT = 'Q86'

FOCUS_VARS = [MAJOR, PROGRAM, GRAD_YEAR]
# GENDER IS NOT INCLUDED BECAUSE WE USE GENDER FOR EVERYTHING
# [AGE, RACE, GENDER, PROGRAM, MAJOR, MINOR, GRAD_YEAR, GPA]
ONE_CHOICE_QUESTIONS = [INTERNSHIP_OFFER, CONFIDENCE_GRAD_GPA, CONFIDENCE_PREPARED_COURSES, CONFIDENCE_PREPARED_COURSES, FALL_COURSES, EXTRACURRICULARS]
TEXT_ANSWERS = [MAJOR_CONS_CLASS, MAJOR_CONS_CLASS]
NUMBER_ANSWERS = [GPA, CONFIDENCE_PERCENTILE_PEERS, AGE]
MANY_CHOICES_QUESTIONS = [MAJOR_PROS, MAJOR_CONS]

# Q84	Q16	Q15	Q90	Q83	Q91	Q85	Q92	Q57	Q46	Q18	Q19	Q21	Q22	Q52	Q20	Q59	Q63	Q26	Q25	Q27	Q28	Q82	Q48	Q9	Q32	Q31	Q30	Q41	Q42	Q35	Q62	Q61	Q38	Q39	Q40	Q51	Q60	Q58	Q60	Q61	Q56	Q75	Q76	Q77	Q78	Q79

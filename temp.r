#Set working directory
# setwd("~/Box Sync/Collaborations/Naomi")

#load Libraries
list.of.packages <- c("psych")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(psych)
#Read in data
# dat <- read_excel("overall_survey.xlsx")
#or
dat <- read.csv("overall_survey.csv")

###################################################
#--------------Data Processing--------------------#
###################################################
#Select only those who agree to participate
dat <- dat[which(dat$Q70 == "Yes I am over 18 and agree to participate in this study."),]

#Remove odd responses for male/female question
dat$Q3[which(dat$Q3 != "Male" &
          dat$Q3 != "Female" &
          dat$Q3 != "Other")] <- NA

#Make characters into factors
dat$Q3 <- as.factor(dat$Q3)
dat$Q4 <- as.factor(dat$Q4)
dat$Q5 <- as.factor(dat$Q5)
dat$Q6 <- as.factor(dat$Q6)
dat$Q7 <- as.factor(dat$Q7)
dat$Q73 <- as.ordered(dat$Q73)
dat$Q81 <- as.factor(dat$Q81)
dat$Q50 <- as.factor(dat$Q50)
dat$Q8 <- as.factor(dat$Q8)

#Separate Responses for Q8, Q10, and Q11
# also questions: Q7, Q91, Q85, Q46, Q19, Q27, Q48, Q9, Q51, Q60,
# dat$Q8

#rescore for average age in range (REPORT THIS)
dat$Q80 <- as.character(dat$Q80)
dat$Q80[which(dat$Q80=="31-39")] <- 35
dat$Q80[which(dat$Q80=="40-49")] <- 45
dat$Q80[which(dat$Q80=="50-59")] <- 55

#make age numeric
dat$Q80 <- as.numeric(dat$Q80)

# make GPA numeric
dat$Q74_2_TEXT <- as.numeric(dat$Q74_2_TEXT)

#Recode Likert Items to Numeric
## Build a function to do this
recodeLikert <- function(x){
  ifelse(x=="Strongly disagree",1,
         ifelse(x=="Disagree",2,
                ifelse(x=="Neither agree nor disagree",3,
                       ifelse(x=="Agree",4,5))))
}

likertItems <- colnames(dat)[colSums(dat=="Strongly disagree" |
                dat=="Disagree" |
                dat=="Neither agree nor disagree" |
                dat=="Agree" |
                dat=="Strongly agree",na.rm=TRUE) > 0]

dat[,likertItems] <- sapply(dat[,likertItems],
                               recodeLikert)

###################################################
#-------------------Input-------------------------#
###################################################

# see pie charts of: gender Q3, race Q81, age Q80, degree Q4,
# major Q5, minor Q6, fall CS courses Q7, graduateion year Q73,
# histogram of: GPA Q74_2_TEXT
# graph of: major pros Q10, major cons Q11
# impact of absences Q84,

###################################################
#----------------Response Rate--------------------#
###################################################

# looking at response rate for various categories
# undergrad/masters/PhD, major/minor, female/male

###################################################
#-----------------Analysis------------------------#
###################################################

# Analysis of Q50: "Have you ever been offered a CS-related internship?"
# hypothesis: upperclassmen/older students/graduate students are more likely to say yes


# Analysis of Q8: "What extracurriculars have you pursued in high school or college? (select all that apply)"
# hypothesis: CS major women are more likely to say debate/sports than non CS major women. Men are more likely to say STEM than women.

# Analysis of Q10: "What factors influenced your decision to pick your major? (select all that apply)"
# hypothesis: CS majors are more likely to say $$$. Women are more likely to say mom/dad/teacher support. Women are more likely to say contribute to society.

# Analysis of Q11: "What do you perceive as being a barrier to your completion of this major and your career in
# this field? (select all that apply)"
# hypothesis: Men=no barriers. Women=not fitting in; parenting; relationships; ability to succeed. All?

# Analysis of Q68: "How much do you agree with the following statement: I am confident in my ability to
# graduate with a 3.0 or higher major GPA (your major GPA does not include AP/IB credits or
# general education/GE classes)."
# hypothesis: All say "strongly agree" (grade inflation since the paper that inspired me to ask this)

# Analysis of Q88: "How much do you agree with the following statement: I am prepared for my CS course(s)
# next semester."
# hypothesis: Men=more confident. CS majors = more confident.

# Analysis of Q93: "With respect to your peers in your major, what percentile would you rank yourself at?
# Please enter a number between 0 and 100"
# hypothesis: Men say higher numbers given the same GPA as a woman.

# Analysis of Q8: "How comfortable are you asking questions in your non-CS courses?""
# hypothesis: Women=less than men. Majors=more than non-majors.

# Analysis of Q84: "How often are you absent from your CS class(es)?""
# hypothesis: ...I wanted to see how this response impacts other responses. (GPA, confidence, etc)

# Analysis of Q15: "How comfortable are you asking questions in your CS courses?""
# hypothesis:  Women=less than men. Majors=more than non-majors.

# Analysis of Q90: "Aside from asking questions,how often do you participate (answer questions/talk in
# discussions/etc) in CS courses?""
# hypothesis:  Women=less than men. Majors=more than non-majors.

# Analysis of Q83: "When you miss a CS class, what is most often the reason why? (only select one)"
# hypothesis:  ...I wanted to see how this response impacts other responses. (GPA, confidence, etc)

# Analysis of Q91: "What helps you feel MORE COMFORTABLE asking questions in your CS course(s)?
# (select all that apply)"
# hypothesis: ... Wanted to see if certain responses here predict Q83 and Q90 above. Also, men select more options?

# Analysis of Q85: "When do you feel LESS COMFORTABLE asking questions in your CS course(s)? (select
# all that apply)"
# hypothesis: ... Wanted to see if certain responses here predict Q83 and Q90 above. Also, WOMEN select more options?

# Analysis of Q92: "Why do you not participate (aside from asking questions: answering questions/participating
# in discussions/etc) more in your CS course(s)?"
# hypothesis: similar to Q85 and Q91

# Analysis of Q57: "How often do you raise your hand in a CS class but never get called on?"
# hypothesis: Men perceive it as happening more, but it actually happens to women more --> same accross genders? More for undergrads and more for upperclassmen.

# Analysis of Q46: "In group projects for CS courses which tasks do you typically take responsibility for? (select
# all that apply)"
# hypothesis: Within CS major: women are more likely to say creative/men technical. For non-technical majors, women are MUCH less likely to say technical.

# Analysis of Q18: "How often do you discuss your academic performance or career plans with a professor or
# faculty member? (during office hours or in other one-on-one situations)"
# hypothesis: women=less than men

# Analysis of Q19: "Has as a CS professor ever invited you, personally, to consider any of the following?
# (select all that apply)"
# hypothesis: Women='join major'/'continue in major'. Men='grad school'/'research'. But between CS/non CS major.... And under v. upperclassman...
# TODO^^

# Analysis of Q21: "How often do you go to TA-led help sessions for CS courses?" "
# hypothesis: women=go more often. non majors = go more often?

# Analysis of Q22: "How often to you visit the CS TAs to ask questions?"
# hypothesis:  women=go more often. non majors = go more often?

# Analysis of Q52 How often do you talk with other students (not TAs) while in the CS TA cubicals or CS
# labs?
# hypothesis: women=talk less? Should look at impact of Q22 in predicting this answer.

# Analysis of Q20: How strongly do you agree with the statement: CS professors and CS courses are
# engaging.
# hypothesis: same across genders; CS majors/grad students/upperclassmen=agree more.

# Analysis of Q59: "How strongly do you agree with the statement: I feel that the CS professors adequately
# represent the diverse backgrounds, views, demographics, and perspectives of students in CS
# courses."
# hypothesis: Men=agree more than women. Undergrad agree more than grad.

# Analysis of Q63: "Do you feel like you have role models of the same gender as you who do CS?""
# hypothesis:  Men=agree more than women. GRAD agree more than undergrad.

# Analysis of Q26 How often have you asked another student (not a TA for the course) to help you
# understand CS course material?
# hypothesis: Men=agree more than women. non-CS majors=agree more than CS majors. Older/upperclassmen/gradstudents=agree more

# Analysis of Q25 How often have you mentored any students in the CS major or CS courses this semester?
# (assisted them with labs, homework, or given internship/job or graduate school advice)
# hypothesis: Same as for Q26.

# Analysis of Q27 Do you attend meetings/events for any of the following? (select all that apply)
# hypothesis: More women than men @WiCS/WIT; otherwise more men. Few non-CS at most clubs; idk about age/graduation. Few grad students.

# Analysis of Q28: "What percentage of your friends are taking classes in the CS department?
# hypothesis: men say more; CS majors say more.

# Analysis of Q82 How much do you agree with the following statement: I want to make more friends in the
# CS major
# hypothesis: women say yes more than men (but do more women IN CS say that than NON-CS??)

# Analysis of Q48 Have you been the recipient of an academic scholarship? (select all that apply)
# hypothesis: similar; more CS majors than non (if $$ was a factor in picking major?); more women for minority scholarships

# Analysis of Q9 Which of the following have you done, or do you plan to do before you graduate? (select all
# that apply)
# hypothesis: more CS majors than non say internship (vice versa for study abroad?). More upperclassmen for research/capstone?

# Analysis of Q32 How often do members of the CS department (students, TAs, professors, etc) ask you
# about your plans to balance a career and parenthood?
# hypothesis: hopefully everyone says never?

# Analysis of Q31 How often do members of the CS department (students, TAs, professors, etc) tell you that
# you should be a stay-at-home parent?
# hypothesis: hopefully everyone says never?

# Analysis of Q30 How often do members of the CS department (students, TAs, professors, etc) tell you that
# you should pursue a full-time career?
# hypothesis: hopefully everyone says never?

# Analysis of Q41 Do you feel like a member of the CS department (students, TAs, professors, etc) has
# treated you differently than your peers of the opposite gender?
# hypothesis:

# Analysis of Q42 Are you aware of CS classmates who believe they have been treated differently by
# members of the CS department (students, TAs, professors, etc) because of their gender?
# hypothesis:

# Analysis of Q35 Has a member of the CS department (students, TAs, professors, etc)ever told you that you
# earned a good grade, got a job, internship, or scholarship offer because of your gender?
# hypothesis:

# Analysis of Q62 How often do you get negative comments about your appearance or attire from members
# of the CS department (students, TAs, professors, etc)?
# hypothesis:

# Analysis of Q61 If members of the CS department (students, TAs, professors, etc) make negative
# comments about your appearance, what do they comment about? (select all that apply)
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q
# hypothesis:

# Analysis of Q88: "I am prepared for my CS course(s) next semester."
modQ88 <- lm(Q88 ~ Q3, data=dat)
summary(modQ88)
boxplot(Q88 ~ Q3, data = dat,
        ylab = "Preparedness",
        col = "lightblue")
TukeyHSD(aov(modQ88))

# p value
# t value tells me how different it is (standardized estimate of how different my data is FROM ZERO, given change)
# multiple R squared (how much variation in output is determined by input)









# pie(table(dat$Q80),main="Age",col=rainbow(10))
# hist(dat$Q80[which(dat$Q80 <=30)],
#      breaks = 10,
#      main ="Histogram of Age",
#     col="lightblue",
#     xlab="Age")








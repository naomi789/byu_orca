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
# hypothesis: CS major women are more likely to say debate/sports than non CS major women

# Analysis of Q10: "What factors influenced your decision to pick your major? (select all that apply)"
# hypothesis

# Analysis of Q
# hypothesis

# Analysis of Q
# hypothesis

# Analysis of Q
# hypothesis

# Analysis of Q
# hypothesis

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








# Latent Growth Curve Models (LGCM) # use lavaan (pretty straightforward) 
# https://www.youtube.com/watch?v=vrHaAdjC97A
# https://pdfs.semanticscholar.org/f704/f45451442926fab8bc29577aad3c82f8104f.pdf

library(lavaan)
library(data.table)
library(ggplot2)## v >= 1.9.6
library(semPlot)

setwd("C:/Users/snjoh/Documents/secret_byu_data/confidence")
# setwd("C:/Users/Blood//Box Sync/Collaborations/Naomi/all_confidence_data")
# setwd("~/Box Sync/Collaborations/Naomi/all_confidence_data")


# read in the data
# first week
weeka_original <- read.csv("2018_09_26.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# weeka <- weeka[,c(2,12:13,19:28)]
weeka <- weeka_original[,c(2, 12, 25:28)] # 24, 22 = major

# regular middle weeks
weekb <- read.csv("2018_10_24.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekb <- weekb[,c(2,12,18:21)]

weekc <- read.csv("2018_11_05.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekc <- weekc[,c(2,12,18:21)]

weekd <- read.csv("2018_11_19.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekd <- weekd[,c(2,12,18:21)]

weeke <- read.csv("2018_12_10.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weeke <- weeke[,c(2,12,18:21)]

weekf <- read.csv("2018_12_17.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekf <- weekf[,c(2,12,18:21)]

# last week
weekg_original <- read.csv("2019_01_06.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekg <- weekg_original[,c(2,12,23:26)]
weekg <- weekg_original[,c(2,12,23:26)] # 18-22 # 27 = gender # 29 is major # 31 and 32 = course and grade (respectively)

weeka$week <- 4 # 4
weekb$week <- 8 # 8
weekc$week <- 10 # 10
weekd$week <- 12 # 12
weeke$week <- 15 # 15
weekf$week <- 16 # 16
weekg$week <- 19 # 19

weekData <- rbind(weeka,weekb,weekc,weekd,weeke,weekf,weekg)
weeka <- NULL
weekb <- NULL
weekc <- NULL
weekd <- NULL
weeke <- NULL
weekf <- NULL
weekg <- NULL


colnames(weekData) <- c("EndDate","Email","FutureSuccess",
                        "PostGradCSPlans","BetterCSthanGE",
                        "BetterCSthanGrades","week")

weekData[weekData=="Strongly disagree"] <- 1
weekData[weekData=="Somewhat disagree"] <- 2
weekData[weekData=="Disagree"] <- 3
weekData[weekData=="Neither agree nor disagree"] <- 4
weekData[weekData=="Agree"] <- 5
weekData[weekData=="Somewhat agree"] <- 6
weekData[weekData=="Strongly agree"] <- 7

weekData[weekData=="Extremely unlikely"] <- 1
weekData[weekData=="Moderately unlikely"] <- 2
weekData[weekData=="Slightly unlikely"] <- 3
weekData[weekData=="Neither likely nor unlikely"] <- 4
weekData[weekData=="Slightlylikely"] <- 5
weekData[weekData=="Moderately likely"] <- 6
weekData[weekData=="Extremely likely"] <- 7

weekData[weekData=="Definitely not"] <- 1
weekData[weekData=="Probably not"] <- 2
weekData[weekData=="Might or might not"] <- 3
weekData[weekData=="Probably yes"] <- 4
weekData[weekData=="Definitely yes"] <- 5

weekData[,c("FutureSuccess","PostGradCSPlans",
            "BetterCSthanGE","BetterCSthanGrades")] <- apply(weekData[,c("FutureSuccess","PostGradCSPlans",
                                                                         "BetterCSthanGE","BetterCSthanGrades")],
                                                             2,
                                                             function(x) as.numeric(x))
weekData$EndDate <- as.Date(weekData$EndDate)

# sPlot <- ggplot(weekData, aes(x=EndDate, y=FutureSuccess, group=Email))+
#   geom_line()
# 
# sPlot

weekData.wide <- data.frame(dcast(setDT(weekData), Email ~ week, value.var = c("FutureSuccess","PostGradCSPlans",
                                                                               "BetterCSthanGE","BetterCSthanGrades")))

# Graph of all students' percieved future success
future_success <- ggplot(weekData, aes(x=week, y=FutureSuccess, group=Email))+
  geom_line()
future_success
post_grad <- ggplot(weekData, aes(x=week, y=PostGradCSPlans, group=Email))+
  geom_line()
post_grad
better_CS_than_GE <- ggplot(weekData, aes(x=week, y=BetterCSthanGE, group=Email))+
  geom_line()
better_CS_than_GE
better_CS_than_grades <- ggplot(weekData, aes(x=week, y=BetterCSthanGrades, group=Email))+
  geom_line()
better_CS_than_grades

# WITH ACTUAL END DATES
# Graph of all students' percieved future success
EndDate_future_success <- ggplot(weekData, aes(x=EndDate, y=FutureSuccess, group=Email))+
  geom_line()
EndDate_future_success

EndDate_post_grad <- ggplot(weekData, aes(x=EndDate, y=PostGradCSPlans, group=Email))+
  geom_line()
EndDate_post_grad

EndDate_better_CS_than_GE <- ggplot(weekData, aes(x=EndDate, y=BetterCSthanGE, group=Email))+
  geom_line()
EndDate_better_CS_than_GE

EndDate_better_CS_than_grades <- ggplot(weekData, aes(x=EndDate, y=BetterCSthanGrades, group=Email))+
  geom_line()
EndDate_better_CS_than_grades


weekData.wide$MajorAtBegining <- NA 
weekData.wide$MajorAtEnd <- NA
weekData.wide$Gender <- NA 
weekData.wide$Class <- NA
weekData.wide$Grade <- NA
weekData.wide$CSSwitch <- NA


weekData.wide[which(weekData.wide$Email %in% weeka_original$RecipientEmail),"MajorAtBegining"] <- weeka_original[which(weekData.wide$Email %in% weeka_original$RecipientEmail),22]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"MajorAtEnd"] <- as.numeric(weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),30])
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Gender"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),27]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Class"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),32]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Grade"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),33]
weekData.wide[,"CSSwitch"] <- ifelse(weekData.wide[,"MajorAtBegining"]=="Computer Science" & weekData.wide[,"MajorAtEnd"]==1,"No Switch CS",
                                     ifelse(weekData.wide[,"MajorAtBegining"]=="Computer Science" & weekData.wide[,"MajorAtEnd"]!=1,"Switch Out",
                                            ifelse(weekData.wide[,"MajorAtBegining"]!="Computer Science" & weekData.wide[,"MajorAtEnd"]==1,"Switch In",
                                                   ifelse(weekData.wide[,"MajorAtBegining"]!="Computer Science" & weekData.wide[,"MajorAtEnd"]!=1,"No Switch nonCS",NA))))

weekData.wide$Grade[weekData.wide$Grade==1] <- "A"
weekData.wide$Grade[weekData.wide$Grade==2] <- "A-"
weekData.wide$Grade[weekData.wide$Grade==3] <- "B+"
weekData.wide$Grade[weekData.wide$Grade==4] <- "B"
weekData.wide$Grade[weekData.wide$Grade==5] <- "B-"
weekData.wide$Grade[weekData.wide$Grade==6] <- "C+"
weekData.wide$Grade[weekData.wide$Grade==7] <- "C"
weekData.wide$Grade[weekData.wide$Grade==8] <- "C-"
weekData.wide$Grade[weekData.wide$Grade==9] <- "D+"
weekData.wide$Grade[weekData.wide$Grade==10] <- "D"
weekData.wide$Grade[weekData.wide$Grade==11] <- "D-"
weekData.wide$Grade[weekData.wide$Grade==12] <- "E"
weekData.wide$Grade[weekData.wide$Grade==13] <- "I"
weekData.wide$Grade[weekData.wide$Grade==14] <- "W"

mat11 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==142),2:8])))
mat12 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==235),2:8])))
mat13 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==236),2:8])))
mat14 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==240),2:8])))

mat21 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==142),9:15])))
mat22 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==235),9:15])))
mat23 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==236),9:15])))
mat24 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==240),9:15])))

mat31 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==142),16:22])))
mat32 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==235),16:22])))
mat33 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==236),16:22])))
mat34 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==240),16:22])))

mat41 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==142),23:29])))
mat42 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==235),23:29])))
mat43 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==236),23:29])))
mat44 <- mean(colMeans(na.omit(weekData.wide[which(weekData.wide$Class==240),23:29])))


#Bar plot 
classDat=matrix(c(mat11,mat21,mat31,mat41,
                  mat12,mat22,mat32,mat42,
                  mat13,mat23,mat33,mat43,
                  mat14,mat24,mat34,mat44), nrow=4,ncol=4, byrow=TRUE)
colnames(classDat)=c("142","235","236","240")
rownames(classDat)=c("FutureSuccess","PostGradCSPlans","BetterCSthanGE", "BetterCSthanGrades")

# Grouped barplot
barplot(classDat, 
        col=rainbow(4,alpha=.6) , 
        beside=T, 
        legend=rownames(classDat), 
        xlab="Class",
        ylab="Average Score",
        ylim=c(0,10))

#Number of people who switched in and out of CS
sum(table(weekData.wide$Email[which(weekData.wide$CSSwitch=="Switch In")]))

sum(table(weekData.wide$Email[which(weekData.wide$CSSwitch=="Switch Out")]))      

########################################################################################
#Plot by CS Switch
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$CSSwitch == "Switch In","green",
                   ifelse(weekData.wide$CSSwitch == "Switch Out","red2",NA)),
        ylab="FutureSuccess",
        xlab="Week")  

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$CSSwitch == "Switch In","green",
                   ifelse(weekData.wide$CSSwitch == "Switch Out","red2",NA)),
        ylab="FutureSuccess",
        xlab="Week")

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$CSSwitch == "Switch In","green",
                   ifelse(weekData.wide$CSSwitch == "Switch Out","red2",NA)),
        ylab="FutureSuccess",
        xlab="Week")

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$CSSwitch == "Switch In","green",
                   ifelse(weekData.wide$CSSwitch == "Switch Out","red2",NA)),
        ylab="FutureSuccess",
        xlab="Week")

########################################################################################
#Plot by grade
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"green","red2"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"green","red2"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"green","red2"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"green","red2"),
        ylab="FutureSuccess",
        xlab="Week")   

########################################################################################
#plot by gender
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$Gender==1,"red2",
                   ifelse(weekData.wide$Gender==2,"blue",NA)),
        ylab="FutureSuccess",
        xlab="Week")    

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$Gender==1,"red2",
                   ifelse(weekData.wide$Gender==2,"blue",NA)),
        ylab="PostGradCSPlans",
        xlab="Week") 

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$Gender==1,"red2",
                   ifelse(weekData.wide$Gender==2,"blue",NA)),
        ylab="BetterCSthanGE",
        xlab="Week") 

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$Gender==1,"red2",
                   ifelse(weekData.wide$Gender==2,"blue",NA)),
        ylab="BetterCSthanGrades",
        xlab="Week") 

########################################################################################
#Plot by class
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$Class==142,"red2",
                   ifelse(weekData.wide$Class==235,"blue",
                          ifelse(weekData.wide$Class==236,"green",
                                 ifelse(weekData.wide$Class==240,"orange",NA)))),
        ylab="FutureSuccess",
        xlab="Week") 

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$Class==142,"red2",
                   ifelse(weekData.wide$Class==235,"blue",
                          ifelse(weekData.wide$Class==236,"green",
                                 ifelse(weekData.wide$Class==240,"orange",NA)))),
        ylab="FutureSuccess",
        xlab="Week") 

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$Class==142,"red2",
                   ifelse(weekData.wide$Class==235,"blue",
                          ifelse(weekData.wide$Class==236,"green",
                                 ifelse(weekData.wide$Class==240,"orange",NA)))),
        ylab="FutureSuccess",
        xlab="Week") 

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$Class==142,"red2",
                   ifelse(weekData.wide$Class==235,"blue",
                          ifelse(weekData.wide$Class==236,"green",
                                 ifelse(weekData.wide$Class==240,"orange",NA)))),
        ylab="FutureSuccess",
        xlab="Week") 


########################################################################################
# Plot by CS Major
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$CSMajor == 1,"green","blue"),
        ylab="FutureSuccess",
        xlab="Week")  

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$CSMajor == 1,"green","blue"),
        ylab="FutureSuccess",
        xlab="Week")

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$CSMajor == 1,"green","blue"),
        ylab="FutureSuccess",
        xlab="Week")

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$CSMajor == 1,"green","blue"),
        ylab="FutureSuccess",
        xlab="Week")

########################################################################################
########################################################################################
########################################################################################

mod.FutureSuccess <-'
#Make Latent Variables
Intercept =~ 1*FutureSuccess_4 + 1*FutureSuccess_8 + 
1*FutureSuccess_10 + 1*FutureSuccess_12 + 
1*FutureSuccess_15 + 1*FutureSuccess_16 + 
1*FutureSuccess_19

Slope =~ 0*FutureSuccess_4 + 0*FutureSuccess_8 + 
0*FutureSuccess_10 + 0*FutureSuccess_12 + 
0*FutureSuccess_15 + 0*FutureSuccess_16 + 
-1*FutureSuccess_19

Intercept ~~ Slope
Intercept ~~ Intercept
Slope ~~ Slope

Intercept ~ 1
Slope ~ 1

#Manifest Error
FutureSuccess_4 ~~ FutureSuccess_4
FutureSuccess_8 ~~ FutureSuccess_8
FutureSuccess_10 ~~ FutureSuccess_10
FutureSuccess_12 ~~ FutureSuccess_12
FutureSuccess_15 ~~ FutureSuccess_15
FutureSuccess_16 ~~ FutureSuccess_16
#FutureSuccess_19 ~~ FutureSuccess_19
'

mod.FutureSuccess.Run <- lavaan(mod.FutureSuccess, missing = "ML", data = weekData.wide)

summary(mod.FutureSuccess.Run, fit.measures="TRUE")

semPaths(mod.FutureSuccess.Run, whatLabels="est")  


mod.PostGradCSPlans <-'
#Make Latent Variables
Intercept =~ 1*PostGradCSPlans_4 + 1*PostGradCSPlans_8 + 
1*PostGradCSPlans_10 + 1*PostGradCSPlans_12 + 
1*PostGradCSPlans_15 + 1*PostGradCSPlans_16 + 
1*PostGradCSPlans_19

Slope =~ 0*PostGradCSPlans_4 + 0*PostGradCSPlans_8 + 
0*PostGradCSPlans_10 + 0*PostGradCSPlans_12 + 
0*PostGradCSPlans_15 + 0*PostGradCSPlans_16 + 
-1*PostGradCSPlans_19

Intercept ~~ Slope
Intercept ~~ Intercept
Slope ~~ Slope

Intercept ~ 1
Slope ~ 1

#Manifest Error
PostGradCSPlans_4 ~~ PostGradCSPlans_4
PostGradCSPlans_8 ~~ PostGradCSPlans_8
PostGradCSPlans_10 ~~ PostGradCSPlans_10
PostGradCSPlans_12 ~~ PostGradCSPlans_12
PostGradCSPlans_15 ~~ PostGradCSPlans_15
PostGradCSPlans_16 ~~ PostGradCSPlans_16
#PostGradCSPlans_19 ~~ PostGradCSPlans_19
'

mod.PostGradCSPlans.Run <- lavaan(mod.PostGradCSPlans, missing = "ML", data = weekData.wide)

summary(mod.PostGradCSPlans.Run, fit.measures="TRUE")

semPaths(mod.PostGradCSPlans.Run, whatLabels="est")  


mod.BetterCSthanGE <-'
#Make Latent Variables
Intercept =~ 1*BetterCSthanGE_4 + 1*BetterCSthanGE_8 + 
1*BetterCSthanGE_10 + 1*BetterCSthanGE_12 + 
1*BetterCSthanGE_15 + 1*BetterCSthanGE_16 + 
1*BetterCSthanGE_19

Slope =~ 0*BetterCSthanGE_4 + 0*BetterCSthanGE_8 + 
0*BetterCSthanGE_10 + 0*BetterCSthanGE_12 + 
0*BetterCSthanGE_15 + 0*BetterCSthanGE_16 + 
-1*BetterCSthanGE_19

Intercept ~~ Slope
Intercept ~~ Intercept
Slope ~~ Slope

Intercept ~ 1
Slope ~ 1

#Manifest Error
BetterCSthanGE_4 ~~ BetterCSthanGE_4
BetterCSthanGE_8 ~~ BetterCSthanGE_8
BetterCSthanGE_10 ~~ BetterCSthanGE_10
BetterCSthanGE_12 ~~ BetterCSthanGE_12
BetterCSthanGE_15 ~~ BetterCSthanGE_15
BetterCSthanGE_16 ~~ BetterCSthanGE_16
#BetterCSthanGE_19 ~~ BetterCSthanGE_19
'

mod.BetterCSthanGE.Run <- lavaan(mod.BetterCSthanGE, missing = "ML", data = weekData.wide)

summary(mod.BetterCSthanGE.Run, fit.measures="TRUE")

semPaths(mod.BetterCSthanGE.Run, whatLabels="est")  





mod.BetterCSthanGrades <-'
#Make Latent Variables
Intercept =~ 1*BetterCSthanGrades_4 + 1*BetterCSthanGrades_8 + 
1*BetterCSthanGrades_10 + 1*BetterCSthanGrades_12 + 
1*BetterCSthanGrades_15 + 1*BetterCSthanGrades_16 + 
1*BetterCSthanGrades_19

Slope =~ 0*BetterCSthanGrades_4 + 0*BetterCSthanGrades_8 + 
0*BetterCSthanGrades_10 + 0*BetterCSthanGrades_12 + 
0*BetterCSthanGrades_15 + 0*BetterCSthanGrades_16 + 
-1*BetterCSthanGrades_19

Intercept ~~ Slope
Intercept ~~ Intercept
Slope ~~ Slope

Intercept ~ 1
Slope ~ 1

#Manifest Error
BetterCSthanGrades_4 ~~ BetterCSthanGrades_4
BetterCSthanGrades_8 ~~ BetterCSthanGrades_8
BetterCSthanGrades_10 ~~ BetterCSthanGrades_10
BetterCSthanGrades_12 ~~ BetterCSthanGrades_12
BetterCSthanGrades_15 ~~ BetterCSthanGrades_15
BetterCSthanGrades_16 ~~ BetterCSthanGrades_16
#BetterCSthanGrades_19 ~~ BetterCSthanGrades_19
'

mod.BetterCSthanGrades.Run <- lavaan(mod.BetterCSthanGrades, missing = "ML", data = weekData.wide)

summary(mod.BetterCSthanGrades.Run, fit.measures="TRUE")

semPaths(mod.BetterCSthanGrades.Run, whatLabels="est")  









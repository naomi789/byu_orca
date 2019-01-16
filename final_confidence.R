# Latent Growth Curve Models (LGCM) # use lavaan (pretty straightforward) 
# https://www.youtube.com/watch?v=vrHaAdjC97A
library(lavaan)
library(data.table)
library(ggplot2)## v >= 1.9.6
library(semPlot)

setwd("C:/Users/Blood//Box Sync/Collaborations/Naomi/all_confidence_data")
#setwd("~/Box Sync/Collaborations/Naomi/all_confidence_data")


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
weekg_original <- read.csv("2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
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
sPlot <- ggplot(weekData, aes(x=week, y=FutureSuccess, group=Email))+
  geom_line()

sPlot

weekData.wide <- data.frame(dcast(setDT(weekData), Email ~ week, value.var = c("FutureSuccess","PostGradCSPlans",
                                                                               "BetterCSthanGE","BetterCSthanGrades")))

weekData.wide$MajorAtBegining <- NA 
weekData.wide$MajorAtEnd <- NA
weekData.wide$Gender <- NA 
weekData.wide$Class <- NA
weekData.wide$Grade <- NA
weekData.wide[which(weekData.wide$Email %in% weeka_original$RecipientEmail),"MajorAtBegining"] <- weeka_original[which(weekData.wide$Email %in% weeka_original$RecipientEmail),22]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"MajorAtEnd"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),29]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Gender"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),27]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Class"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),32]
weekData.wide[which(weekData.wide$Email %in% weekg_original$RecipientEmail),"Grade"] <- weekg_original[which(weekData.wide$Email %in% weekg_original$RecipientEmail),33]

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

#Plot by grade
matplot(c(4,8,10,12,15,16,19),
        main="...successful in future computing activities",
        t(weekData.wide[,2:8]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"red2","blue"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="...after grad... CS pursue a career that inv",
        t(weekData.wide[,9:15]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"red2","blue"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="Better at CS than GE",
        t(weekData.wide[,16:22]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"red2","blue"),
        ylab="FutureSuccess",
        xlab="Week")   

matplot(c(4,8,10,12,15,16,19),
        main="Im better at CS than My grades would say",
        t(weekData.wide[,23:29]),type="l",
        col=ifelse(weekData.wide$Grade%in%c("A","A-","B+","B","B-"),"red2","blue"),
        ylab="FutureSuccess",
        xlab="Week")   

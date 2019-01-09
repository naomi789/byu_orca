# Latent Growth Curve Models (LGCM) # use lavaan (pretty straightforward) 
# https://www.youtube.com/watch?v=vrHaAdjC97A
library(lavaan)
l

# read in the data
# first week
weeka <- read.csv("./../secret_byu_data/confidence/2018_09_26.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# weeka <- weeka[,c(2,12:13,19:28)]
weeka <- weeka[,c(2, 12, 25:28)]

# regular middle weeks
weekb <- read.csv("./../secret_byu_data/confidence/2018_10_24.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekb <- weekb[,c(2,12,18:21)]

weekc <- read.csv("./../secret_byu_data/confidence/2018_11_05.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekc <- weekc[,c(2,12,18:21)]

weekd <- read.csv("./../secret_byu_data/confidence/2018_11_19.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekd <- weekd[,c(2,12,18:21)]

weeke <- read.csv("./../secret_byu_data/confidence/2018_12_10.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weeke <- weeke[,c(2,12,18:21)]

weekf <- read.csv("./../secret_byu_data/confidence/2018_12_17.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
weekf <- weekf[,c(2,12,18:21)]

# last week
weekg <- read.csv("./../secret_byu_data/confidence/2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# weekg <- weekg[,c(2,12,18:50)]
weekg <- weekg[,c(2, 12,23:26)]


weeka$week <- 4 # 4
weekb$week <- 8 # 8
weekc$week <- 10 # 10
weekd$week <- 12 # 12
weeke$week <- 15 # 15
weekf$week <- 16 # 16
weekg$week <- 19 # 19

weekData <- rbind(weeka,weekb,weekc,weekd,weeke,weekf,weekg)

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








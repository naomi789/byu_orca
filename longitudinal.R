# Latent Growth Curve Models (LGCM) # use lavaan (pretty straightforward) 
# https://www.youtube.com/watch?v=vrHaAdjC97A
library(lavaan)

# read in the data
# first week
weeka <- read.csv("./../secret_byu_data/confidence/2018_09_26.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# weeka <- weeka[,c(2,12:13,19:28)]
weeka <- weeka[,c(12, 25:28)]

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
weekg <- weekg[,c(12,23:26)]
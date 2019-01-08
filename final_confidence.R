confidence.data <- read.csv("./../secret_byu_data/confidence/2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# there are 49 columns above

confidence.df <- as.data.frame(as.matrix(confidence.data))



library(devtools)
# install_github("hfgolino/EGA")
library(qgraph)
# head(confidence.data[,18:31])



cor_confidence <- cor_auto(confidence.data[,18:31])
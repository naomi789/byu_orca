confidence.data <- read.csv("./../secret_byu_data/confidence/2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# there are 49 columns above
answers.data <- confidence.data[,c(18:33)]
# confidence.df <- as.data.frame(as.matrix(confidence.data))
colnames(answers.data)
answers.data[,8] <- as.numeric(answers.data[,8])

library(devtools)
# install_github("hfgolino/EGA")
library(qgraph)
# head(confidence.data[,18:31])


answers.data <- answers.data[,c(-10,-11,-14)] # takes out binary data, strings
str(answers.data)
cor_confidence <- cor_auto(answers.data, ordinalLevelMax = 8)
# can I set Q4.2 aka [12] to be ordinal as well??
qgraph(cor_confidence, directed=FALSE, layout = "spring")
# INTERPRETATION
# things that make sense: 
# Q2.1	Q2.2	Q2.3 (are all strongly positively correlated)
# Q1.2 Q 1.1 are negatively correlated  
# Q3.3 (major) and Q2.2 (career w/ programming)
# Q4.3 (grades, but reversed) and Q3.2 (GPA)
# Q4.2 and Q2.2 (double check this)



centrality_confidence <- centrality(cor_confidence)
# checkout Betweenness, etc
centrality_confidence$Betweenness

library(EGA)
ega.trump.ggm <- EGA(data.trump, model = "glasso")



# things that surprise me: 
# Q3.2 (GPA) and Q2.1 ('My experience in my CS course(s) THIS PAST SEMESTER leads me to believe I would be successful in future computing activities.")
# what does ^^ that relationship mean




# library(NetworkToolbox)
# scores.trump <- nams(data.trump, A = ega.trump.tmfg$network, comm = ega.trump.tmfg$wc,standardize = TRUE)
# sentiment.trump <- analyzeSentiment(trump.df$text)
# # colnames(sentiment.trump) # look at them
# scores.sentiment.trump <- cbind(scores.trump$Standardized, sentiment.trump[,12:14], trump.df$created)
# scores.sentiment.trump
# # above = QUESTION 13
# 
# library(plotly)
# cor_matrix <- cor_auto(scores.sentiment.trump)
# # cor.terms <- cor_auto(dtm.data)
# a <- list(showticklabels = TRUE, tickangle = -45)
# plot.cor <- plot_ly(x = colnames(cor_matrix), y = colnames(cor_matrix),
#                     z = cor_matrix, type = "heatmap") %>%
#   layout(xaxis = a,  showlegend = FALSE, margin = list(l=100,b=100,r=100,u=100))
# plot.cor
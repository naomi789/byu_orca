confidence.data <- read.csv("./../secret_byu_data/confidence/2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# there are 49 columns above
answers.data <- confidence.data[,18:31]
# confidence.df <- as.data.frame(as.matrix(confidence.data))



library(devtools)
# install_github("hfgolino/EGA")
library(qgraph)
# head(confidence.data[,18:31])



cor_confidence <- cor_auto(confidence.data[,18:31], ordinalLevelMax = 8)
qgraph(cor_confidence, directed=FALSE, layout = "spring")

centrality_confidence <- centrality(cor_confidence)
# checkout Betweenness, etc

library(EGA)
ega.trump.ggm <- EGA(data.trump, model = "glasso")
# 
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
confidence.data <- read.csv("./../secret_byu_data/confidence/2019_01_06_partial.csv", header = TRUE, stringsAsFactors = FALSE,na.strings = "")
# there are 49 columns above
original.answers <- confidence.data[,c(18:33)]
answers.data <- original.answers
# confidence.df <- as.data.frame(as.matrix(confidence.data))
# colnames(answers.data)
answers.data[,8] <- as.numeric(answers.data[,8])

library(devtools)
# install_github("hfgolino/EGA")
library(qgraph)
# head(confidence.data[,18:31])


answers.data <- answers.data[,c(-10,-11,-14)] # takes out binary data, strings
str(answers.data)
cor_confidence <- cor_auto(answers.data, ordinalLevelMax = 8)
# TODO
# can I set Q4.2 aka [12] to be ordinal as well?? and also [13]
# those are classes and grades

qgraph(cor_confidence, directed=FALSE, layout = "spring")
# INTERPRETATION
# things that make sense: 
# Q2.1	Q2.2	Q2.3 (are all strongly positively correlated)
# Q1.2 Q 1.1 are negatively correlated  
# Q3.3 (major) and Q2.2 (career w/ programming)
# Q4.3 (grades, but reversed) and Q3.2 (GPA)
# Q4.2 and Q2.2 (double check this)

# things that surprise me: 
# Q3.2 (GPA) and Q2.1 ('My experience in my CS course(s) THIS PAST SEMESTER leads me to believe I would be successful in future computing activities.")
# what does ^^ that relationship mean

centrality_confidence <- centrality(cor_confidence)

closeness <- centrality_confidence$Closeness
qgraph(cor_confidence, directed=FALSE, layout = "spring", vsize = closeness*500)

betweenness <- centrality_confidence$Betweenness
qgraph(cor_confidence, directed=FALSE, layout = "spring", vsize = betweenness/5)

indegree <- centrality_confidence$InDegree
qgraph(cor_confidence, directed=FALSE, layout = "spring", vsize = indegree*4)

inexpectedinfluence <- centrality_confidence$InExpectedInfluence
qgraph(cor_confidence, directed=FALSE, layout = "spring", vsize = inexpectedinfluence*5)


library(EGA)
colnames(original.answers)
answers.data <- original.answers[,c(-11,-14)] # this time I include gender
ega.confidence.ggm <- EGA(answers.data, model = "glasso")
# TODO (are we SURE that I couldn't include gender previously??)
# libraries:
library(ggplot2) # for frequency
library(wordcloud) # for wordclouds
library(qgraph) # for heatmap
library(plotly) # for heatmap
library(dplyr) # for heatmap
library(tm) # for correlation matrix

# read in data
positive_data <- read.csv("./positive.csv", header = FALSE, stringsAsFactors = FALSE)
# /most_important_change.csv
# /negative.csv
# /positive.csv


corpus <- Corpus(VectorSource(positive_data[,1]))

corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)
dtm <- DocumentTermMatrix(corpus)

dtm.positive <- DocumentTermMatrix(corpus)
dtm.positive <- removeSparseTerms(dtm.positive, .90)
# dtm.positive
dtm.positive.df <- as.data.frame(as.matrix(dtm.positive))

dtm.positive.df <- sort(colSums(dtm.positive.df),decreasing=TRUE) # sorts most commonly occuring words to the top
dtm.positive.df.freq.data <- data.frame(word = names(dtm.positive.df),freq=dtm.positive.df) # shows them as a DF

# see how often the words that are left occur
freq.plot <- ggplot(dtm.positive.df.freq.data, aes(reorder(word, freq), freq)) + geom_col() + 
  xlab(NULL) + coord_flip() + ylab("Frequency")+
  theme(text = element_text(size = 10))
freq.plot


# see if men and women talk about different things

# see what words are correlated with professors' names
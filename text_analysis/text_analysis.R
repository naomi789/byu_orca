# libraries:
library(ggplot2) # for frequency
library(wordcloud) # for wordclouds
library(qgraph) # for heatmap
library(plotly) # for heatmap
library(dplyr) # for heatmap
library(tm) # for correlation matrix

# read in data
positive_data <- read.csv("./text_analysis/positive.csv", header = FALSE, stringsAsFactors = FALSE)
# /most_important_change.csv
# /negative.csv
# /positive.csv
negative_data <- read.csv("./text_analysis/negative.csv", header = FALSE, stringsAsFactors = FALSE)
changes_data <- read.csv("./text_analysis/most_important_change.csv", header = FALSE, stringsAsFactors = FALSE)


#################################
######### POSITIVE DATA ######### 
#################################
corpus <- Corpus(VectorSource(positive_data[,1]))

corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)
dtm.positive <- DocumentTermMatrix(corpus)

dtm.positive <- removeSparseTerms(dtm.positive, .90)
dtm.positive.df <- as.data.frame(as.matrix(dtm.positive))

dtm.positive.df <- sort(colSums(dtm.positive.df),decreasing=TRUE) # sorts most commonly occuring words to the top
head(dtm.positive.df)
dtm.positive.df.freq.data <- data.frame(word = names(dtm.positive.df), freq = dtm.positive.df) # shows them as a DF
dtm.positive.df.freq.data

# see how often the words that are left occur
freq.plot <- ggplot(dtm.positive.df.freq.data, aes(reorder(word, freq), freq)) + geom_col() + 
  xlab(NULL) + coord_flip() + ylab("Frequency")+
  theme(text = element_text(size = 10))
freq.plot
pdf()
plot(freq.plot)
dev.off()


#################################
######### NEGATIVE DATA ######### 
#################################
corpus <- Corpus(VectorSource(negative_data[,1]))

corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)
dtm.negative <- DocumentTermMatrix(corpus)

dtm.negative <- removeSparseTerms(dtm.negative, .90)
dtm.negative.df <- as.data.frame(as.matrix(dtm.negative))

dtm.negative.df <- sort(colSums(dtm.negative.df),decreasing=TRUE) # sorts most commonly occuring words to the top
head(dtm.negative.df)
dtm.negative.df.freq.data <- data.frame(word = names(dtm.negative.df), freq = dtm.negative.df) # shows them as a DF
dtm.negative.df.freq.data

# see how often the words that are left occur
freq.plot <- ggplot(dtm.negative.df.freq.data, aes(reorder(word, freq), freq)) + geom_col() + 
  xlab(NULL) + coord_flip() + ylab("Frequency")+
  theme(text = element_text(size = 10))
freq.plot

pdf()
plot(freq.plot)
dev.off()

#################################
########## DESIRES DATA ######### 
#################################



corpus <- Corpus(VectorSource(changes_data[,1]))

corpus <- tm_map(corpus, tolower)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("english"))
corpus <- tm_map(corpus, stemDocument)
dtm.changes <- DocumentTermMatrix(corpus)

dtm.changes <- removeSparseTerms(dtm.changes, .90)
dtm.changes.df <- as.data.frame(as.matrix(dtm.changes))

dtm.changes.df <- sort(colSums(dtm.changes.df),decreasing=TRUE) # sorts most commonly occuring words to the top
head(dtm.changes.df)
dtm.changes.df.freq.data <- data.frame(word = names(dtm.changes.df), freq = dtm.changes.df) # shows them as a DF
dtm.changes.df.freq.data

# see how often the words that are left occur
freq.plot <- ggplot(dtm.changes.df.freq.data, aes(reorder(word, freq), freq)) + geom_col() + 
  xlab(NULL) + coord_flip() + ylab("Frequency")+
  theme(text = element_text(size = 10))
freq.plot

pdf()
plot(freq.plot)
dev.off()


# see if men and women talk about different things

# see what words are correlated with professors' names

# also, how do I un-commit something that I shouldn't've committed??
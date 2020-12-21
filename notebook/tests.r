# Imports
library(PMCMRplus)
library(ggplot2)
library(reshape2)
library(nortest)

setwd("/Users/gianlucascoccia/Desktop/MSR2021/analysis/notebook")

# Load data
so = read.csv("../data/processed/so_test_data.csv", header = TRUE)
gh = read.csv("../data/processed/gh_test_data.csv", header = TRUE)

# Extract relevant columns from dataframes 
so_data = matrix(c(so$time_topic_1, so$time_topic_2, so$time_topic_3, so$time_topic_4,
          so$time_topic_5, so$time_topic_6, so$time_topic_8,
          so$time_topic_9, so$time_topic_10, so$time_topic_11, so$time_topic_12,
          so$time_topic_13, so$time_topic_14), ncol=13, 
          dimnames = list(1 : 3806, c("Platform\nIntegration", "UI", "Testing", "Dependencies", "Build\n& Releases", 
                                      "Client-Server", "Error", "Debugging", "Architecture",
                                      "File\nManipulation", "Databases", "Page\nContents", "IPC")))

so_data_plot <- so_data[so_data[, 1] > 0, ] # drop rows with 0 alive time

gh_data = matrix(c(gh$time_topic_1, gh$time_topic_2, gh$time_topic_3, gh$time_topic_4,
                   gh$time_topic_5, gh$time_topic_6, gh$time_topic_7,
                   gh$time_topic_9, gh$time_topic_10, gh$time_topic_11, gh$time_topic_12,
                   gh$time_topic_13, gh$time_topic_14), ncol=12, 
                   dimnames = list(1 : 71611, c("Build\n& Releases", "Platform\nIntegration", "UI", "Messaging", "Account", 
                                                "File\nManipulation", "Feature\nrequest", "Text\nManipulation", "Testing",
                                                "Error", "Cryptos", "Input")))

gh_data_plot <- gh_data[gh_data[, 1] > 0, ] # drop rows with 0 alive time

# Descriptive statistics
summary(so_data / 3600)
summary(gh_data / 3600)

# Anderson-Darling test (Normality test)
ad.test(so_data)
ad.test(gh_data)

# QQ Plot
for(i in 1:13){
  qqnorm(so_data[, i], pch = 1, frame = FALSE)
  qqline(so_data[, i], col = "steelblue", lwd = 2)
}

for(i in 1:12){
  qqnorm(gh_data[, i], pch = 1, frame = FALSE)
  qqline(gh_data[, i], col = "steelblue", lwd = 2)
}


# Friedman test ( non-parametric & independent ANOVA)
friedmanTest(so_data) 
friedmanTest(gh_data)

# Nemenyi Post-hoc tests to compare all the pairs  
frdAllPairsNemenyiTest(so_data, alternative='greater')
frdAllPairsNemenyiTest(gh_data, alternative='greater')

# Single Pairs comparisons with Nemenyi
for(i in 1:13) {
  test_data = so_data[,c(i, 1:i-1, i:ncol(so_data))]
  print(frdManyOneNemenyiTest(test_data, alternative='greater'))
  }

for(i in 1:12) {
  test_data = gh_data[,c(i, 1:i-1, i:ncol(gh_data))]
  print(frdManyOneNemenyiTest(test_data, alternative='greater'))
}

# Plot data
boxplot(so_data_plot / (60 * 60) ,log = 'y', las=2)
par(mar=c(18,4,1,1)+.1)

boxplot(gh_data_plot / (60 * 60) ,log = 'y', las=2)
par(mar=c(18,4,1,1)+.1)

#so_long <- melt(so_data)
#colnames(so_long) <- c("ID","Topic","Value") 

#ggplot(so_long, aes(x=factor(Topic),y=Value/(60 * 60 * 24),fill=factor(Topic)))+
#  geom_boxplot() + scale_y_continuous(trans='log10')
  


setwd("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")

winners<-read.csv("results_winner.csv",header=T)

#smaple 10 ids
sample_id<-sample(unique(winners$keywords),10)
sample<-winners[winners$keywords %in% sample_id, ]
write.csv(sample,"winner_sample.csv")


setwd("C:/Users/wooki/Documents/GitHub/pythoncourse2018/youtube")

winners_sample<-read.csv("winner_sample.csv",header=T)

#select three for each id
winners_sample$Chosen <- 0
winners_sample[-tapply(-seq_along(winners_sample$keywords),winners_sample$keywords, sample, size=1),]$Chosen <- 1
winners_sample_select<-subset(winners_sample,winners_sample$Chosen==1)
write.csv(winners_sample_select,"winner_sample_sample.csv")

winners_sample_select<-subset(winners_sample,winners_sample$good=="x")
write.csv(winners_sample_select,"winner_sample_sample.csv")

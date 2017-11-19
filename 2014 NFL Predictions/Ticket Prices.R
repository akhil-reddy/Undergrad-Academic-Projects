install.packages("neuralnet")
library(stats)
avg2014<-read.csv("2014-average-ticket-price.csv")
navg<-read.csv("national-average.csv")
categories<-read.csv("team-picking-categories.csv")
View(avg2014)
View(categories)
View(navg)
#first model
categories$ticketPrice=0
ticketPrice=navg$Avg.TP...
ref1<-as.data.frame(categories)
ref1<-ref1[,1:ncol(ref1)-1]
View(ref1)
cbind(categories,ticketPrice)
View(categories)
categories$TEAM=as.character(categories$TEAM)
navg$Genre=as.character(navg$Genre)

for(i in 1:nrow(categories)){
  if(categories[i,1]=="Los Angeles Rams"){
    categories[i,1]="St Louis Rams"
  }
}
for(i in 1:nrow(categories)){
  for(j in 1:nrow(navg)){
    if(categories[i,1]==navg[j,1])
    {
      categories[i,18]=(navg[j,2])
    }
  }
}
install.packages("mlbench")
library(mlbench)
#model 1, least square linear regression
colnames(categories)
model1<-lm(ticketPrice~BMK+UNI+CCH+STX+SMK+AFF+SLP+NYP+FRL+BNG+TRD+BWG+FUT+PLA+OWN+BEH,data=categories)
model1
summary(model1)
predict1<-predict(model1)
mean((predict1-categories$ticketPrice)^2)
#2-fold cross validation
nrow(categories)
x<-sample(1:nrow(categories),nrow(categories)/2)
x
y<-c()
l<-1
for(i in 1:nrow(categories)){
  if(i %in% x){}
  else{y[l]<-i
  l<-l+1
  }
}
x
y
S1<-categories[x,]
S2<-categories[y,]
#train S1,test S2
#train S2,test S1

model3<-lm(ticketPrice~BMK+UNI+CCH+STX+SMK+AFF+SLP+NYP+FRL+BNG+TRD+BWG+FUT+PLA+OWN+BEH,data=S1)
predict3<-predict(model3)
model3$coefficients
MSE<-0
mean((predict3-S2$ticketPrice)^2)

model4<-lm(ticketPrice~BMK+UNI+CCH+STX+SMK+AFF+SLP+NYP+FRL+BNG+TRD+BWG+FUT+PLA+OWN+BEH,data=S2)
predict4<-predict(model4)
mean((predict4-S1$ticketPrice)^2)


#model 2, neural network model
library(nnet)
model2<-nnet(ticketPrice~BMK+UNI+CCH+STX+SMK+AFF+SLP+NYP+FRL+BNG+TRD+BWG+FUT+PLA+OWN+BEH,data=categories,size=1)
summary(model2)
predict2<-predict(model2)
mean((predict2-categories$ticketPrice)^2)
#after pca
S<-prcomp(x=categories[,2:ncol(categories)],center = TRUE,scale. = TRUE)
summary(S)
ref1<-S$x[,1:10]
View(ref1)
ref1<-cbind(ref1,ticketPrice)
ref1<-as.data.frame(ref1)
M<-ticketPrice~PC1+PC2+PC3+PC4+PC5+PC6+PC8+PC9+PC10
J<-lm(M,data=ref1)
J$coefficients
#linear regression
J<-nnet(M,data=ref1,size=1) #neural network

predict5<-predict(J)
mean((predict5-ref1$ticketPrice)^2)
#The linear regression gives a lower MSE value
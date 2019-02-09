library(ggplot2)
library(factoextra)
library(cluster)
library(fpc)
library(apcluster)


data=read.csv('results/embedding.csv')
data=data[,-1]
set.seed(123)
km_res = kmeans(data, 4, nstart = 25)
km_clus = km_res[["cluster"]]
km_clus_data = cbind(data, km_clus)
# write csv
#write.csv(km_clus_data,"C:/Users/24837/km_data.csv")

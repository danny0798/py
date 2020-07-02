# -*- coding: utf-8 -*- 
"""Excercise 9.4"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import random

data = pd.read_csv(filepath_or_buffer = './data.csv', sep = ',')[["密度","含糖率"]].values

########################################## K-means ####################################### 
#k = int(sys.argv[1])
k = 4
#Randomly choose k samples from data as mean vectors
mean_vectors = random.sample(data,k)

def dist(p1,p2):
    return np.sqrt(sum((p1-p2)*(p1-p2)))
while True:
 #   print（mean_vectors）
    print(mean_vectors)
    clusters = map ((lambda x:[x]), mean_vectors) 
    for sample in data:
        distances = map((lambda m: dist(sample,m)), mean_vectors) 
        min_index = distances.index(min(distances))
        clusters[min_index].append(sample)
    new_mean_vectors = []
    for c,v in zip(clusters,mean_vectors):
        new_mean_vector = sum(c)/len(c)
        #If the difference betweenthe new mean vector and the old mean vector is less than 0.0001
        #then do not updata the mean vector
        if all(np.divide((new_mean_vector-v),v) < np.array([0.0001,0.0001]) ):
            new_mean_vectors.append(v)   
        else:
            new_mean_vectors.append(new_mean_vector)   
    if np.array_equal(mean_vectors,new_mean_vectors):
        break
    else:
        mean_vectors = new_mean_vectors 

#Show the clustering result
total_colors = ['r','y','g','b','c','m','k']
colors = random.sample(total_colors,k)
for cluster,color in zip(clusters,colors):
    density = map(lambda arr:arr[0],cluster)
    sugar_content = map(lambda arr:arr[1],cluster)
    plt.scatter(density,sugar_content,c = color)
plt.show()
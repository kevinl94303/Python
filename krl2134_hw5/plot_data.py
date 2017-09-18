'''
Name; Kevin Li
UNI: krl2134
plots data from create_data using pyplot
'''

import create_data
import matplotlib.pyplot as plt

def plot_data(data):
    #calls plots based on data and axes
    plot(data,0,1,1)
    plot(data,0,2,2)
    plot(data,0,3,3)
    plot(data,1,2,4)
    plot(data,1,3,5)
    plot(data,2,3,6)
    
    return None
    
def plot(data,x,y,f):
    #plots value in column x vs value in column y
    plt.figure(f)
    
    labels = ["Sepal Width","Sepal Length","Petal Width","Petal Length"]
    for line in data:
        if line[len(line) - 1] == "Iris-setosa":
            plt.scatter(line[x],line[y],c = "red")
        if line[len(line) - 1] == "Iris-versicolor":
            plt.scatter(line[x],line[y],c = "blue")
        if line[len(line) - 1] == "Iris-virginica":
            plt.scatter(line[x],line[y],c = "yellow")
        
    plt.title(labels[x] + " vs " + labels[y])
    plt.xlabel(labels[x])
    plt.ylabel(labels[y])


plot_data(create_data.create_data("iris"))
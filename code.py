from os import stat
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["claps"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean    

def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["claps"],show_hist=False)  
    fig.show()

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

    mean=statistics.mean(mean_list)
    print("sampling mean:",mean)
setup()  

population_mean=statistics.mean(data)
print("population mean:",population_mean)

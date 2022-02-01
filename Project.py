import pandas as pd
import random
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("Project.csv")
data = df["claps"].tolist()




def SampleCalculator():
    samples_100 = []

    for x in range(1, 101):
        r = random.randint(0, len(data)-1)
        Value = data[r]
        samples_100.append(Value)
    
    average1 = statistics.mean(samples_100)
    return average1


All_Averages = []
for x in range(1, 101):
    recieve = SampleCalculator()
    All_Averages.append(recieve)


Sampling_mean = statistics.mean(All_Averages)
normal_mean = statistics.mean(data)
Mean = statistics.mean(data)
standard_deviation = statistics.stdev(All_Averages)
print("Sampling mean"+str(Sampling_mean))
print("Normal mean"+str(normal_mean))
print("Mean"+str(Mean))
print("Standard_deviation"+str(standard_deviation))

z_score = Sampling_mean-Mean/standard_deviation

graph = ff.create_distplot([data],["claps"],show_hist=True)
graph.show()
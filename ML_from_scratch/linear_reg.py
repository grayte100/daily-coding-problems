import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read CSV file

file = pd.read_csv(r"C:\Users\USER\Python Machine Learning\ML_from_scratch\weather_rain.csv")
print(file.to_string)
df = pd.DataFrame(file)
data = np.array(file)

#Separate features and targets
X = [data[:-2] for row in data]
y = [data[-2:] for row in data]

#Perform feature scaling
#X_normalized = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

#Extract x and y values as arrays
#x = df['MinTemp','MaxTemp','Rainfall','Wind Gust Speed','Wind Speed 9am',
       #'Wind Speed 3pm','Humidity 9am','Humidity 3pm','Pressure 9am','Pressure 3pm'
       #'Temp 9am','Temp 3pm'].values
#y = df['Forecasted Weather'].values

epochs = 0

# create the scatter plot
plt.scatter(X, y, color='red')

# set the x and y limits
plt.Xlim(0, 5000)
plt.ylim(0, 100)

# set the x and y labels and the plot title
plt.Xlabel("Vectorized features")
plt.ylabel("Rain Today")
plt.title("Rain tomorrow")

# hide the legend
plt.legend().remove()

# show the plot
plt.show()

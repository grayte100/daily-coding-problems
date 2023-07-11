import numpy as np
from collections import Counter

def euclidean_distance(x1,x2):
    distance = np.sqrt(np.sum((x1-x2)**2))
    return distance

class KNN :
    def __init__ (self, k = None): 
        self.k = k
        
        
    def fit(self, x, y):
        
        self.X_train = x
        self.Y_train = y
    
    def predict(self, X ):
        predictions = [self._predict(x) for x in X]
        return predictions
    
    def _predict(self, x):
        #calculate the euclidean distance
        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        
        #get the closest k
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        #get majority vote
        most_common = Counter(k_nearest_labels).most_common()
        return most_common
import os
import pandas as pd
import requests
from tqdm import tqdm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Bộ dữ liệu BMI và mức đường huyết
bmi = np.array([18, 21, 22, 25, 27, 29, 30, 31, 33, 35, 38, 40])
…plt.xlabel('BMI')
plt.ylabel('Glucose Level')
plt.title('Diabetes Classification with KNN')
plt.colorbar(label='Diabetes (1 = Yes, 0 = No)')
plt.show()

# Chuẩn bị dữ liệu
X = df[['BMI', 'Glucose']].values
y = df['Diabetes'].values

import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 0: Set seed for reproducibility
random.seed(7)

# Step 1: Generate simulated sensor readings
temperature = [round(random.uniform(18, 35), 2) for i in range(5)]  # in °C
humidity = [round(random.uniform(35, 85), 2) for i in range(5)]     # in %

# Step 2: Create a 2D matrix for Comfort Index
# Formula: CI = T - 0.4 * (H - 50)
comfort_index = []
#########################
for H in humidity:
    row = []
    for T in temperature:
        CI = round(T - 0.4 * (H - 50), 2)
        row.append(CI)
    comfort_index.append(row)
#########################

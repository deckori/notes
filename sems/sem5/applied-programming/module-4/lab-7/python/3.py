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

# Step 3: Convert to DataFrame for display
df = pd.DataFrame(comfort_index,
                  index=[str(h) + "%" for h in humidity],
                  columns=[str(t) + "°C" for t in temperature])

print("\nComfort Index (CI) Matrix:\n")
print(df)

# Step 4: Visualize the Comfort Index as a Heatmap
plt.figure(figsize=(7,5))
sns.heatmap(df, annot=True, cmap="coolwarm",
            cbar_kws={'label': 'Comfort Index'})

plt.title("Comfort Index Heatmap (Temperature vs Humidity)")
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.tight_layout()
plt.show()

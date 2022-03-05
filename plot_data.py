import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Step: Loading dataset
df = pd.read_csv('resources/data.csv', sep=',')
# for i, data in df.iterrows():
#     print(data['device_local_date'])
print(len(np.unique(df['device_hash_id'])))
# fig, ax = plt.subplots()
# ax.scatter(df['device_local_date'], df['device_hash_id'])
# ax.legend()
# ax.grid(True)
# plt.show()
# Step 2: plot data
# np.random.seed(19680801)
#
#
# fig, ax = plt.subplots()
# for color in ['tab:blue', 'tab:orange', 'tab:green']:
#     n = 750
#     x, y = np.random.rand(2, n)
#     scale = 200.0 * np.random.rand(n)
#     ax.scatter(x, y, c=color, s=scale, label=color,
#                alpha=0.3, edgecolors='none')
#
# ax.legend()
# ax.grid(True)
#
# plt.show()
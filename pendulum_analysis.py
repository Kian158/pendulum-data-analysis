# # Simple Pendulum Experiment Analysis

# ## Import required libraries

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# ## Load CSV data

t1_df = pd.read_csv('./data/Table_1_FA.csv')
t2_df = pd.read_csv('./data/Table_2_FA.csv')

# ## Rename columns for clarity

column_name = ['Length', 'R1', 'R2', 'R3', 'R4', 'R5']
t1_df.columns = [column_name]
t2_df.columns = [column_name]

# ## Remove the first row (assumed to be invalid data)

t1_df = t1_df[1:]
t2_df = t2_df[1:]

# ## Convert Length column to float

t1_df['Length'] = t1_df['Length'].astype(float)

# ## Initialize control variables

r = 0
r2 = 0

# ## Drop 'T2' column if already exists (based on control variable)

if r != 0:
    t1_df = t1_df.drop('T2', axis=1)

# ## Calculate average times and error bars for Experiment 1

i = 0
j = 0
avgs = np.zeros(10)
while i < 10:
    row = t1_df.iloc[i]
    sumRow = row[1:].sum()
    avgs[i] = sumRow * 0.2  # Each time averaged over 5 readings, scaled
    i += 1

errors = np.zeros(10)
while j < 10:
    row1 = t1_df.iloc[j]
    relevantBit = row1[1:]
    dif = max(relevantBit) - min(relevantBit)
    errors[j] = dif
    j += 1

# ## Compute T² values

T2 = (avgs / 10)**2

# ## Add T² column to DataFrame

t1_df['T2'] = T2.astype(float)

# ## Convert Length to float again (redundant but safe)

t1_df['Length'] = t1_df['Length'].astype(float)

# ## Define linear model for curve fitting

def straight_line(x, m, c):
    return m * x + c  

# ## Prepare data for curve fitting

x_data = t1_df['Length'].values.flatten()
y_data = t1_df['T2'].values.flatten()

# ## Perform linear regression

popt, pcov = curve_fit(straight_line, x_data, y_data)
slope, intercept = popt
err_slope = np.sqrt(float(pcov[0][0]))
err_intercept = np.sqrt(float(pcov[1][1])) 

# ## Plot data with error bars and best-fit line (Experiment 1)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
ax.errorbar(t1_df['Length'], T2 , yerr=errors*0.1, color='k', marker='o', ls='none', capsize=5, capthick=2)
ax.plot(t1_df['Length'], straight_line(x_data, slope, intercept), color='hotpink', ls='--', label='Line of Best Fit')
ax.set_xlabel('Length of Pendulum (m)')
ax.set_ylabel('Time Period Squared (s$^2$)')
plt.legend(loc='upper left', fontsize=12)
plt.title("Graph of length against time period squared for a simple pendulum.")
ax.set_xticks([0] + list(ax.get_xticks()))  
ax.set_yticks([0] + list(ax.get_yticks()))
plt.show()

# ## Calculate g and its uncertainty from the slope

g = (4 * np.pi**2) / slope
err_g = (err_slope / slope) * g
r += 1

print('The value of g, calculated from the gradient, is', g, '+-', err_g, 'ms^-2')

# ----------------------------------------------------------
# ## Repeat the same process for Experiment 2
# ----------------------------------------------------------

if r2 != 0:
    t2_df = t2_df.drop('T2', axis=1)

i2 = 0
j2 = 0
avgs2 = np.zeros(10)
while i2 < 10:
    row2 = t2_df.iloc[i2]
    sumRow2 = row2[1:].sum()
    avgs2[i2] = sumRow2 * 0.2
    i2 += 1

errors2 = np.zeros(10)
while j2 < 10:
    row2 = t2_df.iloc[j2]
    relevantBit2 = row2[1:]
    dif2 = max(relevantBit2) - min(relevantBit2)
    errors2[j2] = dif2
    j2 += 1

T22 = (avgs2 / 10)**2
t2_df['T2'] = T22.astype(float)
t2_df['Length'] = t2_df['Length'].astype(float)

def straight_line2(xi, mi, ci):
    return mi * xi + ci  

x_data2 = t2_df['Length'].values.flatten()
y_data2 = t2_df['T2'].values.flatten()

popt2, pcov2 = curve_fit(straight_line2, x_data2, y_data2)
slope2, intercept2 = popt2
err_slope2 = np.sqrt(float(pcov2[0][0]))
err_intercept2 = np.sqrt(float(pcov2[1][1])) 

fig2 = plt.figure(figsize=(10,6))
ax2 = fig2.add_subplot(1,1,1)
ax2.errorbar(t2_df['Length'], T22 , yerr=errors2*0.1, color='k', marker='o', ls='none', capsize=5, capthick=2)
ax2.plot(t2_df['Length'], straight_line2(x_data2, slope2, intercept2), color='red', ls='--', label='Line of Best Fit')
ax2.set_xlabel('Length of Pendulum (m)')
ax2.set_ylabel('Time Period Squared (s$^2$)')
plt.legend(loc='upper left', fontsize=12)
plt.title("Second graph of length against time period squared for a simple pendulum.")
ax2.set_xticks([0] + list(ax2.get_xticks()))  
ax2.set_yticks([0] + list(ax2.get_yticks()))
plt.show()

g2 = (4 * np.pi**2) / slope2
err_g2 = (err_slope2 / slope2) * g2
r2 += 1

print('The value of g, calculated from the gradient, is', g2, '+-', err_g2, 'ms^-2')

# ## Round off values for presentation

g = round(g, 3)
g2 = round(g2, 3)
err_g = round(err_g, 3)
err_g2 = round(err_g2, 3)

# ## Present final results in a summary table

data = {
    "Calculated g": [g, g2],
    "Uncertainty": [err_g, err_g2],
}

df = pd.DataFrame(data)
df = df.rename(index={0: 'Experiment 1', 1: 'Experiment 2'})

print('All values in meters per second squared')
df

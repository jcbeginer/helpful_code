#this code is used for wireshark pcap -> csv file. 
#and handling that csv file to draw figure of TCP throughput!

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def throughput(time, fil_df):
    # This line will get all rows where 'Time' is between 'time' and 'time-1'
    filtered_time_df = fil_df[(fil_df['Time'] > time-1) & (fil_df['Time'] <= time)]
    # This line will sum the 'Length' of these rows
    return filtered_time_df['Length'].sum()

# Load the data
df = pd.read_csv('1-1.csv')

# Filter the data for UL
filtered_df1 = df[(df['Destination'] == '54.180.119.186')]
filtered_df2 = df[(df['Source'] == '192.168.239.17') & (df['Destination'] == '54.180.119.186')]
filtered_df3 = df[(df['Source'] == '192.168.96.147') & (df['Destination'] == '54.180.119.186')]

# Filter the data for DL
filtered_df4 = df[(df['Source'] == '54.180.119.186')]
filtered_df5 = df[(df['Destination'] == '192.168.239.17') & (df['Source'] == '54.180.119.186')]
filtered_df6 = df[(df['Destination'] == '192.168.96.147') & (df['Source'] == '54.180.119.186')]

# Generate list of times and throughputs
times = np.arange(1, np.max(df['Time']) + 1) # adjust as needed

# For each filtered_df, calculate throughputs and plot
for i, (filtered_df, label, color) in enumerate(zip([filtered_df1, filtered_df2, filtered_df3, filtered_df4, filtered_df5, filtered_df6], 
                                     ['MPTCP (UL)', '5G KT (UL)', '5G LG (UL)', 'MPTCP (DL)', '5G KT (DL)', '5G LG (DL)'],
                                     ['red', 'orange', 'yellow', 'blue', 'green', 'skyblue'])):
    throughputs = [throughput(time, filtered_df) for time in times]
    if i in [0, 5]: # index 0 for df1 and 3 for df4
        plt.plot(times, throughputs, label=label, color=color, lw=2) # set linewidth to 2
    else:
        plt.plot(times, throughputs, label=label, color=color, lw=1)

# Set x-axis and y-axis labels
plt.xlabel('Time [s]')
plt.ylabel('Throughput [bytes/s]')

# Show the legend
plt.legend()

# Show the plot
plt.show()

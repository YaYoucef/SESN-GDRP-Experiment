import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/latency_logs.csv')

for op in df['operation'].unique():
    g = df[df['operation'] == op].groupby('requests')['latency'].mean()
    plt.figure()
    g.plot(marker='o')
    plt.xlabel('Requests')
    plt.ylabel('Latency (s)')
    plt.title(f'{op} Performance')
    plt.grid(True)
    plt.savefig(f'results/{op}_latency.png', dpi=300)
    plt.close()
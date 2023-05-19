import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")
df.columns = ["Name", "% Tokens Reduced", "LogiQA Accuracy"]
df["$ Saved Per $100"] = df["% Tokens Reduced"] * 100
df = df.round(2)

df = df[df.Name.str.contains('Entropy_Optim')]
cost = df["$ Saved Per $100"].values
accuracy = df["LogiQA Accuracy"].values

plt.figure(dpi=300)

plt.plot(cost, accuracy, 'k-')
plt.plot(cost, accuracy, 'r^')
plt.xlabel('Savings: \$100 -> \$')
plt.ylabel('OpenAI Eval LogiQA Accuracy', fontweight='bold', fontsize=10)
plt.title('Accuracy vs. Cost Tradeoff for `EntropyOptim`', fontweight='bold', fontsize=10)

labels = [
    "p=0.05",
    "p=0.10",
    "p=0.25",
    "p=0.50",
]
# Plotting
for i in range(cost.shape[0]):
    plt.text(cost[i], accuracy[i], labels[i], fontweight='bold', fontsize=10)


plt.grid(True)
save_path = 'artifacts/tradeoff.png'
plt.savefig(save_path, bbox_inches="tight")
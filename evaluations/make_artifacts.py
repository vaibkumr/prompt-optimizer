import os
import utils
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd


df = pd.read_csv("results.csv")

df.columns = ["Name", "% Tokens Reduced", "LogiQA Accuracy"]
df["USD Saved Per $100"] = df["% Tokens Reduced"] * 100
df = df.round(2)
utils.dataframe_to_markdown(df, os.path.join("artifacts", f"table.md"))


for col in df.columns[1:]:

    # Plotting
    x = df.Name

    fig = go.Figure(
        data=[go.Bar(x=x, y=df[col], text=df[col], textposition="auto", name=col)]
    )

    fig.update_layout(
        title=f"Comparison for {col}",
        yaxis=dict(title=col),
        xaxis_tickangle=-45,
        barmode="group",
    )

    pio.write_image(
        fig, os.path.join("artifacts", f"{col}_graph.png".replace("\\", "")), scale=2
    )

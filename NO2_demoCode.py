import pandas as pd
import matplotlib.pyplot as plt

fp = r"yourfile\NO2_demo_dataset260323.csv"
df = pd.read_csv(fp)
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
cols = ["NO2", "sarimax", "lstm", "prophet", "arima_garch"]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")
df[cols] = df[cols].interpolate(method="linear")\
                   .bfill()\
                   .ffill()
df_smooth = df.copy()
df_smooth[cols] = df_smooth[cols].rolling(window=30, min_periods=1).mean()

plt.figure(figsize=(15,6))
plt.plot(df_smooth["date"], df_smooth["NO2"], label="Observed", linewidth=2.8, color="#8c2d1a")
plt.plot(df_smooth["date"], df_smooth["sarimax"], label="SARIMAX", linewidth=2.2, color="#d8b365")
plt.plot(df_smooth["date"], df_smooth["arima_garch"], label="ARIMA-GARCH", linewidth=2.2, color="#7f8f6b")
plt.plot(df_smooth["date"], df_smooth["prophet"], label="Prophet", linewidth=2.2, color="#5b7c9d")
plt.plot(df_smooth["date"], df_smooth["lstm"], label="LSTM", linewidth=2.2, color="#9d95a6")

plt.xlabel("Date", fontsize=14)
plt.ylabel("NO₂ Concentration (μg/m³)", fontsize=14)
plt.title("30-Day Smoothed NO₂ Prediction – Tai Po (2017–2019)", fontsize=16)
plt.legend(loc="upper left")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

out_fig = r"yourfile\example_plot.png"
plt.savefig(out_fig, dpi=300, bbox_inches="tight")

plt.show()

print("Fig save", out_fig)
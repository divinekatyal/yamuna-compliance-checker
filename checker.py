import pandas as pd
import matplotlib.pyplot as plt
import os

LIMIT = 3.0  

os.makedirs("output", exist_ok=True)

def load_and_check(filepath):
    
    df = pd.read_csv(filepath)
    
    
    df["avg_bod"] = (df["min_bod"] + df["max_bod"]) / 2.0
    
    
    df["status"] = df["avg_bod"].apply(lambda x: "FAIL" if x > LIMIT else "PASS")
    
    
    df["exceedance"] = (df["avg_bod"] / LIMIT).round(1)
    
    
    failed_stations = df[df["status"] == "FAIL"].sort_values(by="exceedance", ascending=False)
    failed_stations.to_csv("output/compliance_log.csv", index=False)
    print("Saved failed stations to compliance_log.csv")
    
    return df

def show_report(df):
    print("\n--- YAMUNA RIVER BOD REPORT ---")
    
    for year in [2024, 2025]:
        print(f"\nYear: {year}")
        data = df[df["year"] == year]
        
        for idx, row in data.iterrows():
            if row['status'] == "FAIL":
                print(f"{row['station']:20s} | {row['avg_bod']:>4.1f} mg/L | FAIL ({row['exceedance']}x limit)")
            else:
                print(f"{row['station']:20s} | {row['avg_bod']:>4.1f} mg/L | PASS")

def plot_trend(df):
    
    pivot_df = df.pivot(index="station", columns="year", values="avg_bod")
    
    
    order = df["station"].unique()
    pivot_df = pivot_df.reindex(order) 
    
    
    ax = pivot_df.plot(kind="bar", figsize=(10, 6), color=["#1f77b4", "#d62728"])
    
    
    plt.axhline(y=LIMIT, color="red", linestyle="--", linewidth=2, label=f"Safe Limit ({LIMIT} mg/L)")
    
    plt.title("Yamuna River BOD: 2024 vs 2025")
    plt.xlabel("Stations (Upstream to Downstream)")
    plt.ylabel("Average BOD (mg/L)")
    plt.xticks(rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    
    
    plt.savefig("output/yamuna_trend.png", dpi=300)
    print("Saved chart to yamuna_trend.png\n")
    plt.show()

if __name__ == "__main__":
    df = load_and_check("data/yamuna_bod.csv")
    show_report(df)
    plot_trend(df)
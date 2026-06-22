import pandas as pd
import requests
import os

# Create folder if not exists
os.makedirs("data/raw", exist_ok=True)

# ==================================================
# HDFC TOP 100 DIRECT
# ==================================================

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

print("\nHDFC Top 100 Direct")
print(data.keys())

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv(
    "data/raw/hdfc_top100_live_nav.csv",
    index=False
)

print("Saved: hdfc_top100_live_nav.csv")

# ==================================================
# OTHER IMPORTANT SCHEMES
# ==================================================

schemes = {
    119551: "sbi_bluechip_nav.csv",
    120503: "icici_bluechip_nav.csv",
    118632: "nippon_largecap_nav.csv",
    119092: "axis_bluechip_nav.csv",
    120841: "kotak_bluechip_nav.csv"
}

for code, filename in schemes.items():

    print(f"\nFetching AMFI Code: {code}")

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            f"data/raw/{filename}",
            index=False
        )

        print(f"Saved: {filename}")

    else:

        print(
            f"Failed for {code}. "
            f"Status Code: {response.status_code}"
        )

print("\nAll NAV files downloaded successfully.")
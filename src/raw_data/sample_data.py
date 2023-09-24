import pandas as pd

def sample_data_raw():
    print("Pulling sample data from DataRobot"
    )
    data_path = "https://docs.datarobot.com/en/docs/api/guide/common-case/DR_Demo_Sales_Multiseries_training.csv"
    df = pd.read_csv(data_path,
                     infer_datetime_format=True,
                     parse_dates=['Date'],
                     engine='c'
                     )
    return df

if __name__ == "__main__":
    df = sample_data_raw()
    # save to csv in data/raw
    df.to_csv("data/raw/sample_data_raw.csv", index=False)
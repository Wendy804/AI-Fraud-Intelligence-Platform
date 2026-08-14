import pandas as pd


DATA_PATH = "data/cs-training.csv"



def load_data(
    path=DATA_PATH
):

    """
    Load credit risk dataset
    """


    df = pd.read_csv(
        path
    )


    # remove csv index column

    if "Unnamed: 0" in df.columns:

        df = df.drop(
            columns=[
                "Unnamed: 0"
            ]
        )


    return df




def data_summary(df):

    """
    Basic data quality report
    """


    print("=" * 50)


    print("Dataset Shape:")
    print(df.shape)



    print("\nColumns:")
    print(
        df.columns.tolist()
    )



    print("\nMissing Values:")
    print(
        df.isnull().sum()
    )



    print("\nTarget Distribution:")


    if "SeriousDlqin2yrs" in df.columns:


        print(
            df["SeriousDlqin2yrs"]
            .value_counts()
        )



        print("\nDefault Rate:")


        rate = (
            df["SeriousDlqin2yrs"]
            .mean()
        )


        print(
            f"{rate:.2%}"
        )



    print("=" * 50)




if __name__ == "__main__":


    data = load_data()


    data_summary(data)
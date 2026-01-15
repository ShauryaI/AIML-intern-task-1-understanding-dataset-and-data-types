import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('Titanic-Dataset.csv')
df = pd.read_csv('Student_performance_data _.csv')

def main():
    # to print entire DataFrame
    print("Entire Dataframe: ")
    print(df.to_string())
    #print(pd.options.display.max_rows) # the default value is 60
    print("Top 10 Rows: ")
    print(df.head(10))
    print("Rows from bottom: default 5 ")
    print(df.tail())
    print("Information about dataset like row/column count, datatype, non-null count: ")
    print(df.info())
    print("Statistical summary for numeric columns: ")
    print(df.describe())
    print("Statistical summary for all columns: ")
    print(df.describe(include='all'))
    print("Statistical summary for categorial columns: ")
    # there is no categorial column in Student performance dataset
    # print(df.describe(include='object'))
    print("Check for duplicates")
    print(df.duplicated())
    print("Relationship between each column")
    print(df.corr())

    df.plot(kind='hist')

    plt.show()

if __name__ == '__main__':
    main()

import os
import sys
import pandas as pd


def main():

    # Reading csv files
    _cwd = r'C:\Users\chenl\OneDrive\Desktop\Data-Engineer-Tech-Challenge-master'
    for _file in os.listdir(_cwd):
        if _file.endswith('.csv'):
            df = pd.read_csv(fr'{_cwd}\{_file}')
            # Removing common prefixes and suffixes
            df['name'] = df['name'].replace(['Mr\. ', 'Mrs\. ', 'Ms\. ', ' MD', ' DDS', ' DVM', ' PhD'], '', regex=True)
            # Splitting field: name based on first space
            df[['first_name', 'last_name']] = df.name.str.split(' ', 1, expand=True)
            # Removing leading and trailing zeros in field: price
            df['price'] = [s.strip("0") for s in df['price'].astype(str)]
            # Dropping rows which do not have a value in field: name
            df.dropna(subset = ['name'], inplace=True)
            # Creating new column with field: price strictly greater than 100
            price_100 = []
            for _row in df['price']:
                if float(_row) > 100.0:
                    price_100.append(_row)
                else:
                    price_100.append('')
            df['above_100'] = price_100
            file_output = _file[:-4] + "_output.csv"
            df.to_csv(fr'{_cwd}\{file_output}',
                      index=False)

if __name__ == "__main__":
    main()
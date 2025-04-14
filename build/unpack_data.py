import os
import pandas as pd

def unpack_data(input_dir, output_file):
    """
    Unpacks and combines multiple CSV files from a directory into a single CSV file.

    Parameters:
    input_dir (str): Path to the directory containing the CSV files.
    output_file (str): Path to the output combined CSV file.
    """

    # Step 1: Initialize an empty list to store DataFrames
    dataframes = list()

    # Step 2: Loop over files in the input directory
    #directory = os.path.join("c:\\","path")
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            # Step 3: Check if the file is a CSV or matches a naming pattern
            if file.endswith(".csv"):
                # Step 4: Read the CSV file using pandas
                df = pd.read_csv(file)

                # Step 5: Append the DataFrame to the list
                dataframes.append(df)
            
    # Step 6: Concatenate all DataFrames
    # Step 7: Save the combined DataFrame to output_file
    dfs = pd.concat(dataframes)
    dfs.to_csv(output_file, index=False)
    

if __name__ == "__main__":
    # python build\unpack_data.py --input_dir ".\workspaces\Data-Lakes-tp1-student\data\bronze" --output_file ".\workspaces\Data-Lakes-tp1-student\data\bronze\out.csv"

    import argparse

    ###
    import os
    current_directory = os.getcwd()
    print("Current Working Directory:", current_directory)
    ###

    parser = argparse.ArgumentParser(description="Unpack and combine protein data")
    parser.add_argument("--input_dir", type=str, required=True, help="Path to input directory")
    parser.add_argument("--output_file", type=str, required=True, help="Path to output combined CSV file")
    
    args = parser.parse_args()
    print(args.input_dir)

    unpack_data(args.input_dir, args.output_file)

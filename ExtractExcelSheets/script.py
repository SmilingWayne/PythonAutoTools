import pandas as pd
import os

input_folder_path = "./Contents"
output_folder_path = './Result'

for link in os.listdir(input_folder_path):
    # Replace 'filename.xlsx' with the path to your Excel file
    if link.endswith(".xlsx") or link.endswith(".xls"):
        excel_file = pd.ExcelFile(os.path.join(input_folder_path, link))

        # Loop through every sheet in the Excel file
        for sheet_name in excel_file.sheet_names:
            # Read the sheet into a dataframe
            df = pd.read_excel(excel_file, sheet_name, engine="openpyxl")

            # Replace 'sheet_name.csv' with the desired filename for each CSV file
            # "".join(filename.split(
            #     '.')[:-1])
            df.to_csv(os.path.join(output_folder_path, "".join(link.split(
                '.')[:-1]) + "-" + sheet_name + ".csv"), index=False, encoding="utf-8-sig")

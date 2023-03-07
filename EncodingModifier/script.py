import chardet
import pandas as pd
import os

input_folder_path = "./Contents"
output_folder_path = "./Result"

# FIXME: Worked well for csv files.
for file in os.listdir(input_folder_path):
    if file.endswith(".csv"):
        result = "utf-8"
        with open(os.path.join(input_folder_path, file), 'rb') as f:
            result = chardet.detect(f.read())['encoding']
            # print(result)
        with open(os.path.join(input_folder_path, file), "r", encoding="utf-8") as f:
            data = f.read()
        with open(os.path.join(output_folder_path, file), 'w', encoding='utf-8-sig') as f:
            f.write(data)
        print(f"{file} is encoded with utf-8-sig successfully!")

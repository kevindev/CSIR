# importing pandas as pd
import pandas as pd

# load csv file
temp_data = pd.read_csv("c:/temp/CSIR/3/temp_data.csv")

# add field temp in kelvin
temp_data["Temperature_degree_kelvin"] = temp_data["Temperature_degree_celsius"] + 273.15

# display array
print (temp_data)

# saving the new csv
temp_data.to_csv("c:/temp/CSIR/3/temp_data_output.csv")


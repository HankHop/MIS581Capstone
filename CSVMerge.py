"""
    Python Script:
        Combine multiple CSV files using the Pandas Library
"""

import pandas as pd
#Read first andj second csv files into variable
csv_input=pd.read_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/PartyRegistration.csv')
df = pd.DataFrame(csv_input)
csv_input2 = pd.read_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/election-context-2018-Modified.csv')
df2 = pd.DataFrame(csv_input2)
#Merge the two files matching on the primary key of "FIPS"
combined = pd.merge(df, df2, on='FIPS')
combined.to_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/Output.csv', index=False) #print combined file to csv titled "Output"

#Merge the new Output.csv with the third csv file matching on the primary key of "FIPS"
csv_input3 = pd.read_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/Output.csv')
df3 = pd.DataFrame(csv_input3)
csv_input4 = pd.read_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/ElectionReligionData2.csv', encoding = "ISO-8859-1") #This file was very dirty and contained special characters that I avoided by using a different encoding
df4 = pd.DataFrame(csv_input4)
df4["FIPS"] = pd.to_numeric(df4["FIPS"])  #I had to convert this column type to numeric because it was being read as a different data type somehow 
combined = pd.merge(df3, df4, on = 'FIPS')
combined.to_csv('C:/Users/Henry/Documents/CSU Global/MIS581/PythonMerge/FinalOutput.csv', index=False) #Printing the final output of all three csv files
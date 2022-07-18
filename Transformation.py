import pandas as pd

#Importing the extracted csv file
table = pd.read_csv('raw_data.csv')

#Getting all the column name of the Table
columns = table.columns

# Checking for null values to clean the data
table.isnull().sum()/table.count()[0]*100
2
# We have 4 percent data as nan in in vram columm and 1 percent data missing the vram_type
table = table.dropna(axis=0, how='any')

#Check if all the missing values are removed 
table.isnull().sum()/table.count()[0]*100

#Now let's go ahead and check for duplicates 
# for x in columns:
#     if x != 'Name' and x != 'Price' and x != 'Model':
#         print (table[x].unique())

#We can see that GDDR6 has duplicates due to a space after the string 
table['vram_type'][table.loc[table['vram_type']=='GDDR6 '].index] = 'GDDR6'


#As we can see there are no duplicates as well lets go ahead and save the cleaned table 
table.to_excel('cleaned_data.xlsx')




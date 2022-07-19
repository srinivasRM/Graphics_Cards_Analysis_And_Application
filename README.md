# Graphics cards price prediction using regression,Interative application and ETL

Hey guys! My name is Srinivas RM. In the current project I have extracted graphics card current prices from an authorizer retailer in India and performed analysis and created an Interactive application. I have done ETL(Extract,Tranform and Load) using the postgresql on Heroku Database. I have created a Dashboard usign seaborn and visualization which gives us valuable insights on data. I have tested regression models linear model,SGD Regressor,Random Forest Regressor,Decision Tree Regressor,Ridge,MLP Regressor and linear model (Lasso). After which I have selected the best perorming model and performed Hyper parameter tuning and then deployed an interactive application which can generate the visualization and send an email with the visualization to the users email address. 

# ETL

Extraction(https://github.com/srinivasRM/Graphics_Cards_Analysis_And_Application/blob/main/Scraper.py): - I have extracted the data from an Authorized AMD dealers website which sells graphics cards in India using BeautifulSoup library in python and then saved the raw data in the raw_data.csv with the date on which it was extracted using the datetime library. Made sure to convert all the missing values to np.nan for data cleaning in the next step  

Transform(https://github.com/srinivasRM/Graphics_Cards_Analysis_And_Application/blob/main/Transformation.py): - I have cleaned the raw data that was taken in the above step and cleaned the data by removing all the np.nan values and removing all the duplicates as well and created a new file Cleaned_data.xlsx.  

Load(https://github.com/srinivasRM/Graphics_Cards_Analysis_And_Application/blob/main/data_storage_and_visualization.py): -In this file I have written a sql query to read and load all the data from the csv file to the sql database using POSGRESQL and heroku database. In the same file I have extracted the data from the database for visualization and created a visualization of the relation between the features and the price of the Graqphic cards and save it as an report.png file with the date on which the dashboard was created.

# EDA(Eploratory data analysis)
refer to this file for the code - https://github.com/srinivasRM/Graphics_Cards_Analysis_And_Application/blob/main/Model.ipynb

##Here is the detailed report of the relation of each column with target variable('Price')

![report](https://user-images.githubusercontent.com/94186999/179727017-96b8f02a-b7f7-433e-83e5-5cb9bd1f3a1e.png)

## Box plot of the Price column before outlier treatment

![before treating outliers boxplot](https://user-images.githubusercontent.com/94186999/179727688-8f0ef1a0-32ec-4c89-b0b3-b1b51e0d9468.png)

## Distplot of the Price column  before outlier treatment

![before treating outliers distplot](https://user-images.githubusercontent.com/94186999/179727856-bab57465-5a64-4931-a73d-604bb4bb29b9.png)

## Box plot of the Price column  after outlier treatment

![after treating outliers boxplot](https://user-images.githubusercontent.com/94186999/179727916-95f4005d-2b8a-4e6f-8787-94890883777b.png)

## Distplot of the Price column  after outlier treatment

![after treating outlier distplot](https://user-images.githubusercontent.com/94186999/179728066-bf952440-4928-4485-ba64-0d078aada613.png)

As we can see after replacing the values that were greater than 0.75 with the mean of the data and replacing each value in the column with the Z-score i.e afte rnormalizing the data the dist plot shows less skewness when compored to the prior distplot. 

## Testing various models
Here is a table which represents the r2 and adjusted r2 of each model on the current data set. 

![models values](https://user-images.githubusercontent.com/94186999/179728871-0ea6635d-7908-45c4-9a5e-5fe3e0349968.JPG)

Selected Random forest regressor for Hypertuning to improve its performance as it gave the best results and here are the results after hypertuning 

![Hypertuning](https://user-images.githubusercontent.com/94186999/179729094-e4c6d27b-5d93-46bb-8c7a-2f882587d3e9.JPG)

Saved the current model using the pickled module and created the pkl file in the current repository. 

Here is a graph that shows importance of each feature with the target variable('Price')

![Feature importance](https://user-images.githubusercontent.com/94186999/179729844-aa40fd09-3d21-47f3-a10c-4e6d7f0717f9.JPG)

Created file main.py which runs all the .py files which extracts the data, stores the data in the SQL database and then extractes the data from the sql database and creates visualization and deploys the application automatically onto your local browser once the all the files have been run. I used Steamlit for creating the front end application. Here is a screenshot of the application.

![Deployment](https://user-images.githubusercontent.com/94186999/179730473-c4f74ceb-10fe-4378-8aa6-ff224cb59408.JPG)

Let me know if you have any suggestions. You can contact me on this email - rmsrinivas199627@gmail.com

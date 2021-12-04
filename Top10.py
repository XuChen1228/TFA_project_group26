import pandas as pd
raw_data = pd.read_csv('311_Service_Requests_2020.csv')
selected_data = raw_data[['Agency','Complaint Type','Incident Zip']]
selected_data_zip_25 = selected_data.loc[selected_data['Incident Zip'] == 10025]
top10 = selected_data_zip_25['Complaint Type'].value_counts().head(10)
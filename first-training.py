

#csv = wget.download("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
min_payload = 0
max_payload = 5000
import pandas as pd
spacex_df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv")
spacex_df.dtypes
filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] > min_payload) & (spacex_df['Payload Mass (kg)'] < max_payload)]
  
#filtered_df = filtered_df.groupby(['Launch Site', 'class']).size().reset_index(name='class_count')
print(filtered_df)
import pymssql
import pandas as pd
conn = pymssql.connect('192.168.0.16','nmRis','nmRis','nmRis')
sql='SELECT id,accnum,name,study_date,sex,report_doctor_id,report_doctor FROM study'
df0 = pd.read_sql(sql,conn)
df=pd.DataFrame(df0)

df['study_date'] = pd.to_datetime(df['study_date']) 

df = df.set_index('study_date') 

print(df)
print(df['201903'].groupby('report_doctor').size())
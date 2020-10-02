# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:56:57 2020

@author: pavan
"""
import pandas as pd
df_in = pd.read_csv('glassdoor_jobs.csv')

df_in.columns

# Removing unneccesary columns
df = df_in.drop(['Unnamed: 0'],axis = 1)


# Salary Estimate cleaning
df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['emp_provid_sal'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)

df =df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])

salary_dk = salary.apply(lambda x: x.replace('K','').replace('$',''))
salary_hr_est = salary_dk.apply(lambda x: x.lower().replace('per hour','').replace('employer provided salary:',''))

df['min_salary'] = salary_hr_est.apply(lambda x: int(x.split('-') [0]))
df['max_salary'] = salary_hr_est.apply(lambda x: int(x.split('-') [1]))

df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2

#Location : extract only State names

df['job_location'] = df['Location'].apply(lambda x: x.split(',')[1])

df.columns
# Location and head Quaters are same or not
df['same_location'] = df.apply(lambda x: 1 if x['Location'] == x['Headquarters'] else 0,axis = 1)


#Company Name: remove ratngs for the company name
df['company_txt'] = df.apply(lambda x: x['Company Name'] if x.Rating < 0 else x['Company Name'][:-3],axis = 1)

# company age
df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)

#Revenue : Cleanse the Revenue with hexAvg Revenue
#df['avg_revenue'] = df['Revenue'].apply(lambda x: x.lower().replace('million (usd)','').replace('$','').split('to')([0]+[1])/2)
#revenue = df['Revenue'].apply(lambda x: x.split('(')[0])
#revenue_dk = revenue.apply(lambda x: x.replace('to','-').replace('$',''))
#revenue_hr_est = salary_dk.apply(lambda x: x.lower().replace('unknown / non-applicable',''))


#Job Description parsing for specific skills like Python,sprk,aws,java,R,sql
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python'].value_counts()

df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark'].value_counts()

df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['sql'].value_counts()

df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws'].value_counts()

df.to_csv('salary_data_cleansed.csv',index = False)
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#Read the file using pandas
data = pd.read_csv('h1b_data.csv', sep = "," , usecols = {'lca_case_number', 'lca_case_employer_name', 'lca_case_employer_city','lca_case_wage_rate_from','lca_case_wage_rate_unit', 'status'})

print(data.head())


###SECTION1###

##1. Which companies applied for the largest number of visas where the job opening was located in New York?

#Keep only companies from NY
data1 = data.loc[(data['lca_case_employer_city']== 'NEW YORK') | (data['lca_case_employer_city']== 'NY') | (data['lca_case_employer_city']== 'NYC') ]
data1 = data1[['lca_case_employer_name', 'lca_case_number']]
data1 = data1.groupby(['lca_case_employer_name']).count()
max = data1['lca_case_number'].max(axis=None)
result = data1.loc[data1['lca_case_number'] == max]
print(result)

#MPHASIS CORPORATION applied for the largest number of visas in NY with 946 applications

##2. Mean and standard deviation of wages proposed for workets in NY and Mountain View

# Consider only year salaries
data2 = data.loc[data['lca_case_wage_rate_unit']=='Year']

#Gather data for New York and Mountain View
data_NY = data2.loc[data2['lca_case_employer_city']=='NEW YORK']
data_MV = data2.loc[data2['lca_case_employer_city']=='MOUNTAIN VIEW']

#NEW YORK mean and standard deviation
mean_NY = data_NY['lca_case_wage_rate_from'].mean()
std_NY = data_NY['lca_case_wage_rate_from'].std()
print("Average wage for NY is: ", mean_NY)
print("Standard deviation for NY wages is: ", std_NY)

#MOUNTAIN VIEW mean and standard deviation
mean_MV = data_MV['lca_case_wage_rate_from'].mean()
std_MV = data_MV['lca_case_wage_rate_from'].std()
print("Average wage for MV is: ", mean_MV)
print("Standard deviation for MV wages is: ", std_MV)

#Average salary is superior in Mountain View but standard deviation is lower (same kind of job positions at tech companies)

##3. For NYC what is the relationship between the total number of H1B visas requested by an employee end the average wages proposed

data3 = data.loc[data['lca_case_employer_city']== 'NEW YORK']
data3 = data3.loc[data['lca_case_wage_rate_unit']=='Year']

#Group by employer
data_count = data3.groupby(['lca_case_employer_name']).count()
data3 = data3[['lca_case_employer_name', 'lca_case_wage_rate_from']]

#For each employer get mean wage
data3 = data3.groupby(['lca_case_employer_name']).mean()

#Fore each employer count the number of applications
data3['COUNT']= data_count['lca_case_number']
print(data3)


#Plot data using scatter plot
data3.plot(kind="scatter", x="COUNT", y="lca_case_wage_rate_from", alpha = 0.3)
plt.ylim((0,500000))
plt.xlim((0, 50))
plt.xlabel('Number of visa applications')
plt.ylabel('Average salary')
plt.show()





###SECTION2###

#Results for Statuses
data4 = data['status']
print(data4.value_counts())

































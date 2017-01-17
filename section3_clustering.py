import pandas as pd 
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
import matplotlib.pyplot as plt
import numpy
numpy.set_printoptions(threshold=numpy.nan)

from section3 import clean_jobs 



data = pd.read_csv('h1b_data.csv', sep = "," , usecols = {'lca_case_number', 'lca_case_employer_name', 'lca_case_employer_city', 'lca_case_job_title', 'lca_case_employer_state','lca_case_wage_rate_from','lca_case_wage_rate_unit', 'status'}, encoding = 'utf-8', nrows = 200000)
data_clusters = data[['lca_case_job_title', 'lca_case_number', 'lca_case_employer_state']]


# Apply clean_jobs to the column of the dataframe containing job titles
data_clusters['TITLE']= data_clusters['lca_case_job_title'].apply(lambda x: clean_jobs(x))


#Clusters: Create a dictionary that assign words to cluster. 0 = Tech, 1 = Business, 2 = Education and Research, 3 = Other

Cluster = {'engin':0, 'develop':0, 'softwar':0, 'system':0, 'technic':0, 'progamm':0,'data':0, 'comput':0, 'program':0, 'technolog':0, 'it':0, 'manag':1, 'analyst':1,'busi':1, 'consult':1, 'financi':1, 'account':1, 'research':2, 'professor':2 ,'scientist':2, 'architect':3, 'staff':3,'sale':3}


##Clustering
def clusterize(list):
	if list is not None:
		return [int(Cluster[l]) for l in list if l in Cluster.keys()]

def minimum(list):
	if (list is not None):
		if(len(list)!=0):
			return max(list)

#Apply clustering
data_clusters['TITLE'] = data_clusters['TITLE'].apply(lambda x: clusterize(x))

#Take the minimum of the cluster number
data_clusters['TITLE'] = data_clusters['TITLE'].apply(lambda x: minimum(x))


#Drop non classified jobs
data_clusters= data_clusters.dropna(axis = 0)
print(data_clusters.head(100))

##PLOT##

#Tech jobs

data_tech_jobs = data_clusters.loc[data_clusters['TITLE']==0]
data_tech_jobs = data_tech_jobs.groupby(['lca_case_employer_state']).count()
data_tech_jobs = data_tech_jobs.sort_values(by=['lca_case_number'], ascending=False)
data_tech_jobs = data_tech_jobs.drop(['lca_case_job_title', 'TITLE'], axis=1)
data_tech_jobs.plot(kind= 'bar', grid = False, legend = None)
plt.xlabel('State')
plt.ylabel('Number of applications for tech positions')



#Business Jobs

data_bus_jobs = data_clusters.loc[data_clusters['TITLE']==1]
data_bus_jobs = data_bus_jobs.groupby(['lca_case_employer_state']).count()
data_bus_jobs = data_bus_jobs.sort_values(by=['lca_case_number'], ascending=False)
data_bus_jobs = data_bus_jobs.drop(['lca_case_job_title', 'TITLE'], axis=1)
data_bus_jobs.plot(kind= 'bar', grid = False, legend = None)
plt.xlabel('State')
plt.ylabel('Number of applications for business positions')


#Research & Education Jobs

data_edu_jobs = data_clusters.loc[data_clusters['TITLE']==2]
data_edu_jobs = data_edu_jobs.groupby(['lca_case_employer_state']).count()
data_edu_jobs = data_edu_jobs.sort_values(by=['lca_case_number'], ascending=False)
data_edu_jobs = data_edu_jobs.drop(['lca_case_job_title', 'TITLE'], axis=1)
data_edu_jobs.plot(kind= 'bar', grid = False, legend= None)
plt.xlabel('State')
plt.ylabel('Number of applications for research & education positions')



#Other type of jobs

data_other_jobs = data_clusters.loc[data_clusters['TITLE']==3]
data_other_jobs = data_other_jobs.groupby(['lca_case_employer_state']).count()
data_other_jobs = data_other_jobs.sort_values(by=['lca_case_number'], ascending=False)
data_other_jobs = data_other_jobs.drop(['lca_case_job_title', 'TITLE'], axis=1)
data_other_jobs.plot(kind= 'bar', grid = False, legend = None)
plt.xlabel('State')
plt.ylabel('Number of applications for other positions')
plt.show()





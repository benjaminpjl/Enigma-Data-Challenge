import pandas as pd 
import seaborn as sns
sns.set(style="whitegrid", color_codes=True)
import matplotlib.pyplot as plt
import numpy
numpy.set_printoptions(threshold=numpy.nan)
import string
import re 
import itertools
import copy
import igraph
import nltk
from collections import Counter

from nltk.corpus import stopwords
# requires nltk 3.2.1
from nltk import pos_tag


#Read csv file into pandas dataframe
data = pd.read_csv('h1b_data.csv', sep = "," , usecols = {'lca_case_number', 'lca_case_employer_name', 'lca_case_employer_city', 'lca_case_job_title', 'lca_case_employer_state','lca_case_wage_rate_from','lca_case_wage_rate_unit', 'status'})
print(data.head())

###SECTION3###

#Repartition of visa applications per state
data_state = data[['lca_case_number', 'lca_case_employer_state']]
data_state = data_state.loc[data['lca_case_wage_rate_unit']=='Year']
data_state = data_state.groupby(['lca_case_employer_state']).count()

#Plot data as an ordered bar chart
data_state = data_state.sort_values(by=['lca_case_number'], ascending=False)
data_state.plot(kind= 'bar', grid = False, legend = None)
plt.xlabel('State')
plt.ylabel('Number of applications')


##Clustering job position 
##Find the 50 top keywords for the clustering

#Get a list of all the unique job positions
data_clusters = data[['lca_case_job_title', 'lca_case_number']]
list_jobs = data_clusters['lca_case_job_title'].unique().tolist()


#Function that cleans the text (NLP)
def clean_jobs(text, remove_stopwords = True, stemming=True):
	try:

		#convert to lower case
		text = text.lower()

		#remove punctuation
		punct = string.punctuation
		text = ''.join(l for l in text if l not in punct)
		

		# strip extra white space
		text = re.sub(' +',' ',text)

	    # strip leading and trailing white space
		text = text.strip()

	    # tokenize (split based on whitespace)
		tokens = text.split(' ')
		if remove_stopwords:
			stpwds = stopwords.words('english')
	    	# remove stopwords
	    	tokens = [token for token in tokens if token not in stpwds]

		#Stemming
		if stemming:
			stemmer = nltk.stem.PorterStemmer()
	        # apply Porter's stemmer
	        tokens_stemmed = list()
	        for token in tokens:
	    		tokens_stemmed.append(stemmer.stem(token))
	    	tokens = tokens_stemmed
	
		return(tokens)
		
	except Exception:
		pass

	
	
	

#execute the code only if the file is executed directly and not imported
if __name__ == "__main__": 

	#Create a list of all the job positions cleaned by using the clean_jobs function
	list_jobs_cleaned = []
	for job in list_jobs:
		try:
			list_jobs_cleaned.append(clean_jobs(job.decode('utf-8')))
		except Exception:
			pass
	print(list_jobs_cleaned)

	list_jobs_final = [item for sublist in list_jobs_cleaned for item in sublist]
	print(list_jobs_final)

	#Gives the top 50 keywords 
	d = Counter(list_jobs_final)
	d.most_common()
	for k,v in d.most_common(50):
		print ('%s: %i' % (k, v))










import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Manager(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.read_spd()

	def read_spd(self):
		filepath = os.path.expanduser('~/projects/ch1_sea_dl_speeds/data/'+self.filepath)
		data = pd.read_csv(filepath)
		return self.data
		
	def clean_advt_spd(self):
		data = self.data[data.advertised_download.notnull()]
		data = data[data.advertised_download != 0]
		return data_cln_spd
	 
	def clean_cost(self, dont_know=None):
		data = self.data[data.cost_of_service != dont_know]
		return data_cln_cost

	def select_isp(self, data, isp=None):
		data_isp = self.data[self.data.isp_user == isp]
		return data_isp


class Analyser(object):

    def __init__(self, manager):
        self.manager = manager
        self.data = manager.data

	def cost_spd(self, data):
		grouped = data['actual_download'].groupby(data['cost_of_service'])
		grouped_stats = grouped.describe()
		box = grouped.boxplot()	
		return grouped, box, grouped_stats

	def percent_spd(self, spd_data):
	
		act_dl = spd_data.actual_download
		adv_dl = spd_data.advertised_download
		percent_dl = (act_dl / adv_dl) * 100
	
		bins = np.arange(0, percent_dl.max()+10, 10)
		#bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, np.inf]
		#bins = 200
		binned = pd.cut(percent_dl, bins)
	
		percent_dl_binned = pd.value_counts(binned).sort_index()
		percent_dl_binned = (percent_dl_binned / sum(percent_dl_binned)) * 100
		histogram = percent_dl_binnied.hist()   
	
		mean_percent_dl = percent_dl.mean()
	
		return percent_dl_binned, histogram, mean_percent_dl

	
	def analyse_isp(filepath, isp=None):
		data = self.manager.select_isp(df, isp=isp)
	
		percent_dl_binned, mean_percent_dl = percent_spd_isp(df)
	
		return percent_dl_binned, mean_percent_dl

	def full_analysis(self, isps):
	    
	    data_cost = self.manager.clean_cost(dont_know='dont_know')
	    data_spd = self.manager.clean_advt_spd()
	    
	    for isp in isps:
	        data_cost_isp = self.manager.select_isp(data_cost, isp=isp)
	        grouped, box, grouped_stats = self.manager.cost_spd(data_cost_isp)
	        cost_dict[isp]={grouped, box, grouped_stats}
	        
	        data_spd_isp = self.manager.select_isp(data_spd, isp=isp)
	        binned_dl, histogram, mean_dl = percent_spd(data_spd)
	        spd_dict[isp]={binned_dl, histogram, mean_dl}
	        
	        return spd_dict, cost_dict

class Plotter(object): 

	def full_plot(data):
		pass

isps = ['comcast','centurylink','wave']

data = read_spd('sea_broadband_dl_speed_test_2016.csv')
data, grouped = clean_cost(data, dont_know='dont_know')
print data.head(10)
print grouped
    
    
# percent_dl_binned, mean_percent_dl = analyse_isp('sea_broadband_dl_speed_test_2016.csv', isp='wave')
# print percent_dl_binned
# print mean_percent_dl
#print hist_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

class Manager(object):
	def read_spd(filepath):
		filepath = os.path.expanduser('~/projects/ch1_sea_dl_speeds/data/'+filepath)
		df = pd.read_csv(filepath)
		return df

	def clean_advt_spd(spd_data):
		spd_data = spd_data[spd_data.advertised_download.notnull()]
		spd_data = spd_data[spd_data.advertised_download != 0]
		return spd_data
	 
	def clean_cost(spd_data, dont_know=None):
		spd_data = spd_data[spd_data.cost_of_service != dont_know]
		return spd_data, grouped

	def select_isp(spd_data, isp=None):
		select_isp = spd_data[spd_data.isp_user == isp]
		return select_isp


class Analyser(object):
	def cost_spd(data):
		grouped = spd_data['actual_download'].groupby(spd_data['cost_of_service'])
		return grouped

	def percent_spd_isp(spd_data):
		spd_data = clean_advt_spd(spd_data)
	
		act_dl = spd_data.actual_download
		adv_dl = spd_data.advertised_download
		percent_dl = (act_dl / adv_dl) * 100
	
		bins = np.arange(0, percent_dl.max()+10, 10)
		#bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, np.inf]
		#bins = 200
		binned = pd.cut(percent_dl, bins)
	
		percent_dl_binned = pd.value_counts(binned).sort_index()
		percent_dl_binned = (percent_dl_binned / sum(percent_dl_binned)) * 100    
	
		mean_percent_dl = percent_dl.mean()
	
		return percent_dl_binned, mean_percent_dl

	
	def analyse_isp(filepath, isp=None):
		df = read_spd(filepath)
		df = select_isp(df, isp=isp)
	
		percent_dl_binned, mean_percent_dl = percent_spd_isp(df)
	
		return percent_dl_binned, mean_percent_dl

class Plotter(object): 
	def full_plot(data):
		pass

data = read_spd('sea_broadband_dl_speed_test_2016.csv')
data, grouped = clean_cost(data, dont_know='dont_know')
print data.head(10)
print '-------------------------------------'
print grouped
    
    
# percent_dl_binned, mean_percent_dl = analyse_isp('sea_broadband_dl_speed_test_2016.csv', isp='wave')
# print percent_dl_binned
# print mean_percent_dl
#print hist_data
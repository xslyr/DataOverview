#/usr/bin/python3
#!encoding:utf8
#
#	Created at 26-05-2023
#	Coder: Wesley R. Silva
#	Library with functionalities similar a "Pandas Dataframe Describe".
#

import pandas as pd
import numpy as np

class DataOverview:
	possible_dtypes = ['int64','float64','object','bool', 'datetime64']
	cols = ['dtype','count','null','mean','std','std%','min','max','mode','n_mode','25%','50%','75%']
	details = pd.DataFrame([], index=cols)

	def __init__(self, dataframe):	
		if not isinstance(dataframe, pd.DataFrame):
			raise ValueError("It's necessary an dataframe argument to instantiate this object.")
		else:
			self.df = dataframe
			for i in range(self.df.columns.size):
				self.details = pd.concat([self.details, self.__extractData(i)], axis=1)
		return

	def columns_type(self):
		cols_dtype = { t:0 for t in self.possible_dtypes }
		for i in self.df.columns:
			cols_dtype[ str(self.df[i].dtypes) ] +=1
		return  cols_dtype
    
	def show(self, type='all'):
		aux = pd.DataFrame([], index=self.cols)
		if type not in ['all']+self.possible_dtypes:
			raise ValueError('Error type parameter. Choose one of this values: {}'.format(['all']+self.possible_dtypes))
		elif (type in self.possible_dtypes) and (self.columns_type()[type]>0):
			for i,col in enumerate(self.details):
				if self.details[col]['dtype'] == type:
					aux = pd.concat([aux, self.__extractData(i)], axis=1)
		else:
			aux = self.details
		return aux

	def __extractData(self, i):
		aux = pd.DataFrame(np.zeros(shape=(len(self.cols),1)), index=self.cols, columns=[self.df.columns[i]])
		aux.loc['dtype'] = 'object' if self.df[aux.columns[0]].dtypes == 'O' else self.df[aux.columns[0]].dtypes
		aux.loc['count'] = self.df[aux.columns[0]].count()
		aux.loc['null'] = self.df[aux.columns[0] ].isnull().sum()+self.df[aux.columns[0] ].isna().sum()
		aux.loc['mode'] = self.df[aux.columns[0]].mode(dropna=False).iloc[0]
		aux.loc['n_mode'] = self.df[aux.columns[0]].value_counts().sort_values(ascending=False).iloc[0]
		if self.df[aux.columns[0]].dtypes in ['int64','float64']:
			aux.loc['mean'] = self.df[aux.columns[0]].mean()
			aux.loc['std'] = self.df[aux.columns[0]].std()
			aux.loc['min'] = self.df[aux.columns[0]].min()
			aux.loc['max'] = self.df[aux.columns[0]].max()
			aux.loc['std%'] = '{:.2f}'.format(100*self.df[aux.columns[0]].std()/(self.df[aux.columns[0]].max()-self.df[aux.columns[0]].min()))
			aux.loc['25%'] = self.df[aux.columns[0]].quantile(q=0.25)
			aux.loc['50%'] = self.df[aux.columns[0]].quantile(q=0.5)
			aux.loc['75%'] = self.df[aux.columns[0]].quantile(q=0.75)
		return aux



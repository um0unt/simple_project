# -*- coding:utf-8 -*-

import pandas as pd

get_df = pd.read_csv('dump.csv', sep=',', header=0)                		#read data from scv

tcp_df = pd.DataFrame(get_df[get_df['Protocol'] == 'TCP'])				#select only tcp form dump

tcp_df.drop(['No.','Time','Length','Protocol'], axis=1, inplace=True)	#delete unnecessary columns

tcp_df['Info'].replace(													#regular expression for
			to_replace='(\[((\w+\s)|[^\]])+\]\s*)|(\w+\=\d+)|\s+', 		#getting port numbers
			value='', 													#from string Info
			inplace=True, 												
			regex=True
			)

tcp_df = pd.concat(														#expand column Info on
			[tcp_df,tcp_df['Info'].str.split('>', expand=True)], 		#two 0 and 1
			axis=1
			)

tcp_df = tcp_df.rename(columns={0:'Src name port', 1:'Dst name port'})	#rename columns 0 and 1

tcp_df.drop(['Info'], axis=1, inplace=True)								#delete coloumn Info

result = pd.DataFrame(tcp_df.groupby(									#create result table
				['Source',
				'Destination',
				'Src name port',
				'Dst name port'
				])['Source'].size());

result = result.rename(columns={'Source':'Number of requests'})			#rename sort colunm

print(result)															#show dataframe in terminal

result.to_csv('result.csv')                                      		#save result in file
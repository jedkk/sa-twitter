import twint
import os
from time import sleep


c = twint.Config()
c.User_full = True        
c.Limit   = 10000        
c.Store_csv = True       


months = ['01', '02', '03', '04']
for m in months:
	for d in range(1, 31):
		c.Search = f'#model3 OR "tesla model 3" lang:en since:2022-{m}-{str(d).zfill(2)} until:2022-{m}-{str(d+1).zfill(2)}'  # 1 to 30 == 1/2 to 30/31
		c.Output = f'month{m}_{str(d).zfill(2)}.csv'  # Path to csv file, 'month01_30.csv'
		#twint.run.Search(c)
		#sleep(3) # Twitter's robots.txt states crawl-delay of 1sec

		# If no tweets found, retry once for that day.
		if not os.path.exists(f'month{m}_{str(d).zfill(2)}.csv'):
			print(f'Trying for month {m}, {d} to {d+1}')
			twint.run.Search(c)
			sleep(3)
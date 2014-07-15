import collections
import json
import sys
import csv
import os

from os.path import expanduser
home = expanduser("~")
os.chdir(home)
# https://docs.python.org/2/library/collections.html#collections.defaultdict
results = collections.defaultdict(int)
#fileobj=open('matched_activities.json')
f=open('matched_activities.json').readlines()
for line in f:
	try:
		d=json.loads(line)
		rule=d["matching_rules"] #returns a list of dicts
		for things in rule:
			ruleval= things["value"]
			#print ruleval
			results[ruleval]+=1
	except:
		#print >>sys.stderr, "bad record={}".format(line)
		continue

with open('summary.csv', 'a+b') as o:
    o.write(json.dumps(results)+ '\n')

#f.close()
o.close()

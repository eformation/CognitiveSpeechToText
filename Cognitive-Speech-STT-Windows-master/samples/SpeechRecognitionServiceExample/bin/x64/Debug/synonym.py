import requests
import json
import re
import sys
from collections import deque
import numpy
import pandas as pd

url = "http://thesaurus.altervista.org/thesaurus/v1"
syn_que = []
completed = []
j=0
#querystring = {"word":"confidence","language":"en_US","key":"jSUdcDDXG9Blytmt0xG2","output":"json"}

# headers = {
#     'Cache-Control': "no-cache",
#     'Postman-Token': "b2e3ad7d-1f9d-1faa-f266-a8cad714053c"
#     }
def get_response_json(word):

	querystring = {"word":word,"language":"en_US","key":"jSUdcDDXG9Blytmt0xG2","output":"json"}
	
	response = requests.request("GET", url, params=querystring)
	json_data = json.loads(response.text)
	#print(json_data)
	thesaurus_response = json_data["response"]
	return thesaurus_response


def find_synonyms(thesaurus_response,word):
	global j
	global completed
	global syn_que

	completed.append(word)
	for list_ in thesaurus_response:
		for key,value in list_.items():
			#print(key)
			for key2,val in value.items():
				if (key2 == 'synonyms'):
					list_words = val.split('|')
					# print("----------------------")
					# print(list_words)
					temp_list = [x for x in list_words if  not re.match(r".*\(.*\).*",x)]
					for word in temp_list:
						if word not in syn_que:
							syn_que.append(word)
						else:
							continue
					# final_list = final_list + [x for x in list_words if  not re.match(r".*\(.*\).*",x)]
					# s = set(final_list)
					# final_list = list(s)
	#print(final_list)
	
	j=j+1
	# print(syn_que)
	if (j<len(syn_que)):
		
		# print(syn_que[j])
		thesaurus_response=get_response_json(syn_que[j])
		find_synonyms(thesaurus_response,syn_que[j])


if __name__ == "__main__":
	word = str(input('enter a word for which you want to find synonyms:'))
	syn_que.append(word)
	thesaurus_response=get_response_json(word)
	find_synonyms(thesaurus_response,word)
	
# print(completed)
x = [1,2,3]
df = pd.DataFrame(x,columns=['val'])
a = df.ix[1]


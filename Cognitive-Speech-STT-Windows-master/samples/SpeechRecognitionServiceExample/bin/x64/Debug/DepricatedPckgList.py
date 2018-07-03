import inspect
#import synonym
from subprocess import PIPE,Popen
import re
from itertools import chain
import sys
import changelogs

logs = changelogs.get("pandas")
final_func_list=[]

ver = '0.20.1'
s = logs[ver]

lines = s.splitlines()

l = []
for i in lines:
    if i.find('deprecated')!=-1:
        #print(i)
        if re.search(r"(\``(.*?)\``)",i)!=None:
            x = re.findall(r"(\``(.*?)\``)",i)
            #a = x.group().replace('``', '')
            a = x[0][1]
            #a = x[len(x)-1][1]
            l.append(a)

deprecated_list = list(set(l))
#deprecated_list_new=[l.split('(')[0].split('.')[0] for l in deprecated_list]
#print(deprecated_list)
#print('-----------------------------------------------------------------------')

process=Popen(['pip','list','--outdated'],stdout=PIPE,stderr=PIPE)
stdout,stderr=process.communicate()
#print (stdout)

list_stdout=[x.split() for x in stdout.decode('utf8').split('\r\n') ]
#rint (list_stdout)
#print(sys.argv[1])
with open(sys.argv[1],'r') as myfile:
	data = myfile.readlines()

#print(data)
list_packages=[item.split()[1] for item in data if re.match("import.*",item) ]
#print (list_packages)

list_pckges_inspect=[item for item in list_packages if item in chain.from_iterable(list_stdout)]
#print (list_pckges_inspect)

l=[(index,line.split('.')[1].split('(')[0]) for index,line in enumerate(data) if re.match(".*\.[a-zA-Z0-9]+[\[(].*?",line)]

#print(l)

l_temp=[(index+1,line.split('[')[0]) for index,line in l]
#print(l_temp)

#print(l_temp)

#file_func_list=list(set(l_temp))

#print(file_func_list)
#print(deprecated_list)

l2 = [s.replace("()","") for s in deprecated_list] 
l3 = []
for i in l2:
    if i.find(".")!=-1:
        l3.append(i.split(".")[1])
#print(l3) 


for i,val in l_temp:
	for s in l3:
		if val in s:
			final_func_list.append((i,val))

final_func_list=list(set(final_func_list))

print(final_func_list)


print ('--------------------------------------------------')
print ('Final list of modules which depricated ' , list_pckges_inspect)
print ('Final list of functions from thos modules which are depricated ',final_func_list)


# with open("DeprecatedEngineOutput.txt", "w") as text_file:
#     text_file.write("\n")
#     text_file.write("Final list of modules which depricated: " + str(list_pckges_inspect))
#     text_file.write("\n")
#     text_file.write("Final list of functions from thos modules which are depricated: " + str(final_func_list))







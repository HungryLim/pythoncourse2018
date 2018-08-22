
#pip install meetup-api
import imp

## first arg is folder name, second arg is navigating to file
meetup = imp.load_source('pythoncourse2018-prep', 'C:/Users/wooki/Desktop/meetup_api.py')
api = meetup.client

## methods we can use
## https://meetup-api.readthedocs.io/en/latest/meetup_api.html#api-client-details




polgroups = api.GetFindGroups({"zip" : "63130", "text" : "political"})
len(polgroups)



a=[g.members for g in polgroups]
a.sort()
a[len(a)-1]

for i in polgroups:
    if i.members == 2840:
        print i.name
        print i.urlname

pop_group=api.GetGroup({"urlname" : "politicalcafe-66"}) #answer for num1
pop_group.__dict__.keys()
print pop_group.members

pop_group_members = api.GetMembers({"group_urlname" : "politicalcafe-66"})
pop_group_members.__dict__.keys()
pop_group_members.results[0].keys()


ppl = pop_group_members.__dict__["results"]
len(ppl)
ppl[1]["id"]

ids=[]
for g in ppl:
   a=g["id"]
   ids.append(a)
ids[0]

import time
def find_most_pop_member(ids):
    tt=[]
    kk=[]
    for i in ids:
        try:
            aa = api.GetGroups({"member_id" : i})
        except ValueError:
            time.sleep(1)
            aa = api.GetGroups({"member_id" : i})
            bb = len(aa.results)
            kk.append(i)
            tt.append(bb)
            together=zip(kk,tt)
    return together
find_most_pop_member(ids)

import pandas as pd
import numpy as np
df = pd.DataFrame(together, columns = ["id","num"])
df.sort_values(by = "num",ascending=False)

max_person=df["id"][102] #answer for num2

max_person_groups=api.GetGroups({"member_id" : max_person})
print max_person_groups.results

max_person_groups.results


import pandas as pd
import numpy as np
df = pd.DataFrame(together, columns = ["id","num"])
df.sort_values(by = "num",ascending=False)

max_person=df["id"][102]

max_person_groups=api.GetGroups({"member_id" : max_person})
max_person_groups.results
max_person_groups.results[0].keys()

max_person_groups.results[0]["urlname"]
numofmem=[]
names=[]
for g in max_person_groups.results:
    num=g["members"]
    name=g["name"]
    numofmem.append(num)
    names.append(name)

get=zip(names,numofmem)

df2 = pd.DataFrame(get, columns = ["name","num"])
df2.sort_values(by = "num",ascending=False)
df2["name"][5] #answer for num3
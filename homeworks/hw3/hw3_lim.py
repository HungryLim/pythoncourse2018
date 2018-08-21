
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

pop_group=api.GetGroup({"urlname" : "politicalcafe-66"})
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
tt=[]
kk=[]
for i in ids:
    print i
    try:
        aa = api.GetGroups({"member_id" : i})
    except ValueError:
        time.sleep(2)
        aa = api.GetGroups({"member_id" : i})
    bb = len(aa.results)
    kk.append(i)
    tt.append(bb)
together=zip(kk,tt)

if together:
    return values.index(max(values))




# coding: utf-8

# In[42]:


path = "/Users/ericlu/Downloads/APA_Election.txt"
file = open(path, "r").readlines()[7:]
preferences = []
for line in file:
    preferences.append([int(i.strip("\n")) for i in line.split(",")])
print(preferences[:10])


# In[80]:


from collections import defaultdict
def plurality_vote(preferences):
    print("Plurality Vote:")
    votes = defaultdict(int)
    for line in preferences:
        votes[line[1]]+=line[0]
    print(votes)
    print(sum(votes.values()))
    print("Winner is:",max(votes, key = votes.get))
plurality_vote(preferences)


# In[83]:


import copy
from collections import defaultdict
def instant_runoff(preferences):
    candidates = list(range(5))
    pref = copy.deepcopy(preferences)
    loser = -1
    winner = -1
    while len(candidates)>1:
        votes = defaultdict(int)
        for line in pref:
            if len(line)>1:
                #print(line)
                votes[line[1]]+=line[0]
        winner = max(votes, key = votes.get)
        total = sum(votes.values())
        percent = float(votes[winner])/float(total)
        print("percent", percent)
        if(percent>0.5):
            print(votes)
            print("sum",sum(votes.values()))
            break
        loser = min(votes, key = votes.get)
        print(votes)
#         print(sum(votes.values()))
#         print(loser)
        candidates.remove(loser)
        print(candidates)
        for line in pref:
            if line[0] is loser:
                if loser in line[1:]:
                    del line[line.index(loser,1)]
            else:
                if loser in line:
                    line.remove(loser)
    print("Winner is:", winner)
instant_runoff(preferences)


# In[89]:


from collections import defaultdict
import copy
def borda_count(preferences, candidates): 
    max_score = candidates-1
    print(max_score)
    pref = copy.deepcopy(preferences)
    borda = defaultdict(int)
    #print(pref)
    for line in pref:
        for i in range(1,len(line)):
            borda[line[i]]+=(max_score-i)*line[0]
        #print(borda)
    print(borda)
    print(sum(borda.values())/9)
    winner = max(borda, key=borda.get)
    print(winner)
borda_count(preferences, 5)


# In[90]:


import copy
from collections import defaultdict
def approval_voting(preferences):
    candidates = list(range(5))
    pref = copy.deepcopy(preferences)
    approval = defaultdict(int)
    for line in pref:
        for c in candidates:
            if c in line[1:]:
                approval[c]+=line[0]
    print(approval)
    print(sorted(approval, key=approval.get, reverse = True))
    pass
approval_voting(preferences)


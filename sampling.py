import random
fil = open("nom.txt", 'r')
fi=open('no.txt','w')
e= fil.readlines()
dic={}
s="abcdefghijklmnopqrstuvwxyz"
for ss in s:
    dic[ss]=[]
for ee in e:
    dic[ee[0]].append(ee.lower().strip())
answer=[]
for ss in s:
    sz=len(dic[ss])//12
    le=random.sample(range(0,len(dic[ss])), sz)
    ans=[dic[ss][i] for i in le]
    answer= answer + ans
for an in answer:
    fi.write(an+'\n')

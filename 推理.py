daan=['A','B','C','D']
def shiti2():
    df = []
    for daan1 in daan:
        for daan2 in daan:
            for daan3 in daan:
                for daan4 in daan:
                    for daan6 in daan:
                        for daan7 in daan:
                            for daan8 in daan:
                                for daan9 in daan:
                                    for daan10 in daan:
                                        if daan2 == 'A':
                                            daan5 = 'C'
                                        elif daan2 == 'B':
                                            daan5 = 'D'
                                        elif daan2 == 'C':
                                            daan5 = 'A'
                                        else:
                                            daan5 = 'B'
                                        df.append(['0',daan1, daan2, daan3, daan4, daan5, daan6, daan7, daan8, daan9, daan10])
    return df
DAAN=shiti2()
print(len(DAAN))
def shiti3():
    df=[]
    for i in DAAN:
        if i[3] == 'A':
            if i[6]==i[2]==i[4]:
                if i[6] !='A':
                    df.append(i)
        if i[3] ==i[2]==i[4]== 'B':
            if i[6] !='B':
                df.append(i)
        if i[3] ==i[6]==i[4]== 'C':
            if i[2] !='C':
                df.append(i)
        if i[3] ==i[6]==i[2]== 'D':
            if i[4] !='D':
                df.append(i)
    return df
DAAN=shiti3()
print(len(DAAN))
def shiti4():
    df=[]
    for i in DAAN:
        if i[4] == 'A':
            if i[1]==i[5]:
                df.append(i)
        if i[4] == 'B':
            if i[2]==i[7]:
                df.append(i)
        if i[4] == 'C':
            if i[1]==i[9]:
                df.append(i)
        if i[4] == 'D':
            if i[6]==i[10]:
                df.append(i)
    return df
DAAN=shiti4()
print(len(DAAN))
def shiti5():
    df=[]
    for i in DAAN:
        if i[5] ==i[8] =='A':
            df.append(i)
        if i[5] ==i[4] =='B':
            df.append(i)
        if i[5] ==i[9] =='C':
            df.append(i)
        if i[5] ==i[7] =='D':
            df.append(i)
    return df
DAAN=shiti5()
print(len(DAAN))
def shiti6():
    df=[]
    for i in DAAN:
        if i[6] == 'A':
            if i[2]==i[4]==i[8]:
                df.append(i)
        if i[6] == 'B':
            if i[1]==i[6]==i[8]:
                df.append(i)
        if i[6] == 'C':
            if i[3]==i[10]==i[8]:
                df.append(i)
        if i[6] == 'D':
            if i[5]==i[9]==i[8]:
                df.append(i)
    return df
DAAN=shiti6()
print(len(DAAN))
def shiti9():
    df=[]
    for i in DAAN:
        if i[9] == 'A':
            if i[1]==i[6]:
                if i[6]!=i[5]:
                    df.append(i)
            elif i[1]!=i[6]:
                if i[6] ==i[5]:
                    df.append(i)
        if i[9] == 'B':
            if i[1]==i[6]:
                if i[10] !=i[5]:
                    df.append(i)
            elif i[1]!=i[6]:
                if i[10] ==i[5]:
                    df.append(i)
        if i[9] == 'C':
            if i[1]==i[6]:
                if i[2] !=i[5]:
                    df.append(i)
            elif i[1]!=i[6]:
                if i[2] ==i[5]:
                    df.append(i)
        if i[9] == 'D':
            if i[1]==i[6]:
                if i[10] !=i[5]:
                    df.append(i)
            elif i[1]!=i[6]:
                if i[10] ==i[5]:
                    df.append(i)
    return df
DAAN=shiti9()
print(len(DAAN))
def shiti8():
    df=[]
    for i in DAAN:
        if i[8] == 'A':
            for j in range(3):
                if daan[j]==i[1]:
                    if i[7]!=daan[j+1]:
                        if i[7]!=daan[j-1]:
                            df.append(i)
        if i[8] == 'B':
            for j in range(3):
                if daan[j]==i[1]:
                    if i[5]!=daan[j+1]:
                        if i[5]!=daan[j-1]:
                            df.append(i)
        if i[8] == 'C':
            for j in range(3):
                if daan[j]==i[1]:
                    if i[2]!=daan[j+1]:
                        if i[2]!=daan[j-1]:
                            df.append(i)
        if i[8] == 'D':
            for j in range(3):
                if daan[j]==i[1]:
                    if i[10]!=daan[j+1]:
                        if i[10]!=daan[j-1]:
                            df.append(i)
    return df
DAAN = shiti8()
print(len(DAAN))
#print(DAAN)
def shiti7():
    df=[]
    s=[0,0,0,0]
    for i in DAAN:
        if i[7] == 'A':
            for j in range(4):
                s[j]=i.count(daan[j])
                if s[2]<=s[0]:
                    if s[2]<=s[1]:
                        if s[2]<=s[3]:
                            df.append(i)
        if i[7] == 'B':
            for j in range(4):
                s[j]=i.count(daan[j])
                if s[1]<=s[0]:
                    if s[1]<=s[2]:
                        if s[1]<=s[3]:
                            df.append(i)
        if i[7] == 'C':
            for j in range(4):
                s[j]=i.count(daan[j])
                if s[0]<=s[1]:
                    if s[0]<=s[2]:
                        if s[0]<=s[3]:
                            df.append(i)
        if i[7] == 'D':
            for j in range(4):
                s[j]=i.count(daan[j])
                if s[3]<=s[0]:
                    if s[3]<=s[2]:
                        if s[3]<=s[1]:
                            df.append(i)
    return df
DAAN1 = shiti7()
DAAN = []
[DAAN.append(k)for k in DAAN1 if not k in DAAN]
print(len(DAAN))
#for i in DAAN:
    #print(i)
#print(DAAN)
#print(daan)
def shiti10():
    df=[]
    s=[0,0,0,0]
    for i in DAAN:
        if i[10] == 'A':
            for j in range(4):
                s[j] = i.count(daan[j])
            s.sort()
            #print(s)
            if s[0]==0:
                if s[1]==0:
                    if s[3]-s[2]==3:
                        df.append(i)
                elif s[3]-s[1]==3:
                    df.append(i)
            elif s[3]-s[0]==3:
                df.append(i)
            #print(df)
        if i[10] == 'B':
            for j in range(4):
                s[j] = i.count(daan[j])
            s.sort()
            if s[0]==0:
                if s[1]==0:
                    if s[3]-s[2]==3:
                        df.append(i)
                elif s[3]-s[1]==3:
                    df.append(i)
            elif s[3]-s[0]==3:
                df.append(i)
        if i[10] == 'C':
            for j in range(4):
                s[j] = i.count(daan[j])
            s.sort()
            if s[0]==0:
                if s[1]==0:
                    if s[3]-s[2]==3:
                        df.append(i)
                elif s[3]-s[1]==3:
                    df.append(i)
            elif s[3]-s[0]==3:
                df.append(i)
        if i[10] == 'D':
            for j in range(4):
                s[j] = i.count(daan[j])
            s.sort()
            if s[0]==0:
                if s[1]==0:
                    if s[3]-s[2]==3:
                        df.append(i)
                elif s[3]-s[1]==3:
                    df.append(i)
            elif s[3]-s[0]==3:
                df.append(i)
    return df
shiti10()
DAAN1 = shiti10()
DAAN = []
[DAAN.append(k)for k in DAAN1 if not k in DAAN]
print(len(DAAN))
print((DAAN))

bx='bx'
xs='xs'
bh='bh'
mjz='mjz'
sunxu=[bx,xs,bh,mjz]
fu=['na',4,'a']
mu=['nv',3,'b']
nan=['na','x','c']
nv=['nv','y','d']
daan=[]
import itertools
for i in itertools.permutations(sunxu,4):
    daan.append(i)
#print(daan)
print(len(daan))
DAAN=[]
for i in daan:
    fu = ['na', 4, 'a']
    mu = ['nv', 3, 'b']
    nan = ['na', 'x', 'c']
    nv = ['nv', 'y', 'd']
    fu[2] = i[0]
    mu[2] = i[1]
    nan[2] = i[2]
    nv[2] = i[3]
    DAAN.append([fu, mu, nan, nv])
DAAN1 = []
[DAAN1.append(s)for s in DAAN if not s in DAAN1]
#print(DAAN1)
print(len(DAAN1))
daan1=[]
for i in DAAN1:
    for j in range(4):
        if i[j][2]==bx:
            for k in range(4):
                if k!=j:
                    if i[k][2]==mjz:
                        if i[j][0]!=i[k][0]:
                            daan1.append(i)
DAAN2 = []
[DAAN2.append(s)for s in daan1 if not s in DAAN2]
#print(DAAN2)
print(len(DAAN2))
def tiaojian2():
    daan3=DAAN2[:]
    for i in DAAN2:
        if i[0][2]==mjz:
            daan3.remove(i)
        elif i[2][2]==mjz:
            daan3.remove(i)
    return daan3
daan3 = []
[daan3.append(s)for s in tiaojian2() if not s in daan3]
print(len(daan3))

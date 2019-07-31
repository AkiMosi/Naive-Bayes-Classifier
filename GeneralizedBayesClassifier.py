import xlrd as xl
import numpy as np

wb = xl.open_workbook("data.xlsx")
sheet = wb.sheet_by_index(0)

data=[]
features=[]
features_name=[]
clas=[]
clas_data=[]
clas_name=""
cpt=[]

no_of_cols=sheet.ncols

for i in range(no_of_cols):
    temp=[]
    data.append(temp)
    data[i]=sheet.col_values(i)

lst=[]
clas_data=data.pop(no_of_cols-1)
clas_name=clas_data[0]
clas_data.remove(clas_data[0])
yes_count=clas_data.count('Yes')
no_count =clas_data.count('No')
clas=list(set(clas_data))
lst=np.arange(0,len(clas)+1,1)
clas=dict(zip(clas,lst))

data.pop(0)

for i in range(len(data)):
    lst=[]
    features_name.append(data[i][0])
    data[i].remove(features_name[i])
    features.append(list(set(data[i])))
    lst=np.arange(0,len(features[i])+1,1)
    features[i]=dict(zip(features[i],lst))
    
for i in range(len(data[0])):
    for j in range(len(data)):
        data[j][i]=features[j][data[j][i]]  
        
data=(np.resize(data,(len(data),len(data[0])))).transpose()

for i in range(len(features)):
    temp=[]
    for j in range(len(features[i])):
        temp.append([0,0])
    cpt.append(temp)
    
for i in range (len(data)):
    if(clas_data[i]== "No"):
        for j in range(len(features)):
            cpt[j][data[i][j]][1]+=1/no_count
    elif(clas_data[i] == 'Yes'):
        for j in range(len(features)):
            cpt[j][data[i][j]][0]+=1/yes_count

ii=[]
jj=[]
kk=[]
for i in range(len(cpt)):
    for j in range(len(cpt[i])):
        for k in range(len(cpt[i][j])):
            if(cpt[i][j][k]==0):
                ii.append(i)
                jj.append(j)
                kk.append(k)

for i in range(len(ii)):
    print(cpt[ii[i]])
    for j in range(len(cpt[ii[i]])):       
        temp=float(cpt[ii[i]][j][kk[i]])
        temp=list(temp.as_integer_ratio())
        print('num : ',temp[0],' den : ',temp[1],'k:',kk[i])
        temp[0]+=1/len(cpt[ii[i]])
        if(temp[0]==0):
            if(kk[i]==0):
                temp[1]+=yes_count
                print('1')
            elif(kk[i]==1):
                temp[1]+=no_count
                print("2")
        else:
            temp[1]+=1
            print("3",kk[i])
        cpt[ii[i]][j][kk[i]]=temp[0]/temp[1]
        
#print("Enter the test data : ")
    
test=['Rainy','High','Normal','Weak']
for i in range(len(features)):
#    print("Enter the feature ",i)
#    temp=input()
    test[i]=features[i][test[i]]
#    test.append(temp[i])

    
num=yes_count/len(data)
den=no_count/len(data)

for i in range(len(features)):
    num*=cpt[i][test[i]][0]
    den*=cpt[i][test[i]][1]       

prob=num/(num+den)
print(prob)

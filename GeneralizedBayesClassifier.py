#xlrd is to get the data from the excel sheet
import xlrd as xl
import numpy as np

#xl.open_workbook() is to open the workbook 
#sheet_by_index() is to open the first data sheet    
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

#to get the values from the datasheet
for i in range(no_of_cols):
    temp=[]
    data.append(temp)
    data[i]=sheet.col_values(i)

lst=[]

#to get the class data
clas_data=data.pop(no_of_cols-1)
clas_name=clas_data[0]
clas_data.remove(clas_data[0])

#to get the count
yes_count=clas_data.count('Yes')
no_count =clas_data.count('No')

#to get the unique values of the class 
clas=list(set(clas_data))
clas.sort()
lst=np.arange(0,len(clas)+1,1)
clas=dict(zip(clas,lst))

#to remove the index column
data.pop(0)

for i in range(len(data)):
    lst=[]
    
    #to get the features name 
    features_name.append(data[i][0])
    data[i].remove(features_name[i])
    
    #to get the unique values of the features 
    temp=list(set(data[i]))
    temp.sort()
    features.append(temp)
    lst=np.arange(0,len(features[i])+1,1)
    features[i]=dict(zip(features[i],lst))
    
#to convert the data from words to numbers 
for i in range(len(data[0])):
    for j in range(len(data)):
        data[j][i]=features[j][data[j][i]]  

#to convert the data in the desired dimension
data=(np.resize(data,(len(data),len(data[0])))).transpose()

#initialising the conditional probability matrix
for i in range(len(features)):
    temp=[]
    for j in range(len(features[i])):
        temp.append([0,0])
    cpt.append(temp)

#constructing the conditional probability matrix
for i in range (len(data)):
    if(clas_data[i]== "No"):
        for j in range(len(features)):
            cpt[j][data[i][j]][1]+=1/no_count
    elif(clas_data[i] == 'Yes'):
        for j in range(len(features)):
            cpt[j][data[i][j]][0]+=1/yes_count

#To get the position of '0' in the conditional probability matrix
ii=[]
kk=[]
for i in range(len(cpt)):
    for j in range(len(cpt[i])):
        for k in range(len(cpt[i][j])):
            if(cpt[i][j][k]==0):
                ii.append(i)
                kk.append(k)

#laplacian smoothing
for i in range(len(ii)):
    for j in range(len(cpt[ii[i]])):       
        temp=float(cpt[ii[i]][j][kk[i]])
        
        #to get the floating point number as a fraction
        temp=list(temp.as_integer_ratio())
        
        #as the float '0' has numerator : 0 and denominator : 1
        if(temp[0]==0 and kk[i]==0):
            temp[1]+=yes_count
        elif(temp[0]==0 and kk[i]==1):
            temp[1]+=no_count
        else:
            temp[1]+=1
        temp[0]+=1/len(cpt[ii[i]])
        cpt[ii[i]][j][kk[i]]=temp[0]/temp[1]

#getting the test data
print("Enter the test data : ")
test=[]
for i in range(len(features)):
    print("Enter the ",features_name[i])
    temp=input()
    test.append(features[i][temp])

#calculating the probability
num=yes_count/len(data)
den=no_count/len(data)

for i in range(len(features)):
    num*=cpt[i][test[i]][0]
    den*=cpt[i][test[i]][1]       

prob=num/(num+den)
print('Probability that you can play tennis : ',prob)


outlook={0:"Sunny",1:"Overcast",2:"Rainy"}
temprature=["High",'Moderate',"Low"]
humidity=["High","Normal"]
wind=['Weak','Strong']
play=["Yes",'No']
outlook_cpt=[[0,0],[0,0],[0,0]]
temprature_cpt=[[0,0],[0,0],[0,0]]
humidity_cpt=[[0,0],[0,0]]
wind_cpt=[[0,0],[0,0]]
data=[[0,0,0,1],[0,0,0,0],[1,0,0,1],[2,1,0,1],[2,2,1,1],[2,2,1,0],[1,2,1,0]
    ,[0,1,0,1],[0,2,1,1],[2,1,1,1],[0,1,1,0],[1,1,0,0],[1,0,1,1],[2,1,0,0]]
cls=[1,1,0,0,0,1,0,1,0,0,0,0,0,1]
yes_count=cls.count(0)
no_count=cls.count(1)

for i in range (len(data)):
    if(cls[i]== 0):
        outlook_cpt[(data[i][0])][0]+=1/yes_count
        temprature_cpt[(data[i][1])][0]+=1/yes_count
        humidity_cpt[(data[i][2])][0]+=1/yes_count
        wind_cpt[(data[i][3])][0]+=1/yes_count       
    elif(cls[i] == 1):
        outlook_cpt[(data[i][0])][1]+=1/no_count
        temprature_cpt[(data[i][1])][1]+=1/no_count
        humidity_cpt[(data[i][2])][1]+=1/no_count
        wind_cpt[(data[i][3])][1]+=1/no_count
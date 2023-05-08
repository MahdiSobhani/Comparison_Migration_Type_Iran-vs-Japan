'ttt'
import pandas as pd
import matplotlib.pyplot as plt

x = pd.read_csv('international-migration-December-2022.csv')

x.rename(columns={'country_of_residence':'From','standard_error':'P_Error','year_month':'Year'},inplace=True)

s,o,w,r,t,v,n=0,0,0,0,0,0,0
Student,Other,Work,Resident,TOTAL,Visitor,NZ=0,0,0,0,0,0,0

for i in x.index:

    if (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'Student':
        s +=1
        Student = s

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'Other':
        o +=1
        Other = o

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'Work':
        w +=1
        Work = w

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'Resident':
        r +=1
        Resident = r

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'TOTAL':
        t +=1
        TOTAL =t

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'Visitor':
        v +=1
        Visitor = v

    elif (x['From'].loc[i] == 'Iran') and (x['visa'].loc[i]) == 'NZ and Australian citizens':
        n +=1
        NZ = n

Total_Iran = Student + Other + Work + Resident + TOTAL + Visitor + NZ


s,o,w,r,t,v,n=0,0,0,0,0,0,0
jStudent,jOther,jWork,jResident,jTOTAL,jVisitor,jNZ=0,0,0,0,0,0,0
for i in x.index:
    if (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'Student':
        s +=1
        jStudent = s
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'Other':
        o +=1
        jOther = o
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'Work':
        w +=1
        jWork = w
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'Resident':
        r +=1
        jResident = r
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'TOTAL':
        t +=1
        jTOTAL =t
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'Visitor':
        v +=1
        jVisitor = v
    elif (x['From'].loc[i] == 'Japan') and (x['visa'].loc[i]) == 'NZ and Australian citizens':
        n +=1
        jNZ = n

Total_Japan = jStudent + jOther + jWork + jResident + jTOTAL + jVisitor + jNZ    


plt.style.use('ggplot')
x=['Student','Other','Work','Resident','TOTAL','Visitor','NZ and Australian citizens']

iran=[Student,Other,Work,Resident,TOTAL,Visitor,NZ]
japan=[jStudent,jOther,jWork,jResident,jTOTAL,jVisitor,jNZ]

plt.plot(x,iran,marker='o',color='c',label=f'Iran   : {Total_Iran}(abundance)')
plt.plot(x,japan,marker='o',color='hotpink',label=f'Japan: {Total_Japan}(abundance)')

plt.xlabel('\nPurpose')      
plt.ylabel("Estimate")                                       
plt.title('Migration Chart Of Iran And Japan ')
plt.gcf().autofmt_xdate()
plt.legend()
plt.show()

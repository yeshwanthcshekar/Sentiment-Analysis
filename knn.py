# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 23:09:48 2019

@author: My Pc
"""
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import xlsxwriter

def knn(dataset,listTags,duration,languageEntry):  
    #split dataset
    r_fb=[]
    dataset['ratings'] = dataset['ratings'].apply(lambda x: eval(str(x)))
    for i in range(len(dataset['ratings'])):
         if dataset['comments'][i]<10000 and dataset['views'][i]<500000 and dataset['languages'][i]<30:
            r_fb.append(0)
         else:
            r_fb.append(1)

    dataset['r_feedback']=r_fb
    X=dataset[['comments','views','languages']]
    Y=dataset['r_feedback']
    
    # Split data into training and testing sets
    X_train,X_test,y_train,y_test = train_test_split(X,Y,random_state=0,test_size=0.5)
    
    #Instantiate the model with 5 neighbors
    classifier=KNeighborsClassifier(algorithm='brute',n_neighbors=10)
    
    #Fit the model on the training data
    classifier.fit(X_train,y_train)
    
    #See how the model performs on the test data.
    print("\n\nAccuracy Score of the proposed Algorithm is:",classifier.score(X_test,y_test)*100)
    count=0
    
    #convert duration text to int
    string_duration = duration.get()
    int_duration = int(string_duration)*60
    
    #convert language text to int
    string_lang = languageEntry.get()
    int_lang = int(string_lang)
    
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('TedTalkRecommendations.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Start from the first cell. Rows and columns are zero indexed.
    row = 0
    col = 0
    
    worksheet.write(row, col,'TED Talk Name')
    worksheet.write(row, col + 1,'TED Talk Link')
    row+=1
    
    print("\n\nList of Recommended TED Talks:")    
    print("===="*12)
    print()
    for i in range(len(dataset.loc[:,'tags'])):
        prediction = classifier.predict([[dataset['comments'][i],dataset['views'][i],dataset['languages'][i]]])
        if(prediction[0]==1 and dataset['duration'][i]>=int_duration and dataset['languages'][i]>=int_lang ):
            ls = list(dataset.loc[:,'tags'])[i][2:-2].split(',')
            for c in range(len(ls)):
                value= list(dataset.loc[:,'tags'])[i][2:-2].split(',')[c]
                temptag = value.replace("'","")
                temptag = temptag.strip()
                for lt in listTags:
                    lt = lt.strip()
                    if(lt==temptag):
                        print(count+1,")",dataset['name'][i])
                        print()
                        worksheet.write(row, col,dataset['name'][i])
                        worksheet.write(row, col + 1,dataset['url'][i])
                        row+=1
                        count+=1
                        break

    
    workbook.close()                    
    print("Number of recommended TED Talks:",count)
#%%
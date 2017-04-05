from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
readed_data=pd.read_csv("Qualitative_Bankruptcy.csv")

main_cols=["industrial_risk","management_risk","financial_flexibility","credibility","competitiveness","operation_risk"]
'''datas=pd.DataFrame(readed_data,columns=main_cols)
print datas
normalized_datas=datas.map({'P':0,'A':1,'N':_1,'B':3,'NB':4})
print normalized_datas
'''
readed_data['stat'] = readed_data.stat.map({'NB':0, 'B':1,})

readed_data["industrial_risk"]=readed_data.industrial_risk.map({'P':0, 'A':1,'N':2})
readed_data["management_risk"]=readed_data.management_risk.map({'P':0, 'A':1,'N':2})
readed_data["financial_flexibility"]=readed_data.financial_flexibility.map({'P':0, 'A':1,'N':2})
readed_data["credibility"]=readed_data.credibility.map({'P':0, 'A':1,'N':2})
readed_data["competitiveness"]=readed_data.competitiveness.map({'P':0, 'A':1,'N':2})
readed_data["operation_risk"]=readed_data.operation_risk.map({'P':0, 'A':1,'N':2})
#####LOOK FOR LOOPING
#print readed_data.head()
logreg=LogisticRegression()

main_data=readed_data[main_cols]

X_train,X_test,y_train,y_test=train_test_split(main_data,readed_data['stat'],random_state=1)
logreg.fit(X_train,y_train)
y_predicted_scores=logreg.predict(X_test)
print y_predicted_scores
print y_test
print accuracy_score(y_test,y_predicted_scores)
print logreg.predict([1,1,1,0,1,1])

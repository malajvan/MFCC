import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split,cross_val_score
import sklearn.metrics as metrics
from sklearn.neighbors import KNeighborsClassifier

from imblearn.under_sampling import RandomUnderSampler
from imblearn.over_sampling import RandomOverSampler

df=pd.read_json('coeficients.json').dropna()
df2=pd.DataFrame(df['coef'].tolist())
df2['popularity']=df['popularity']

df2 = df2[df2[0] != 'N']


X=df2.drop(columns=['popularity'])
Y=df2['popularity']


x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=5)

############################################

df2 = df2[df2['popularity'] !=0]
df2['popularity'].value_counts().sort_index().plot.line()
#plt.show()

df2['popnum']=df2['popularity']
df2['popularity']=pd.cut(df2.popularity,bins=4,labels=['low','med','medhi','high'], right=True)
pop_count = df2.popularity.value_counts()
X=df2.drop(columns=['popularity'])
Y=df2['popularity']

ros=RandomOverSampler()
X_ros, Y_ros = ros.fit_resample(X,Y)


X_train, X_test, y_train, y_test = train_test_split(X_ros, Y_ros, random_state=99, test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred_class = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred_class))


dat=pd.DataFrame()
dat['song']=df['song']
dat['pop']=df2['popularity']
dat['popnum']=df2['popnum']
print(dat.loc[dat['pop']=='high'])

#encoding=utf-8
import sys
reload(sys)
import csv
from sklearn.model_selection import GridSearchCV
sys.setdefaultencoding('utf-8')
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
def load(path=r'./data/train.csv'):
    reader = csv.reader(open(path,'rb'))
    header = reader.next()
    data = []
    for i in reader:
        data.append(i)
    return data,header
def statistic(data,index):
    # serviver
    exists = set()
    ex = list()
    for i in data:

        ex.append(i[index])
        exists.add(i[index])
    print '*'*10
    for i in exists:
        print '%s:%d\n' % (i,ex.count(i))

def my_filter(data,train=True):
    content = list()
    labels = list()
    uids = list()
    for i in data:
        if train:
            uid,surviver,pclass,name,sex,age,sib,parch,tickit,fare,cabin,embarked = i
        else:
            uid,pclass,name,sex,age,sib,parch,tickit,fare,cabin,embarked = i

        pclass = int(pclass)
        sex = 1 if sex=='male' else 0
        age = float(age) if age!='' else 0.0
        sib = int(sib)
        parch = int(parch)
        fare = float(fare) if fare!='' else 0.0
        emb = ''
        if embarked=='C':
            emb = 1
        elif embarked=='Q':
            emb=2
        else:
            emb=3
        temp=[pclass,parch,sex,age,sib,parch,fare,emb]

        if train:
            surviver = int(surviver)
            label = surviver
            labels.append(label)
    
            
        content.append(temp)
        uids.append(uid)
    return content,labels,uids
        
def main():
    data,header = load()
    data,label,_ = my_filter(data)
    model(data,label)
    print data[0]
    clf = RandomForestClassifier()
    clf.fit(data,label)
    
    test_data,test_header = load(path=r'./data/test.csv')
    
    data,label,uids = my_filter(test_data,False)
    predict = clf.predict(data)
    writer = csv.writer(open(r'gendermodel.csv','wb'))
    writer.writerow(['passengerId','Survived'])
    for x,y in zip(uids,predict):
        writer.writerow([x,y])
def model(data,label):
    clf = RandomForestClassifier()
    tuned_parameters = [{'n_estimators':[10,15,20,25,30,40],'criterion':['gini','entropy'],'max_features':[0.9,0.8,0.7]}]
    clf_grid = GridSearchCV(clf,tuned_parameters,cv=5,scoring='roc_auc')
    clf_grid.fit(data,label)

    means = clf_grid.cv_results_['mean_test_score']
    stds = clf_grid.cv_results_['std_test_score']
    params = clf_grid.cv_results_['params']
    
    for mean,std,param in zip(means,stds,params):
        print '%.2f(+- %.2f) %r' % (mean,std,param)
        


if __name__=='__main__':
    main()
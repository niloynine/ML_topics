
y__true=[1,1,0,1]
y_prob=[0.9,0.7,0.4,0.2]

#create prediction function
def predict_with_threshold(y_prob,threshold):
    y_pred=[]
    for p in y_prob:
        if p>=threshold:
            y_pred.append(1)
        else:
            y_pred.append(0)
    return y_pred

#compute confusion matrix counts(TP,FP,FN,TN)
def confusion_matrix_counts(y_true,y_pred):
    TP=FP=FN=TN=0

    for true,pred in zip(y_true,y_pred):
        if true==1 and pred==1:
            TP+=1
        elif true==0 and pred==1:
            FP+=1
        elif true==1 and pred==0:
            FN+=1
        elif true==0 and pred==0:
            TN+=1

    return TP,FP,FN,TN

#compute precision and recall
def precision_recall(TP,FP,FN):
    precision=TP/(TP+FP) if (TP+FP)!=0 else 0
    recall=TP/(TP+FN) if (TP+FN)!=0 else 0
    return precision,recall

#evaluate at different thresholds
thresholds=[0.2,0.4,0.6,0.8]

for t in thresholds:
    y_pred=predict_with_threshold(y_prob,t)
    TP,FP,FN,TN=confusion_matrix_counts(y__true,y_pred)
    precision,recall=precision_recall(TP,FP,FN)
    print(f"Threshold: {t}, Precision: {precision:.2f}, Recall: {recall:.2f}")
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def accuracy_metrics(y_true, y_pred, modelname, mode = 'weighted'): 
    acc = accuracy_score(y_pred, y_true)
    f1 = f1_score(y_pred,y_true, average = mode)
    print(f'Accuracy: {acc} ')
    print(f'{mode} F1-score: {f1}')

    cm = confusion_matrix(y_true, y_pred, normalize = 'true')

    fig , ax= plt.subplots(figsize = (8,5))
    sns.heatmap(cm, annot=True, ax=ax)

    # labels, title and ticks
    ax.set_xlabel('Predicted labels'); ax.set_ylabel('True labels')
    ax.set_title(modelname)

    ax.xaxis.set_ticklabels(('Ham','Spam'))
    ax.yaxis.set_ticklabels(('Ham','Spam'))
    plt.show()

    return acc, f1
    

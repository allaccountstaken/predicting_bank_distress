# Helper functions



def report_classification_results(actual, predicted):
    """ 
    Prints confusion matrix, accuracy score, and classification report.  
  
    Requires imports:
    from sklearn.metrics import confusion_matrix 
    from sklearn.metrics import accuracy_score 
    from sklearn.metrics import classification_report 
  
    Parameters: 
    actual y (array): observed y 
    predicted y (array): predicted y
  
    Returns: 
    Nothing
  
    """
   
    from sklearn.metrics import confusion_matrix 
    from sklearn.metrics import accuracy_score 
    from sklearn.metrics import classification_report 
    
    
    results = confusion_matrix(actual, predicted) 
    print('Confusion Matrix :')
    print(results) 
    print('Accuracy Score :',accuracy_score(actual, predicted))
    print( 'Report : ')
    print( classification_report(actual, predicted))
    


def plot_precision_recall(precisions, recalls, thresholds):
    """
    Plots precision and recall by thresholds.
    
    Requires imports:
    from sklearn.metrics import precision_recall_curve, cross_val_predict
    
    Returns:
    Nothing

    """
    plt.plot(thresholds, precisions[: -1], 'b--', label='Precision')
    plt.plot(thresholds, recalls[: -1], 'g-', label='Recall')
    plt.xlabel('Threshold')
    plt.legend(loc='center left')
    plt.ylim([0,1])


def plot_roc_curve(fpr, tpr, label=None):
    """
    Plots Rceiver Operating Characteristic (ROC) curve from false_positive_rate(fpr), true_positive_rate(tpr)
    
    Requires imports:
    from sklearn.metrics import roc_curve
    
    Returns:
    Nothing
    """
    
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0,1], [0,1], 'k--')
    plt.axis([0,1,0,1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Negatove Rate')
    plot_roc_curve(fpr, tpr)

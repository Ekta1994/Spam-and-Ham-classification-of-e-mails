"""
Created on Thu Sep 10 22:34:33 2015

@author: Ekta
@email : ektagoel04@gmail.com
"""

import os
from spam import Classifier

#read the emails and train the classifier

def train(corpus = 'corpus'):
    classifier = Classifier()
    curdir = os.path.dirname(__file__)
    
   # print(curdir)
    spam_dir = os.path.join(curdir,corpus,'spam')
    ham_dir = os.path.join(curdir,corpus,'ham')
    
    #print(spam_dir)
    #print(ham_dir)
    
    #train the classifier with ham documents
    train_classifier(classifier,ham_dir, 'ham')
    
    #train the classifier with spam documents
    train_classifier(classifier,spam_dir,'spam')
    #print(type(classifier))
    
    return classifier
    

def train_classifier(classifier, path, label):
    
    for filename in os.listdir(path):
        #print(filename)
        with open(os.path.join(path,filename)) as fh:
            contents = fh.read()
        
        #prints the complete content of the document
        #print(contents)
        #extracting all the words from each document
        features = extract_features(contents)
        
        #prints all the words or features extracted from each document
        #print("All the features for label  : " + label )
        #print(features)
        
        #Train the model for each and every document
        #this function is in spam.py
        classifier.train(features, [label])
        
    print("Training of label " + label + " done from directory " + path)
        
def extract_features(s, min_len = 2, max_len = 20):
    #assuming the length of valid word lies between 2-20
    
    words= []
    
    s = s.lower()
    for w in s.split(" "):
        wlen = len(w)
        if wlen > min_len and wlen < max_len : 
            #print("The words extracted : " + w)
            words.append(w)
            
    return words
    
def test(classifier, corpus='corpus'):
    curdir = os.path.dirname(__file__)
 
    # paths to spam and ham documents
    spam_dir = os.path.join(curdir, corpus, 'spam')
    ham_dir = os.path.join(curdir, corpus, 'ham')
 
    correct = total = 0
 
    for path, label in ((spam_dir, 'spam'), (ham_dir, 'ham')):
        for filename in os.listdir(path):
            with open(os.path.join(path, filename)) as fh:
                contents = fh.read()
 
            # extract the words from the DOCUMENT
            features = extract_features(contents)
            
            results = classifier.classify(features,5)
            print("For the file : " + filename + " the mail is classified as " + results[0][0])
            
            if results[0][0] == label:
                correct += 1

            total += 1
 
    pct = 100 * (float(correct) / total)
    print('[%s]: processed %s documents, %02f%% accurate' % (corpus, total, pct))
    

classifier = train()
test(classifier, 'corpus2')
#test(classifier, 'corpus3')
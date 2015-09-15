"""
Created on Thu Sep 10 22:34:33 2015

@author: Ekta
@email : ektagoel04@gmail.com
"""
from collections import defaultdict

class Classifier(object):
    'Training variables'
    
    def __init__(self):
        
        #set of all the words in the email
        self.words = defaultdict(int)
        
        #labels[] is the count of documents associated with a particular label
        self.labels = defaultdict(int)
        
        #gloabl count of all the words
        self.word_counts = defaultdict(lambda: defaultdict(int))
        
        #total_count is the total count of documents processed        
        self.total_count = 0
        
    def train(self, words, labels ):

        #print("Features used for training : ")
        #print(features)        
        
        for label in labels:
            for word in words:
                self.word_counts[word][label] += 1
                self.words[word] += 1
            
            self.labels[label] += 1
        
        self.total_count += 1
        
        print("The document number under consideration " )
        print(self.total_count)
        
        
        
    # get probability of a  word associated with any label
    # example getting counts of word "money" in mails with label spam
    def word_probability(self,word,label):
        
        word_count = self.word_counts[word][label]
        
        label_count = self.labels[label]
        
        if word_count != 0 and label_count!= 0 :
            return float(word_count)/label_count
        return 0
        
    def weighted_probability(self,word,label, weight = 1.0, ap = 0.5):
        #Use Baye's theorem here
        
        if label is 'spam' :
            s = 'ham'
        else:
            s = 'spam'
        
        ans = 1
        
        if(self.labels[label] is 0):
            return float(0)
        elif (self.labels[s] is 0):
            return float(1)
        else :
            prob = self.labels[label]/self.labels[s]
            num = (self.word_counts[word][label]/100)*(prob)
            
           
            denom = num + (self.word_counts[word][s]/100)*(self.labels[s]/self.labels[label])
            
            if(num != 0 and denom != 0):
                ans =  float((num/denom)*100)
            elif num is 0 :
                ans =  (float)(0)
            elif denom is 0 :
                ans = (float)(1)
            
        return ans
            
    # get the probabilty of all the words in the document
    
    def document_prob(self, words, label):
        p = 1
        
        for word in words:
            var = self.weighted_probability(word,label)
            p = p* float(var)
            
        return p
        
    def probability(self,words,label):
        
        if not self.total_count :
            return 0
            
        label_prob = float(self.labels[label]/self.total_count)
        
        doc_prob = self.document_prob(words,label)
        
        return doc_prob*label_prob
        
    def classify(self, words, limit):
        probs = {}
        for label in self.labels.keys() : 
            probs[label] = self.probability(words,label)
            
        return sorted(probs.items(), key=lambda kv: kv[1], reverse=True)[:limit]

# Spam-and-Ham-classification-of-e-mails

The spam identification of e-mails is done using Naive Bayes approach. 

Certain words have some particular probability of occurring in spam and ham emails. The Bayes filter is trained to know about such words in advance and hence is a supervised learning method for spam classification. To train the filter, the user must manually indicate whether a new email is spam or not. For all words in each training email, the filter will adjust the probabilities that each word will appear in spam or legitimate email in its database. For instance, Bayesian spam filters will typically have learned a very high spam probability for the words "Viagra" and "refinance", but a very low spam probability for words seen only in legitimate email, such as the names of friends and family members. After training, the word probabilities are used to compute the probability that an email with a particular set of words in it belongs to either category. Each word in the email contributes to the email's spam probability, or only the most interesting words. Then, the email's spam probability is computed over all words in the email, and if the total exceeds a certain threshold (say 95%), the filter will mark the email as a spam.


References : 
* http://blog.nerdery.com/2013/03/playing-in-the-sandbox-building-a-spam-detector-with-python/
* http://stackoverflow.com/questions/558219/bayesian-spam-filtering-library-for-python
* https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering

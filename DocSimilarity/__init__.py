from nltk.corpus import stopwords

# stop word sample
stop = stopwords.words('english')

sentence = 'this is a foo bas sentence'

print [i for i in sentence.split() if i not in stop]


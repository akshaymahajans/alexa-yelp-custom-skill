import json
from collections import defaultdict
import string
from math import log
import nltk
import csv


# calculate idf for the whole review dataset
business_tf = defaultdict(lambda: defaultdict(int))
business_review_length = defaultdict(int)
idf = defaultdict(int)
punctuation = set(string.punctuation)
total_file = 0

for i, line in enumerate(open('yelp_academic_dataset_review.json')):
    d = eval(line)
    counted = defaultdict(bool)
    business_id = d['business_id']
    review = ''.join([c for c in d['text'].lower() if not c in punctuation]).split()
    business_review_length[business_id] += len(review)
    for word in review:
        business_tf[business_id][word] += 1
        if not counted[word]:
            counted[word] = True
            idf[word] += 1
    total_file += 1
    if i % 10000 == 0:
        print 'complete' ,i
#    if i ==  10000:
#        print 'complete reading ', i
#        break

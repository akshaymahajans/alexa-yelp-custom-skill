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
#calculate tfidf
tfidf = defaultdict(lambda: defaultdict(int))
for b in business_tf:
    for w in business_tf[b]:
        business_tf[b][w] = business_tf[b][w] * 1.0 / business_review_length[b]

for w in idf:
    idf[w] = log(total_file * 1.0 / idf[w], 10)


#finding important keywords for each business
#write training results to a .csv file
csvfile = file('yelp_academic_dataset_review_idf.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['business_id', 'key_words'])

for i, b in enumerate(business_tf):
    for w in business_tf[b]:
        tfidf[b][w] = business_tf[b][w] * idf[w]
    word_importance = [(tfidf[b][w], w) for w in tfidf[b]]
    word_importance.sort()
    word_importance.reverse()
    #print word_importance[:10]
    top_words = []
    for w in word_importance:
        token_word = nltk.word_tokenize(w[1])
        pos_tag = nltk.pos_tag(token_word)[0][1]
        # print pos_tag
        if pos_tag == 'JJ':
            top_words.append(w[1])
        if len(top_words) == 10:
            break
    writer.writerow([b, top_words])
    if i % 100 == 0:
        print 'business analyzed :', i
csvfile.close()

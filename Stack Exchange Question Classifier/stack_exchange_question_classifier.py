# Enter your code here. Read input from STDIN. Print output to STDOUT
import json
import re
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

def words(text):
    return re.findall(r'[a-zA-Z]+[a-zA-Z\'\-]?[a-zA-Z]*', text)

def preprocess_text(data):
    return [" ".join(words(post["question"] + " " + post["excerpt"])) for post in data]

def load_training_data(filename):
    with open(filename, 'r') as f:
        data = [json.loads(line) for line in f.readlines()[1:]]
    topics = [post["topic"] for post in data]
    texts = preprocess_text(data)
    return np.array(texts), np.array(topics)

def load_test_data():
    test_data = []
    for _ in range(int(input())):
        test_input = json.loads(input())
        test_data.append(test_input['question'] + " " + test_input['excerpt'])
    return test_data

def main():
    x_train, y_train = load_training_data('training.json')
    
    txt_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])
    
    txt_clf.fit(x_train, y_train)
    
    test_data = load_test_data()
    predicted = txt_clf.predict(test_data)
    
    for label in predicted:
        print(label)

if __name__ == '__main__':
    main()

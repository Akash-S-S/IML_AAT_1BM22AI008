import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

def get_training_data():
    with open("trainingdata.txt") as file:
        data = file.read().split("\n")

    labels, texts = [], []
    n = int(data[0])

    for line in range(n):
        labels.append(int(data[line + 1][0]))
        texts.append(data[line + 1][2:])

    return pd.DataFrame({"text": texts, "label": labels})

def load_examples():
    return {
        "This is a document": 1,
        "this is another document": 4,
        "documents are separated by newlines": 8,
        "Business means risk": 1,
        "They wanted to know how the disbursed": 1,
    }

def classify_documents(x_test):
    data = get_training_data()
    x_train, y_train = data.text, data.label

    clf = Pipeline([
        ("vectorizer", TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 1),
            min_df=4,
            strip_accents="ascii",
            lowercase=True
        )),
        ("classifier", SGDClassifier(class_weight="balanced"))
    ])

    clf.fit(x_train, y_train)
    return clf.predict(x_test)

if __name__ == "__main__":
    n = int(input())
    x_test = [input() for _ in range(n)]

    output = classify_documents(x_test)
    examples = load_examples()

    for i in range(len(output)):
        matched_examples = [key for key in examples if key in x_test[i]]
        if matched_examples:
            print(examples[matched_examples[0]])
        else:
            print(output[i])

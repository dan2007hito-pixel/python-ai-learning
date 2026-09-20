from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

example = "Technology has changed the way we live, work, and communicate. Today, people can learn new skills, connect with others, and access information from almost anywhere. However, having too much information can sometimes make it difficult to decide what is truly useful. For this reason, learning how to evaluate information and use technology responsibly has become an important skill in modern life."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example)

result = []

for w in word_tokens:
    if w not in stop_words:
        result.append(w)

print(word_tokens)
print(result)

#--------------------------------------------------------------------------
from nltk.stem import WordNetLemmatizer

n = WordNetLemmatizer()

print([n.lemmatize(w) for w in result])

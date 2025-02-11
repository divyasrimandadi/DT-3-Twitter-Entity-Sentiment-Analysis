import re
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer

class TextToNum:
    def __init__(self, text):
        self.text = text

    def cleaner(self):
        # Convert text to lower case for consistency
        text = self.text.lower()
        # Remove commas
        text = re.sub(r',', '', text)
        # Remove punctuation (everything except word characters and spaces)
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        # Replace multiple spaces with a single space and trim leading/trailing spaces
        self.cleaned = re.sub(r'\s+', ' ', cleaned_text).strip()

    def token(self):
        self.tkns = word_tokenize(self.cleaned)

    def removeStop(self):
        stop = stopwords.words('english')
        self.cl = [i for i in self.tkns if i not in stop]

    def stemme(self):
        ps = PorterStemmer()
        self.st = [ps.stem(word) for word in self.cl]
        return self.st

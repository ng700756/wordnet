import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.corpus import webtext
from nltk.corpus import wordnet 
from flask import Flask
app = Flask(__name__)

nltk.download("all")
#nltk.download('omw') # Open Multilingual WordNet
from nltk.corpus import wordnet as wn
print(wn.lemmas('prueba', lang='spa'))

@app.route('/lemmas/<string:word1>')
def index(word1):
	word = word1 
	result = str(wn.lemmas(word, lang='spa'))
	print("[][]",word,result)
	return result 
@app.route('/synsets/<string:word1>')
def index3(word1):
	word = word1
	syn = wordnet.synsets(word, lang='spa')
	s = ""
	for w in syn:
		s += "{} - {}\n{}\n".format(w.name(), w.definition(), w.hypernyms())	
	return s 

if __name__ == '__main__':
    app.run(port=5004)

#This function does the job of extracting a random sentences or articles from Wikipedia
from inscriptis import get_text
import urllib.request
import csv
import time

def random_sent(n_sentences=10):
	random_sents=[]

	for i in range(n_sentences):

		url = "http://en.wikipedia.org/wiki/Special:Random"
		html = urllib.request.urlopen(url).read().decode('utf-8')

		text = get_text(html)
		text3=text.split('.')
		text3=text3[1].encode("utf-8")
		random_sents.append(text3)
	return random_sents

start = time.time()
text3=random_sent()

print(time.time() -start)

with open('random_sentences.csv', 'w') as myfile:
	wr = csv.writer(myfile)
	wr.writerow(text3)
print(time.time() -start)
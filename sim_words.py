from scipy.spatial import distance
import spacy
import numpy as np
import sys

seed_word = "word"
if len(sys.argv) > 1:
	seed_word = sys.argv[1]
else:
	print("must supply seed word as argument")

nlp = spacy.load("en_core_web_lg")

#https://stackoverflow.com/questions/54717449/mapping-word-vector-to-the-most-similar-closest-word-using-spacy
seed_vector = np.array([nlp.vocab[seed_word].vector])

ids = [x for x in nlp.vocab.vectors.keys()]
word_vectors = [nlp.vocab.vectors[x] for x in ids]
word_vectors = np.array(word_vectors)

results = distance.cdist(seed_vector, word_vectors, metric='cosine')
similar_words = set()

#https://stackoverflow.com/questions/42184499/cannot-understand-numpy-argpartition-output
axis = -1
k=50
B = results.argpartition(k,axis=axis)[(*axis%results.ndim*(slice(None),),slice(k))]
idx = np.take_along_axis(B,np.take_along_axis(results,B,axis).argsort(axis),axis)

counter = 0
smaller = idx[0][0:k]
for i in smaller:
	output_word = nlp.vocab[ids[i]].text
	if output_word.lower() not in similar_words:
		print("{} : {}".format(counter, output_word)) 
	similar_words.add(output_word.lower())
	counter += 1

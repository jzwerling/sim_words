# sim_words
sim_words.py takes a string as an argument, and returns a set of words based on the cosine similarity of the word vectors to the vector of the original words.  This is done using the SpaCy model en_core_web_lg, which contains word vectors, and numpy and some scipy to do the vector calculations.

**sample usage:**<br>
python sim_words.py dinosaur

And the output should look something like:<br>
0 : dinosaur<br>
3 : dinosaurs<br>
6 : FOSSILS<br>
9 : prehistoric<br>
12 : dino<br>
15 : Fossilized<br>
18 : sauropod<br>
20 : Triceratops<br>
22 : SKELETON<br>
25 : DINOs<br>
29 : SKELETONS<br>
32 : FOSSIL<br>
35 : STEGOSAURUS<br>
38 : Reptile<br>
41 : Extinct<br>
44 : velociraptor<br>
48 : lizard<br>

I printed it out like this as was curious to see the order of the results, and how similar they were (exact duplicates are removed).  If you are not me, you can probably get rid of the print statement and the counter and get the results in the similar_words set.

# img_exploration
A proof-of-concept exploratory tool for quickly assessing what a collection of photos is primarily of.

get_contents_and_frequencies.py: This is basically the whole of the project. Uses Google Vision API to identify the contents of an image (as best as it can) throws thoses labels in a list anf then pickles it for later. It is a misnomer at this point that it gets frequencies, we just do a count plot later.

count_graph.py: Loads the pickle, does dome neccessary proccessing to get seaborn to graph it, then graphs using a countplot 

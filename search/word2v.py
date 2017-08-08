import word2vec

vector = word2vec.doc2vec('alldata.txt', 'vectors.bin', cbow=0, size=100, window=10, negative=5, hs=0, sample='1e-4', threads=12, iter_=20, min_count=1, verbose=True)
#vector.save("Vectors")

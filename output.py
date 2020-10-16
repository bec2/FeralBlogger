from textgenrnn import textgenrnn
t = textgenrnn(‘textgenrnn_weights.hdf5')
t.generate(5, temperature=0.5)

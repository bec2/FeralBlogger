from textgenrnn import textgenrnn
t = textgenrnn()
t.train_from_file(‘plaintext.txt’, num_epochs=3)

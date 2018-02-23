# pyVocab

A simple command line program that tests your knowledge of python terminology.

The vocabulary is pulled from individual gloassries at the end of each chapter 
in the book Think Like A Computer Scientist By Allen B. Downey. Many of the 
functions in here are general enough that they could be used to make other 
multiple choice tests or trivia games from a properly formated group of .txt files. 

The formatting of the .txt files should be as follows.

vocab word: definition of vocab word.
vocab word: definition of vocab word

Basically ":" and "." are used as delineators to seperate the .txt into a list
and ultimately a dictionary of alternating vocab word and definition. Make sure
there are no other ":" or "." in your file, and the very last definition has no "."
as this would create an odd number of items in a list that must be even to work. 

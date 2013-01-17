Naive Bayes Classifier
=============

A naive bayes classifier implemented in python. This is a simple implementation in about 70 sloc including a persistence layer that allows you to save and reload your classifier.

Usage
-------

	import bayes
	classifier = bayes.Classifier()

	data = [
		('training string 1', 'type_1'),
		('training string 2', 'type_1'),
		('training string 3', 'type_1'),
		('training string 4', 'type_2'),
		('training string 5', 'type_2')
		...
	]
	classifier.train(data)
	
	#you can save the data for later
	classifier.save('demo.bayes')
	
	print classifier.classify('this is a test string')

License:
-------

See LICENSE

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

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

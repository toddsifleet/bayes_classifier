from collections import defaultdict, Counter
from math import log
import cPickle as pickle
import re

class Classifier:
    def __init__(self, file_name = None):
        '''A classic Naive Bayes Classifier

            http://en.wikipedia.org/wiki/Naive_Bayes_classifier

            This is not optimized at all but it works well for simple classification of 
            documents into preset buckets.

            To use it you must train it with data:
                >b = BayesClassifier()
                >b.train(data)
            The training data must be in the from:
                [('string to train with', 'classification'), ...]

            Then you can classify strings:
                >b.classify('this is a test string')

            self.categories holds all of our data from training
            
            In the form:
            {
                category_1: {
                    word_1: count,
                    word_2: count
                },
                category_2: {
                    word_1: count,
                    word_2: count
                },
                ...

            }

            Persistence:
            If you want to you can store the Classifier to a text file.  To do this:
            classifier.save('path_to_file)
            To load the saved data into a classifier you can do it two ways:
                1.) At initilization Classifier('path_to_file')
                2.) After initilization classifier.load('path_to_file')

        '''

        self.categories = defaultdict(Counter)
        self.word_count = defaultdict(float)

        if file_name:
            #we try to load the file, if it doesn't exists we don't care we will create
            #when we save the classifier
            try:
                self.load(file_name)
                return 

            except IOError as e:
                print e
        

    def load(self, file_name = None):
        '''Load data from a text file

        This updates our current training set with data stored
        in a pickeled text file.  We don't overwrite any data
        we just add the new data, so this is safe to use before
        or after other training.

        '''

        #update the file_name if it is specified
        if file_name is not None:
            self.file_name = file_name

        with open( self.file_name, "rb" ) as fh:
            data = pickle.load(fh)
            for category, words in data['categories'].items():
                self.categories[category].update(words)
                self.word_count[category] += data['word_count'][category]

    def save(self, file_name = None):
        #pickle and save the current data
        #update the file_name if it is specified
        if file_name is not None:
            self.file_name = file_name

        
        if not file_name:
            return False
        with open( file_name, "wb" ) as fh:
            data = {
                'categories': self.categories,
                'word_count': self.word_count
            }
            pickle.dump(data,  fh)

    def get_words(self, input):
        '''Parse a string and count words

            Cleaning:
                1.) Convert to lower case
                2.) Split by any non letters

            Splitting:
                1.) Split by non-letters

            Filtering:
                1.) Filter out words less than < 3

            Arguments:
                input: a string to split

            Return:
                A counter dictionary of word counts where each key is a word and
                each value is the number of times that word appeared in the string.

        '''

        words = re.split('[^a-z]+', input.lower())
        return Counter([w for w in words if len(w) > 2])

    def train(self, docs):
        '''Train the filter

            Given a set of training data this loops through each document
            and trains the filter

            Arguments:
                docs: a list of tuples in the form: (data, category)
                    data: a string of text to proccess
                    category: the value to associate with this string

        '''

        for data, category in docs:
            words = self.get_words(data)
            self.categories[category].update(words)
            self.word_count[category] += sum(words.values())

    def classify(self, string):
        '''Classify a String 

            Once our filter is trained given a string input this function
            classifies it into a doctype.  

            Arguments:
                string: the string to classify
                
        '''
        words = self.get_words(string) #a counter of the words in the string

        score = defaultdict(float) #score for each category
        #loop through each word and category to calculate the probability for each category
        for word in words:
            for category, category_words in self.categories.items():
                #score += log(count_current_word_classified_as_cateogry / total_words_in_category)
                if category_words[word]:
                    score[category] += log(category_words[word] / self.word_count[category])
                else:
                    score[category] += log(.01 / self.word_count[category])

        #the total number of words across all categories
        total = sum(self.word_count.values())
        for category in self.word_count:
            score[category] += log(self.word_count[category] / total)

        #return the most likely category
        if score:
            return max(score, key = lambda x: score[x])

        return None
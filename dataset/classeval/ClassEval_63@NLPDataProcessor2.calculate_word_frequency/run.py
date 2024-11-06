import os
import unittest
from collections import Counter
import re

class NLPDataProcessor2:

    def process_data(self, string_list):
        words_list = []
        for string in string_list:
            # Remove non-English letters and convert to lowercase
            processed_string = re.sub(r'[^a-zA-Z\s]', '', string.lower())
            # Split the string into words
            words = processed_string.split()
            words_list.append(words)
        return words_list

    def calculate_word_frequency(self, words_list):
        word_frequency = Counter()
        for words in words_list:
            word_frequency.update(words)
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        top_5_word_frequency = dict(list(sorted_word_frequency.items())[:5])
        return top_5_word_frequency

    def process(self, string_list):
        words_list = self.process_data(string_list)
        word_frequency_dict = self.calculate_word_frequency(words_list)
        return word_frequency_dict
class Test(unittest.TestCase):
    def test(self):
            self.processor = NLPDataProcessor2()
            words_list = [['hello', 'world'], ['this', 'is', 'a', 'test'], ['hello', 'world', 'this', 'is', 'another', 'test'],
                          ['hello', 'hello', 'world']]
            expected_output = {'hello': 4, 'world': 3, 'this': 2, 'is': 2, 'test': 2}
            return self.processor.calculate_word_frequency(words_list),expected_output
t=Test()
a=t.test()
with open('/home/changshu/CODEMIND/dataset/classeval/ClassEval_63@NLPDataProcessor2.calculate_word_frequency/output.txt', 'w') as wr:
    wr.write(str(a))
        
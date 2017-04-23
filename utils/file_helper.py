from data.s140_unigram import S140Unigram
from data.tweet import Tweet
from utils import text_cleaner


def read_input_data(input_file_path):

    with open(input_file_path) as input_file:
        for line in input_file:
            line = line.strip()
            array = line.split('\t')
            yield Tweet(array[0], text_cleaner.clean_str(array[1]),
                        array[2], float(array[3]))


def read_s140_lexicon(lexicon_file_path):

    with open(lexicon_file_path) as lexicon_file:
        for line in lexicon_file:
            line = line.strip()
            array = line.split('\t')
            yield S140Unigram(array[0], float(array[1]))

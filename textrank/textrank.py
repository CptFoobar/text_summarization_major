from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from sys import stdout
import os

def main():
    LANGUAGE = "english"
    SENTENCES_COUNT = 2
    stop = set(stopwords.words('english'))

    #retrieve each of the articles
    articles = os.listdir("../data/articles")
    count = 0
    for article in articles:
        stdout.write("\rProgress: {:02.0f}%".format(float(count)/len(articles)*100))
        stdout.flush()
        # print 'Reading articles/' + article
        # articleFile = io.open('articles/' + article, 'r')
        parser = PlaintextParser.from_file(os.path.abspath(os.path.join("../data/articles", article)), Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)

        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)

        summary = ""
        file_name = os.path.splitext(article)[0].split('.')[0]
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            summary += str(sentence)

        summary_tokens = [token.lower().translate(None, punctuation) for token in word_tokenize(summary) if token not in punctuation and token.lower() not in stop and token != "'s"]

        with open(os.path.join("results", file_name + ".txt"), "w") as keywords_file:
            keywords_file.write('\n'.join(set(summary_tokens)))

        count += 1

    print "\nDone..."

if __name__ == "__main__":
    main()

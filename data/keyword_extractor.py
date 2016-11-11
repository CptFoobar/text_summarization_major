from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from os import listdir
from os.path import isfile, isdir, splitext, join

def main():
    summaries_root = "summaries-gold"
    summary_dirs = [f for f in listdir(summaries_root) if isdir(join(summaries_root, f))]
    stop = set(stopwords.words('english'))
    for s_dir in summary_dirs:
        summary_files = [s for s in listdir(join(summaries_root, s_dir)) if splitext(s)[1] == ".gold"]
        summary_keywords = Counter()
        sk = []
        for summary_file in summary_files:
            with open(join(join(summaries_root, s_dir), summary_file), 'r') as summary_file_handle:
                summary = summary_file_handle.read()
            summary_tokens = word_tokenize(summary)
            summary_tokens = [token.lower() for token in summary_tokens if token not in punctuation and token.lower() not in stop and token != "'s"]
            for token in summary_tokens:
                summary_keywords[token] += 1
            sk.extend(summary_tokens)

        # TODO: Check if setting threshold count improves quality of keywords extracted
        #summary_tokens = {k for (k,v) in dict(summary_tokens).items() if v > 1}
        #summary_tokens_dict = dict(summary_tokens)
        with open(join("summaries_keywords", s_dir + ".keywords.gold"), 'w') as keywords_file:
            for token, val in summary_keywords.items():
                keywords_file.write(token + "\n")

if __name__ == "__main__":
    main()

import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from collections import Counter

def compute_human_summaries_rogue():
    summaries_root = "data/summaries-gold"
    summary_dirs = [f for f in os.listdir(summaries_root) if os.path.isdir(os.path.join(summaries_root, f))]
    stop = set(stopwords.words('english'))
    rogue_score_overall = []
    for s_dir in summary_dirs:
        all_summaries_tokenized = []
        summary_keywords = Counter()
        summary_files = [s for s in os.listdir(os.path.join(summaries_root, s_dir)) if os.path.splitext(s)[1] == ".gold"]

        for summary_file in summary_files:
            with open(os.path.join(os.path.join(summaries_root, s_dir), summary_file), 'r') as summary_file_handle:
                summary = summary_file_handle.read()

            summary_tokens = word_tokenize(summary)
            summary_tokens = [token.lower() for token in summary_tokens if token not in punctuation and token.lower() not in stop and token != "'s"]

            all_summaries_tokenized.append(summary_tokens)
            for token in summary_tokens:
                summary_keywords[token] += 1

        keywords_complete = [k for (k,v) in summary_keywords.items()]
        rogue_scores = []

        for keywords_set in all_summaries_tokenized:
            rogue_scores.append(len(set(keywords_set).intersection(set(keywords_complete)))/float(len(set(keywords_complete))))

        rogue_score_overall.append(sum(rogue_scores)/len(rogue_scores))
    print "Average ROGUE-1 Score for human generated summaries: {:02.5f}".format(sum(rogue_score_overall)/len(rogue_score_overall))

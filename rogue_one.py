import os
import argparse

def main(args):
    if (args.human):
        from rogue_one_human import compute_human_summaries_rogue
        compute_human_summaries_rogue()
        return

    gold_files_path = os.path.abspath(args.gold)
    test_files_path = os.path.abspath(args.test)
    if (not os.path.isdir(gold_files_path) or not os.path.isdir(test_files_path)):
        print "Invalid file paths..."
        return
    rogue_one_scores = []
    for keywords_file in os.listdir(test_files_path):
        if (not os.path.isfile(os.path.join(gold_files_path, os.path.splitext(keywords_file)[0].split('.')[0] + ".keywords.gold"))):
            continue
        keywords_test = []
        keywords_gold = []
        with open(os.path.join(test_files_path, keywords_file), 'r') as keywords_file_handle:
            keywords_test = {keyword.lower() for keyword in keywords_file_handle.read().split()}
        with open(os.path.join(gold_files_path, os.path.splitext(keywords_file)[0].split('.')[0] + ".keywords.gold"), 'r') as keywords_file_handle:
            keywords_gold = {keyword.lower() for keyword in keywords_file_handle.read().split()}
        rogue_one_scores.append(float(len(keywords_test.intersection(keywords_gold)))/len(keywords_gold))
        #print "{0}: {1}/{2}".format(keywords_file, len(keywords_test.intersection(keywords_gold)), len(keywords_gold))
        #print keywords_test.intersection(keywords_gold)
    #print rogue_one_scores
    print "Average ROGUE-1 Score: {:07.5f}".format(sum(rogue_one_scores)/len(rogue_one_scores))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # option for specifying path to gold
    parser.add_argument("-g", "--gold", type=str, help="Specify path to gold dataset directory")

    # option for specifying path to test dataset
    parser.add_argument("-t", "--test", type=str, help="Specify path to gold dataset (file path)")

    parser.add_argument("-m", "--human", action="store_true", help="Compute ROGUE-1 score for human generated summaries")

    args = parser.parse_args()

    main(args)

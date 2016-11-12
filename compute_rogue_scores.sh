#!/bin/sh

echo "Please wait, this may take a while...\n"
num_articles=$(ls data/articles | wc -l)
echo "Total articles: $num_articles\n"

for algorithm in lexrank lsa textrank
do
    echo "Running $algorithm..."
    cd $algorithm
    /usr/bin/time -f "Time Elapsed: %e seconds" python "$algorithm.py"
    cd ..
    python rogue_one.py --gold data/summaries_keywords --test $algorithm/results
done
echo "Done\nComputing ROGUE-1 Scores for human generated summaries..."
python rogue_one.py --human

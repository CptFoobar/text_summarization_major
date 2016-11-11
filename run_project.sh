#!/bin/sh

# TODO: Insert Intro line here
# echo "Intro"

echo "Verifying dataset..."
if ! [ -d "data/articles" ] || ! [ -f "data/keyword_extractor.py" ]; then
    echo "Dataset missing/incomplete. Exiting..."
    exit 1
else
    echo "Filtering Dataset..."
    sh +x filter_data.sh
    echo "Extracting keywords from gold..."
    cd data
    mkdir -p summaries_keywords
    python keyword_extractor.py
    cd ..
    echo "Done\nComputing ROGUE-1 Scores for TextRank, LexRank, LSA..."
    sh +x compute_rogue_scores.sh
fi

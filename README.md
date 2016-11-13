## Text Summarization Algorithms
### A Comparative Study

Developed as a part of our Semester 7 Major Project, this repository contains scripts and code to run and test the performance of popular text summarization algorithms.
The algorithms studied are:
- TextRank [[Mihalcea Tarau 2004]](https://web.eecs.umich.edu/%7Emihalcea/papers/mihalcea.emnlp04.pdf)
- LexRank [[Erkan Radev 2004]](https://www.cs.cmu.edu/afs/cs/project/jair/pub/volume22/erkan04a-html/erkan04a.html)
- LSA [[Steinberger Ježek 2004]](http://www.kiv.zcu.cz/~jstein/publikace/isim2004.pdf)

#### DataSet
For our experiments, the Opinosis dataset was used. It can be obtained [here](http://kavita-ganesan.com/modules/pubdlcnt/pubdlcnt.php?file=http://kavita-ganesan.com/sites/default/files/OpinosisDataset1.0_0.zip&nid=149)
```
@inproceedings{ganesan2010opinosis,
 title={Opinosis: a graph-based approach to abstractive summarization of highly redundant opinions},
 author={Ganesan, Kavita and Zhai, ChengXiang and Han, Jiawei},
 booktitle={Proceedings of the 23rd International Conference on Computational Linguistics},
 pages={340--348},
 year={2010},
 organization={Association for Computational Linguistics}
}
```

#### Performance Metric
To compare the relative performance of the algorithms, a simple implementation of ROGUE-1 metric in python was used.

#### Replicating project results
To imitate the results of our project, one may do the following:
1. Clone this repository and ensure that the Opinosis Dataset is present. If not, download from the link above and extract into `data/`.
2. Run the `run-project` script.
   ```bash
   $ sh +x run-project.sh
   ```
   This script will clean the dataset, extract keywords, run the algorithms on the dataset, and print their respective running times and ROGUE-1 scores.
   - Individual performances of each of the algorithms can be computed by simply first running the `$algorithm/$algorithm.py` script, followed by running the `rogue_one` script with:

    ```bash
    $ python rogue_one.py --gold data/summaries_keywords --test $algorithm/results
    ```

#### Dependencies
- python 2.7+
- nltk
- sumy
- networkx

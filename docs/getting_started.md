# Getting started with using the MSR2021Replication

## Install Mallet

To install the Mallet tool, first is necessary to have the Apache ant build tool installed. Install the binary from [https://ant.apache.org/](https://ant.apache.org/) and follow the [manual instructions](https://ant.apache.org/manual/install.html#getBinary) to configure it.

With ant installed and configured, open the Mallet 2.0.8 folder in the MSR2021Replication repository at `mallet/mallet-2.0.8` and run the following command:

```sh
ant
```

The Mallet tool will be available to use at `mallet/mallet-2.0.8/bin/mallet`.

## Install python libraries

pip intall and etc
pip install:
- pandas
- nltk


Dentro do python console
 >>> import nltk
  >>> nltk.download('punkt')


## Run the MSR2021Replication

To run the MSR2021Replication, with the original dataset, it is necessary to run the following steps
1. `python3 clean_stackoverflow_data.py`
1. `python3 export_so_to_mallet.py`

Run mallet instructions:

```sh
mallet/mallet-2.0.8/bin/mallet import-dir --input mallet/git_data/ --output mallet/git.mallet --keep-sequence --remove-stopwords --extra-stopwords mallet/extra_stopwords_github.txt
```

```sh
mallet/mallet-2.0.8/bin/mallet train-topics --random-seed 100 --input mallet/git.mallet --num-topics 15 --optimize-interval 20 --output-state mallet/git-topic-state.gz --output-topic-keys mallet/git_keys.txt --output-doc-topics mallet/git_composition.txt --diagnostics-file mallet/git_results/git_diagnostics.xml
```

Run scripts with the mallet output

1. `python3 parse_topics_composition.py`


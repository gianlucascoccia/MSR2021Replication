# Replication package for the MSR2021 "Challenges in Developing Desktop Web Apps: a Study of Stack Overflow and GitHub" paper

## Authors: Gian Luca Scoccia, Partizio Migliarini, Marco Autili

### Abstract

Software companies have an interest in reaching the maximum amount of potential customers while, at the same time, providing a frictionless experience. Desktop web app frameworks are promising in this respect, allowing developers and companies to reuse existing code and knowledge of web applications to create cross-platform apps integrated with native APIs. Despite their growing popularity, existing challenges in employing these technologies have not been documented, and it is hard for individuals and companies to weigh benefits and pros against drawbacks and cons.
In this paper, we address this issue by investigating the challenges that developers frequently experience when adopting desktop web app frameworks. To achieve this goal, we mine and apply topic modeling techniques to a dataset of 10,822 Stack Overflow posts related to the development of desktop web applications. Analyzing the resulting topics, we found that: i) developers often experience issues regarding the build and deployment processes for multiple platforms; ii) reusing exist- ing libraries and development tools in the context of desktop applications is often cumbersome; iii) it is hard to solve issues that arise when interacting with native APIs. Furthermore, we confirm our finding by providing evidence that the identified issues are also present in the issue reports of 453 open-source applications publicly hosted on GitHub.

Paper preprint available here: http\\.url

# Online appendix

The online appendix with the complete discussion of all topics mentioned in the paper is available here: http\\.url

# Replication package

Data used in the study is available in the folder [data/processed](data/processed).

Below, we describe in a step-by-step fashion how this data was collected and processed.

Quick links:

[Stack Overflow dataset](##stack-overflow-dataset)
[GitHub dataset](##github-dataset)
[Topic modeling](##topic-modeling)
[Statistical analysis](##statistical-analysis)


## Stack Overflow dataset

Starting point for the Stack Oveflow dataset was the [SOTorrent](https://empirical-software.engineering/sotorrent/) dataset.

### Tags selection

Selection of tags related to desktop web apps questions, by means of significance and relevance metrics, is performed by the scripts: [extract_tagset_from_csv.py](notebook/extract_tagset_from_csv.py) and [createT.py](notebook/create_T.py).

### Selection of relevant Stack Overflow questions

The queries used to select relevant Stack Overflow questions from SOTorrent are available in the file: [so_torrent_queries.txt](so_torrent_queries.txt)

First query selects relevant questions (based on their tags).

Second query was used to collect accepted answers for the questions returned by the first query.

## GitHub dataset


## Topic modeling

Topic modeling was executed by means of the [Mallet tool](http://mallet.cs.umass.edu).

The commands used to execute the tool from the command line is provided in the [mallet_instructions.txt](mallet_instructions.txt) file. 

## Statistical analysis


# Extracting Insights from White Papers - Text Analysis


## Introduction

This Repository corresponds to the Final Project of the Analytics Lab class, from the Business Intelligence and Process Management programm from the Berlin School of Economics and Law.

The purpose is to explore some ways to extract insights from diverse White Papers (in this case, blockchain protocol whitepapers) to gain some knowledge about that type of unstructured data. This serves mainly as a conceptual level, as the models presented are not completely production-ready. It is only to assess the validity and utility of the several Text Analytics techniques.

The structure is as stated:

------------------------------------
- Dashboard
    - integrated Notebook with all the Methods Application (based on the Exploration Notebooks)
- Dataset 
    - numeric data as well as the train data for one of the models
- Libraries
    - the code for the Data Preprocessing task
- Notebooks
    - the different exploration Notebooks for the different methods applied
- Test-White-Papers
    - the 4 white papers that will be used for validation
- White-Papers
    - the complete dataset
------------------------------------


## Technical Requirements

To run smoothly in your own environment, Python 3. and Jupyter Notebook (or Lab) should be installed. The best advice is to install Anaconda, as it is a ready-environment for Python and Machine Learning.

To install the packages needed specific to this project, you would need to run the following commands:

    pip install tika
    pip install tensorflow
    pip install keras
    pip install theano * in case tensorflow doesn't work
    pip install gensim
    pip install spacy
    pip install wordcloud
    

## Possible Errors

1. Error with Spacy

    OSError: [E050] Can't find model 'en_core_web_md'. It doesn't seem to be a shortcut link, a Python package or a valid path to a data directory.

Solution: upgrade your pip library to the version 19:

    pip install -U pip

Then, install manually the library, from Terminal:

    python3 -m spacy download en_core_web_md
    
## Sources

Some of the inspirations on this Repository:

    - https://towardsdatascience.com/applying-machine-learning-to-classify-an-unsupervised-text-document-e7bb6265f52
    - https://towardsdatascience.com/machine-learning-nlp-text-classification-using-scikit-learn-python-and-nltk-c52b92a7c73a
    - https://github.com/kavgan/nlp-in-practice/blob/master/word2vec/Word2Vec.ipynb

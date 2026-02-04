Project 1 — Levenshtein Distance (Edit Distance)

Implements the Levenshtein distance algorithm using Dynamic Programming to calculate the minimum number of edits required to transform one string into another.

Features

Supports insertion, deletion, substitution operations

Uses DP matrix for efficient computation

Example

Input: START → STARE
Output: Edit Distance = 1


📌 Based on DP table comparison between characters. 



🔹 Project 2 — Sentence Cleaning & Basic NLP Preprocessing

Performs text cleaning using:

Lowercasing

Regex word extraction

Stop word removal

Simple stemming using mapping

Example Processing

Input: The quick,Brown foxes... they are JUMPING over 10 lazy dogs!
Output: ['quick', 'brown', 'fox', 'jump', 'lazy', 'dogs']


📌 Uses regex and dictionary-based stemming. 

🔹 Project 3 — Spam Detection (Keyword Based)

Simple spam classifier using keyword matching.

Spam Keywords

win

free

prize

click here

subscribe now

Output

Returns "spam" if spam words detected

Otherwise "not spam"

📌 Uses case-insensitive keyword search. 

🔹 Project 4 — Text Cleaning for Sentiment Analysis

Prepares text for sentiment analysis by removing:

Hashtags

Special characters

Stop words

Example

Input: I Love this movie!!! #awesome
Output: ['i', 'love', 'movie']


📌 Uses regex filtering and tokenization. 

🔹 Project 5 — Advanced Distance + Keyboard Error Weighting

Contains:

Standard Levenshtein Distance

Weighted Keyboard Distance (accounts for nearby keyboard mistakes)

Example

Typed: HELLP
Correct: HELLO


Suggests correction if weighted distance is lower than standard edit distance.

📌 Useful for typo correction systems.


ngram.py

This module implements a bigram language model using the NLTK library.

Performs tokenization and case normalization

Generates bigrams from input text

Computes frequency counts of bigram occurrences

Extracts conditional word frequencies based on a given preceding token

This implementation illustrates how n-gram statistics are derived from raw text data.

smooth.py

This module demonstrates Laplace (add-one) smoothing, a fundamental technique used to address the zero-probability problem in language models.

Computes word probabilities using add-one smoothing

Incorporates a predefined vocabulary size

Ensures non-zero probability assignment to unseen words

The script provides a clear example of probability estimation in discrete language models.

noisy.py

This module implements a simplified noisy channel model for spelling correction.

Uses edit distance as a likelihood function

Computes prior probabilities from word frequency counts

Determines the most probable correction for a given misspelled input

The model demonstrates how probabilistic inference can be applied to error correction in natural language input.

Evaluate.py

This module computes perplexity, a standard evaluation metric for language models.

Calculates entropy from a sequence of word probabilities

Converts entropy into perplexity

Provides insight into the predictive performance of a language model

Perplexity is widely used to assess how well a model predicts unseen text.

# naivebayes-spamham
In this project we build a naive-bayes email spam-ham classifier from scratch using TDD.

## Running tests from command line
Run from the root directory of the project.

    python -m unittest discover tests

The command above means from module unittest run discover tests

## Classes used
1. EmailObject: Represents an email and parses the email as per RFC for emails. We will use mail gem for this. It can parse HTML messages, plaintext and multipart.


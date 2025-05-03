# Name: Patrick K.
# GitHub Username: patrick-eng7
# Date: 5/3/2025
# Description: This program calculates the sample standard deviation of the
#              lengths of words in a given string. It assumes the string
#              contains only space-separated words with no punctuation.
#              The program computes word lengths, calculates the mean, and
#              uses the standard deviation formula for a sample to return
#              the final result.

def word_length_std_dev(text):
    words = text.split()

    if len(words) < 2:
        return 0.0  # Not enough data to compute sample standard deviation

    # Step 1: Get lengths of each word
    lengths = [len(word) for word in words]

    # Step 2: Calculate the mean
    mean = sum(lengths) / len(lengths)

    # Step 3: Calculate the squared differences
    squared_diffs = [(length - mean) ** 2 for length in lengths]

    # Step 4: Calculate sample variance (divide by N - 1)
    variance = sum(squared_diffs) / (len(lengths) - 1)

    # Step 5: Take square root to get standard deviation
    std_dev = variance ** 0.5

    return std_dev


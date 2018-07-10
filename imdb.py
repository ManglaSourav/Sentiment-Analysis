
#Functions for downloading the IMDB Review data-set from the internet and loading it #into memory.

import os
import download
import glob

data_dir = "./data/IMDB/"
data_url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"

# Read and return all the contents of the text-file with the given path.
def _read_text_file(path):
    with open(path,'rt') as file:
        lines = file.readlines()
        text = " ".join(lines)
    return text

def download_and_extract():
    download.download_and_extract(url=data_url,download_dir=data_dir)

def load_data(train=True):
    train_test_path = "train" if train else "test"
    dir_base = os.path.join(data_dir, "aclImdb_v1/aclImdb", train_test_path)
    
    # Filename-patterns for the data-files.
    path_pattern_pos = os.path.join(dir_base, "pos/", "*.txt")
    path_pattern_neg = os.path.join(dir_base, "neg/", "*.txt")
    
    # Get lists of all the file-paths for the data.
    paths_pos = glob.glob(path_pattern_pos)
    paths_neg = glob.glob(path_pattern_neg)
    # Read all the text-files.
    data_pos = [_read_text_file(path) for path in paths_pos]
    data_neg = [_read_text_file(path) for path in paths_neg]
    
    x = data_pos + data_neg
        
    # Create a list of the sentiments for the text-data.
    # 1.0 is a positive sentiment, 0.0 is a negative sentiment.
    y = [1.0] * len(data_pos) + [0.0] * len(data_neg)

    return x, y


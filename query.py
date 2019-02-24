import re

def query(search):
    word_list = []
    pattern = re.compile(r'[\W_]+')
    search = pattern.sub(' ',search)
    word_list = search.split()
    return word_list

def rankFiles():
    pass

if __name__ == "__main__":
    pass
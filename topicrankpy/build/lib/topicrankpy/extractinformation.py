import textract
import re
from urlextract import URLExtract
import networkx as nx
import matplotlib as plt
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')
nltk.download('maxent_ne_chunker')
nltk.download('stopwords')
nltk.download('universal_tagset')
nltk.download('stopwords')
nltk.download('words')
from topicrankpy import topicrank as tr


def top_phrases_extraction(path,no_of_phrases):

    text = textract.process(path)
    # initialize keyphrase extraction model, here TopicRank
    extractor =  tr.TopicRank()
    # load the content of the document, here document is expected to be in raw
    # format (i.e. a simple text file) and preprocessing is carried out using spacy
    extractor.load_document(input=str(text,encoding='utf-8'),language='en')
    # keyphrase candidate selection, in the case of TopicRank: sequences of nouns
    # and adjectives (i.e. `(Noun|Adj)*`)
    extractor.candidate_selection()
    # candidate weighting, in the case of TopicRank: using a random walk algorithm
    extractor.candidate_weighting()
    # N-best selection, keyphrases contains the 10 highest scored candidates as
    # (keyphrase, score) tuples
    keyphrases = extractor.get_n_best(no_of_phrases)
    return keyphrases


def extract_phone_numbers(path):
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
    phone_numbers = r.findall(string)
    return [re.sub(r'\D', '', number) for number in phone_numbers]


def extract_email_addresses(path):
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    r = re.compile(r'[\w\.-]+@[\w\.-]+')
    return r.findall(string)


def ie_preprocess(path):
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    
    document = ' '.join([i for i in string.split() if i not in stop])
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

def extract_names(path):

    names = []
    sentences = ie_preprocess(path)
    for tagged_sentence in sentences:
        for chunk in nltk.ne_chunk(tagged_sentence):
            if type(chunk) == nltk.tree.Tree:
                if chunk.label() == 'PERSON':
                    names.append(' '.join([c[0] for c in chunk]))
    return names

def extract_urls(path):
    
    text = textract.process(path)
    string= str(text,encoding='utf-8')
    extractor = URLExtract()
    urls = extractor.find_urls(string)
    return urls

def extract_all(path,no_of_phrases_count):
    top_phrases = top_phrases_extraction(path,no_of_phrases_count)
    phone_numbers = extract_phone_numbers(path)
    email_address = extract_email_addresses(path)
    names = extract_names(path)
    urls = extract_urls(path)
    data = {
        
        'Top_Phrases_With_Ranking' : top_phrases,
        'Phone_Numbers' : phone_numbers,
        'Email_address' : email_address,
        'Important Names' : names,
        'URLS': urls

    }
    print(data)


#extract_all('/home/ayush/Documents/Resume-Tech.pdf',15)    


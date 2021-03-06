## Important topics/phrases extraction using TopicRank algorithm.

### Overview
TopicRank is an unsupervised method that aims to extract keyphrases from the most important topics of a document. Topics are defined as clusters of similar keyphrase candidates.
This new method is an improvement of the TextRank method applied to keyphrase extraction (Mihalcea and Tarau,2004). In the TextRank method, a document is represented by a graph where words are vertices and edges represent co-occurrence relations. A graph-based ranking model derived from PageRank (Brin and Page, 1998) is then used to assign a significance score to each word. TopicRank represents a document as a complete graph where vertices are not words but topics. It defines a topic as a cluster of similar single and multi-word expressions.

<img src="https://s3imagenew.s3.amazonaws.com/Processing-steps-of-TopicRank.jpg" width=400 height=400 />

### 1. Topic Identification and Clustering:
   This project follows Wan and Xiao (2008) and extract the longest sequences of nouns and adjectives from the document as        keyphrase candidates. Other methods use syntactically filtered n-grams that are most likely to contain a larger number of      candidates matching with reference keyphrases, but the n-gram restricted length is a problem. Indeed, n-grams do not            always capture as much information as the longest noun phrases. Also, they are less likely to be grammatically correct.
   
   To automatically group similar noun phrases as a single entity, this project uses Hirearchical Agglomerative Clustering        algorithm. For this clustering algorithm, vectorized text has been passed to "Jaccard" corfficient for finding similarity      between phrases. 

### 2. Graph-Based Ranking:
   TextRank(Graph-based ranking model) is used to assign significance score to each topic.To understand how textrank algorithm    works please refer : https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf
   
## Getting Started    
   
   Using this library, you will be able to extract meaningful information from documents like:
   <ul>
   <li>Top N phrases</li>
   <li>Url's</li>
   <li>Email Id's</li>
   <li>Phone numbers</li>
   <li>Important names</li>
   </ul>
   
## Installation   
```
pip3 install topicrankpy

```

```
from topicrankpy import extractinformation as t

```


```
t.extract_all('path_of_document',no_of_phrases)    

```
Output: For testing purpose, I have used my Resume. 
```
{
  'Top_Phrases_With_Ranking': [
    ('data engineering',
    0.03882171811465683),
    ('machine learning',
    0.0231421447805223),
    ('technologies',
    0.01656229201773112),
    ('algorithms',
    0.015179556679089493),
    ('python',
    0.014202240623362651),
    ('android application',
    0.013784183422746128),
    ('deep learning',
    0.012663419387693997),
    ('cloud services',
    0.012062811163957745),
    ('kafka',
    0.011780856748625147),
    ('elasticsearch',
    0.011594082728116736)
  ],
  'Phone_Numbers': [
    '4168328255'
  ],
  'Email_address': [
    'patelaayush678@gmail.com'
  ],
  'Important Names': [
    'Aayush Patel',
    'AWS Certified Solutions Architect',
    'Award Machine Learning Artificial Intelligence',
    'Advance Data Science',
    'Google Play Store',
    'Chahal Academy',
    'Apache Spark Hadoop',
    'Kafka',
    'Kafka Streams',
    'Apache Cassandra',
    'Flume',
    'Amazon Kinesis',
    'Amazon EMR',
    'Elastic Map Reduce',
    'Machine Learning Deep',
    'Data Preprocessing',
    'Keras',
    'Open CV',
    'Python',
    'Amazon Web Services',
    'Google Cloud Platform',
    'System',
    'Linux Windows',
    'Gujarat',
    'Python',
    'Cloud',
    'Teksun Lab Pvt',
    'Ltd',
    'Kinesis',
    'Collect',
    'Applied',
    'Python',
    'Data',
    'Machine Learning Intern',
    'Experts Hub',
    'Keras',
    'Sardar Vallabhbhai Patel Institute Technology',
    'Android',
    'Kinesis',
    'Cognito',
    'Desktop Application',
    'Python',
    'Apache Kafka',
    'Apache Cassandra Elasticsearch',
    'Twitter API',
    'Elastic Load Transform',
    'Kafka Connector Sink',
    'Cassandra',
    'Inspector',
    'Ontario Fire Code',
    'Build Log Analytics Solutions',
    'Google Play Store',
    'Trent University'
  ],
  'URLS': [
    'https://www.linkedin.com/in/aayushpatel678/',
    'https://github.com/Aayushpatel007',
    'https://www.youtube.com/watch?v=tvBZz7L5EBI'
  ]
}

```

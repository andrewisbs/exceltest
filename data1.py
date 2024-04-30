import pandas as pd
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
nltk.download('punkt')

df = pd.read_csv('DATA_ECOM_VAS_v1-.xlsx-Grossreport.csv')
df_pay = df['Payment System Name']


all_pay = ' '.join(df_pay)  
tokens = word_tokenize(all_pay.lower())  


word_freq = Counter(tokens)
top_words = word_freq.most_common()


for word, freq in top_words:
    print(f"{word}: {freq}")



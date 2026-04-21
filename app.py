import streamlit as st
import pickle
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

ps = PorterStemmer()

def preprocess(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text = y[:]
    y.clear()
    
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
            
    text = y[:]
    y.clear()
    
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)





tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))
encoder = pickle.load(open('label_encoder.pkl','rb'))


st.title("Movie Review Classifier")
input_text = st.text_area("Enter your Review", height=200)

if st.button("Predict"):
    if input_text.strip() != '':

        transformed_text = preprocess(input_text)

        vec_text = tfidf.transform([transformed_text])

        pred = model.predict(vec_text)

        result = encoder.inverse_transform(pred)

        if result[0] == 'positive':
            st.success("Prediction: Positive")
        else:
            st.error("Prediction: Negative")
    else:
        st.warning("Please enter some text")


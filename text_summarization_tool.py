pip install transformers torch
from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Input: Lengthy article text
article = """
Natural Language Processing (NLP) is a subfield of artificial intelligence (AI) 
that focuses on enabling computers to understand, interpret, and generate human language. 
Recent advancements in deep learning have significantly improved NLP performance in tasks 
such as machine translation, sentiment analysis, question answering, and text summarization. 
Transformers, particularly models like BERT and GPT, have revolutionized the field with their 
ability to learn context and meaning from massive amounts of text data. Applications of NLP 
are now widespread in chatbots, voice assistants, search engines, and more. With increasing 
research and development, NLP continues to bridge the gap between humans and machines.
"""

# Summarize the text
summary = summarizer(article, max_length=100, min_length=30, do_sample=False)

# Output: Summary of the article
print("Original Text:\n", article)
print("\n--- Summary ---\n")
print(summary[0]['summary_text'])

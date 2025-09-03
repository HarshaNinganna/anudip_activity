from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def check_plagiarism(text1, text2):
    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    # Compute cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return round(similarity[0][0] * 100, 2)

if __name__ == "__main__":
    print("=== AI Plagiarism Checker ===")
    doc1 = input("\nEnter first text/document:\n")
    doc2 = input("\nEnter second text/document:\n")
    
    score = check_plagiarism(doc1, doc2)
    print(f"\n Similarity Score: {score}%")
    
    if score > 70:
        print(" High chance of plagiarism detected!")
    elif score > 40:
        print(" Some similarity found.")
    else:
        print(" Texts are mostly original.")

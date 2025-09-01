from transformers import pipeline
import re

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def extract_skills(text):
    # Simple keyword-based skill extraction
    skills_keywords = [
        "python", "java", "javascript", "react", "django", "sql", "html", "css",
        "node.js", "machine learning", "data analysis", "api", "git", "docker",
        "aws", "linux", "flask", "pandas", "numpy"
    ]
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    return list(set(found_skills))

def analyze_resume(resume_text):
    # Sentiment of resume tone
    sentiment = sentiment_analyzer(resume_text[:500])  # analyze first 500 chars
    tone = sentiment[0]['label']
    confidence = round(sentiment[0]['score'] * 100, 2)

    # Skills extraction
    skills = extract_skills(resume_text)

    print("\n Resume Analysis Result")
    print("-" * 40)
    print(f" Detected Tone: {tone} ({confidence}% confidence)")
    print(f" Extracted Skills: {', '.join(skills) if skills else 'No major skills detected'}")
    print("-" * 40)


if __name__ == "__main__":
    print("=== AI Resume Analyzer ===")
    resume_text = input("Paste resume text here:\n\n")
    analyze_resume(resume_text)

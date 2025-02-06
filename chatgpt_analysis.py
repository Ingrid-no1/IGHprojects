import os
import pandas as pd
import re
import logging
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from textblob import TextBlob

# Ensure consistent results from langdetect
DetectorFactory.seed = 0

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def clean_text(text: str) -> str:
    """Cleans the input text by removing emojis, special characters, and extra spaces."""
    if pd.isnull(text):
        return ""
    text = re.sub(r"[^\x00-\x7F]+", "", text)  # Remove non-ASCII characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespaces
    return text


def is_english(text: str) -> bool:
    """Detects if the given text is in English."""
    try:
        return detect(text) == "en"
    except LangDetectException:
        return False


def get_sentiment(text: str) -> float:
    """Calculates sentiment polarity using TextBlob."""
    return TextBlob(text).sentiment.polarity


def classify_sentiment(polarity: float) -> str:
    """Classifies sentiment based on polarity score."""
    if polarity > 0:
        return "Positive"
    elif polarity == 0:
        return "Neutral"
    return "Negative"


def main():
    # Define file paths
    input_file = os.path.join("chatgpt_reviews.csv")  
    output_file = os.path.join("output", "processed_reviews.csv")

    # Read CSV file (limit to first 100 rows)
    df = pd.read_csv(input_file, nrows=100, usecols=["reviewId", "content"])
    logging.info(f"Loaded {len(df)} reviews.")

    # Clean and filter text
    df["content"] = df["content"].apply(clean_text)
    df = df[df["content"] != ""]
    df = df[df["content"].apply(is_english)]

    # Apply sentiment analysis
    df["polarity"] = df["content"].apply(get_sentiment)
    df["sentiment_category"] = df["polarity"].apply(classify_sentiment)

    # Save processed data
    os.makedirs("output", exist_ok=True)
    df.to_csv(output_file, index=False)
    logging.info(f"Processed data saved to {output_file}")

    # Print the first 5 rows of the processed data
    logging.info("Processed Data Preview:")
    print(df.head())  # Display the first 5 rows

if __name__ == "__main__":
    main()
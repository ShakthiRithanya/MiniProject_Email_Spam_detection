# Project Report: Spam Email Detection using Logistic Regression

## 1. Executive Summary
This project aims to develop a robust binary classification system to identify spam messages from legitimate communication (ham). Using a dataset of SMS messages, we implemented a Natural Language Processing (NLP) pipeline and a Logistic Regression model. The final system is deployed as a Streamlit web application, providing real-time predictions with high confidence.

## 2. Methodology
### 2.1 Data Collection
We utilized the **SMS Spam Collection Dataset**, containing over 5,500 messages labeled as `ham` or `spam`.

### 2.2 Text Preprocessing
Raw text data was cleaned using the following steps:
- **Case Normalization:** Converted all text to lowercase.
- **Noise Removal:** Removed punctuation and special characters.
- **Stopword Removal:** Eliminated common English words (e.g., "is", "the", "at") that do not contribute to sentiment.
- **Tokenization:** Split sentences into individual words.

### 2.3 Feature Engineering
We applied **TF-IDF (Term Frequency - Inverse Document Frequency)** vectorization to convert text into numerical format. This technique highlights words that are frequent in a specific document but rare across the entire corpus, helping the model identify "spammy" keywords.

## 3. Implementation
### 3.1 Model Selection
**Logistic Regression** was chosen for its:
- Efficiency with high-dimensional text data.
- Interpretability (we can see which words influence the spam score).
- Low computational cost for real-time deployment.

### 3.2 Evaluation Metrics
The model was evaluated on a 30% test set using:
- **Accuracy:** Overall correctness.
- **Precision:** Ability to avoid labeling ham as spam (critical for user experience).
- **Recall:** Ability to catch all spam messages.
- **F1 Score:** Harmonic mean of precision and recall.

## 4. Results
| Metric | Value |
| --- | --- |
| Accuracy | ~98% |
| Precision | ~99% |
| Recall | ~90% |
| F1 Score | ~94% |

**Top Predictors of Spam:**
- "claim", "won", "prize", "urgent", "congratulations", "text".

## 5. Deployment
The model and vectorizer were serialized using `joblib` and integrated into a **Streamlit** dashboard. Users can enter any text to get an instant "Safe" or "Spam" verdict along with a confidence probability.

## 6. Conclusion
The Logistic Regression model proves to be a highly effective baseline for spam detection. Future improvements could involve using deep learning models (like LSTMs or Transformers) for better context understanding, though the current solution provides an excellent balance of speed and accuracy.

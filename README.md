# Project X 
Group members: Mohammad Badri - 100003064
               A
               D
This repository contains the materials for **Project X**.  
- Presentation Slides: see [`slides/`](./slides/) folder  
- Notebooks: see [`notebooks/`](./notebooks/) folder
- Data: when you access correct data, place it in [`data/`](./data/) folder
- Results: the folder [`results/`](./result/) contains our figures and tables.
  
---
- Read more about this project on Medium: <Medium_Article_link>
---
Here is the structured **README.md** file based on the analysis of your Jupyter notebooks.

-----

# Quantifying Raskolnikov: A Computational Analysis of *Crime and Punishment*

## 📖 Project Overview

This project applies Natural Language Processing (NLP) techniques to Fyodor Dostoevsky’s *Crime and Punishment* to quantify the psychological and social trajectory of its protagonist, Rodion Raskolnikov. By combining structural, sentiment, and network analyses, the project attempts to map the transition from isolation and instability to social reintegration and spiritual redemption.

## ❓ Research Question

**How can Raskolnikov’s psychological instability, social isolation, and eventual recovery be quantified through textual features such as narrative coherence, social network density, and emotional vocabulary?**

-----

## 📂 Dataset & Preprocessing

  * **Source Text**: *Crime and Punishment* (English translation) via Project Gutenberg.
  * **Preprocessing Pipeline**:
      * **Cleaning**: Removal of Gutenberg headers/footers and license text.
      * **Segmentation**: Regex-based splitting of the text into **Chapters**, **Paragraphs**, and **Sentences**.
      * **Character Identification**: Utilization of a JSON character library (`Crime_punishment.json`) to map various aliases (e.g., "Rodya", "Rodion Romanovich") to canonical character IDs.
      * **Tokenization**: Word and sentence tokenization using NLTK, SpaCy, or Regex depending on the specific analysis.

-----

## 📓 Notebook Overview

### 1\. Social & Character Analysis

  * **`Charactere_Network.ipynb`**

      * **Purpose**: Tracks Raskolnikov’s social integration by analyzing character co-occurrences in sliding text windows.
      * **Key Output**: Interactive network graphs comparing the **First 10 Chapters** (Early) vs. **Last 10 Chapters** (Late).
      * **Finding**: Raskolnikov moves from isolation (9 connections, low weight) to stronger social integration (12 connections, 3x higher interaction weight) in the late novel.

  * **`personality_change.ipynb`**

      * **Purpose**: Detects stylistic shifts in Raskolnikov’s internal monologue using linguistic markers.
      * **Key Metrics**: "I-ratio" (self-focus), negation ratio, modal verb usage, and lexical diversity.
      * **Key Output**: PCA scatter plot visualizing the distinct linguistic separation between pre-murder and post-murder narrative segments.

### 2\. Narrative Coherence (Structure)

  * **`Chapters_coherence.ipynb`**

      * **Purpose**: Measures the semantic stability of the writing at a macro (chapter) level using Sentence-BERT embeddings.
      * **Method**: Calculates the cosine similarity of sentences to their chapter centroid.
      * **Finding**: The mean coherence remains surprisingly stable between early and late chapters (\~0.418), suggesting the chaotic mental state is conveyed through content rather than structural fragmentation at the chapter level.

  * **`Paragraph_Coherence.ipynb`**

      * **Purpose**: Measures semantic stability at a micro (paragraph) level, focusing specifically on paragraphs mentioning Raskolnikov.
      * **Key Output**: Coherence distribution histograms and comparative statistics for Raskolnikov-focused paragraphs.
      * **Finding**: Raskolnikov-specific paragraphs show a marginal increase in coherence from Early (0.521) to Late (0.522) phases.

### 3\. Sentiment & Decision Making

  * **`Decision_Trajectory.ipynb`**

      * **Purpose**: Traces the moral arc by isolating sentences where Raskolnikov makes explicit decisions.
      * **Method**: Uses `distilbert-base-uncased-finetuned-sst-2-english` to score the sentiment of decision-making sentences.
      * **Key Output**: A trajectory plot mapping moral/constructive decisions (+1) vs. destructive decisions (-1) across the narrative timeline.

  * **`Sentiment_Analysis.ipynb`**

      * **Purpose**: Maps the general emotional arc of the novel using VADER sentiment analysis.
      * **Key Output**: Chapter-by-chapter average sentiment scores visualizing peaks of tension and relief.

### 4\. Thematic Analysis (Emotion & Spirituality)

  * **`spirtuality_analysis.ipynb`**

      * **Purpose**: Tracks the density of religious and spiritual vocabulary (e.g., "redemption," "soul," "sin") across the text.
      * **Key Output**: A line graph comparing Religious Density across Early, Middle, and Late phases.
      * **Finding**: Spiritual vocabulary peaks in the **Middle** chapters (\~0.0058), coinciding with Raskolnikov's peak crisis and moral struggle.

  * **`EmotionsWords.ipynb`**

      * **Purpose**: Profiles specific emotional states using a lexicon of 12 categories (e.g., Justice, Anxiety, Guilt).
      * **Key Output**: Frequency counts for specific emotions.
      * **Finding**: "Justice" is the most frequent emotion-related category associated with Raskolnikov.

-----

## 🔗 How It Supports the Argument

These notebooks collectively provide quantitative evidence for Raskolnikov's transformation:

1.  **From Isolation to Connection**: The **Network Analysis** proves a measurable increase in social weight and degree.
2.  **From Crisis to Resolution**: The **Spiritual Analysis** identifies the middle of the book as the peak of moral struggle, while **Decision Trajectory** maps the shift from destructive to constructive choices.
3.  **Linguistic Signature**: The **Personality Change** PCA confirms that the murder event fundamentally alters the linguistic patterns associated with the protagonist.

-----

## 💻 How to Run

### Requirements

  * Python 3.8+
  * Jupyter Notebook

### Dependencies

Install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn nltk spacy networkx pyvis sentence-transformers scikit-learn
```

*Note: You may need to download specific SpaCy and NLTK models:*

```bash
python -m spacy download en_core_web_sm
# In Python:
# nltk.download('vader_lexicon')
# nltk.download('punkt')
```

### Execution Order

1.  Place `Crime-punishment.txt` in the `../data/` folder.
2.  Ensure `Crime_punishment.json` is in the `Character Library/` folder.
3.  Run notebooks in any order, though `Charactere_Network.ipynb` and `spirtuality_analysis.ipynb` provide the strongest high-level overviews.

-----

## ⚠️ Limitations & Notes

  * **Translation Bias**: This analysis is performed on an English translation. Dostoevsky's original Russian syntax and vocabulary might yield different linguistic fingerprints.
  * **Proxy Metrics**: "Co-occurrence" in the network analysis implies proximity, not necessarily positive interaction. A hostile argument counts as a social connection in this model.
  * **Lexicon Limitations**: Keyword-based analyses (Spirituality, Emotions) depend on specific word lists and may miss context that transformer-based models (used in the Decision Trajectory) might catch.
## 📑 Project Outline


---
## 🚀 Environment Setup

Before starting, please **fork this repository** and create a fresh Python virtual environment.  
All required libraries are listed in `requirements.txt`.

> ⚠️ If you encounter errors during `pip install`, try removing the version pinning for the failing package(s) in `requirements.txt`.  
> On Apple M1/M2 systems you may also need to install additional system packages (the “M1 shizzle”).

---

### macOS / Linux (bash/zsh)

```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (PowerShell)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Windows (Git Bash)
```bash
# Select Python version (if using pyenv)
pyenv local 3.11.3

# Create and activate virtual environment
python -m venv .venv
source .venv/Scripts/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
```

You’re now ready to run the session notebooks!

Deactivate the environment when you’re done:
```bash
deactivate
```
## 👤 Author
- **Mohammad Badri**
- **Abd Alah Fashesh**
- **Dima Barada**  
B.Sc. Computer Science, SRH University Leipzig  
NLP Final Project — Winter Semester 2025

# %% [markdown]
# # 3) POS Pattern Frequency (Adj+N, V+N, etc.)
# 
# This notebook is part of Applied NLP – Session 2: Phrases & Collocations.
# 
# Overview:
# - Analyze grammatical patterns in bigrams using Part-of-Speech (POS) tagging.
# - Identify common POS patterns like ADJ+NOUN, VERB+NOUN, NOUN+NOUN across two works by the same author.
# - Visualize the distribution of POS patterns to understand syntactic phrase structure.
# 
# Learning objectives:
# - Apply spaCy POS tagging to tokenized text for grammatical analysis.
# - Compute and compare POS bigram patterns across literary texts.
# - Visualize syntactic patterns to identify stylistic features.
# - Understand how preprocessing choices (stopwords, filtering) affect syntactic analysis.
# 
# Quick start:
# 1. Edit the CONFIG dictionary in the next code cell to point to your two plain-text books.
# 2. (Optional) Toggle use_stopwords to remove common function words.
# 3. Run cells from top to bottom. The main outputs are saved to ../results/.
# 4. Ensure en_core_web_sm spaCy model is installed (included in requirements.txt).
# 
# Prerequisites:
# - A Python environment with requirements.txt packages installed (pandas, matplotlib, spacy).
# - spaCy English model: en_core_web_sm (should be installed via requirements.txt).
# - The text files for the two works placed in ../data/.
# 
# Notes and tips:
# - The notebook uses the same robust preprocessing as notebooks 1-2 (strip_gutenberg, normalize quotes, etc.).
# - POS tagging can be slow on large texts; consider slicing tokens or processing in chunks.
# - Common patterns: ADJ+NOUN (descriptive phrases), VERB+NOUN (action phrases), NOUN+NOUN (compounds).
# - Compare patterns between your two books to see if syntactic style differs.
# - For non-English texts, change the spaCy model in the CONFIG or POS tagging cell (e.g., de_core_news_sm for German).
# 
# Goal: Identify and visualize the most frequent Part-of-Speech bigram patterns (e.g., ADJ+NOUN, VERB+NOUN) in your two selected works.
# 

# %% [markdown]
# ## 0. Setup & Configuration
# 
# - Fill the CONFIG paths for your two books (plain text).
# - Toggle stopwords and thresholds as needed.
# 

import re, os, math, json, collections
from pathlib import Path
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (9, 4.5)
plt.rcParams["axes.grid"] = True

CONFIG = {
    "book1_path": "../data/Crime-punishment.txt",          # Crime and Punishment
    "book2_path": "../data/The-Brotherskaramazov.txt",     # (not used here)
    "language": "en",
    "use_stopwords": False,
    "min_ngram_count": 5,
    "top_k": 20
}

# Unicode-aware word tokenizer
WORD_RE = re.compile(r"[^\W\d_]+(?:[-'][^\W\d_]+)*", flags=re.UNICODE)
STOPWORDS = set()

# %% [markdown]
# ## 1. Load & Normalize Text
# 
# - Fix hyphenated line breaks (e.g., end-of-line hyphens).
# - Normalize whitespace.
# - Lowercase consistently.
# 

# --- Robust Project Gutenberg boilerplate stripper --------------------------
_GB_START_MARKERS = [
    r"\\\*\s*START OF (THIS|THE) PROJECT GUTENBERG EBOOK",   # modern
    r"START OF (THIS|THE) PROJECT GUTENBERG EBOOK",             # fallback
    r"End of the Project Gutenberg(?:'s)? Etext",               # very old variants sometimes inverted
]
_GB_END_MARKERS = [
    r"\\\*\s*END OF (THIS|THE) PROJECT GUTENBERG EBOOK",      # modern
    r"END OF (THIS|THE) PROJECT GUTENBERG EBOOK",                # fallback
    r"End of Project Gutenberg(?:'s)? (?:Etext|eBook)",          # older variants
    r"\\\\s*END: FULL LICENSE\s\\\*",                      # license block end (older)
]

def strip_gutenberg(text: str) -> str:
    """
    Returns text between Gutenberg START and END markers (case-insensitive).
    """
    # (same function implementation as provided)
    pass

def load_text(p: str) -> str:
    with open(p, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()

def normalize_text(t: str) -> str:
    t = strip_gutenberg(t)
    t = re.sub(r"-\s*\n", "", t)
    t = re.sub(r"\s+", " ", t)
    return t

text1 = normalize_text(load_text(CONFIG["book1_path"]))
text2 = normalize_text(load_text(CONFIG["book2_path"]))

tokens1 = WORD_RE.findall(text1.lower())
tokens2 = WORD_RE.findall(text2.lower())

if CONFIG["use_stopwords"]:
    tokens1 = [t for t in tokens1 if t not in STOPWORDS]
    tokens2 = [t for t in tokens2 if t not in STOPWORDS]

tokens = tokens1 + tokens2

# %% [markdown]
# ## 2. Chapter Tokenization
# 
# Split the text into chapters to analyze vocabulary and POS patterns per chapter.
# 

def split_into_chapters(text: str):
    parts = re.split(r'(CHAPTER\s+[IVXLCDM]+)', text)
    chapters = {}
    current_chapter = 0
    for i in range(1, len(parts), 2):
        current_chapter += 1
        chapter_text = parts[i] + parts[i+1]
        chapters[current_chapter] = chapter_text.strip()
    return chapters

chapters_text = split_into_chapters(text1)

chapters = {}
for ch_num, ch_text in chapters_text.items():
    toks = WORD_RE.findall(ch_text.lower())
    
    if CONFIG["use_stopwords"]:
        toks = [t for t in toks if t not in STOPWORDS]
    
    chapters[ch_num] = toks

# %% [markdown]
# ## 3. Religious Term Analysis
# 
# - Define a set of religious terms.
# - Calculate the frequency and density of religious terms in the text.
# 

religion_cp_terms = [
    # ---- Explicit Chapter 5 terms (USER-PROVIDED) ----
    "excommunication", "church of christ", "conscience", "mercy", "charity", "gospel", "mysticism",
    # ---- Core Christian / Orthodox vocabulary ----
    "god", "lord", "christ", "jesus", "church", "faith", "belief", "religion",
    "saint", "priest", "monk", "elder",
    # ---- Sin, morality, inner struggle ----
    "sin", "sinful", "sinner", "repent", "repentance", "redemption", "salvation", "forgiveness",
    "guilt", "shame", "humility", "sacrifice",
    # ---- Soul & transcendence ----
    "soul", "spirit", "spiritual", "heaven", "hell", "damnation", "eternal", "immortal",
    # ---- Ritual & religious action ----
    "prayer", "pray", "confession", "confess", "cross", "blessing", "fasting",
    # ---- Divine authority & punishment ----
    "divine", "judgment", "justice", "punishment",
    # ---- Suffering & ethics (Dostoevsky-specific) ----
    "suffering", "atonement", "good", "evil", "miracle", "grace", "providence"
]
religion_cp_set = set(religion_cp_terms)

# Function to extract religious terms frequency
def extract_religious_terms(tokens, religion_set):
    tokens = [t.lower() for t in tokens]
    counts = Counter(tokens)
    return {term: counts[term] for term in religion_set if counts[term] > 0}

# Frequency of religious terms in Crime and Punishment
religious_freq_cp = extract_religious_terms(tokens1, religion_cp_set)

# %% [markdown]
# ## 4. Spiritual Density by Narrative Phases
# 
# Analyze religious vocabulary density over different narrative phases: early, middle, and late.
# 

early_chapters = range(1, 4)    # Part 1
middle_chapters = range(4, 7)   # Parts 2–4
late_chapters = range(7, 10)    # Epilogue + ending

def religious_density(tokens, religion_set):
    tokens = [t.lower() for t in tokens]
    if len(tokens) == 0:
        return 0
    return sum(1 for t in tokens if t in religion_set) / len(tokens)

def phase_density(chapters_dict, chapter_range):
    densities = []
    for ch in chapter_range:
        densities.append(religious_density(chapters_dict[ch], religion_cp_set))
    return sum(densities) / len(densities)

early_density  = phase_density(chapters, early_chapters)
middle_density = phase_density(chapters, middle_chapters)
late_density   = phase_density(chapters, late_chapters)

# Visualize the changes in spiritual density over the narrative
phases = ["Early", "Middle", "Late"]
values = [early_density, middle_density, late_density]

plt.figure()
plt.plot(phases, values, marker="o")
plt.xlabel("Narrative Phase")
plt.ylabel("Religious Vocabulary Density")
plt.title("Raskolnikov’s Spiritual Development in Crime and Punishment")
plt.grid(True)
plt.show()

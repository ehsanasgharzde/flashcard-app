# Flashcard-Style Language Learning App

The Flashcard-Style Language Learning App is a Python application built with tkinter. It helps users learn a new language by presenting flashcards with words and their translations. Users can mark words as learned and continue to the next word.

## Features

- Interactive flashcards for learning words and their translations.
- Mark words as learned to focus on new words.
- Colorful and user-friendly graphical user interface (GUI).

## Files

- `main.py`: The Python script containing the language learning application.

## How to Use

1. Run `main.py` using Python.
2. The app will display a flashcard with a word in the target language (e.g., French).
3. Wait for the card to flip and reveal the translation in the source language (e.g., English).
4. Click the "Correct" button if you've learned the word or the "Wrong" button to continue practicing.
5. The app will track learned words and focus on new ones.

## Requirements

- Python 3.x
- tkinter library (usually included with Python)
- pandas library (for data handling)

## Data Handling

- The app reads word pairs (e.g., French-English) from a CSV file.
- If no data file is found, it uses a fallback dataset.
- Learned words are removed from the dataset and saved.

## Usage Notes

- Customize the data file with your own word pairs.
- This app is designed for interactive language learning but may be extended for other subjects.
- For a more comprehensive language learning experience, consider adding features like pronunciation and practice quizzes.

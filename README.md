# Telegram Translator Bot without limit

This is a simple Telegram bot that translates text and documents between different languages using Microsoft Cognitive Services. Users can select the source and target languages and then input the text or upload a document for translation.

## Features

- Supports over 50 languages for translation.
- Users can select source and target languages through an interactive button interface.
- Translates both text messages and document content.
- Utilizes Microsoft Translator API for high-quality translations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sajjad-salam/translator-bot.git
   cd translator-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install pyTelegramBotAPI requests
   ```

3. Set up your environment:

   - Replace the bot token in the `TeleBot` initialization with your bot token from Telegram:
     ```python
     bot = telebot.TeleBot("your-bot-token")
     ```

4. Run the bot:
   ```bash
   python bot.py
   ```

## Usage

- Start the bot by sending the `/start` command in a chat.
- The bot will prompt you to select the source language and then the target language.
- Once both languages are selected, you can input text or upload a document for translation.
- The bot will translate the text or document content and send the translated text back to you.

### Command: `/start`

- Initiates the language selection process by showing a button-based language selector.

### Text Translation:

- After selecting languages, the bot waits for the user to send a text message and responds with the translated version.

### Document Translation:

- You can upload a document, and the bot will translate its content from the selected source language to the target language.

## Code Explanation

- **Language Selection:** The bot provides inline buttons for users to select the source and target languages using the `A5()` function.
- **Translation Process:** The `texttttttttttttt` function interacts with Microsoft Translator API to perform the actual translation, utilizing the API token fetched by `tokkk()`.
- **Text Message Handling:** The `T3()` function processes text messages and translates the text based on the selected languages.
- **Document Handling:** The `C0()` function processes uploaded documents by reading their content, translating the text, and sending the result back to the user.
- **Callback Queries:** Inline buttons are handled by callback functions such as `F0` and `T0` to guide the user through the translation steps.

<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>

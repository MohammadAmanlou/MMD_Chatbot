# MMD_Chatbot

## Overview

MMD_Chatbot is a Telegram-based chatbot that leverages the GPT-3.5 language model from OpenAI to interact with users. The bot can respond to user messages and handle basic commands, providing an engaging conversational experience.

## Features

- **Start Command**: Sends a welcome message when the `/start` command is issued.
- **Message Handling**: Generates and sends responses based on user input using the GPT-3.5 language model.
- **Exit Handling**: Recognizes specific keywords (e.g., 'خروج', 'bye', 'تمام') to end the conversation politely.

## Prerequisites

- Python 3.8 or higher
- A Telegram bot token (obtainable from BotFather on Telegram)
- An OpenAI API key for accessing GPT-3.5

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/MMD_Chatbot.git
    cd MMD_Chatbot
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Set your Telegram bot token**:
    Open the `main.py` file and replace `""` with your Telegram bot token in the `application = Application.builder().token("").build()` line.

2. **Set your OpenAI API key**:
    Replace `""` with your OpenAI API key in the `llm = ChatOpenAI(api_key="")` line.

## Usage

1. **Run the bot**:
    ```sh
    python main.py
    ```

2. **Start interacting with the bot**:
    Open Telegram, find your bot, and start a conversation by sending the `/start` command. You can then send messages to the bot and receive responses.

## Code Explanation

- **main.py**: Contains the main logic for the bot, including command handling and message responses.
  - `generate_response(prompt)`: Generates a response using the GPT-3.5 language model based on the user prompt.
  - `start_command(update, context)`: Sends a welcome message when the `/start` command is issued.
  - `handle_message(update, context)`: Handles incoming messages, generates responses, and sends them back to the user.
  - `main()`: Initializes the bot, sets up command handlers, and starts polling for updates.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT-3.5 language model.
- [python-telegram-bot](https://python-telegram-bot.org/) for the Telegram bot framework.

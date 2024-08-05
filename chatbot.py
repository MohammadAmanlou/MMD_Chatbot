from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from queue import Queue

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    base_url="",
    api_key="",
    max_tokens=1500,
    n=1,
    stop=None,
    temperature=0.7,
)

async def generate_response(prompt):
    """Generates a response based on the user prompt."""
    response = llm.invoke([HumanMessage(content=prompt)]).content
    return response

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a message when the command /start is issued."""
    await update.message.reply_text("Chatbot: Hi! How can I help you?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles user messages and generates responses."""
    user_input = update.message.text
    if user_input.lower() in ['خروج', 'bye', 'تمام']:
        await update.message.reply_text("Chatbot: Bye!")
        return

    prompt = f"User: {user_input}\nChatbot:"
    response = await generate_response(prompt)
    await update.message.reply_text(f"Chatbot: {response}")

def main():
    """Starts the bot."""
    print('Starting a bot....')
    my_queue = Queue()

    # Create the Application and pass it your bot's token.
    application = Application.builder().token("").build()

    # Register handlers
    application.add_handler(CommandHandler('start', start_command))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()

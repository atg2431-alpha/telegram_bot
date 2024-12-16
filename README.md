# Chatbot with Enhanced Memory and Contextual Response Generation

This project implements a conversational chatbot powered by a **LLaMA** language model integrated with additional tools like Wikipedia and Tavily for enhanced contextual responses. The bot also features persistent chat memory using ChromaDB and a Telegram bot interface for user interactions.

## Features
- **Advanced Language Model**: Utilizes the LLaMA model for generating human-like responses.
- **Tool Integration**: Supports Wikipedia and Tavily for querying external knowledge.
- **Memory Persistence**: Saves chat history with ChromaDB for better contextual understanding.
- **Graph-Based Execution**: Implements a state graph to streamline message processing.
- **Telegram Bot Interface**: Allows users to interact with the chatbot via Telegram.

---

## File Structure
### 1. `models.py`
- Defines the LLaMA model and binds external tools (Wikipedia and Tavily) to extend its capabilities.
- Implements a state graph for managing chatbot responses.

### 2. `main.py`
- Handles the Telegram bot interface using the Aiogram framework.
- Processes user inputs, retrieves memory, generates responses, and sends back the final output.

### 3. `chat_memory.py`
- Manages persistent storage of chat history using ChromaDB.
- Functions:
  - `store_message`: Saves messages with metadata.
  - `retrieve_messages`: Fetches the most recent messages.
  - `clear_memory`: Deletes all stored messages for a specific chat.

### 4. `requirements.txt`
- Lists all the dependencies required to run the project.

---

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the project root.
    - Add the following variables:
      ```
      TELEGRAM_BOT_TOKEN=your-telegram-bot-token
      TAVILY_API_KEY=your-tavily-api-key
      LANGCHAIN_TOKEN=your-langchain-api-key
      ```

---

## Usage
1. **Run the bot**:
    ```bash
    python main.py
    ```
2. **Interact via Telegram**:
   - Start the bot with the `/start` command.
   - Send messages to receive responses.
   - Use `/clear` to clear chat memory.

---

## Contribution Guidelines
Contributions are welcome! Feel free to submit issues or pull requests.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Commit your changes.
4. Submit a pull request.

## Contact
If you have any questions or feedback, feel free to reach out via GitHub or email.


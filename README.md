# Weather Assistant

A Python-based weather chatbot powered by OpenAI's GPT-3.5 and OpenWeatherMap API. This assistant can fetch and provide current weather details for any city while maintaining conversational memory.

## Features

- Fetch current weather details using the OpenWeatherMap API.
- Persistent conversation memory with LangChain's `ConversationBufferMemory`.
- Simple keyword-based validation to handle only weather-related queries.

## Prerequisites

1. Python 3.8 or higher
2. An OpenWeatherMap API key
3. OpenAI API key

## Setup

1. Clone this repository:
   ```bash
   git clone <repository-url>
2. Navigate to the project directory:
   ```bash
   cd weather-assistant
3. Create a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
5. Create a .env file in the root directory and add the following:
   ```bash
   WEATHER_API_KEY=your_openweathermap_api_key
   OPENAI_API_KEY=your_openai_api_key

## Usage

1. Run the script:
   ```bash
   python main.py
2. Interact with the chatbot by asking weather-related queries. Example:
   ```bash
   You: What's the weather in New York?
   Agent: The current weather in New York is clear sky with a temperature of 25°C.

3. To exit the chatbot, type:
   ```bash
   exit

## Validation

The chatbot validates queries to ensure they are weather-related. For instance:

- **Valid**: "What's the temperature in Tokyo?"
- **Invalid**: "Tell me about Python programming."

If a query is not weather-related, the chatbot responds:

Agent: I'm sorry, I can only answer weather-related questions.



## Project Structure

```bash
weather-assistant/
├── main.py               # Main script to run the chatbot
├── requirements.txt      # List of dependencies
├── .env                  # Environment variables (add API keys here)
└── README.md             # Project documentation
```

## Tools & Technologies

- **LangChain**: For conversational memory and tooling.
- **OpenAI GPT-3.5**: For natural language understanding.
- **OpenWeatherMap API**: For fetching weather data.
- **dotenv**: For environment variable management.


   

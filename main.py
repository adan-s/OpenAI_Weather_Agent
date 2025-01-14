import os
import requests
from dotenv import load_dotenv
from langchain.tools import Tool
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI


load_dotenv()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY not found in environment variables.")

# Define the Weather Tool function
def fetch_weather(city: str) -> str:
    """Fetches weather data for a given city using the OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        city_name = data.get("name", "Unknown location")
        weather = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        return f"The current weather in {city_name} is {weather} with a temperature of {temperature}°C."
    except Exception as e:
        return f"Error fetching weather data: {str(e)}"

# Create the Weather Tool
weather_tool = Tool(
    name="WeatherTool",
    func=fetch_weather,
    description="Fetches current weather details for a specified city. Input should be a city name."
)

# Initialize the OpenAI chat model
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

# Add persistent memory to the agent
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Initialize the agent with the weather tool and memory
tools = [weather_tool]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="conversational-react-description",
    memory=memory,
)

def is_weather_query(query: str) -> bool:
    """Validates if the input query is related to weather."""
    keywords = ["weather", "temperature", "forecast", "rain", "sun", "cloud", "wind", "snow", "climate"]
    return any(keyword in query.lower() for keyword in keywords)

if __name__ == "__main__":
    print("Welcome to the Weather Assistant!")
    print("Ask me about the weather in any city. Type 'exit' to end the chat.\n")

    while True:
        query = input("You: ")
        if query.strip().lower() == "exit":
            print("Goodbye! Have a great day!")
            break

        if is_weather_query(query):
            try:
                response = agent.invoke(query)
                print(f"Agent: {response['output']}")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Agent: I'm sorry, I can only answer weather-related questions.")

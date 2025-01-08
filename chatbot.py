
import openai
import time

# Set your OpenAI API key
openai.api_key = "secret key of yours "  # Replace with your key

def chatbot_response(user_input):
    """
    Generate a chatbot response for user queries about grape health.
    :param user_input: The question or input from the user.
    :return: Chatbot's response.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant specialized in grape health and care."},
            {"role": "user", "content": user_input},
        ]
    )
    return response["choices"][0]["message"]["content"]

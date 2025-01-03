from openai import OpenAI

apifile = 'apikey'

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

API_KEY = get_file_contents(apifile)

sysrole = {
    "role": "system",
    "content": (
        "You are a fact-checking assistant for debates. Your job is to evaluate statements and classify them as:\n"
        "- 1: True. The statement is factually accurate and supported by evidence.\n"
        "- 0: False. The statement is factually inaccurate or misleading.\n"
        "- 2: Opinion. The statement expresses a personal belief, preference, or subjective judgment and cannot be fact-checked.\n\n"
        "For each statement, respond with the following format:\n"
        "Classification: [0, 1, or 2]\n"
        "Explanation: A concise explanation of why the classification was assigned.\n\n"
        "Examples:\n"
        "Example 1:\n"
        "Statement: 'Water boils at 100 degrees Celsius at sea level.'\n"
        "Classification: 1\n"
        "Explanation: This is a scientifically verified fact under standard atmospheric conditions.\n\n"
        "Example 2:\n"
        "Statement: 'The moon is made of cheese.'\n"
        "Classification: 0\n"
        "Explanation: The moon is composed of rock and metal, not cheese, making this statement false.\n\n"
        "Example 3:\n"
        "Statement: 'Chocolate ice cream is the best dessert.'\n"
        "Classification: 2\n"
        "Explanation: This is a subjective opinion about dessert preferences and cannot be fact-checked.\n\n"
        "Be concise and consistent in your evaluations."
    ),
}


messages = [
    sysrole,
    {   
        "role": "user",
        "content": (
            "2.7 million people came to america in 2022"
        ),
    },
]

client = OpenAI(api_key=API_KEY, base_url="https://api.perplexity.ai")

# chat completion without streaming
response = client.chat.completions.create(
    model="llama-3.1-sonar-small-128k-online",
    messages=messages,
)
print(response.choices[0].message.content)




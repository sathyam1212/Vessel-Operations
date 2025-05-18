import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = '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'

def test_openai_api():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        )
        print("AI Response:", response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_openai_api()
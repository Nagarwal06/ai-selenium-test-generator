import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_selenium_tests(user_story: str) -> str:
    prompt = f"""
You are a Senior QA Automation Engineer.

Generate Selenium test cases using Python and PyTest
for the following user story.

Include:
- Positive test cases
- Negative test cases
- Edge cases
- Assertions
- Page Object Model where appropriate

Target application: https://www.saucedemo.com/

User Story:
{user_story}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    with open("input/user_story.txt") as f:
        story = f.read()

    tests = generate_selenium_tests(story)

    os.makedirs("selenium_tests", exist_ok=True)
    with open("selenium_tests/test_login.py", "w") as f:
        f.write(tests)

    print("✅ Selenium tests generated successfully")

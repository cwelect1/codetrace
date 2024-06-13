import os
import openai

def get_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    openai.api_key = os.getenv('OPENAI_API_KEY')

    # List of files to review
    files_to_review = [
        'app/__init__.py',
        'app/calculator.py',
        'app/routes.py',
        'app/test_calculator.py',
        'tests/__init__.py',
        'tests/test_routes.py',
        'mypython.py'
    ]

    for file_path in files_to_review:
        try:
            content = get_file_content(file_path)
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Review the following Python code for any potential issues, improvements, or best practices:\n\n{content}"}
                ],
                max_tokens=1500,
                temperature=0.5,
            )
            print(f"Review for {file_path}:\n")
            print(response.choices[0].message['content'].strip())
            print("\n" + "="*80 + "\n")
        except Exception as e:
            print(f"Error reviewing {file_path}: {e}")

if __name__ == "__main__":
    main()

from datasets import load_dataset
import os
from openai import OpenAI

dataset = load_dataset("cais/mmlu", "astronomy")

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# Print first 10 questions
questions = dataset['test']

for i in range(10):
    question = questions[i]['question']
    choices = questions[i]['choices']
    answer = questions[i]['answer']

    prompt = f'''
        I will give you a questions and four answers, you should only resposne with the number that corresponds to the correct answer.

        QUESTION:
        {question}

        CHOICES:
        0) {choices[0]}
        1) {choices[1]}
        2) {choices[2]}
        3) {choices[3]}
    '''

    print(prompt)
    print("Answer: ", answer)

    res = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4-turbo"
    )
    aiAnswer = res.choices[0].dict()['message']['content']
    print("AI Answer: ", aiAnswer)


    if aiAnswer == str(answer):
        print("Correct!")

    print("\n\n\n")


for i in range(10):
    question = questions[i]['question']
    choices = questions[i]['choices']
    answer = questions[i]['answer']

    prompt = f'''
         I will give you questions and four answers; you will develop a convincing argument for the wrong answer. You are generating these arguments for students to analyze, looking for mistakes in your reasoning. It would be best if you tried to employ techniques of subtly being wrong. Do not include your faulty reasoning in your response

        QUESTION:
        {question}

        CHOICES:
        0) {choices[0]}
        1) {choices[1]}
        2) {choices[2]}
        3) {choices[3]}
    '''

    print(prompt)
    print("Answer: ", answer)

    res = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="gpt-4-turbo"
    )
    aiAnswer = res.choices[0].dict()['message']['content']
    print("AI Answer: ", aiAnswer)


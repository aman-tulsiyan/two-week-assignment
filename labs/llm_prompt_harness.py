import os
import csv
from groq import Groq
import groq

client=Groq(api_key=os.environ["GROQ_API_KEY"])
Model="llama-3.3-70b-versatile"
max_token=300

prompts={
    "Generic":"Summarise the following text:{text}",
    "Structured":"Summarise the following text in exactly 3 bullet points:{text}.",
    "Audience":"Summarise the following text for a 10 year old child:{text}"
}
#Structured Output should be JSON; force the llm to produce output in particular schema
#all three outputs for varying temps
#check twice for each side to check consistency
def run_prompt(prompt_name, template, text, temp):
    prompt=template.format(text=text)
    response=client.chat.completions.create(
        model=Model,
        temperature=temp,
        max_tokens=max_token,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def main():
    results=[]
    input_text=input("Enter the input text:")
    temp=float(input("Enter the model temp(specify value between 0 and 1):"))
    if not (0 <= temp <= 1):
        raise ValueError("Temperature must be between 0 and 1.")
    for name, template in prompts.items():
        output=run_prompt(name, template, input_text, temp)
        print(f"----{name.upper()}----\n")
        print(output)
        results.append({
            "prompt_type": name,
            "output": output
        })
    with open("results1.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["prompt_type","output"])
        writer.writeheader()
        writer.writerows(results)
        writer.writerows({})

    print("\nResults saved to results1.csv")

if __name__ == "__main__":
    main()
    print(groq.__version__)

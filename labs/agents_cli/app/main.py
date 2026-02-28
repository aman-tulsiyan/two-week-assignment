# main.py

from app.agent import run_agent

if __name__ == "__main__":
    print("Tool Agent Started. Type 'exit' to quit.\n")

    while True:
        query = input("Ask: ")

        if query.lower() == "exit":
            break

        response = run_agent(query)
        print(response)
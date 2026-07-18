from agent.memory import Memory


def main():

    memory = Memory()

    memory.add_user_message(
        "Research Artificial Intelligence."
    )

    memory.add_model_message(
        "I should search Wikipedia."
    )

    memory.add_tool_message(
        "Artificial intelligence (AI) is the simulation of human intelligence by machines."
    )

    memory.add_model_message(
        "Now I have enough information."
    )

    history = memory.get_history()

    print("=" * 60)
    print(f"History contains {len(history)} messages.")
    print("=" * 60)

    for index, content in enumerate(history, start=1):
        print(f"\nMessage {index}")
        print(f"Role: {content.role}")

        for part in content.parts:
            print(part.text)


if __name__ == "__main__":
    main()
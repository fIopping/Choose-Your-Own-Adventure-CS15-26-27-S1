if user_choice == "b":
    story = """

    """

    # ANSI escape sequences for colors
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    RESET = "\033[0m"  # Reset to default color


    def print_colored_messages():
        try:
            print(f"{RED}This is red text{RESET}")
            print(f"{GREEN}This is green text{RESET}")
            print(f"{YELLOW}This is yellow text{RESET}")
            print(f"{BLUE}This is blue text{RESET}")
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")


    if __name__ == "__main__":
        print_colored_messages()









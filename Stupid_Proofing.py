def ask_yes_no(prompt: str) -> bool:
    """Stupid-proofs yes/no inputs. Returns True for yes, False for no."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ('y', 'yes', 'yeah', 'yup', '1'):
            return True
        elif user_input in ('n', 'no', 'nope', 'nah', '0'):
            return False
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")




def ask_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    """Stupid-proofs integer inputs with optional range boundaries."""
    while True:
        user_input = input(prompt).strip()
        try:
            value = int(user_input)
            
            # Check boundaries if they are set
            if min_val is not None and value < min_val:
                print(f"Number too low. Must be at least {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Number too high. Must be no more than {max_val}.")
                continue
                
            return value
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")




def ask_choice(prompt: str, valid_choices: list) -> str:
    """Stupid-proofs inputs by matching against a specific list of valid options."""
    # Convert all valid choices to lowercase strings for easy, uniform comparison
    cleaned_choices = [str(choice).strip().lower() for choice in valid_choices]
    
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in cleaned_choices:
            # Return the original case-sensitive version from the user's list
            idx = cleaned_choices.index(user_input)
            return str(valid_choices[idx])
        else:
            options_str = ", ".join(f"'{c}'" for c in valid_choices)
            print(f"Invalid choice. Please choose from: {options_str}")

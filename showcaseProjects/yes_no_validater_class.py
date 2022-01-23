class Yes_No_validater:
    def __init__(self):
        self.function = None

    def yes_or_no_input(self, question):
        choice = input(f'{question} Please type YES or NO: ').upper()
        if choice == "NO":
            self.correct_input = False
        elif choice == "YES":
            self.correct_input = False
        else:
            print("Please type 'Yes' or 'No': ")
            print()
            self.correct_input = True
            
        return choice

    def validate_input(self, prompt_question):
        self.correct_input = True
        while self.correct_input:
            yes_or_no = self.yes_or_no_input(prompt_question)
        return yes_or_no
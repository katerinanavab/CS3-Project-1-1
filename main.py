import random

# You can initialize important data at the top of the program!
trivia = [{ 
           'question': "Who is the mayor of Pelican town?",
           'answer': 'Lewis',
           'options': ['Lewis', 'You', 'Marnie', 'Pierre']
           },
          { 
           'question': "It's Abigail's birthday! Pick a loved gift:",
           'answer': 'Amethyst',
           'options': ['Amethyst', 'Holly', 'Sugar', 'Quartz']
           },
          { 
           'question': "Which ore is found on floor 40 of the mines?",
           'answer': 'Silver',
           'options': ['Silver', 'Gold', 'Copper', 'Iridium']
           },
          ]


# Display the question and possible options
# Function takes question (String), answer (String), options (list)
# Function returns a boolean
def ask_question(question, answer, options):
    # 1. Print out a question from the trivia list
    print(question) 
    # 2. Print out the options (list)
    random.shuffle(options)
    for option in options:
        print(f"★ {option}")
    # 3. Get user input
    choice = input("Enter answer: ")
    # 4. Check if choice matches correct answer
    if choice.lower() == answer.lower():
        return True
    return False

# Main method for game loop
def main():
    print("Let's play 🐓 Stardew Valley 🚜 Trivia!")
    score = 0

    for num in range(len(trivia)):
        current = trivia[num] # dictionary
        # Get data from that item
        q = current['question']
        a = current['answer']
        ops = current['options']
        # Pass in q, a, and options into ask_question
        is_correct = ask_question(q, a, ops)
        print(is_correct) # test ask_question function
        # Update score accordingly
        if is_correct:
            score+=1

    # Display final score
    print(score)



if __name__ == "__main__":
    main()

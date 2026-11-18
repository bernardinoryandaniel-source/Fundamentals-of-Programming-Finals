import random

# Color codes for terminal feedback
GREEN = "\033[92m"
YELLOW = "\033[93m"
GRAY = "\033[90m"
RESET = "\033[0m"

# Dictionary grouped by word length, then by category
word_pool = {
    5: {
        "FRUIT": ["APPLE", "MANGO", "BERRY", "CACAO", "PEARS", "GUAVA", "LEMON", "MELON", "PEACH", "PRUNE", "GRAPE", "OLIVE", "CHICO", "ROWAN", "CAROB", "ACORN", "WHEAT", "BEANS", "BACCA", "HAZEL" ],
        "ANIMAL": ["TIGER", "ZEBRA", "SHARK", "WHALE", "SLOTH", "OTTER", "BISON", "MOUSE", "LEMUR", "OTTER", "PANDA", "MOOSE", "LLAMA", "EAGLE", "SKUNK", "RHINO", "GOOSE", "KOALA", "HORSE", "CAMEL"],
        "SPACE": ["EARTH", "ORBIT", "PLUTO", "COMET", "TITAN", "CERES", "VENUS"],
        "PLACE":["BEACH", "RIVER", "OCEAN", "ARENA", "FIELD", "STORE", "SWAMP", "TOWER", "COURT", "RIDGE", "PLAZA", "CLIFF", "GROVE", "HOTEL", "MOTEL", "MANOR", "HOUSE", "MARSH", "SHORE", "OASIS"],
    },
    6: {
        "FRUIT": ["BANANA", "CHERRY", "ORANGE"],
        "ANIMAL": ["MONKEY", "DONKEY", "JAGUAR"],
        "SPACE": ["SATURN", "GALAXY", "METEOR", "TRITON",],
        "PLACE": []
    },
    7: {
        "FRUIT": ["AVOCADO", "APRICOT", "COCONUT"],
        "ANIMAL": ["GIRAFFE", "DOLPHIN", "HAMSTER"],
        "SPACE": ["JUPITER", "NEPTUNE", "SHUTTLE"],
        "PLACE": []
    },
    8: {
        "FRUIT": ["TOMATOES", "MANDARIN"],
        "ANIMAL": ["KANGAROO", "ELEPHANT", "FLAMINGO"],
        "SPACE": ["UNIVERSE", "ASTEROID", "STARSHIP"],
        "PLACE": []    },
    9: {
        "FRUIT": ["PINEAPPLE", "RASPBERRY"],
        "ANIMAL": ["CHIMPANZEE", "ALLIGATOR"],
        "SPACE": ["TELESCOPE", "ASTRONAUT", "SUPERNOVA"],
        "PLACE":[]
    },
    10: {
        "FRUIT": ["WATERMELON", "STRAWBERRY"],
        "ANIMAL": ["RHINOCEROS", "CHAMELEON"],
        "SPACE": ["SPACECRAFT", "METEORITE", "EXOPLANETS"],
        "PLACE":[]
    }
}

print("🟩 🟨 ⬛ WELCOME TO CUSTOM LENGTH WORDLE ⬛ 🟨 🟩")
print("Type 'QUIT' at any time to exit.\n")

#Scoreboard
Score = 0

# MASTER INFINITE LOOP
while True:
    
    # 1. LOOP TO SELECT VALID WORD LENGTH (5 to 10)
    while True:
        length_input = input("Choose word length (5-10): ").strip()
        if length_input.upper() == "QUIT":
            print("Thanks for playing! Goodbye! 👋")
            exit()
            
        if length_input.isdigit():
            word_len = int(length_input)
            if 5 <= word_len <= 10:
                break
        print("❌ Invalid selection. Please enter a number between 5 and 10.")

    # 2. Pick a random category and secret word based on the chosen length
    available_categories = word_pool[word_len]
    category = random.choice(list(available_categories.keys()))
    secret_word = random.choice(available_categories[category])
    
    max_attempts = 7
    game_won = False
    
    print("\n" + "=" * 40)
    print(f"💡 CATEGORY: {category} ({word_len} letters)")
    print(f"You have {max_attempts} tries to guess the word.")
    print("=" * 40 + "\n")

    # 3. TURN LOOP (The 6 attempts)
    for attempt in range(1, max_attempts + 1):
        
        # 4. LOOP TO VALIDATE THE GUESS LENGTH
        while True:
            guess = input(f"Attempt {attempt}/{max_attempts} | Enter {word_len}-letter word: ").upper().strip()
            
            if guess == "QUIT":
                print("\nThanks for playing! Goodbye! 👋")
                exit()
                
            if len(guess) == word_len and guess.isalpha():
                break
            print(f"❌ Invalid. Input must be exactly {word_len} letters long (no numbers).")

        # 5. Process color feedback dynamically based on selected length
        feedback = ""
        for i in range(word_len):
            if guess[i] == secret_word[i]:
                feedback += f"{GREEN}{guess[i]}{RESET} "
            elif guess[i] in secret_word:
                feedback += f"{YELLOW}{guess[i]}{RESET} "
            else:
                feedback += f"{GRAY}{guess[i]}{RESET} "
                
        print(f"Result: {feedback}\n")

        # Check for a win
        if guess == secret_word:
            EarnedScore = (8 - attempt)
            Score += EarnedScore
            print(f"🎉 Winner! You guessed the word '{secret_word}' in {attempt} tries!\n")
            print(f"🏆 You gained {EarnedScore} points!")
            print(f"💰 Total Score: {Score} points\n")
            game_won = True
            break
            
    if not game_won:
        print(f"💀 Game Over! The secret word was: {secret_word}\n")
        Score = 0
        
    # Ask to continue
    play_again = input("Press Enter to play another round, or type 'NO' to quit: ").upper().strip()
    if play_again == "NO" or play_again == "QUIT":
        print(f"Your final score: {Score} points\n")
        print("Thanks for playing! Goodbye! 👋")
        break

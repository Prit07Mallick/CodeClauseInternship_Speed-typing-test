import time
import random

def get_random_sentence():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a high-level programming language.",
        "Coding is fun and challenging at the same time.",
        "Practice makes perfect!",
        "Hello, World! This is a typing test.",
    ]
    return random.choice(sentences)

def speed_typing_test():
    print("Welcome to the Speed Typing Test!")
    input("Press Enter to start...")
    
    sentence = get_random_sentence()
    print(f"\nType the following sentence:\n\n{sentence}\n")

    start_time = time.time()
    user_input = input("Your typing: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    words_per_minute = (len(sentence.split()) / elapsed_time) * 60
    accuracy = calculate_accuracy(sentence, user_input)

    print(f"\nTime: {elapsed_time:.2f} seconds")
    print(f"Words per minute: {words_per_minute:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")

def calculate_accuracy(original, user_input):
    original_words = original.split()
    user_words = user_input.split()

    correct_words = sum(1 for ow, uw in zip(original_words, user_words) if ow == uw)
    accuracy = (correct_words / len(original_words)) * 100

    return accuracy

if __name__ == "__main__":
    speed_typing_test()

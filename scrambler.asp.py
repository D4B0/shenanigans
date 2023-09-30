import re
import time
import math
import random
import string

stopcode = ["0", "!STOP", "!CANCEL", "!CLOSE"]

def slow_prt(text, prt_time, ending=""):
    if isinstance(prt_time, (int, float)):
        for slow_txt in text:
            time.sleep(prt_time)
            print(slow_txt, end="", flush=True)
    elif isinstance(prt_time, list):
        loop_no = 0; arr_no = 0;
        interval = round(len(text) / len(prt_time))
        for slow_txt in text:
            try:
                if loop_no % interval == 0:
                    if arr_no != 0:
                        time.sleep(prt_time[arr_no - 1])
                    arr_no += 1
                loop_no += 1
            except ZeroDivisionError as exception:
                pass
            print(slow_txt, end="", flush=True)
    if ending != "":
        print("", end=f"{ending}", flush=True)


def scramble(base_word):
    punct = ["'", "`", '"', ",", ".", ":", ";", "!", "?"]
    sym_math = ["-", "+", "=", "*", "/", "%", "^"]
    sym_others = ["@", "#", "&", "_", "(", ")", "<", ">"]
    delimiters = []
    delimiters.extend(punct)
    delimiters.extend(sym_math)
    delimiters.extend(sym_others)

    for delimiter in delimiters:
        base_word = base_word.replace(f"{delimiter}", f" {delimiter} ")
    sentence = base_word.split()

    # Initialisation
    scrambled_sentence = ""
    scrambled_sentence_arr = []
    for word in sentence:
        # Word Initialisation
        scrambled_word = "" # Scrambled Word String
        scrambled_arr = [] # Scrambled as Array
        word_arr = [] # Current Word as Array
        
        # Filling in the word array
        for i in range(len(word)):
            word_arr.append(word[i])

        # Scrambling word
        while len(scrambled_arr) != len(word_arr):
            # Select random char that's not at max
            rand_letter = random.choice(word_arr)
            letter_count = word_arr.count(rand_letter)
            repeat_count = scrambled_arr.count(rand_letter)

            # Add char if it isn't at its max
            if letter_count != repeat_count:
                scrambled_arr.append(rand_letter)
                
        
        scrambled_word = "".join(scrambled_arr)
        scrambled_sentence = scrambled_sentence + f"{scrambled_word} " 
        scrambled_sentence_arr.append(scrambled_arr)
        
    for delimiter in delimiters:
        base_word = base_word.replace(f" {delimiter} ", f"{delimiter}")
        scrambled_sentence = scrambled_sentence.replace(f" {delimiter} ", f"{delimiter}")

    # Printing    
    scramble_dump = {
        "base_text": base_word,
        "scrambled": scrambled_sentence,
        "base_text_arr": sentence,
        "scrambled_arr": scrambled_sentence_arr,
    }
    return scramble_dump


slow_prt("Word Scrambler lite", [0.03, 0.04, 0.6, 0.03, 0.015, 0.035, 0.09], ending="\n")
slow_prt("———————————————————", [0.02, 0.017, 0.25, 0.015, 0.009], ending="\n")
slow_prt("*Works with words and phrases", [0.02, 0.02, 0.15, 0.01, 0.002], ending="\n")
slow_prt("- (Be Mindful of punctuation)", [0.02, 0.02, 0.15, 0.01, 0.002], ending="\n")
slow_prt("*Type 0 or !CANCEL to close", [0.02, 0.02, 0.15, 0.01, 0.002], ending="\n\n")


while True:
    try:
        slow_prt("Base Text\n", [0.08, 0.11, 0.24, 0.41])
        base_word = input(">> ").strip()

        # Break on stopcode
        if base_word.upper() in stopcode:
            print("Program Closing in", end=" ")
            slow_prt("5\b4\b3\b2\b1\b0 ", 1., ending="\n")
            break

        slow_prt("Scrambling\b'", 0.06); 
        slow_prt("...", 0.15, ending="\n")

        # Scramble
        x = scramble(base_word)
        slow_prt(f"Unmodified Text:", [0.1, 0.12, 0.15, 0.3], ending=" ")
        slow_prt(f"{x['base_text']}", [0.06, 0.1, 0.05, 0.2], ending="\n")
        slow_prt(f"Scrambled Text:", [0.2, 0.2, 0.35, 0.7], ending=" ")
        slow_prt(f"{x['scrambled']}", [0.2, 0.2, 0.35, 0.7], ending="\n")

    except (ValueError, TypeError) as exception:
        raise f"UNKNOWN ERROR ENCOUNTERED {exception}"
        break
    
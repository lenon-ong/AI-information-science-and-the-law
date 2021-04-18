present_tense_list = ["see", "bear", "sell", "forget", "go hurt", "ride", "leave", "take", "be"]
past_tense_list = ["saw", "bore", "sold", "forgot", "went hurt", "rode", "left", "took", "was"]
tense_dictionary = dict(zip(past_tense_list, present_tense_list))
# key = past tense verb. value = respective present tense verb

def Present2Past(verb):
    for key, value in tense_dictionary.items():
        if value == verb: # if user's string input matches a value in present_tense_list, print the key.
            print(key)
            return
        else:
            print("")


user_input = input("Type the present tense of a verb here to convert it into past tense: ")

Present2Past(user_input)
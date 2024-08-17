names = ["Ivan", "Mario", "Monti", "Marto Stam", "Marto Cho",
         "Gesha", "Ivo", "Marto Mih", "Mitko", "Kalata", "Bruno"]
places = ["Sofia", "Grudovo", "Plovdiv", "Pomorie", "Krapec"]
verbs = ["plays", "watches", "listens to", "screams at", "drinks", "eats"]
nouns = ["football", "bottle of alcohol", "weights", "bike", "video game"]
adverbs = ["aggressively", "impatiently", "playfully", "expertly", "seriously"]
details = ["on the sidewalk", "in the grocery store", "at work", "at home", "at night", "during Christmas"]


def get_random_word(words):
    import random
    return random.choice(words)


print("Hello, this is your first random sentence:")
while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)
    print(f"{random_name} from {random_place} {random_adverb} {random_verb} "
          f"{random_noun} {random_detail}.")
    input("Click [Enter] to generate a new one.")

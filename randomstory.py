import random

# Story templates
stories = [
    "Once upon a time, there was a {adjective} {noun} who loved to {verb}. One day, it met a {adjective2} {noun2} and they became {relationship}.",
    "In the land of {place}, a {adjective} {noun} discovered a magical {object}. It granted them the power to {power}, but only for {duration}.",
    "Long ago, a {adjective} {noun} set out on a journey to find the lost {object}. Along the way, they encountered a {adjective2} {creature} who helped them on their quest."
]

# Word lists
nouns = ["wizard", "dragon", "knight", "princess", "robot", "detective"]
adjectives = ["brave", "clever", "mysterious", "fearless", "kind", "wicked"]
verbs = ["explore", "dance", "fight", "solve mysteries", "cast spells"]
places = ["Enchanted Forest", "Ancient Ruins", "Galaxy Z9", "Cyber City"]
objects = ["golden key", "enchanted book", "crystal ball", "time machine"]
powers = ["fly", "become invisible", "control fire", "speak to animals"]
durations = ["one hour", "a day", "a lifetime", "until sunset"]
creatures = ["elf", "giant", "talking cat", "ghost"]
relationships = ["best friends", "rivals", "soulmates", "teammates"]

# Generate a random story
def generate_story():
    story_template = random.choice(stories)
    story = story_template.format(
        adjective=random.choice(adjectives),
        noun=random.choice(nouns),
        verb=random.choice(verbs),
        adjective2=random.choice(adjectives),
        noun2=random.choice(nouns),
        relationship=random.choice(relationships),
        place=random.choice(places),
        object=random.choice(objects),
        power=random.choice(powers),
        duration=random.choice(durations),
        creature=random.choice(creatures)
    )
    
    return story

# Run the generator
print("\n📝 Your Random Story:\n")
print(generate_story())

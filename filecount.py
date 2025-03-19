def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = text.split()
        print(f"Word Count: {len(words)}")

count_words("sample.txt")

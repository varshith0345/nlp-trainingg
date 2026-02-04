import re

def clean_sentence(text):
    text = text.lower()
    words = re.findall(r"[a-z]+", text)

    stop_words = {"the", "are", "they", "over"}
    stem_map = {
        "foxes": "fox",
        "jumping": "jump"
    }

    result = []
    for word in words:
        if word in stop_words:
            continue
        result.append(stem_map.get(word, word))

    return result


sentence = """The quick,Brown foxes...
they are JUMPING over
10 lazy dogs!"""

print(clean_sentence(sentence))

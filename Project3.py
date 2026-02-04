spam_words = ["win", "free", "prize", "click here", "subscribe now"]
def is_spam(text, spam_words):
    text = text.lower()
    for word in spam_words:
        if word in text:
            return "spam"
    return "not spam"


message = "you are winning a free prize now!"
print(is_spam(message, spam_words))

def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()

def greet(func):
    greetings=func("Hi, I am created by function \ passed as an argument")
    print(greetings)

greet(shout)
greet(whisper)


import nltk
from nltk.chat.util import Chat, reflections

pairs=[
    [
        r"my name is (.*)",
        ["Hello %1, How are you?"]
    ],
    [
        r"Hi|Hello|Hey there|Hola",
        ["Hello my name is Hiesenberg"]
    ],
    [
        r"what is your name ?",
        ["I am a bot created by Heisenbergwhat. you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"I (.*) good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["Raghav created me using Python's NLTK library ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
    ],
    [
        r"i am looking for online guides and courses to learn data science, can you suggest?",
        ["Crazy_Tech has many great articles with each step explanation along with code, you can explore"]
    ],
    [
        r"quit",
        ["Thank you for using our intelligence services"]
    ],
    

]

def chat():
    print("Hey there! I am Heisenberg at your service")
    
    # Populate reflections dynamically
    reflections = {}
    for pattern, responses in pairs:
        for i, part in enumerate(pattern.split('(')[1:]):
            placeholder = '%' + str(i + 1)
            reflections[placeholder] = part.split(')')[0]

    # Create Chat instance with reflections
    chat = Chat(pairs)
    chat._substitute = lambda word: reflections.get(word, word)
    
    # Start conversation
    chat.converse()

chat()


# if above chat() function not work then use this ==>
# def chat():
#     print("Hey there! I am Heisenberg at your service")
#     chat = Chat(pairs)
#     chat.converse()



#still not work then,
# def chat():
#     print("Hey there! I am Heisenberg at your service")
#     chat = Chat(pairs, reflections)
#     while True:
#         inp = input("> ")
#         if inp == "quit":
#             print("TNknk you!")
#             break
#         response = chat.respond(inp)
#         print(response)


'''
# if above not work, then use this code.

import random
class Chatbot:
    def __init__(self):
        self.pairs = {
            "how are you ?" : ["i am dong good", "i am just a bot, i have no feelings","very bad!"],
            "which is your favourite film" : ["Inception", "fight club"],
            "what are you ?" : ["i am a bot"]
        }
    
    def getResponse(self, inp):
        inp = inp.lower()
        if inp in self.pairs:
            size = len(self.pairs[inp])
            index = random.randint(0, (size-1))
            return self.pairs[inp][index]
        if "my name is " in inp:
            name = inp.split("my name is ")[1]
            return f"Hi {name.capitalize()}!"
        else:
            return "i don't recognize it , Sorry"
        
chat = Chatbot()
while True:
    inp = input("> ")
    if inp == "quit":
        break
    print(chat.getResponse(inp))
'''
import random as r


random = r.Random()


quotes = [
    "Your parents are a bag of d*cks.",
    "If I die, don't eat my *ss that'd be weird.",
    "Camping is just being homeless without the change.",
    "Isn't it obvious Morty? I f*cked a planet.",
    "I wasn't born into the God business, I f*cking earned it.",
    "I programmed you to believe that.",
    "Whose kidneys are these?",
    "Stealing stuff is about the stuff, not the stealing.",
    "I think you have to think ahead and live in the moment.",
    "There's a lesson here and I'm not going to be the one to figure it out.",
    "I ain't better than sh*t, Jack",
    "Morty, you know outer space is up right?",
    "Morty, I'm a drunk, not a hack.",
    "I've got an emo streak. It's part of what makes me so rad.",
    "Can somebody just let me out of here? If I die in a cage I lose a bet.",
    "You guys, are the f*cking worst! Your gods are a lie! F*ck you, f*ck nature and f*ck trees!",
    "Ooh yeah, shame me. At least when I'm disgusting it's on purpose.",
    "Mr. President, if I've learned one thing today, it's that sometimes you have to not give a f*ck!",
    "Wait for the ramp, Morty. They love the slow ramp. It really gets their d*cks hard",
    "I love watching bukkake. I mean, like, I don't know if I would personally ever do it.",
    "That's because losers look stuff up while the rest of us are carp'en all them 'diems.",
]


def get_quote():
    return random.choice(quotes)

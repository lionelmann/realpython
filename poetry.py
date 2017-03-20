from random import choice

noun    = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb    = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj     = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep    = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverb  = ["curiously", "extravegantly", "tantalizing", "furiously", "sensuously"]

def makePoem(str):
    #nouns
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)

    #make sure all nouns are different
    while n1 == n2:
        n2 = choice(noun)
    while n1 == n3 or n2 == n3:
        n3 = choice(noun)

    #verbs
    v1 = choice(verb)
    v2 = choice(verb)
    v3 = choice(verb)

    #make sure all verbs are different
    while v1 == v2:
        v2 = choice(verb)
    while v1 == v3 or v2 == v3:
        v3 = choice(verb)
    
    print("{}, {}, {}".format(n1,n2,n3))
    print("{}, {}, {}".format(v1,v2,v3))

    return str

makePoem(str)

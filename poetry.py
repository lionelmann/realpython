from random import choice

noun    = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verb    = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adj     = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prep    = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverb  = ["curiously", "extravegantly", "tantalizing", "furiously", "sensuously"]

def makePoem(str):
    adverb1 = choice(adverb)

    prep1 = choice(prep)
    prep2 = choice(prep)

    while prep1 == prep2:
        prep2 = choice(prep)
    
    #nouns
    n1 = choice(noun)
    n2 = choice(noun)
    n3 = choice(noun)

    #make sure all nouns are different
    while n1 == n2: #if n1 equals n2 do while again
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

    adj1 = choice(adj)
    adj2 = choice(adj)
    adj3 = choice(adj)

    #make sure all adjectives are different
    while adj1 == adj2:
        adj2 = choice(adj)
    while adj1 == adj3 or adj2 == adj3:
        adj3 = choice(adj)

    print("A {} {}".format(adj1,n1))
    print("A {} {} {} {} the {} {} {}, the {} {}".format(adj1,n1,v1,prep1,adj2, n2, adverb1, n1, v2 ))
    print("the {} {} {} a {} {}".format(n1,v3, prep2, adj3, n3 ))

    return str

makePoem(str)

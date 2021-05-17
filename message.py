import random, pyperclip
def message():
    starters = ['Can I recover my ', 'I lost my ', 'I can\'t sign into my ', 'I lost my main ', 'I need to recover my ', 'Please help me I cannot access my ', 'I can\'t access my ']
    typ = ['game', 'account', 'village', 'base']
    s = random.randint(0, len(starters)-1)
    t = random.randint(0, len(typ)-1)
    pyperclip.copy(starters[s]+typ[t])

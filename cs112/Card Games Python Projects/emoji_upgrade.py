emojis = [":)", ":(", "._.", ":)))"]

def upgrade():
    
    for i in emojis:
        print(i)
    message = input('type one of the emojis above to recieve an alternate emoticon ')

    word = message.split(" ")
    emojis_up = {
    ':)': '^o^', ':(': '<_>', '._.': '-_-', ':)))': ':D'}

    output = ' '
    for word in word:
        output += emojis_up.get(word, word) + ' '

    print(output)
    upgrade()
    return output


upgrade()
    


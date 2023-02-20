def unpack_users(path):
    try:
        with open(path,"r") as f:
            content=f.readlines()
        for i in range(len(content)):
            if content[i][-1]=='\n':
                content[i]=content[i][:-1]
    except FileNotFoundError:
        raise FileNotFoundError(f"File {path}' does not exist")
    return content

def unpack_words(path):
    try:
        with open(path,"r") as f:
            words=f.readlines()
        for i in range(len(words)):
            if words[i][-1]=='\n':
                words[i]=words[i][:-1]
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' does not exist")
    return words

def add_new_users(players,file_name_players):
    try:
        with open(file_name_players,"w") as f:
            for name in players:
                f.write(name+"\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name_players}' does not exist")
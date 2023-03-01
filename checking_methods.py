def username_exists(username,players,name_status):
    if username in players:
        name_status.configure(text="Name not available")
        return True
    else:
        name_status.configure(text="Name available")
        return False

def validate_name(username,players,name_status,game_button):
    if len(username)==0:
        name_status.configure(text="Still waiting...")
        game_button.configure(state='disabled')
        return False
    elif username in players:
        name_status.configure(text="Name not available")
        game_button.configure(state='disabled')
        return False
    else:
        name_status.configure(text="Name available")
        game_button.configure(state='active')
        return True
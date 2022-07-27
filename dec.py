def show_menu(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
    return wrapper

@show_menu
def get_menu(menu):
    menu = menu.split()
    for i in range(len(menu)):
        print(f"{i+1}. {menu[i]}")


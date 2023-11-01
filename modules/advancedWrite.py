from colorama import init, Fore, Back
init()
class AdvancedWrite:
    def __init__(self) -> None:
        pass
    
    def info(self, text):
        print(f"{Back.LIGHTCYAN_EX}{Fore.BLACK}     INFO     {Fore.RESET}{Back.RESET}")
        print(f"{Back.LIGHTCYAN_EX}  {Back.RESET} {text}")
    
    def warning(self, text):
        print(f"{Back.LIGHTYELLOW_EX}{Fore.BLACK}     WARN     {Fore.RESET}{Back.RESET}")
        print(f"{Back.LIGHTYELLOW_EX}  {Back.RESET} {text}")
        
    def success(self, text):
        print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK}    SUCCESS    {Fore.RESET}{Back.RESET}")
        print(f"{Back.LIGHTGREEN_EX}  {Back.RESET} {text}")
        
    def error(self, text):
        print(f"{Back.LIGHTRED_EX}{Fore.BLACK}     ERROR     {Fore.RESET}{Back.RESET}")
        print(f"{Back.LIGHTRED_EX}  {Back.RESET} {text}")
       
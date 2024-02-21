import os
import platform

class Components:
    def __init__(self) -> None:
        pass
    def clearConsole():
        OS_Platform = platform.system()

        if OS_Platform == "Windows":
            os.system("cls")
        elif OS_Platform == "Linux":
            os.system("clear")
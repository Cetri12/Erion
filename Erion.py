
# Erion. v1.00.00 made 10/21/2026

Version = "Version: 1.00.00"
Build_Data = [Version, "Utility File", "Gen1"]

Mode = ""
Text = ""
File = ""

def TO_ELY():
    global File
    global Mode
    global Text

    if Mode == "File":
        with open(File, "r") as ElyFile:
            ElyText = ElyFile.read().lower()
            
            ElyText = ElyText.replace("b", "o")
            ElyText = ElyText.replace("c", "#")
            ElyText = ElyText.replace("d", "Δ")
            ElyText = ElyText.replace("e", "∑")
            ElyText = ElyText.replace("f", "₼")
            ElyText = ElyText.replace("g", "þ")
            ElyText = ElyText.replace("h", "ţ")
            ElyText = ElyText.replace("j", "ƒ")
            ElyText = ElyText.replace("k", "š")
            ElyText = ElyText.replace("l", "∫")
            ElyText = ElyText.replace("n", "ŋ")
            ElyText = ElyText.replace("o", "ȱ")
            ElyText = ElyText.replace("p", "π")
            ElyText = ElyText.replace("q", "¦")
            ElyText = ElyText.replace("s", "^")
            ElyText = ElyText.replace("t", "Ŧ")
            ElyText = ElyText.replace("u", "₺")
            ElyText = ElyText.replace("v", "‡")
            ElyText = ElyText.replace("w", "~")
            ElyText = ElyText.replace("x", "e")
            ElyText = ElyText.replace("y", "ỹ")
            ElyText = ElyText.replace("z", "Ω")
            print(ElyText)
        
    else:
        ElyText = Text
        ElyText = ElyText.replace("b", "o")
        ElyText = ElyText.replace("c", "#")
        ElyText = ElyText.replace("d", "Δ")
        ElyText = ElyText.replace("e", "∑")
        ElyText = ElyText.replace("f", "₼")
        ElyText = ElyText.replace("g", "þ")
        ElyText = ElyText.replace("h", "ţ")
        ElyText = ElyText.replace("j", "ƒ")
        ElyText = ElyText.replace("k", "š")
        ElyText = ElyText.replace("l", "∫")
        ElyText = ElyText.replace("n", "ŋ")
        ElyText = ElyText.replace("o", "ȱ")
        ElyText = ElyText.replace("p", "π")
        ElyText = ElyText.replace("q", "¦")
        ElyText = ElyText.replace("s", "^")
        ElyText = ElyText.replace("t", "Ŧ")
        ElyText = ElyText.replace("u", "₺")
        ElyText = ElyText.replace("v", "‡")
        ElyText = ElyText.replace("w", "~")
        ElyText = ElyText.replace("x", "e")
        ElyText = ElyText.replace("y", "ỹ")
        ElyText = ElyText.replace("z", "Ω")
        print(ElyText)
            
            


def ELYRION():
    global Mode
    global Text
    global File

    a = input("File or Text: ")
    if "file" in a.lower():
        File = input("File Name: ")
        Mode = "File"
        TO_ELY()

        

    if "text" in a.lower() or "txt" in a.lower():
        Text = input("Text: ")
        Mode = "Text"
        TO_ELY()


def intro():
    print("\033[35mErion")
    print(Version)
    print("English <--> ∑∫ỹriȱŋ")
    print("Eng translates to English, Ely translates to ∑∫ỹriȱŋ")
    a = input("Mode: \033[0m")
    if a.lower() == "ely":
        ELYRION()
    
    if a.lower() == "eng":
        print("Not Working Yet 😅")
        #ENGLISH()

intro()
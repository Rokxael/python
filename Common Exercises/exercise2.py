text = input("Phrase or texy you want to check: ")

def main():
    palabra = input("Please select a word: ")
    if palabra in text:
        print(text.count(palabra))
    else:
        print("The word you are looking fdor is not on this text")
        main()
    
    def rerun():
        again = input("Do you need help with anmy other word? Y / N: ")
        if again == "y":
            main()
        elif again == "n":
            print("Thanks for using my progam")
            return
        else:
            print("Please use a valid option")
            rerun()
    rerun()

main()
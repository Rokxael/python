def main():
    text = input("Phrase or texy you want to check: ")
    text1 = text.replace(" ","")
    text2 = text1[::-1]

    if text1.lower() == text2.lower():
        print("The text is a palindrome")
    else:
        print("The text is not a palindrome")    

    def rerun():
        again = input("Do you need help with anmy other phrase? Y / N: ")
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
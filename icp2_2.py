def string_alternative(inpStr):
    print("Output String: {}".format(inpStr[::2]))

def main():
    inpStr=input("Enter the Input String:")
    string_alternative("".join(inpStr.split()))

if __name__=="__main__":
    main()
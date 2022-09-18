def largestWord(s):
    # Sort the words in increasing
    # order of their lengths
    s = sorted(s, key=len)

    # Print last word
    print(s[-1])


# Driver Code
if __name__ == "__main__":
    # Given string
    s = input("enter the string:")

    # Split the string into words
    l = list(s.split(" "))

    largestWord(l)
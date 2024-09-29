def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def textToString():
    words = main().split()
    return(len(words))

#function that takes the text from book as string returns number of times each character appears in string
def numEachChacter():
    book_lower = main().lower()
    #dictionary to hold character count
    x_count = {}
    for word in book_lower:
        if word .isalpha():
            if word in x_count:
                x_count[word] += 1
            else:
                x_count[word] = 1 
    return x_count

def sort_dict():
    res = numEachChacter()
    for x in sorted(res, key=res.get, reverse=True):
        print(f"The '{x}' characer was found {res[x]} times")
    
def report():
    print("--- Begin report of books/frankenstein.txt ---")      
    print(f"{textToString()} words found in the document")      
    sort_dict()
    print("--- End report ---")
if __name__ == "__main__":

    report()
def read_book():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def count_words():
    words = read_book().split()
    return(len(words))

def count_characters_dict():
    book_lower = read_book().lower()
    x_count = {}
    for word in book_lower:
        if word.isalpha():
            if word in x_count:
                x_count[word] += 1
            else:
                x_count[word] = 1 
    return x_count

def sort_dict():
    countDict = count_characters_dict()
    for x in sorted(res, key=countDict.get, reverse=True):
        print(f"The '{x}' character was found {countDict[x]} times")
    
def report():
    print("--- Begin report of books/frankenstein.txt ---")      
    print(f"{count_words()} words found in the document")      
    sort_dict()
    print("--- End report ---")

if __name__ == "__main__":
    report()
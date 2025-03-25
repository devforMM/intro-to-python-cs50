def main():
 mot=input("Input: ").lower
 print(f"Output: {shorten(mot)}")



def shorten(word):
 voyells="aeiou"
 voyells=list(voyells)
 for char in word:
    if char in voyells:
       word=word.replace(char,"")
 return word



if __name__=="__main__":
  main()


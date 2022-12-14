import random
import matplotlib.pyplot as plt


def evaluateFrequency(word, book1, chapter1, verse1, book2, chapter2, verse2):
    file1 = open("bible.txt", "r")
    file1 = file1.readlines()
    count = 0
    for i in range(0, len(file1)):
        if(book1 in file1[i]):
            line0 = i
    for n in range(0, len(file1)):
        if(book2 in file1[n]):
            line1 = n
            break
    chverse1 = chapter1+":"+verse1
    chverse2 = chapter2+":"+verse2
    for j in range(line0, line1):
        if chverse1 in file1[j]:
            newline1 = j
            break
    for k in range(line1, len(file1)):
        if chverse2 in file1[k]:
            newline2 = k
            break
    for m in range(newline1, newline2):
        if word in file1[m]:
            count+=1
    return "The word "+word+" has a frequency of "+str(count/1000)+" per 1000 words"

def main():
    file1 = open("bible.txt", "r")
    file1 = file1.readlines()
    count = 0
    book1 = input("Enter the first book: ")
    chapter1 = input("Enter the first chapter: ")
    verse1 = input("Enter the first verse: ")
    print()
    book2 = input("Enter the second book: ")
    chapter2 = input("Enter the second chapter: ")
    verse2 = input("Enter the second verse: ")
    word = input("What word would you like to search for?")
    print(evaluateFrequency(word, book1, chapter1, verse1, book2, chapter2, verse2))
    wordcount = 0
    freqcount = 0
    freqlist = []
    count2 = 0
    even = []
    uneven = []
    word3 = ""
    while True:
        randnum1 = random.randint(1, len(file1))
        len1 = len(file1[randnum1].split())
        while(len1<=1):
            randnum1 = random.randint(1, len(file1))
            len1 = len(file1[randnum1].split())
        arr = file1[randnum1].split()
        randnum2 = random.randint(1, len1-1)
        word2 = arr[randnum2]
        while(len(word2)<5):
            randnum2 = random.randint(1, len1-1)
            word2 = arr[randnum2]
        for i in range(0, len(file1)):
            if word2 in file1[i]:
                wordcount+=1
            freqcount+=len(file1[i].split())
            if freqcount>=5000 and count2==0:
                freqlist.append(wordcount/freqcount)
                wordcount = 0
                freqcount = 0
                count2+=1
            elif freqcount>=5000 and count2>0:
                if 5*freqlist[0]<(wordcount/freqcount) or freqlist[0]/5>(wordcount/freqcount):
                    uneven.append(word2)
                wordcount = 0
                freqcount = 0
                count2+=1
        if len(uneven)>0:
            break
    freqcount = 0
    while freqcount<100000:
        for i in range(0, len(file1)):
            if word3 in file1[i]:
                wordcount+=1
            freqcount+=len(file1[i].split())
            if freqcount>=5000 and count2==0:
                freqlist.append(wordcount/freqcount)
                wordcount = 0
                freqcount = 0
                count2+=1
            elif freqcount>=5000 and count2>0:
                if 5*freqlist[0]<(wordcount/freqcount) or freqlist[0]/5>(wordcount/freqcount):
                    randnum1 = random.randint(1, len(file1))
                    len1 = len(file1[randnum1].split())
                    while(len1<=1):
                        randnum1 = random.randint(1, len(file1))
                        len1 = len(file1[randnum1].split())
                    arr = file1[randnum1].split()
                    randnum2 = random.randint(1, len1-1)
                    word3 = arr[randnum2]
                    wordcount = 0
                    freqcount = 0
                    count2=0
                    break
                count2+=1
    even.append(word3)
    if not word3[len(word3)-1].isalpha():
        word3 = word3[0:len(word3)-1]
    print(word3+ "is a word that is evenly distributed")
    word2 = uneven[0]            
    if not word2[len(word2)-1].isalpha():
        word2 = word2[0:len(word2)-1]
    print(word2+" is a word that is unevenly distributed")
    evencount = 0
    unevencount = 0
    wordcount = 0
    x1list = []
    y1list = []
    for i in range(0, len(file1)):
        wordcount+=len(file1[i].split())
        if(word3 in file1[i]):
            evencount+=1
        if(wordcount>5000):
            y1list.append(evencount)
            x1list.append(wordcount+5000)
            wordcount=0
    plt.plot(x1list, y1list)
    plt.show()
    evencount = 0
    unevencount = 0
    wordcount = 0
    x1list = []
    y1list = []
    for i in range(0, len(file1)):
        wordcount+=len(file1[i].split())
        if(word2 in file1[i]):
            unevencount+=1
        if(wordcount>5000):
            y1list.append(unevencount)
            x1list.append(wordcount+5000)
            wordcount=0
    plt.plot(x1list, y1list)
    plt.show()
        
    
main()

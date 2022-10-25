import random

def main():
    booknames = ["Genesis", "Exodus", "Leviticus", "Numbers Deuteronomy", "The Book of Joshua", "The Book of Judges", "The Book of Ruth", "The First Book of Samuel",
                "The Second Book of Samuel", "The First Book of the Kings", "The Second Book of the Kings", "The First Book of the Chronicles",
                "The Second Book of the Chronicles",
                'Ezra',
                'The Book of Nehemiah',
                'The Book of Esther',
                'The Book of Job',
                'The Book of Psalms',
                'The Proverbs',
                'Ecclesiastes',
                'The Song of Solomon'
                'The Book of the Prophet Isaiah',
                'The Book of the Prophet Jeremiah',
                'The Lamentations of Jeremiah',
                'The Book of the Prophet Ezekiel',
                'The Book of Daniel',
                'Hosea',
                'Joel',
                'Amos',
                'Obadiah',
                'Jonah',
                'Micah',
                'Nahum',
                'Habakkuk',
                'Zephaniah',
                'Haggai',
                'Zechariah',
                'Malachi',
                'The Gospel According to Saint Matthew',
                'The Gospel According to Saint Mark',
                'The Gospel According to Saint Luke',
                'The Gospel According to Saint John',
                'The Acts of the Apostles',
                'The Epistle of Paul the Apostle to the Romans',
                'The First Epistle of Paul the Apostle to the Corinthians',
                'The Second Epistle of Paul the Apostle to the Corinthians',
                'The Epistle of Paul the Apostle to the Galatians',
                'The Epistle of Paul the Apostle to the Ephesians',
                'The Epistle of Paul the Apostle to the Philippians',
                'The Epistle of Paul the Apostle to the Colossians',
                'The First Epistle of Paul the Apostle to the Thessalonians',
                'The Second Epistle of Paul the Apostle to the Thessalonians',
                'The First Epistle of Paul the Apostle to Timothy',
                'The Second Epistle of Paul the Apostle to Timothy',
                'The Epistle of Paul the Apostle to Titus',
                'The Epistle of Paul the Apostle to Philemon',
                'The Epistle of Paul the Apostle to the Hebrews',
                'The General Epistle of James',
                'The First Epistle General of Peter',
                'The Second General Epistle of Peter',
                'The First Epistle General of John',
                'The Second Epistle General of John',
                'The Third Epistle General of John',
                'The General Epistle of Jude',
                'The Revelation of Saint John the Divine']
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
    word = input("What word would you like to search for?")
    for m in range(newline1, newline2):
        if word in file1[m]:
            count+=1
    print("The word "+word+" showed up in this section "+str(count)+" times")
    wordcount = 0
    freqcount = 0
    freqlist = []
    count2 = 0
    even = []
    uneven = []
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
                    break
                wordcount = 0
                freqcount = 0
                count2+=1
        if len(uneven)>0:
            break                    
    word2 = uneven[0]            
    if not word2[len(word2)-1].isalpha():
        word2 = word2[0:len(word2)-1]
    print(word2+" is a word that is unevenly distributed")
    
    
main()

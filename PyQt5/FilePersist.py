class Book:
    def __init__(self,name,author):
        self.name=name
        self.author=author
# first=Book("Home alone","random")
# mis=Book("Any","Chetan bhagat")
# f=open("persit.db","wt")
# l=[first,mis]
# for item in l:
#     f.write(item.name+" ; "+item.author+"\n")
# f.close()
f=open("persist.db")
l=[]
for i in f:
    temp=i.split(" ")
    l.append(Book(temp[0],temp[1]))

for book in l:
    print(book.name," ; ",book.author)
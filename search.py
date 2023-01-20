from googlesearch import search
import wikipedia

query = input("Enter what do you want to search on goole?\nEnter the topic please or the query: ").lower()

try:
    result = wikipedia.summary(query, sentences=2)
    print("Acording to wikipedia: ")
    print(result)
except:
    print("")

i = 0
print("And down there are some of the websites links to view about more...")

for url in search(query):
    print(url)
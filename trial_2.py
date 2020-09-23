import wikipedia

a = input("Ask me something: ")
wikipedia.set_lang("en")
print(wikipedia.summary(a,sentences=3))
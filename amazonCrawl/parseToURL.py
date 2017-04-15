sourcePath = "100items.txt"
def parseStartUrls(source):
        with open(source) as f:
            content = f.readlines()
        return ["https://www.amazon.com/dp/"+x.strip() for x in content]

print parseStartUrls(sourcePath)
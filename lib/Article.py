
class Article:
    # store all article instances
    all_articles = []
    #initializing the attributes
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        self.all_articles.append(self)
    # returns the title name
    def title(self):
        return self._title
    
    # returns the name of the article author
    def author(self):
        return self._author
    
    # returns magazine with the articles mentioned
    def magazine(self):
        return self._magazine
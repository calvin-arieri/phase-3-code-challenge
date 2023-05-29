import Article

class Author:
    all_authors = []
    #initialize the author name
    def __init__(self, name):
        self._name = name
        self.all_authors.append(self)

    def name(self):
        return self._name
    
    # selects articles related to the current author
    def articles(self):
        return [article for article in Article.all_articles if article.author() == self]
    
    # selects magazines related to the current author
    def magazines(self):
        return list(set(article.magazine() for article in self.articles()))
    
    # adding new article(writer)
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    
    # find the categories that the author has written
    def topic_areas(self):
        return list(set(magazine.category() for magazine in self.magazines())) 
    
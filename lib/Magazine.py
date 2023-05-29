import Article


class Magazine:
    # receives all the magazine  instances

    all_magazines = []

    # initialize name and category
    def __init__(self, name, category):
        self._name = name
        self._category = category
        # adds instances to all magazine instance
        self.all_magazines.append(self) 

    # gives the name of the magazine 
    def name(self):
        return self._name
    
    # returns the category of the magazine
    def category(self):
        return self._category
    
    
    @classmethod
    def all(cls):
        # returns a list of  all magazine class instances
        return cls.all_magazines
    
    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            # iterates over all magazine instances and returns first magazine object that matches the given name
            if magazine.name() == name:
                return magazine
            
    # Returns a list of titles of all articles written for magazines of the current class (Magazine) 
    @classmethod                 
    def article_titles(cls):
        return [article.title() for article in Article.all_articles if article.magazine() == cls]

    def contributing_authors(self):
        # Retrieves a list of authors who have written articles for the current magazine instance
        authors = [article.author() for article in Article.all_articles if article.magazine() == self]
        return [author for author in authors if authors.count(author) > 2]
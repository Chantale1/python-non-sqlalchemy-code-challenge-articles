class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = str(title)
        Article.all.append(self)


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self.__name = name
        Author.all.append(self)

    @property
    def name(self):
        return self.__name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self.articles()))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
             return [article.title for article in self.articles()] or None

    def contributing_authors(self):

     return [author for author in self.contributors() if sum(1 for article in self.articles() if article.author == author) > 2] or None

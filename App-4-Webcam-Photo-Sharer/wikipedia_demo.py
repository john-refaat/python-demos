import wikipedia

class Wiki:
    def search_wiki(self, query):
        try:
            page = wikipedia.page(query)
            print(page.title)
        except wikipedia.exceptions.DisambiguationError as e:
            for result in wikipedia.search(query):
                try:
                    page = wikipedia.page(result)
                    print(page.title)
                    print(page.images)
                    return page.images[0]
                except wikipedia.exceptions.DisambiguationError | Exception as e:
                    print(e)
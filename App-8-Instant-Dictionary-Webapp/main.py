from inspect import isclass

import justpy as jp

from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home
from webapp.page import Page

imports = list(globals().values())

print('Routes:')
for imp in imports:
    if isclass(imp) and issubclass(imp, Page) and hasattr(imp, 'path'):
        print(f'Route: {imp}: {imp.path}')
        jp.Route(imp.path, imp.serve)


# jp.Route(Home.path, Home.serve)
# jp.Route(About.path, About.serve)
# jp.Route(Dictionary.path, Dictionary.serve)

jp.justpy(port=8001)
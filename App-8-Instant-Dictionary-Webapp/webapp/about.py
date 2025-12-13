import justpy as jp

from webapp.layout import DefaultLayout
from webapp.page import Page


class About(Page):

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)
        layout = DefaultLayout(a=wp)

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen text-center")
        jp.Div(a=div, text="What is Lorem Ipsum?", classes="text-4xl")
        jp.Div(a=div, classes="text-lg", text= """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
            when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining 
            essentially unchanged. It was popularised in the 1960s with the release of Letraset 
            sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
            like Aldus PageMaker including versions of Lorem Ipsum.
        """)
        return wp

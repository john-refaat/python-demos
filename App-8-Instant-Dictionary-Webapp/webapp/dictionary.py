import justpy as jp

from definition import Definition
from webapp.layout import DefaultLayout
from webapp.page import Page


class Dictionary(Page):

    path = "/dictionary"

    @classmethod
    def serve(cls, request):
        wp = jp.QuasarPage(tailwind=True)

        layout = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-4")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl")
        jp.Div(a=div, text="Gets the definition of any English word instantly", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-4")
        input_box = jp.Input(a=input_div, placeholder="Type in a word here...",
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:outline-none "
                         "focus:border-purple-500 py-2 px-4 focus:bg-white" )

        input_box.on('input', cls.get_definition)


        output_div = jp.Div(a=div, classes="m-2 p-2 overflow-y-auto txt-lg border-2 border-gray-400 h-40")

        input_box.output_div =  output_div

        print(cls)
        print(request)

        return wp

    @staticmethod
    def get_definition(widget, msg):
        print('get definition')
        term_definition = Definition(widget.value).get()
        #widget.output_div.text = " ".join([f"{i+1}- {x}" for i, x in enumerate(term_definition)])
        widget.output_div.delete_components()
        for d in term_definition:
            jp.Span(a=widget.output_div, text=d)
            jp.Br(a=widget.output_div)
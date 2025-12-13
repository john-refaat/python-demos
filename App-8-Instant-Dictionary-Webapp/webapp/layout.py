import justpy as jp


class DefaultLayout(jp.QLayout):

    def __init__(self, a=None):
        super().__init__(a=a, view="hHh lpR fFf")
        header = jp.QHeader(a=self, elevated=True, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True, v_model="leftDrawerOpen", side="left", bordered=True)
        scroll = jp.QScrollArea(a=drawer, classes="fit")
        qList = jp.QList(a=scroll, bordered=True)

        a_classes = "p-2 m-2 text-lg text-blue-500 hover:text-blue-800"
        jp.A(a=qList, href="/", text="Home", classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, href="/dictionary", text="Dictionary", classes=a_classes)
        jp.Br(a=qList)
        jp.A(a=qList, href="/about", text="About", classes=a_classes)
        jp.Br(a=qList)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                         icon="menu", click=self.toggle_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

    @staticmethod
    def toggle_drawer(widget, msg):
        widget.drawer.value = not widget.drawer.value


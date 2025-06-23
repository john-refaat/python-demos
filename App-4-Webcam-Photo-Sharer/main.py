from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from duckduck_go_demo import search_and_download_images
Builder.load_file("frontend.kv")

class FirstScreen(Screen):

    def search_image(self):
        print("Search Image")
        img_file = search_and_download_images(self.manager.current_screen.ids.user_query.text)
        print(img_file)
        self.manager.current_screen.ids.img.source = img_file if img_file else "images/beach.jpg"

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
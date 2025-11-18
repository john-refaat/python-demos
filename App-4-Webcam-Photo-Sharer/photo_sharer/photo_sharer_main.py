import time
import pyperclip

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import get_color_from_hex
from photo_sharer.file_uploader import FileUploader

Builder.load_file("photo_sharer_frontend.kv")

def copy_to_system_clipboard(text: str) -> None:
    """
    Copy the given text to the OS clipboard using tkinter.
    This does not use Kivy's clipboard backend, so it doesn't require xsel/xclip.
    """
    if not text:
        return

    root = tk.Tk()
    root.withdraw()  # Hide the tkinter window
    try:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()  # Now it stays on the clipboard after window is closed
    finally:
        root.destroy()

class CameraScreen(Screen):

    def capture(self):
        print("Capture")
        camera = self.ids['camera']
        time_str = time.strftime("%Y%m%d_%H%M%S")
        file_path = f"files/photo_{time_str}.png"
        camera.export_to_png(file_path)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.image.source = file_path
        self.manager.current_screen.ids.link_label.text = ""
        self.manager.current_screen.ids.link_label.color = get_color_from_hex('#FFFFFF')

    def toggle_camera(self):
        if not self.ids['camera'].play:
            self.start()
        else:
            self.stop()

    def start(self):
        print("Start")
        self.ids['camera'].opacity = 1
        self.ids['camera'].play = True
        self.ids.toggle_camera_button.text = 'Stop Camera'
        self.ids['capture_button'].disabled = False

    def stop(self):
        print("Stop")
        self.ids['camera'].opacity = 0
        self.ids['camera'].play = False
        self.ids['camera'].texture = None
        self.ids.toggle_camera_button.text = 'Start Camera'
        self.ids['capture_button'].disabled = True

class ImageScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_uploader = FileUploader()

    def create_link(self):
        print("Share")
        file_path = self.manager.current_screen.ids.image.source
        print(file_path)
        upload_link =  self.file_uploader.upload(file_path)
        self.ids.link_label.text = upload_link

    def back(self):
        print("Back")
        self.manager.current = "camera_screen"

    def open(self):
        print("Open")
        import webbrowser
        link = self.ids.link_label.text
        webbrowser.open(link)

    def copy_link(self):
        desired_text = self.ids.link_label.text.strip()
        if desired_text:
            pyperclip.copy(desired_text)
            self.ids.link_label.color = get_color_from_hex('#00FF00')

        

    def delete(self):
        print("Delete")
        import os
        file_path = self.manager.current_screen.ids.image.source
        os.remove(file_path)
        self.manager.current = "camera_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()



if __name__ == '__main__':
    MainApp().run()


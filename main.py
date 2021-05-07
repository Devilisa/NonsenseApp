from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from audioAdapter import AudioAdapter


class Tester(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_music = AudioAdapter('', False)
        self.background_music = AudioAdapter('', True)

    def play_sound(self):
        self.button_music.play_music()
        self.background_music.play_music()

    def stop_sound(self):
        self.button_music.play_music()
        self.background_music.stop_music()

    def increase_volume(self):
        self.button_music.play_music()
        self.background_music.increase_volume()

    def reduce_volume(self):
        self.button_music.play_music()
        self.background_music.reduce_volume()

    def set_volume(self):
        self.button_music.play_music()
        self.background_music.set_volume(0.5)


class SampleApp(App):

    def build(self):
        return Tester()


myApp = SampleApp()
myApp.run()

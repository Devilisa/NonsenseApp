from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from audioAdapter import AudioAdapter


class Tester(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.adapter = AudioAdapter('звук фон 3.mp3',True)

    def play_sound(self):
        self.adapter.play_music()

    def stop_sound(self):
        self.adapter.stop_music()

    def increase_volume(self):
        self.adapter.increase_volume()

    def reduce_volume(self):
        self.adapter.reduce_volume()

    def set_volume(self):
        self.adapter.set_volume(0.5)


class SampleApp(App):

    def build(self):
        return Tester()


myApp = SampleApp()
myApp.run()
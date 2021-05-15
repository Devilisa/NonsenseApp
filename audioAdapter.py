from kivy.core.audio import SoundLoader

class AudioAdapter:
    def __init__(self, music_file, loop):
        self.sound = SoundLoader.load(music_file)
        if self.sound:
            self.sound.loop = loop
        else:
            raise Exception("Не удалось загрузить музыкальный файл")

    def play_music(self):
        if self.sound.state == "play":
            pass
        else:
            self.sound.play()

    def stop_music(self):
        if self.sound.state == "stop":
            pass
        else:
            self.sound.stop()

    def increase_volume(self):
        if self.sound.volume < 0.9:
            self.sound.volume = self.sound.volume + 0.1
        else:
            self.sound.volume = 1

    def reduce_volume(self):
        if self.sound.volume > 0.1:
            self.sound.volume = self.sound.volume - 0.1
        else:
            self.sound.volume = 0

    def set_volume(self, level):
        if level <= 0:
            self.sound.volume = 0
        elif level >= 1:
            self.sound.volume = 1
        else:
            self.sound.volume = level


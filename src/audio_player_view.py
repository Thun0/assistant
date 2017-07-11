from view_component import ViewComponent
from settings import Settings
from button import Button
from log import Log


class AudioPlayerView(ViewComponent):

    def __init__(self):
        Log.i("Creating audio player view")
        self.buttons = []
        self.x = Settings.AUDIO_PLAYER_X
        self.y = Settings.AUDIO_PLAYER_Y
        self.buttons.append(Button("../res/audio_player/play_btn.png"))
        self.buttons.append(Button("../res/audio_player/stop_btn.png"))
        self.buttons.append(Button("../res/audio_player/next_btn.png"))
        self.buttons.append(Button("../res/audio_player/prev_btn.png"))

    def update(self):
        pass

    def blit(self, display):
        for btn in self.buttons:
            btn.blit(display)

from view_component import ViewComponent
from settings import Settings
from button import Button


class AudioPlayerView(ViewComponent):

    def __init__(self):
        self.x = Settings.AUDIO_PLAYER_X
        self.y = Settings.AUDIO_PLAYER_Y
        self.play_btn = Button("../res/audio_player/play_btn.png")
        self.stop_btn = Button("../res/audio_player/stop_btn.png")
        self.next_btn = Button("../res/audio_player/next_btn.png")
        self.prev_btn = Button("../res/audio_player/prev_btn.png")

    def update(self):
        pass

    def blit(self, display):
        self.play_btn.blit(display)
        self.stop_btn.blit(display)
        self.next_btn.blit(display)
        self.prev_btn.blit(display)

from pydub import AudioSegment
from pydub.playback import play
from log import Log
import eyed3


class AudioPlayer:

    def load_and_play_audio_file(self, filepath):
        idx = filepath.rfind(".")
        if idx == -1:
            Log.e("Extension not found in: " + filepath)
            return
        extension = filepath[idx+1:]
        # TODO: Check if file exists
        self.get_tag_info(filepath)
        audio = AudioSegment.from_file(filepath, format=extension)
        play(audio)

    def get_tag_info(self, filepath):
        audiofile = eyed3.load(filepath)
        print(audiofile)
        # print(audiofile.tag.title)

    def loop(self):
        Log.i("Audio player started")
        while True:
            pass

    def play_audio(self):
        pass

    def audio_loop(self):
        pass

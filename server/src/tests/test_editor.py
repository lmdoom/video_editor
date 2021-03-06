from src.tests.test_base import TestBase
import matplotlib.pyplot as plt


class TestEditor(TestBase):

    def test_slice_video(self):
        self.editor.slice_video(
            source=self.storage.list()[0].path,
            destination=self.storage.generate_file_path('test_slice_video.mp4'),
            start=0,
            end=2
        )

    def test_extract_audio(self):
        self.editor.extract_audio_from_video(
            self.storage.list()[0].path,
            self.storage.generate_file_path('test_extract_audio.mp3'),
            start=0,
            end=4
        )

    def test_apply_audio(self):
        self.editor.slice_video(
            source=self.storage.generate_file_path('test_1.mp4'),
            destination=self.storage.generate_file_path('test_apply_video.mp4'),
            start=0,
            end=5
        )
        self.editor.extract_audio_from_video(
            source=self.storage.generate_file_path('test_1.mp4'),
            destination=self.storage.generate_file_path('test_apply_audio.mp3'),
            start=8,
            end=13
        )
        self.editor.apply_audio(
            video_path=self.storage.generate_file_path('test_apply_video.mp4'),
            audio_path=self.storage.generate_file_path('test_apply_audio.mp3'),
            destination=self.storage.generate_file_path('test_apply_video_and_audio.mp4'),
        )

    def test_join_audios(self):
        self.editor.slice_video(
            source=self.storage.generate_file_path('test_1.mp4'),
            destination=self.storage.generate_file_path('test_apply_video.mp4'),
            start=0,
            end=5
        )
        self.editor.extract_audio_from_video(
            source=self.storage.generate_file_path('test_1.mp4'),
            destination=self.storage.generate_file_path('test_apply_audio.mp3'),
            start=8,
            end=13
        )
        self.editor.apply_audio(
            video_path=self.storage.generate_file_path('test_apply_video.mp4'),
            audio_path=self.storage.generate_file_path('test_apply_audio.mp3'),
            destination=self.storage.generate_file_path('test_apply_video_and_audio.mp4'),
        )

    def test_join_video(self):
        self.editor.join_videos(
            video_1=self.storage.generate_file_path('Big Video2.mp4'),
            video_2=self.storage.generate_file_path('Big Video2.mp4'),
            destination=self.storage.generate_file_path('test_video_joined.mp4'),
        )

    def test_slice_audio(self):
        self.editor.slice_audio(
            source=self.storage.generate_file_path('joined_audios.mp3'),
            destination=self.storage.generate_file_path('audio_cut.mp3'),
            start=0,
            end=13
        )

    def test_audio_wave_form(self):
        signal, time = self.editor.get_audio_wave_form_signal(
            audio_file_path=self.storage.generate_file_path('First_Reaper_Rev.mp3'),
        )
        plt.figure(1)
        plt.title('Signal Wave...')
        plt.plot(time, signal)
        plt.show()

    def test_video_wave_form(self):
        signal, time = self.editor.get_video_wave_form_signal(
            video_file_path=self.storage.generate_file_path('t_video5945077835449239268.mp4'),
        )
        plt.figure(1)
        plt.title('Signal Wave...')
        plt.plot(time, signal)
        plt.show()

    def test_resize_video(self):
        self.editor.resize_video(
            source=self.storage.generate_file_path('guitar_ESP.mp4'),
            destination=self.storage.generate_file_path('resized.mp4'),
            width=320
        )

    def test_resize_video_to_youtube_standard(self):
        self.editor.resize_video(
            source=self.storage.generate_file_path('Big Video2.mp4'),
            destination=self.storage.generate_file_path('resized.mp4'),
            width=1080,
        )

    def test_crop_video(self):
        self.editor.crop_video(
            source=self.storage.generate_file_path('20200529_152027.mp4'),
            destination=self.storage.generate_file_path('cropped.mp4'),
            x1=100,
            x2=-60
        )

    def test_image_to_video(self):
        self.editor.image_to_video(
            image_path=self.storage.generate_file_path('logo.jpg'),
            destination=self.storage.generate_file_path('logo_video.mp4'),
            duration=5
        )

    def test_video_fade_out(self):
        self.editor.video_fade_out(
            source=self.storage.generate_file_path('logo_video.mp4'),
            destination=self.storage.generate_file_path('logo_video_fade_out.mp4'),
            duration=2
        )

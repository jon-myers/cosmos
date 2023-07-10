# software written by Jon Myers [github.com/jon-myers ; jbmyers@ucsc.edu]
# Free to use, modify, and distribute with attribution for non-commercial
# purposes only.

from pydub import AudioSegment
import numpy as np
import io
from IPython.display import Audio, display
import scipy as sp
import matplotlib.pyplot as plt
import librosa
# import librosa.display

def audio_segment_to_np(segment, sample_rate = 48000, normalize = True):
    '''Converts an AudioSegment to a NumPy array.  The AudioSegment must be
    mono or stereo.  If stereo, the array will have two columns.  The array
    will be normalized to the range [-1, 1].  The sample rate of the array
    will be set to the specified sample_rate.'''
    segment.set_frame_rate(sample_rate)
    channel_sounds = segment.split_to_mono()
    arr = [s.get_array_of_samples() for s in channel_sounds]
    fp_arr = np.array(arr).T.astype(np.float32)
    if (normalize): 
        fp_arr /= np.iinfo(arr[0].typecode).max # normalize
    return fp_arr


def np_to_audio_segment(np_array, sample_rate=48000, channels=2):
    '''Converts a NumPy array to an AudioSegment.  The NumPy array must be
    mono or stereo.  '''
    # Convert the NumPy array to raw audio data
    raw_audio = np.array(np_array * 32767, dtype=np.int16).tobytes()
    # Create a new AudioSegment from the raw audio data
    audio_segment = AudioSegment(
        data=raw_audio,
        sample_width=2,  # 2 bytes per sample
        frame_rate=sample_rate,
        channels=channels  # Mono audio
    )
    return audio_segment

def load_audio(path, sample_rate=48000):
    '''Loads an audio file into a NumPy array'''
    audio_segment = AudioSegment.from_file(path)
    np_data = audio_segment_to_np(audio_segment, sample_rate=sample_rate)
    if (np.max(np.abs(np_data)) > 1):
        print(f"Max amplitude was {np.max(np.abs(np_data))}, normalizing.")
        np_data /= np.max(np.abs(np_data))
    if (np.shape(np_data)[1] == 1):
        np_data = np.repeat(np_data, 2, axis=1)
    return np_data

class AudioTrack:
    '''A class for storing and processing audio data in a numpy array'''
    def __init__(self, duration=10, sample_rate=48000, channels=2):
        self.duration = duration
        self.sample_rate = sample_rate
        self.channels = channels
        size = self.sample_rate * self.duration
        size = int(size)
        self.data = np.zeros((size, self.channels), dtype=np.float32)
    
    def show_audio(self):
        '''displays an audio element that the user can playback in the 
        notebook'''
        if (np.max(np.abs(self.data)) > 1):
            print("Audio would have clipped, had to normalize it first.")
            self.data /= np.max(np.abs(self.data))
        left = self.data[:, 0]
        right = self.data[:, 1]
        left = np.trim_zeros(left, 'b')
        right = np.trim_zeros(right, 'b')
        idx = np.max([np.shape(left)[0], np.shape(right)[0]])
        trimmed_data = self.data[:idx, :]
        audio_segment = np_to_audio_segment(trimmed_data, self.sample_rate)
        temp_file = io.BytesIO()
        audio_segment.export(temp_file, format="mp3")
        display(Audio(temp_file.getvalue(), rate=self.sample_rate))

    def add_audio(self, sample, time=0.0, gain=1.0, pan=0.0):
        '''adds a sample to the audio track at the specified time and gain
        pan is between -1 (left) and 1 (right)
        gain is between 0 and 1
        '''
        if (gain > 1.0): gain = 1.0
        if (gain < 0.0): gain = 0.0
        if (pan > 1.0): pan = 1.0
        if (pan < -1.0): pan = -1.0
        if (sample.shape[1] != self.channels):
            if (sample.shape[1] == 1):
                sample = np.repeat(sample, self.channels, axis=1)
            else:
                sample = sample.mean(axis=1).reshape(-1, 1)
        theta = np.pi * pan / 4
        mult = 2 ** (1/2) / 2
        b = (np.cos(theta) + np.sin(theta)) * mult
        a = (np.cos(theta) - np.sin(theta)) * mult
        sample = np.array([a * sample[:, 0], b * sample[:, 1]]).T
        start = int(time * self.sample_rate)
        end = start + sample.shape[0]
        if end > self.data.shape[0]:
            self.data = np.pad(self.data, ((0, end - self.data.shape[0]), (0, 0)), 'constant')
            # text = "Sample extends beyond the duration of the AudioTrack"
            # raise ValueError(text)
        self.data[start:end] += sample * gain
        

    def clear(self):
        '''clears the audio track, retaining its original size and shape'''
        self.data = np.zeros(self.data.shape, dtype=np.float32)

    def plot_spectrogram(self):
        left = self.data[:, 0]
        right = self.data[:, 1]
        left = np.trim_zeros(left, 'b')
        right = np.trim_zeros(right, 'b')
        idx = np.max([np.shape(left)[0], np.shape(right)[0]])
        trimmed_data = self.data[:idx, :]
        plt.figure(figsize=(20, 10))
        plt.subplot(2, 1, 1)
        plt.title("Left Channel")
        plt.specgram(trimmed_data[:, 0], Fs=self.sample_rate)
        plt.subplot(2, 1, 2)
        plt.title("Right Channel")
        plt.specgram(trimmed_data[:, 1], Fs=self.sample_rate)
        plt.show()

    def plot_cqt_spectrogram(self):
        left = self.data[:, 0]
        right = self.data[:, 1]
        left = np.trim_zeros(left, 'b')
        right = np.trim_zeros(right, 'b')
        idx = np.max([np.shape(left)[0], np.shape(right)[0]])
        trimmed_data = self.data[:idx, :]
        plt.figure(figsize=(20, 10))
        plt.subplot(2, 1, 1)
        plt.title("Left Channel")
        librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.cqt(trimmed_data[:, 0], sr=self.sample_rate)), ref=np.max), sr=self.sample_rate, x_axis='time', y_axis='cqt_note')
        plt.subplot(2, 1, 2)
        plt.title("Right Channel")
        librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.cqt(trimmed_data[:, 1], sr=self.sample_rate)), ref=np.max), sr=self.sample_rate, x_axis='time', y_axis='cqt_note')
        plt.show()

    def plot_waveform(self):
        left = self.data[:, 0]
        right = self.data[:, 1]
        left = np.trim_zeros(left, 'b')
        right = np.trim_zeros(right, 'b')
        idx = np.max([np.shape(left)[0], np.shape(right)[0]])
        trimmed_data = self.data[:idx, :]
        left = trimmed_data[:, 0]
        right = trimmed_data[:, 1]
        time_axis = np.arange(0, len(left)) / self.sample_rate
        # left channel above right channel
        # clear plt first
        plt.clf()
        plt.figure(figsize=(20, 10))
        plt.subplot(2, 1, 1)
        plt.title("Left Channel")
        plt.plot(time_axis, left)
        # y axis between -1 and 1
        plt.ylim(-1, 1)
        plt.subplot(2, 1, 2)
        plt.title("Right Channel")
        plt.plot(time_axis, right)
        plt.ylim(-1, 1)
        plt.show()


    
def play_audio(item):
    """helper method that can display audio whether you pass in a path, 
    AudioSegment, cosmos.AudioTrack, or np.array """
    if (item.__class__ == AudioTrack):
        item.show_audio()
    elif (item.__class__ == np.ndarray):
        audio_segment = np_to_audio_segment(item)
        temp_file = io.BytesIO()
        audio_segment.export(temp_file, format="wav")
        display(Audio(temp_file.getvalue(), rate=48000))
    elif (item.__class__ == AudioSegment):
        temp_file = io.BytesIO()
        item.export(temp_file, format="wav")
        display(Audio(temp_file.getvalue(), rate=48000))
    elif (item.__class__ == str):
        audio_segment = AudioSegment.from_file(item)
        temp_file = io.BytesIO()
        audio_segment.export(temp_file, format="wav")
        display(Audio(temp_file.getvalue(), rate=48000))



class PulseStructure:

    def __init__(self, size=4, duration=2, start_time=0):
        self.pulse_dur = duration / size
        self.times = np.linspace(start_time, start_time + duration, size,
                                    endpoint=False)

class Meter:
    '''a class for specifying hierarchically organized pulse structures'''
    def __init__(self, hierarchy=[4, 2, 2], tempo=120, cycles=1, start_time=0):
        self.hierarchy = hierarchy
        self.tempo = tempo
        self.cycles = cycles
        self.cycle_duration = hierarchy[0] * 60 / tempo
        self.start_time = start_time
        self.layer_durs = []
        for i, item in enumerate(self.hierarchy):
            if (i == 0):
                self.layer_durs.append(self.cycle_duration / item)
            else:
                container_dur = self.layer_durs[-1]
                self.layer_durs.append(container_dur / item)

    def get_time(self, pulse = [0, 0, 0], cycle = 0):
        '''returns the time of the specified pulse'''
        time = 0
        for i, item in enumerate(pulse):
            time += item * self.layer_durs[i]
        return time + cycle * self.cycle_duration
    
    def all_times(self, top_layer = None):
        '''returns a list of all the times in the meter'''
        if (top_layer is None):
            top_layer = len(self.hierarchy)
        all_times = []
        ranges = [np.arange(i) for i in self.hierarchy[:top_layer]]
        meshgrid = np.meshgrid(*ranges)
        combinations = np.column_stack([i.ravel() for i in meshgrid])
        cycle_times = np.array([self.get_time(i) for i in combinations])
        cycle_times.sort()
        all_times = np.tile(cycle_times, self.cycles) + self.start_time
        all_times = np.tile(cycle_times, self.cycles) + self.start_time
        adds = (np.arange(self.cycles) * self.cycle_duration).repeat(len(cycle_times))
        all_times += adds
        return all_times

class RandomWalk:
    '''a class for generating random walks'''

    def __init__(self, low=0, high=1, start=0.5, max_step=0.2):
        self.low = low
        self.high = high
        self.current = start
        self.max_step = max_step
    
    def step(self):
        self.current += np.random.uniform(-self.max_step, self.max_step)
        self.current = np.clip(self.current, self.low, self.high)
        return self.current

class Pattern:

    def __init__(self, durations, gains, samples, cycles=1, pans=None):
        self.durations = np.array(durations)
        self.gains = gains
        self.samples = samples
        self.cycles = cycles
        if (pans is None):
            self.pans = np.zeros(len(durations))
        else: 
            self.pans = np.array(pans)
        if (self.pans.size != self.durations.size):
            self.pans = np.repeat(self.pans[:1], self.durations.size)
        if (len(durations) != len(gains)):
            raise ValueError("durations and gains must be the same length")
        if (type(samples) == np.ndarray):
            self.samples = np.repeat([samples], len(durations), axis=0)
        if (len(samples) == 1):
            self.samples = np.repeat(samples, len(durations), axis=0)

    @staticmethod
    def randomized(size, cycle_duration, samples, cycles=1, divergence=2):
        '''divergence is the width of the durational difference; 
        the higher the divergence, the more dissimilar the durations of 
        successive events will be'''
        durations = 2 ** np.random.uniform(-divergence/2, divergence/2, size)
        durations *= cycle_duration / sum(durations)
        sample_choices = np.random.choice(np.arange(len(samples)), size)
        sample_choices = [samples[i] for i in sample_choices]
        gains = np.random.uniform(0.25, 1.0, size)
        pans = np.random.uniform(-1, 1, size)
        return Pattern(durations, gains, sample_choices, cycles, pans)
    
    @property
    def dur_tot(self):
        return self.cycles * sum(self.durations)
    
    @property
    def cycle_dur(self):
        return sum(self.durations)

    def set_cycle_duration(self, duration):
        '''sets the duration of a cycle of the pattern in seconds'''
        # self.cycles = duration / sum(self.durations)
        current_cycle_dur = sum(self.durations)
        rate = duration / current_cycle_dur
        self.durations *= rate

    def to_audio(self, sample_rate=48000):
        '''converts the pattern to a np array of audio data'''
        # overhang is length of biggest sample
        overhang = max([np.shape(i)[0] for i in self.samples])
        # overhang = self.samples[:].shape()
        # print(sum(self.durations))
        data_size = int(sample_rate * sum(self.durations) * self.cycles) + overhang
        audio = np.zeros((data_size, 2))
        start_time = 0
        for c in range(self.cycles):
            for i, item in enumerate(self.samples):
                end_time = start_time + np.shape(item)[0]
                add = item * self.gains[i]
                theta = np.pi * self.pans[i] / 4
                mult = 2 ** (1/2) / 2
                b = (np.cos(theta) + np.sin(theta)) * mult
                a = (np.cos(theta) - np.sin(theta)) * mult
                add = np.column_stack([add[:, 0] * a, add[:, 1] * b])
                audio[start_time:end_time] += add
                start_time += int(self.durations[i] * sample_rate)
        return audio
    
import scipy as sp

class SineWave:

    def __init__(self, frequency=440, duration=1.0, gain=1.0, pan=0.0, fade=True, sample_rate=48000):
        self.frequency = frequency
        self.duration = duration
        self.gain = gain
        self.sample_rate = sample_rate
        self.pan = pan
        self.fade = fade

    def to_audio(self):
        '''returns a sine wave of the specified frequency and duration'''
        samples = int(self.duration * self.sample_rate)
        x = np.arange(samples)
        y = np.sin(2 * np.pi * self.frequency * x / self.sample_rate)
        y *= self.gain
        theta = np.pi * self.pan / 4
        mult = 2 ** (1/2) / 2
        a = (np.cos(theta) + np.sin(theta)) * mult
        b = (np.cos(theta) - np.sin(theta)) * mult

        out = np.array([y * b, y * a]).T
        fade_size = int(self.sample_rate * 0.01)
        if (self.fade):
            fade = np.linspace(0, 1, fade_size)
            out[:fade_size] *= fade[:, np.newaxis]
            out[-fade_size:] *= fade[::-1, np.newaxis]
        return out

class MovingSineWave:

    def __init__(self, frequencies=[220, 330, 220], durations=[1, 1], gain=1, pan=0, fade=True, sample_rate=48000):
        self.frequencies = frequencies
        self.durations = durations
        self.gain = gain
        self.pan = pan
        self.sample_rate = sample_rate
        self.fade = fade

    def to_audio(self):
        # sample_times = np.linspace(0, sum(self.durations), int(sum(self.durations) * self.sample_rate))
        segments = []
        for i in range(len(self.durations)):
            sample_times = np.linspace(0, self.durations[i], int(self.durations[i] * self.sample_rate))
            segments.append(sp.signal.chirp(sample_times, self.frequencies[i], sample_times[-1], self.frequencies[i+1]))
        out = np.concatenate(segments)
        out *= self.gain
        theta = np.pi * self.pan / 4
        mult = 2 ** (1/2) / 2
        a = (np.cos(theta) + np.sin(theta)) * mult
        b = (np.cos(theta) - np.sin(theta)) * mult
        out = np.array([out * b, out * a]).T
        fade_size = int(self.sample_rate * 0.01)
        if (self.fade):
            fade = np.linspace(0, 1, fade_size)
            out[:fade_size] *= fade[:, np.newaxis]
            out[-fade_size:] *= fade[::-1, np.newaxis]
        return out

# sw = SineWave(440, 1, 0.5)


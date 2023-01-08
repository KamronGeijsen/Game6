import time
from typing import List

import pygame
import numpy as np
import scipy




BPM = 148/4
slider_speed = 1

screen_height = 100
screen_width = 100
track_width = 1000*0.5
note_width = track_width/8
note_height = note_width/5
note_space = note_width*slider_speed
scroll = -2


file = "tracks/Toby Fox - Undertale - Death by Glamour.wav"
sample_rate, samples = scipy.io.wavfile.read(file)
# frequencies, times, spectrogram = scipy.signal.spectrogram(samples, sample_rate)
# print(len(spectrogram))
track_x = (1000-track_width)/2
track_bar = screen_height*0.1
track_scroll_offset = 0.09
track_bar_scroll = track_bar / (note_space*4)

print(sample_rate)
# pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
track_mixer = pygame.mixer.Sound(file)
tick_mixer = pygame.mixer.Sound("tick1.mp3")

sub_bars = 4

# def start_from():
#     sec_delay = (scroll+track_scroll_offset)/ (BPM / 60 * sub_bars)
#     sample_delay = sample_rate * sec_delay
#     print(sec_delay, sample_delay)
#     print(len(pygame.mixer.Sound("tick1.mp3").get_raw()))
#     raw_data = pygame.mixer.Sound("tick1.mp3").get_raw()[int(sample_delay):]
#     return pygame.mixer.Sound(buffer=raw_data)


class Note:
    def __init__(self, x, y, w=1):
        self.x = x
        self.y = y
        self.w = w
        self.h = 1


class LongNote:
    def __init__(self, x, y, next, w=1):
        # self.
        self.x = x
        self.y = y
        self.w = w

        self.h = next


def undertale_generator():

    melody1 = [
        (0, 0),
        (1, 1),
        (3, 2),
        (2, 2.5),
        (0, 3.5),
        (0, 4.5),
        (1, 5),
        (3, 6),
        (2, 6.5),
    ]

    for i in range(16):
        yield Note(3, i, 2)
    for i in range(16):
        yield Note(2, i+16, 4)
    # for i in range(16):
    yield LongNote(3, 32, 6)
    yield LongNote(4, 38, 1)
    yield LongNote(5, 39, 1)
    yield LongNote(3, 40, 6)
    yield LongNote(2, 46, 1)
    yield LongNote(5, 47, 1)
    yield LongNote(4, 48, 7)
    yield LongNote(2, 55.25, 0.25)
    yield LongNote(3, 55.5, 0.25)
    yield LongNote(4, 55.75, 0.25)
    yield LongNote(5, 56, 8)

    melody2 = [
        (3, 0),
        (2, 0.25),
        (1, 0.5),
        (0, 0.75),
    ]
    for n, i in enumerate(range(64, 96, 8)):
        yield Note(n+0, i + 0)
        yield Note(n+3, i + 1)
        for p, d in melody2:
            yield Note(n+p, 2 + i + d)
        yield Note(n+0, i + 4.5)
        yield Note(n+3, i + 5)
        for p, d in melody2:
            yield Note(n+p, 6 + i + d)
    for i in range(96, 128, 8):
        yield LongNote(3, i, 0.5)
        yield Note(2, i+0.75)
        yield Note(3, i+1)
        yield LongNote(4, i+1.25, .5)


    # time = 0
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p+2, d+i*8)
    # time+=32
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p*2, time+d+i*8, 2)
    # melody2 = [
    #     (3, 0),
    #     (2, 0.25),
    #     (1, 0.5),
    #     (0, 0.75),
    #     (1, 1),
    # ]
    # for n, i in enumerate(range(64, 96, 8)):
    #     yield Note(n+0, i + 0)
    #     yield Note(n+1, i + 0.5)
    #     yield Note(n+3, i + 1)
    #     yield Note(n+2, i + 1.5)
    #     for p, d in melody2:
    #         yield Note(n+p, 2 + i + d)
    #     yield Note(n+0, i + 3.5)
    #     yield Note(n+0, i + 4.5)
    #     yield Note(n+3, i + 5)
    #     yield Note(n+2, i + 5.5)
    #     for p, d in melody2:
    #         yield Note(n+p, 6 + i + d)
    #     yield Note(n+0, i + 7.5)


notes: List[Note] = list(undertale_generator())

track_finger_count = [0]*8
last_track_finger_count = [0]*8
last_time = time.perf_counter()

wave_img = [pygame.surface.Surface((0, 0))]
total_pixels = 0


expected_lines_press = [0]*8
expected_lines_hold = [0]*8


def get_expected_lines():
    global last_track_finger_count
    LENIENCY = 0.2
    for i in range(8):
        expected_lines_press[i] = 0
        expected_lines_hold[i] = 0
    for n in notes:
        if scroll*sub_bars - LENIENCY < n.y < scroll*sub_bars + LENIENCY:
            for i in range(n.x, n.x+n.w):
                expected_lines_press[i] = max(1-abs(scroll*sub_bars - n.y)/LENIENCY, expected_lines_press[i])
        if type(n) == LongNote:
            if n.y - LENIENCY < scroll * sub_bars < n.y + n.h + LENIENCY:
                for i in range(n.x, n.x + n.w):
                    if n.y < scroll * sub_bars < n.y + n.h:
                        expected_lines_hold[i] = max(1, expected_lines_hold[i])
                    elif n.y - LENIENCY < scroll * sub_bars:
                        expected_lines_hold[i] = max(1-abs(scroll * sub_bars - n.y)/LENIENCY, expected_lines_hold[i])
                    elif scroll * sub_bars < n.y + n.h + LENIENCY:
                        expected_lines_hold[i] = max(1-abs(n.y+n.h - scroll * sub_bars)/LENIENCY, expected_lines_hold[i])

    for i in range(8):
        if track_finger_count[i] > last_track_finger_count[i]:
            if expected_lines_press[i] > 0:
                tick_mixer.play()

    last_track_finger_count = list(track_finger_count)


def generate_wave():
    global note_width, note_space, wave_img, total_pixels, last_time, track_mixer

    img_width = note_width
    total_pixels = len(samples)/sample_rate*(BPM/60)*note_space*sub_bars
    wave_img = [pygame.surface.Surface((img_width, 32768)) for _ in range(int(total_pixels)//32768+1)]
    samples_per_pixel = len(samples) / total_pixels
    l = 0
    n = int(total_pixels)-1
    for i in np.arange(samples_per_pixel, len(samples), samples_per_pixel):
        sample_slice = samples[l:int(i)]
        max = (np.amax(sample_slice) + 32768) / 65536
        min = (np.amin(sample_slice) + 32768) / 65536
        pygame.draw.line(wave_img[n // 32768], (255, 255, 255), (min * img_width, n % 32768), (max * img_width, n % 32768))
        l = int(i)
        n-=1
    last_time = time.perf_counter()
    # if scroll > 0:
    #     track_mixer.stop()
    #     print(scroll)
    #     track_mixer = start_from()
    #     track_mixer.play()


def scroller():
    global last_time, scroll, BPM
    current_time = time.perf_counter()

    interval = (current_time-last_time)
    last_time = current_time
    old_scroll = scroll

    scroll += interval * BPM/60
    if old_scroll < -track_scroll_offset < scroll:
        track_mixer.play()


def resize(event: pygame.event):
    global track_x, track_width, note_width, note_height, note_space, screen_width, screen_height, last_time, track_bar, track_bar_scroll
    screen_height = event.y
    screen_width = event.x
    track_width = screen_width*0.5
    note_width = track_width/8
    note_height = note_width/5
    note_space = note_width*slider_speed
    track_x = (screen_width-track_width)/2
    last_time = time.perf_counter()
    track_bar = screen_height * 0.1
    track_bar_scroll = track_bar / (note_space*4)


# def draw_feedback_animation(screen: pygame.Surface):
#     screen.


def draw(screen: pygame.Surface):

    # Finger press line lightup

    for i in range(8):
        if track_finger_count[i]:
            pygame.draw.rect(screen, (16, 16, 16), pygame.Rect(track_x+i*note_width, 0, note_width, screen_height))

    # Line borders (vert lines)

    for i in range(1, 8):
        pygame.draw.rect(screen, (48, 48, 48), pygame.Rect(track_x+i*note_width-note_width/100, 0, note_width/50, screen_height))

    # Line Beat and quarter beats (horiz lines)

    for i in np.arange(-(scroll-track_bar_scroll-int(scroll))*note_space*sub_bars, screen_height, note_space*sub_bars):
        for l in range(sub_bars):
            pygame.draw.rect(screen, (64, 64, 64), pygame.Rect(track_x, screen_height - i - note_height / 10 - l * note_space, track_width, note_height / 5))
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(track_x, screen_height - i - note_height / 6, track_width, note_height / 3))

    # Feedback of what should be pressed and what you pressed

    for i in range(8):
        press = expected_lines_press[i] * 255
        hold = expected_lines_hold[i] * 255

        if press > hold:
            c = (int(press*0.2), press, int(press*0.2))
        else:
            c = (int(hold * 0.2), hold, hold)
        pygame.draw.rect(screen, c, pygame.Rect(50 * i, 5, 50, 20))

        c = 255 if track_finger_count[i] else 0
        pygame.draw.rect(screen, (c, c, c), pygame.Rect(50 * i, 30, 50, 20))
        pygame.draw.line(screen, (128, 128, 128), (50 * i+50, 0), (50 * i+50, 50))
        pygame.draw.line(screen, (128, 128, 128), (50 * i , 0), (50 * i, 50))

    # Notes

    for n in notes:
        if type(n) == LongNote:
            pygame.draw.rect(screen, (128, 0, 64), pygame.Rect(
                track_x + n.x * note_width,
                screen_height-track_bar - n.y * note_space - note_height / 2 + note_space * sub_bars * scroll - note_space*n.h,
                n.w * note_width, note_height+note_space*n.h))
        else:
            pygame.draw.rect(screen, (192, 32, 32), pygame.Rect(
                track_x + n.x * note_width,
                screen_height - track_bar - n.y * note_space - note_height / 2 + note_space * sub_bars * scroll,
                n.w * note_width, note_height))

    # WAV

    i = -(screen_height-total_pixels+note_space*sub_bars*(scroll+track_scroll_offset))
    screen.blit(wave_img[int(i)//32768], [track_x + track_width, -(i%32768) - track_bar])
    if 32768-i%32768 < screen_height and i < total_pixels:
        screen.blit(wave_img[int(i) // 32768 + 1], [track_x + track_width, -(i % 32768) + 32768 - track_bar])
    pygame.draw.line(screen, (255, 255, 255), (track_x, screen_height-track_bar), (track_x+track_width, screen_height-track_bar))

    # Vertical borders of the track

    pygame.draw.rect(screen, (192, 192, 192), pygame.Rect(track_x - note_width / 50, 0, note_width / 25, screen_height))
    pygame.draw.rect(screen, (192, 192, 192), pygame.Rect(track_x+track_width - note_width / 50, 0, note_width / 25, screen_height))


import time
from typing import List

import pygame
import numpy as np
import scipy




BPM = 148/4
slider_speed = 4

screen_height = 100
screen_width = 100
track_width = 1000*0.5
note_width = track_width/8
note_height = note_width/5
note_space = note_width*slider_speed
scroll = -4

file = "tracks/Toby Fox - Undertale - Death by Glamour.wav"
sample_rate, samples = scipy.io.wavfile.read(file)
track_x = (1000-track_width)/2
track_scroll_offset = 0.09

print(sample_rate)
# pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
track_mixer = pygame.mixer.Sound(file)

class Note:
    def __init__(self, x, y, w=1):
        self.x = x
        self.y = y
        self.w = w
        self.h = 1


class LongNote:
    def __init__(self, x, y, h, w=1):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


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
    yield LongNote(2, 55, 0.5)
    yield LongNote(3, 55, 0.5)
    yield LongNote(4, 55.5, 0.5)
    yield LongNote(5, 56, 8)

    melody2 = [
        (3, 0),
        (2, 0.25),
        (1, 0.5),
        (0, 0.75),
        (1, 1),
    ]
    for i in range(0,32,8):
        yield Note(2, i + 64)
        yield Note(3, i + 64.5)
        yield Note(5, i + 65)
        yield Note(4, i + 65.5)
        for p, d in melody2:
            yield Note(2+p, 66 + i + d)
        yield Note(2, i + 67.5)
        yield Note(2, i + 68.5)
        yield Note(5, i + 69)
        yield Note(4, i + 69.5)
        for p, d in melody2:
            yield Note(2+p, 70 + i + d)
        yield Note(2, i + 71.5)
    # time = 0
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p+2, d+i*8)
    # time+=32
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p*2, time+d+i*8, 2)


notes: List[Note] = list(undertale_generator())
sub_bars = 4

track_finger_count = [0]*8
measurements = []
last_time = time.perf_counter()

wave_img = [pygame.surface.Surface((0, 0))]
total_pixels = 0
def generate_wave():
    global note_width, note_space, wave_img, total_pixels

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
        pygame.draw.line(wave_img[n//32768], (255, 255, 255), (min*img_width, n%32768), (max*img_width, n%32768))
        l = int(i)
        n-=1
    print("done")


def scroller():
    global last_time, scroll, BPM
    current_time = time.perf_counter()

    interval = (current_time-last_time)
    last_time = current_time
    old_scroll = scroll

    scroll += interval * BPM/60
    if old_scroll < -track_scroll_offset < scroll:
        track_mixer.play(loops=0, maxtime=0, fade_ms=0)


def resize(event: pygame.event):
    global track_x, track_width, note_width, note_height, note_space, screen_width, screen_height, last_time
    screen_height = event.y
    screen_width = event.x
    track_width = screen_width*0.5
    note_width = track_width/8
    note_height = note_width/5
    note_space = note_width*slider_speed
    track_x = (screen_width-track_width)/2
    last_time = time.perf_counter()


def draw(screen: pygame.Surface):
    scroller()

    for i in range(8):
        if track_finger_count[i]:
            screen.fill((16, 16, 16), (track_x+i*note_width, 0, note_width, screen_height))
    for i in range(1, 8):
        screen.fill((48, 48, 48), (track_x+i*note_width-note_width/100, 0, note_width/50, screen_height))
    for i in np.arange(-(scroll-int(scroll))*note_space*sub_bars, screen_height, note_space*sub_bars):
        for l in range(sub_bars):
            screen.fill((64, 64, 64), (track_x, screen_height - i - note_height / 10 - l * note_space, track_width, note_height / 5))
        screen.fill((128, 128, 128), (track_x, screen_height - i - note_height / 6, track_width, note_height / 3))



    # pygame.draw.line(screen, (255, 255, 255), (track_x, scroll+note_space), (track_x, height))



    for n in notes:
        if type(n) == LongNote:
            pygame.draw.rect(screen, (255, 0, 128), pygame.Rect(track_x + n.x * note_width,
                                        screen_height - n.y * note_space - note_height / 2 + note_space * sub_bars * scroll - note_space*n.h,
                                        n.w * note_width,
                                        note_height+note_space*n.h))
        else:
            pygame.draw.rect(screen, (255, 0, 128), pygame.Rect(track_x+n.x*note_width, screen_height-n.y*note_space-note_height/2+note_space*sub_bars*scroll, n.w*note_width, note_height))

    # sec_offs = scroll/(BPM/60)
    i = -(screen_height-total_pixels+note_space*sub_bars*(scroll+track_scroll_offset))
    screen.blit(wave_img[int(i)//32768], [track_x + track_width, -(i%32768)])
    if 32768-i%32768 < screen_height and i < total_pixels:
        screen.blit(wave_img[int(i) // 32768 + 1], [track_x + track_width, -(i % 32768) + 32768])
    # screen.blit(wave_img, [0, 0])
    # print(note_space*sub_bars*scroll)

    # pygame.draw.line(screen, (255, 255, 255), (track_x, 0), (track_x, height))
    # pygame.draw.line(screen, (255, 255, 255), (track_x+track_width, 0), (track_x+track_width, height))


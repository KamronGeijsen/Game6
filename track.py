import time
from typing import List

import pygame
import numpy as np
import scipy

BPM = 148/4
slider_speed = 4

screen_height = 100
screen_width = 100
track_width = 1000*0.75
note_width = track_width/8
note_height = note_width/5
note_space = note_width*slider_speed
scroll = -2
# scroll = 20
# scroll = 48
# scroll = 38

file = "tracks/Toby Fox - Undertale - Death by Glamour.wav"
sample_rate, samples = scipy.io.wavfile.read(file)
# frequencies, times, spectrogram = scipy.signal.spectrogram(samples, sample_rate)
# print(len(spectrogram))
track_x = (1000-track_width)/2
track_bar = screen_height*0.1
track_scroll_offset = 0.09
track_bar_scroll = track_bar / (note_space*4)

print(sample_rate)
pygame.mixer.pre_init(48000, -16, 2, 512)
pygame.mixer.init()
track_mixer = pygame.mixer.Sound(file)
tick_mixer = pygame.mixer.Sound("tick1.wav")
# print(pygame.mixer.get_init())

sub_bars = 4
combo = 0
score = 0

debug_hits = []


def start_from():
    sec_delay = (scroll+track_scroll_offset) / (BPM / 60)
    sample_delay = sample_rate * sec_delay
    raw_data = samples[int(sample_delay):]
    return pygame.mixer.Sound(buffer=raw_data)


def set_tick_volume(m):
    global tick_mixer
    sample_rate, samples = scipy.io.wavfile.read("tick1.wav")
    # print(type(tick_mixer.get_raw()))
    print(len(samples))
    dt = np.dtype(int)
    dt = dt.newbyteorder('<')
    samples = np.frombuffer(tick_mixer.get_raw(), dtype=dt)
    print(len(samples))
    samples = samples*m
    print(sample_rate, pygame.mixer.get_init())
    tick_mixer = pygame.mixer.Sound(buffer=samples)

set_tick_volume(2)


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

    for p, d in melody1:
        yield Note(p+2, d)
    for p, d in melody1:
        yield Note(p+2, d+8)
    for p, d in melody1:
        yield Note(p*2, d+16, 2)
    for p, d in melody1:
        yield Note(p*2, d+24, 2)
    # for i in range(16):
    #     yield Note(3, i, 2)
    # for i in range(16):
    #     yield Note(2, i+16, 4)
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
    # for n, i in enumerate(range(64, 96, 8)):
    #     yield Note(n+0, i + 0)
    #     yield Note(n+3, i + 1)
    #     for p, d in melody2:
    #         yield Note(n+p, 2 + i + d)
    #     yield Note(n+0, i + 4.5)
    #     yield Note(n+3, i + 5)
    #     for p, d in melody2:
    #         yield Note(n+p, 6 + i + d)
    for n, i in enumerate(range(96, 160, 16)):
        yield Note(4, i)
        yield Note(5, i + 0.5)
        yield Note(4, i + 1.0)
        yield Note(2, i + 1.25)
        yield Note(2, i + 1.75)
        yield Note(3, i + 2.25)
        yield Note(4, i + 2.5)
        yield Note(5, i + 3)
        yield Note(4, i + 3.5)
        yield Note(2, i + 4.0)
        yield Note(3, i + 4.5)
        yield Note(4, i + 5.00)
        yield Note(5, i + 5.25)
        yield Note(4, i + 5.5)
        yield Note(4, i + 6.0)
        yield Note(3, i + 6.25)
        yield Note(2, i + 6.5)
        yield Note(3, i + 7)
        yield Note(2, i + 7.5)

        yield Note(2, i + 8.0)
        yield Note(3, i + 8.25)
        yield Note(4, i + 8.5)
        yield Note(5, i + 8.75)
        yield Note(2, i + 9)

        if n == 3:
            yield Note(2, i + 10)
            yield Note(3, i + 10.25)
            yield Note(4, i + 10.5)
            yield Note(5, i + 10.75)
            yield Note(2, i + 11)

            yield Note(2, i + 12)
            yield Note(3, i + 12.25)
            yield Note(4, i + 12.5)
            yield Note(5, i + 12.75)

            yield Note(2, i + 13)
            yield Note(3, i + 13.25)
            yield Note(4, i + 13.5)
            yield Note(5, i + 13.75)

            yield Note(2, i + 14)
        else:
            yield Note(3, i + 12)
            yield Note(4, i + 12.125)
            yield Note(5, i + 12.25)
            yield Note(5, i + 13)

            yield Note(4, i + 13.5)
            yield Note(3, i + 14)
            yield Note(3, i + 14.5)
            yield Note(2, i + 15)

            yield Note(3, i + 15.5)

        for n, i in enumerate(range(96, 160, 8)):
            yield Note(0, i, 2)
            if n == 7:
                yield Note(0, i + 2, 2)
                yield Note(0, i + 4, 2)
                yield Note(0, i + 5, 2)
                yield Note(0, i + 6, 2)

        yield Note(2, 160 - 0.5)
        yield Note(3, 160 - 0.325)
        yield Note(4, 160 - 0.25)
        yield Note(5, 160 - 0.125)
        for n, i in enumerate(range(160, 224, 16)):
            if n == 0 or n == 2:
                yield Note(0, i, 8)
                yield LongNote(6, i, 2, 2)
                yield LongNote(4, i, 2, 2)
                yield LongNote(5, i + 2, 2, 2)
                yield LongNote(3, i + 2, 2, 2)
                yield Note(0, i+4, 8)
                yield LongNote(2, i + 4, 3)
                yield LongNote(5, i + 4, 1)
                yield LongNote(4, i + 5, 1)
                yield LongNote(7, i + 6, 1)
                yield LongNote(6, i + 7, 1)
                yield Note(3, i + 7)
                yield LongNote(2, i + 8, 2)
                yield LongNote(5, i + 8, 2)
                yield LongNote(4, i + 10, 2)
                yield Note(3, i + 10)
            else:
                yield Note(0, i, 8)
                yield LongNote(0, i, 2, 2)
                yield LongNote(2, i, 2, 2)
                yield LongNote(1, i + 2, 2, 2)
                yield LongNote(3, i + 2, 2, 2)
                yield Note(0, i + 4, 8)
                yield LongNote(5, i + 4, 3)
                yield LongNote(2, i + 4, 1)
                yield LongNote(3, i + 5, 1)
                yield LongNote(0, i + 6, 1)
                yield LongNote(1, i + 7, 1)
                yield Note(4, i + 7)
                yield LongNote(5, i + 8, 2)
                yield LongNote(2, i + 8, 2)
                yield LongNote(3, i + 10, 2)
                yield Note(4, i + 10)
            if n == 0 or n == 2:
                for l in range(4):
                    yield Note(1, i + 12.00 + l, 2)
                    yield Note(4, i + 12.00 + l, 1)
                    yield Note(5, i + 12.125 + l, 1)
                    yield Note(6, i + 12.25 + l, 1)
                    yield Note(7, i + 12.325 + l, 1)
            elif n == 1:
                for l in range(4):
                    yield Note(5, i + 12.00 + l, 2)
                    yield Note(3, i + 12.00 + l, 1)
                    yield Note(2, i + 12.125 + l, 1)
                    yield Note(1, i + 12.25 + l, 1)
                    yield Note(0, i + 12.325 + l, 1)
        yield Note(3, 224 - 4, 2)
        yield Note(3, 224 - 3.25, 2)
        yield Note(2, 224 - 2.5, 4)
        yield Note(1, 224 - 2, 6)
        yield Note(1, 224 - 1.825, 6)
        yield Note(0, 224 - 1, 8)

        for n, i in enumerate(range(224, 288, 16)):
            if n == 1 or n == 3:
                yield Note(6, i+0.5, 2)
            else:
                yield Note(6, i, 2)
            yield Note(6, i+1, 2)
            yield Note(5, i+1.5, 2)
            yield Note(6, i+1.75, 2)

            yield Note(5, i + 3, 2)
            yield Note(3, i + 3.5, 2)
            yield Note(1, i + 4, 2)
            yield Note(3, i + 4.5, 2)
            yield Note(5, i + 5, 2)
            yield Note(3, i + 5.75, 2)
            yield Note(1, i + 6, 2)

            yield Note(1, i + 3, 2)
            yield Note(5, i + 4, 2)
            yield Note(1, i + 5, 2)
            yield Note(5, i + 6, 2)

            yield Note(4, i + 7)
            yield Note(3, i + 7.5)
            yield Note(3, i + 8, 3)
            yield Note(2, i + 8.75, 3)
            yield Note(3, i + 9.5, 3)
            yield Note(2, i + 10, 3)

            yield Note(3, i + 11)
            yield Note(4, i + 11.5)
            yield Note(2, i + 12, 3)
            yield Note(3, i + 12.75, 3)
            yield Note(2, i + 13.5, 3)
            yield Note(3, i + 14, 3)

            if n == 1 or n == 3:
                yield Note(4, i+15)
                yield Note(5, i + 15.5)
            else:
                yield Note(4, i + 15)
                yield Note(3, i + 15.5)

        for i in range(4):
            for p, d in melody1:
                yield Note(p*2, 288+d+i*8, 2)
        for p, d in melody1[:8]:
            yield Note(p + 2, 320 + d)
        # for n, i in enumerate(range(224, 288)):
        #     if n//16 % 2 == 0:
        #         yield Note(0+n//4%2, i)
        #         yield Note(2+n//4%2, i+.5)
        #     else:
        #         yield Note(7-n//8%2, i)
        #         yield Note(5-n//8%2, i + .5)



        # for n, i in enumerate(range(160, 224, 4)):
        #     if n%4 == 1:
        #         yield Note(0, i+3, 2)
        #     if n%4 == 2:
        #         yield Note(0, i+2, 2)
        #     if n%4 == 3:
        #         yield Note(0, i + 1, 2)
        #         yield Note(0, i + 2, 2)
        #         yield Note(0, i + 3, 2)
        #     yield Note(0, i, 2)


        # yield LongNote(3, i, 0.5)
        # yield Note(2, i+0.75)
        # yield Note(3, i+1)
        # yield LongNote(4, i+1.25, .5)
        #
        # yield LongNote(4, i+2, 0.5)
        # yield Note(5, i + 2.75)
        # yield Note(4, i + 3)
        # yield LongNote(3, i + 3.25, .5)


    # time = 0
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p+2, d+i*8)
    # time+=32
    # for i in range(4):
    #     for p, d in melody1:
    #         yield Note(p*2, time+d+i*8, 2)
    melody2 = [
        (3, 0),
        (2, 0.25),
        (1, 0.5),
        (0, 0.75),
        (1, 1),
    ]
    for n, i in enumerate(range(64, 96, 8)):
        yield Note(n+0, i + 0)
        yield Note(n+1, i + 0.5)
        yield Note(n+3, i + 1)
        yield Note(n+2, i + 1.5)
        for p, d in melody2:
            yield Note(n+p, 2 + i + d)
        yield Note(n+0, i + 3.5)
        yield Note(n+0, i + 4.5)
        yield Note(n+3, i + 5)
        yield Note(n+2, i + 5.5)
        for p, d in melody2:
            yield Note(n+p, 6 + i + d)
        yield Note(n+0, i + 7.5)


notes: List[Note] = list(undertale_generator())

track_finger_count = [0]*8
last_track_finger_count = [0]*8
last_time = time.perf_counter()

wave_img = [pygame.surface.Surface((0, 0))]
total_pixels = 0


expected_lines_press = [0]*8
expected_lines_hold = [0]*8


last_time_animation = 0
animations = []

class Animation:
    def __init__(self, t, x, y, s):
        self.t, self.x, self.y, self.s = t, x, y, s


def get_expected_lines():
    global last_track_finger_count, combo, score
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
                animations.append(Animation(expected_lines_press[i], i, 0, expected_lines_press[i]))
                debug_hits.append(expected_lines_press[i])
                tick_mixer.play()
                combo += 1
                score += expected_lines_press[i] * (1+combo/100)
            else:
                combo = 0

    last_track_finger_count = list(track_finger_count)


def generate_wave():
    global note_width, note_space, wave_img, total_pixels, last_time, track_mixer

    track_mixer.stop()
    img_width = note_width
    total_pixels = len(samples)/sample_rate*(BPM/60)*note_space*sub_bars
    wave_img = [pygame.surface.Surface((img_width, 32768)) for _ in range(int(total_pixels)//32768+1)]
    samples_per_pixel = len(samples) / total_pixels
    print("tot:",total_pixels)
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
    if scroll > 0:
        track_mixer = start_from()
        track_mixer.play()


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




def draw_feedback_animation(screen: pygame.Surface):
    global last_time_animation, animations
    current_time = time.perf_counter()
    interval = (current_time - last_time_animation)
    last_time_animation = current_time

    animations = [a for a in animations if a.t > 0]
    for a in animations:
        r = (a.s-a.t)*note_width*2
        s = pygame.Surface((r, r), pygame.SRCALPHA)
        s.set_alpha(a.t*255)
        pygame.draw.ellipse(s, (255, 255, 255), (0, 0, r, r))
        screen.blit(s, (track_x+note_width*a.x-r/2+note_width*.5, screen_height-track_bar-r/2))
        a.t -= interval*2

    for n, h in enumerate(debug_hits[-10:]):
        screen.fill((255, 255, 255), (0, 100+n*10, h*100, 10))



def draw(screen: pygame.Surface):

    # Finger press line lightup

    for i in range(8):
        if track_finger_count[i]:
            pygame.draw.rect(screen, (16, 16, 16), pygame.Rect(track_x+i*note_width, 0, note_width, screen_height))

    # Line borders (vert lines)

    for i in range(1, 8):
        pygame.draw.rect(screen, (48, 48, 48), pygame.Rect(track_x+i*note_width-note_width/100, 0, note_width/50, screen_height))

    # Line Beat and quarter beats (horiz lines)

    for i in np.arange(-(scroll-track_bar_scroll-np.floor(scroll))*note_space*sub_bars, screen_height, note_space*sub_bars):
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
        pygame.draw.line(screen, (128, 128, 128), (50 * i, 0), (50 * i, 50))

    # Notes

    for n in notes:
        if type(n) == LongNote:
            pygame.draw.rect(screen, (128, 0, 64), pygame.Rect(
                track_x + n.x * note_width + note_width*0.05,
                screen_height-track_bar - n.y * note_space - note_height / 2 + note_space * sub_bars * scroll - note_space*n.h,
                n.w * note_width*0.9, note_height+note_space*n.h))
        else:
            pygame.draw.rect(screen, (192, 32, 32), pygame.Rect(
                track_x + n.x * note_width + note_width*0.05,
                screen_height - track_bar - n.y * note_space - note_height / 2 + note_space * sub_bars * scroll,
                n.w * note_width - note_width*0.1, note_height))

    draw_feedback_animation(screen)

    # WAV

    i = -(screen_height-total_pixels+note_space*sub_bars*(scroll+track_scroll_offset))
    if 0 <= int(i)//32768 < len(wave_img):
        screen.blit(wave_img[int(i)//32768], [track_x + track_width, -(i%32768) - track_bar])
    if 32768-i%32768 < screen_height and i < total_pixels:
        screen.blit(wave_img[int(i) // 32768 + 1], [track_x + track_width, -(i % 32768) + 32768 - track_bar])

    # The track bar

    bar_fade = int(note_height)*2
    temp_surface = pygame.Surface((track_width, bar_fade), pygame.SRCALPHA)
    temp_surface.fill([0, 0, 0, 0])
    for i in range(bar_fade):
        t = (bar_fade-abs(i))/bar_fade
        pygame.draw.line(temp_surface, (255, 255, 255, int(t*t*t*255)), (0, i),
                         (track_width, i))
    screen.blit(temp_surface, (track_x, screen_height-track_bar))

    # Combo text

    font = pygame.font.Font(pygame.font.get_default_font(), 32)
    text = font.render('Combo ' + str(combo), True, (255,255,255))
    screen.blit(text, dest=(0, 200))

    text = font.render(f'Score {score*1000:.2f}', True, (255, 255, 255))
    screen.blit(text, dest=(0, 250))

    # Vertical borders of the track

    pygame.draw.rect(screen, (192, 192, 192), pygame.Rect(track_x - note_width / 50, 0, note_width / 25, screen_height))
    pygame.draw.rect(screen, (192, 192, 192), pygame.Rect(track_x+track_width - note_width / 50, 0, note_width / 25, screen_height))


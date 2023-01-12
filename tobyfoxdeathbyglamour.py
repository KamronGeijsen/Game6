from track import Note, LongNote

file = "tracks/Toby Fox - Undertale - Death by Glamour.wav"
BPM = 148/4
track_scroll_offset = 0.09


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

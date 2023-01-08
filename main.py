import pygame

import track

WIDTH, HEIGHT = 400, 300


def run():
    global WIDTH, HEIGHT

    # Initialize the game engine
    pygame.init()


    # Set the height and width of the screen
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE | pygame.FULLSCREEN)
    pygame.display.set_caption("Game6")
    # bitscreen = pygame.surface.Surface((TILE * WIDTH_BLOCKS, TILE * HEIGHT_BLOCKS))

    track.resize(type("mock_event", (), {"x": WIDTH, "y": HEIGHT})())
    track.generate_wave()
    clock = pygame.time.Clock()
    while 1:
        # clock.tick(60)
        #
        # previous_buttons = dict(buttons.copy())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if 49 <= event.key < 57:
                    track.track_finger_count[event.key-49] += 1
            elif event.type == pygame.KEYUP:
                if 49 <= event.key < 57:
                    track.track_finger_count[event.key - 49] -= 1
            elif event.type == pygame.WINDOWRESIZED:
                WIDTH, HEIGHT = event.x, event.y
                track.resize(event)
                track.generate_wave()
            elif event.type == pygame.FINGERDOWN:
                # print("DOWN", event.x)
                if track.track_x < event.x * WIDTH < track.track_x+track.track_width:
                    track_num = int((event.x*WIDTH-track.track_x) / track.note_width)
                    track.track_finger_count[track_num] += 1
                    # print("DOWN", track_num, track.track_finger_count)
            elif event.type == pygame.FINGERUP:
                # print("UP", event.x)
                if track.track_x < event.x * WIDTH < track.track_x+track.track_width:
                    track_num = int((event.x*WIDTH-track.track_x) / track.note_width)
                    track.track_finger_count[track_num] -= 1
                    # print("DOWN", track_num, track.track_finger_count)
            elif event.type == pygame.FINGERMOTION:
                # print("MOVE", event)
                old_x = event.x-event.dx
                if track.track_x < old_x * WIDTH < track.track_x+track.track_width:
                    track_num = int((old_x*WIDTH-track.track_x) / track.note_width)
                    track.track_finger_count[track_num] -= 1
                    # print("DOWN", track_num, track.track_finger_count)
                if track.track_x < event.x * WIDTH < track.track_x+track.track_width:
                    track_num = int((event.x*WIDTH-track.track_x) / track.note_width)
                    track.track_finger_count[track_num] += 1
                    # print("DOWN", track_num, track.track_finger_count)

        track.get_expected_lines()
        track.scroller()

        bitscreen = pygame.surface.Surface((WIDTH, HEIGHT))
        bitscreen.fill((0, 0, 0))

        track.draw(bitscreen)

        screen.blit(bitscreen, [0, 0])
        pygame.display.flip()
run()
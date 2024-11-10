import random
from pgzero.builtins import Actor, Rect
import pgzrun

WIDTH = 800
HEIGHT = 600

grid_size = 10
cell_size = WIDTH // grid_size
menu_active = True
music_on = True

hero_position = [5, 5]
enemy_position = [3, 3]


hero_sprites_idle = ["hero_idle1", "hero_idle2"]
hero_sprites_move = ["hero_walk1", "hero_walk2"]
enemy_sprites_idle = ["enemy_idle1", "enemy_idle2"]
enemy_sprites_move = ["enemy_walk1", "enemy_walk2"]

hero = Actor("images/" + hero_sprites_idle[0], pos=(hero_position[0]*cell_size, hero_position[1]*cell_size))
enemy = Actor("images/" + enemy_sprites_idle[0], pos=(enemy_position[0]*cell_size, enemy_position[1]*cell_size))

hero_frame = 0
enemy_frame = 0

buttons = {
    "start_game": Rect((300, 200), (200, 50)),
    "toggle_music": Rect((300, 300), (200, 50)),
    "exit_game": Rect((300, 400), (200, 50))
}


if music_on:
    music.play("sounds/bg_music")

def draw():
    screen.clear()
    if menu_active:
        draw_menu()
    else:
        draw_game()

def draw_menu():
    screen.draw.text("Ana Menü", center=(WIDTH // 2, 100), fontsize=50, color="white")
    screen.draw.filled_rect(buttons["start_game"], "green")
    screen.draw.text("Oyuna Başla", center=buttons["start_game"].center, color="black")
    screen.draw.filled_rect(buttons["toggle_music"], "blue")
    screen.draw.text("Müziği Aç/Kapat", center=buttons["toggle_music"].center, color="black")
    screen.draw.filled_rect(buttons["exit_game"], "red")
    screen.draw.text("Çıkış", center=buttons["exit_game"].center, color="black")

def draw_game():
    for x in range(grid_size):
        for y in range(grid_size):
            screen.draw.rect(Rect((x * cell_size, y * cell_size), (cell_size, cell_size)), "darkgray")
    hero.draw()
    enemy.draw()

def update():
    global hero_frame, enemy_frame
    if not menu_active:
        hero.image = "images/" + hero_sprites_idle[hero_frame // 10 % len(hero_sprites_idle)]
        enemy.image = "images/" + enemy_sprites_idle[enemy_frame // 10 % len(enemy_sprites_idle)]
        hero_frame += 1
        enemy_frame += 1
        move_enemy()

def move_enemy():
    global enemy_position
    direction = random.choice(["up", "down", "left", "right"])
    if direction == "up" and enemy_position[1] > 0:
        enemy_position[1] -= 1
    elif direction == "down" and enemy_position[1] < grid_size - 1:
        enemy_position[1] += 1
    elif direction == "left" and enemy_position[0] > 0:
        enemy_position[0] -= 1
    elif direction == "right" and enemy_position[0] < grid_size - 1:
        enemy_position[0] += 1
    enemy.pos = (enemy_position[0] * cell_size, enemy_position[1] * cell_size)

def on_key_down(key):
    global hero_position
    if not menu_active:
        if key == keys.UP and hero_position[1] > 0:
            hero_position[1] -= 1
        elif key == keys.DOWN and hero_position[1] < grid_size - 1:
            hero_position[1] += 1
        elif key == keys.LEFT and hero_position[0] > 0:
            hero_position[0] -= 1
        elif key == keys.RIGHT and hero_position[0] < grid_size - 1:
            hero_position[0] += 1
        hero.pos = (hero_position[0] * cell_size, hero_position[1] * cell_size)

def on_mouse_down(pos):
    global menu_active, music_on
    if menu_active:
        if buttons["start_game"].collidepoint(pos):
            menu_active = False
        elif buttons["toggle_music"].collidepoint(pos):
            music_on = not music_on
            if music_on:
                music.play("sounds/bg_music")
            else:
                music.stop()
        elif buttons["exit_game"].collidepoint(pos):
            exit()

pgzrun.go()

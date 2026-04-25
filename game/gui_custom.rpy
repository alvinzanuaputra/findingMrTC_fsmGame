## Custom GUI overrides for visual polish.
## This file is intended to override defaults in screens.rpy.
init offset = 10

## FIX: Ren'Py 8.5 tidak punya config.menu_select_sound.
## Kita pakai hover_sound di style tombol (lihat di bawah).


################################################################################
## SAY SCREEN (CUSTOM TEXTBOX + NAMEBOX)
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1280
        ysize 220

        if who:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


style window:
    xalign 0.5
    yalign 1.0
    xsize 1280
    ysize 220
    # FIX: Kotak dialog semi-transparan.
    background Frame(Solid("#0D1B2ACC"), 0, 0)


style namebox:
    xpos 75
    xanchor 0.0
    ypos -45
    ypadding 10
    xpadding 20
    background Frame(Solid("#00B0FF33"), 10, 10)


style say_dialogue:
    xpos 75
    xsize 1130
    ypos 25
    color "#E8EAF6"
    line_spacing 8
    # FIX: Font dialog jangan kebesaran, pastikan muat di textbox.
    size 24


################################################################################
## CHOICE MENU POLISH
################################################################################

style choice_button:
    xalign 0.5
    xsize 900
    ypadding 18
    xpadding 30
    background Frame(Solid("#1A237E99"), 15, 15)
    hover_background Frame(Solid("#283593CC"), 15, 15)
    selected_background Frame(Solid("#00B0FF44"), 15, 15)
    hover_sound "audio/sfx/select.mp3"


style choice_button_text:
    color "#E8EAF6"
    hover_color "#FFFFFF"
    size 26
    xalign 0.5
    text_align 0.5


################################################################################
## MAIN MENU (CUSTOM)
################################################################################

screen main_menu():
    tag menu

    # FIX: Background main menu fill layar.
    add im.Scale("images/places/lab_giga.jpg", 1280, 720)
    add Solid("#00000088")

    vbox:
        xalign 0.5
        yalign 0.4
        spacing 15

        text "FINDING MR. TC":
            xalign 0.5
            size 72
            color "#00B0FF"
            outlines [(3, "#0D1B2A", 0, 0)]
            font "DejaVuSans.ttf"

        text "Visual Novel · Puzzle Adventure":
            xalign 0.5
            size 24
            color "#90CAF9"

        null height 30

        textbutton "▶  Mulai Game" action Start():
            xalign 0.5
            style "main_menu_button"

        textbutton "⚙  Pengaturan" action ShowMenu("preferences"):
            xalign 0.5
            style "main_menu_button"

        textbutton "✖  Keluar" action Quit():
            xalign 0.5
            style "main_menu_button"


style main_menu_button:
    xsize 320
    ypadding 16
    xpadding 30
    xalign 0.5
    background Frame(Solid("#0D1B2ACC"), 12, 12)
    hover_background Frame(Solid("#00B0FF55"), 12, 12)
    hover_sound "audio/sfx/select.mp3"


style main_menu_button_text:
    xalign 0.5
    size 28
    color "#E8EAF6"
    hover_color "#FFFFFF"


################################################################################
## ENDING SCREEN (REUSABLE)
################################################################################

screen ending_screen(judul, warna, deskripsi):
    add Solid("#00000099")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 25

        text judul:
            xalign 0.5
            size 56
            color warna
            outlines [(2, "#000000", 0, 0)]

        null height 10

        text deskripsi:
            xalign 0.5
            size 24
            color "#CFD8DC"
            text_align 0.5
            xsize 800

        null height 30

        hbox:
            xalign 0.5
            spacing 30
            textbutton "🔄 Main Lagi" action Start() style "choice_button"
            textbutton "🚪 Keluar" action Quit() style "choice_button"

style toggle_btn:
    size 13
    color "#90CAF9"
    bold True
    hover_color "#FFFFFF"


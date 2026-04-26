screen hud():
    frame:
        xalign 0.98
        yalign 0.02
        padding (12, 8)
        background Frame("gui/frame.png", 5, 5)

        hbox:
            spacing 6
            text "Baterai" size 20 color "#ffffff"
            for i in range(5):
                if i < baterai:
                    text "■" color "#4fc3f7" size 18
                else:
                    text "□" color "#555555" size 18

screen misi():
    frame:
        xalign 0.01
        yalign 0.02
        padding (12, 10)
        background Frame("gui/frame.png", 5, 5)
        vbox:
            spacing 4
            text "MISI AKTIF" size 16 bold True color "#ffcc02"
            for lab in ["Alpro", "RPL", "NETICS", "KBJ", "KCV", "PKT", "MCI", "GIGA"]:
                if lab in labs_done:
                    text "Selesai: [lab]" size 14 color "#a5d6a7"
                else:
                    text "Belum: [lab]" size 14 color "#aaaaaa"
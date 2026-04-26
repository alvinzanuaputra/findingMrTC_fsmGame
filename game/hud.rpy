screen game_hud():
    zorder 100

    if hud_misi_visible:
        frame:
            xalign 0.0
            yalign 0.0
            xoffset 18
            yoffset 18
            xpadding 12
            ypadding 10
            xminimum 170
            background Frame(Solid("#0D1B2AE0"), 10, 10)
            vbox:
                spacing 3
                text "📋 MISI":
                    size 13
                    color "#90CAF9"
                    bold True
                null height 3
                hbox:
                    spacing 6
                    text ("✅" if lab1_done else "○") size 13 color ("#00E676" if lab1_done else "#546E7A")
                    text "AlPRO" size 12 color ("#E0E0E0" if lab1_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab2_done else "○") size 13 color ("#00E676" if lab2_done else "#546E7A")
                    text "RPL" size 12 color ("#E0E0E0" if lab2_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab3_done else "○") size 13 color ("#00E676" if lab3_done else "#546E7A")
                    text "NETICS (TKJ)" size 12 color ("#E0E0E0" if lab3_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab4_done else "○") size 13 color ("#00E676" if lab4_done else "#546E7A")
                    text "KBJ" size 12 color ("#E0E0E0" if lab4_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab5_done else "○") size 13 color ("#00E676" if lab5_done else "#546E7A")
                    text "KCV" size 12 color ("#E0E0E0" if lab5_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab6_done else "○") size 13 color ("#00E676" if lab6_done else "#546E7A")
                    text "PKT" size 12 color ("#E0E0E0" if lab6_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab7_done else "○") size 13 color ("#00E676" if lab7_done else "#546E7A")
                    text "MCI" size 12 color ("#E0E0E0" if lab7_done else "#78909C")
                hbox:
                    spacing 6
                    text ("✅" if lab8_done else "○") size 13 color ("#FFD700" if lab8_done else "#546E7A")
                    text "GIGA ⭐" size 12 color ("#FFD700" if lab8_done else "#78909C")
                null height 3
                $ done_count = int(lab1_done)+int(lab2_done)+int(lab3_done)+int(lab4_done)+int(lab5_done)+int(lab6_done)+int(lab7_done)+int(lab8_done)
                text "[done_count]/8 Selesai":
                    size 11 color "#546E7A" italic True

    textbutton "['>' if hud_misi_visible else '<']":
        xalign 0.0
        yalign 0.0
        xoffset 188
        yoffset 20
        xpadding 6
        ypadding 3
        background Solid("#00000066")
        text_style "toggle_btn"
        action [ToggleVariable("hud_misi_visible")]

    if hud_nyawa_visible:
        frame:
            xalign 1.0
            yalign 0.0
            xoffset -32
            yoffset 18
            xpadding 12
            ypadding 10
            xminimum 160
            background Frame(Solid("#0D1B2AE0"), 10, 10)
            vbox:
                spacing 4
                xalign 1.0
                text "NYAWA":
                    size 13
                    color "#90CAF9"
                    bold True
                    xalign 1.0
                hbox:
                    spacing 3
                    xalign 1.0
                    for i in range(5):
                        if i < nyawa:
                            if nyawa >= 4:
                                text "♥" color "#FF4081" size 20
                            elif nyawa == 3:
                                text "♥" color "#FF8A65" size 20
                            elif nyawa == 2:
                                text "♥" color "#FFEB3B" size 20
                            else:
                                text "♥" color "#FF1744" size 20
                        else:
                            text "♡" color "#37474F" size 20
                if nyawa == 5:
                    text "SEMPURNA ✨":
                        size 11 color "#00E676" xalign 1.0 italic True
                elif nyawa >= 3:
                    text "AMAN":
                        size 11 color "#69F0AE" xalign 1.0 italic True
                elif nyawa == 2:
                    text "⚠ HATI-HATI":
                        size 11 color "#FFEB3B" xalign 1.0 italic True
                else:
                    text "🚨 KRITIS":
                        size 11 color "#FF1744" xalign 1.0 italic True

    textbutton "['>' if hud_nyawa_visible else '<']":
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 20
        xpadding 6
        ypadding 3
        background Solid("#00000066")
        text_style "toggle_btn"
        action [ToggleVariable("hud_nyawa_visible")]
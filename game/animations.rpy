transform pos_left:
    xanchor 0.5 xpos 0.2
    yalign 1.0
    zoom 0.75

# Posisi KANAN - aman tidak keluar layar
transform pos_right:
    xanchor 0.5 xpos 0.8
    yalign 1.0
    zoom 0.75

# Entrance dari kiri
transform enter_left:
    xanchor 0.5 xpos -0.2 yalign 1.0 zoom 0.75 alpha 0.0
    ease 0.25 xpos 0.2 alpha 1.0

# Entrance dari kanan
transform enter_right:
    xanchor 0.5 xpos 1.2 yalign 1.0 zoom 0.75 alpha 0.0
    ease 0.25 xpos 0.8 alpha 1.0

# Exit ke kiri
transform exit_left:
    ease 0.25 xpos -0.2 alpha 0.0

# Exit ke kanan
transform exit_right:
    ease 0.25 xpos 1.2 alpha 0.0

# Active speaker
transform active_speak:
    ease 0.2 zoom 0.85 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

# Idle (diam, mengecil dan kusam)
transform idle_dim:
    ease 0.2 zoom 0.75 alpha 0.7 matrixcolor BrightnessMatrix(-0.35)

# Idle kembali aktif
transform idle_bright:
    ease 0.2 zoom 0.85 alpha 1.0 matrixcolor BrightnessMatrix(0.0)

# Shake saat salah
transform char_shake:
    xoffset 0
    linear 0.04 xoffset -10
    linear 0.04 xoffset 10
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset 0

# Bounce saat benar
transform char_bounce:
    yoffset 0
    ease 0.1 yoffset -15
    ease 0.1 yoffset 0
    ease 0.08 yoffset -8
    ease 0.08 yoffset 0

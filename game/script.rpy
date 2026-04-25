## === IMAGES YANG DIPAKAI DI PROLOG ===
# FIX: Background selalu fill layar (1280x720).
image bg siakad_loading = im.Scale("images/places/siakad_loading.jpg", 1280, 720)
image bg chatwa_bapaktc = im.Scale("images/places/chatwa_bapaktc.jpg", 1280, 720)
image bg map = im.Scale("images/places/map.jpg", 1280, 720)

# Flicker/loading effect (prolog)
image bg_siakad_flicker:
    im.Scale("images/places/siakad_loading.jpg", 1280, 720)
    alpha 1.0
    pause 2.0
    linear 0.1 alpha 0.85
    linear 0.1 alpha 1.0
    pause 1.5
    linear 0.15 alpha 0.7
    linear 0.15 alpha 1.0
    repeat

image maba normal = "images/character/char_maba_normal.png"
image char_maba_normal = "images/character/char_maba_normal.png"

## === IMAGES UNTUK LAB 1 (ALPRO) ===
image bg lab_alpo = im.Scale("images/places/lab_alpro.jpg", 1280, 720)
image bg flowchart_blok_kode = im.Scale("images/places/flowchart_blok_kode.jpg", 1280, 720)
image bg lab_rpl = im.Scale("images/places/lab_rpl.jpg", 1280, 720)
image bg terracota_tekateki = im.Scale("images/places/terracota_tekateki.jpg", 1280, 720)
image bg lab_tkj = im.Scale("images/places/lab_tkj.jpg", 1280, 720)
image bg mengetik_sciten = im.Scale("images/places/mengetik_sciten.jpg", 1280, 720)
image bg lab_kbj = im.Scale("images/places/lab_kbj.jpg", 1280, 720)
image bg kabel_power_router = im.Scale("images/places/kabel_power_router.jpg", 1280, 720)
image bg lab_kcv = im.Scale("images/places/lab_kcv.jpg", 1280, 720)
image bg mahasiswa_gondrong_dataset = im.Scale("images/places/mahasiswa_gondrong_dataset.jpg", 1280, 720)
image bg lab_pkt = im.Scale("images/places/lab_pkt.jpg", 1280, 720)
image bg angka_32 = im.Scale("images/places/angka_32.jpg", 1280, 720)
image bg lab_mci = im.Scale("images/places/lab_mci.jpg", 1280, 720)
image bg nodeWa_dan_cctv = im.Scale("images/places/nodeWa_dan_cctv.png", 1280, 720)
image bg lab_giga = im.Scale("images/places/lab_giga.jpg", 1280, 720)
image bg pilih_a_atau_b = im.Scale("images/places/pilih_a_atau_b.jpg", 1280, 720)
image bg plaza_supeno = im.Scale("images/places/plaza_supeno.jpg", 1280, 720)
image bg fsm_diagram = im.Scale("images/places/fsm_diagram.jpg", 1280, 720)

image kalab ap = "images/character/char_kalab_ap.png"
image kalab santai = "images/character/char_kalab_santai.png"
image kalab netics = "images/character/char_kalab_netics.png"
image kalab kbj = "images/character/char_kalab_kbj_male.png"
image kalab kcv = "images/character/char_kalab_kcv.png"
image kalab pkt = "images/character/char_kalab_pkt.png"
image kalab mci = "images/character/char_kalab_mci.png"
image kalab giga = "images/character/char_kalab_giga.png"
image char_kalab_ap = "images/character/char_kalab_ap.png"
image char_kalab_santai = "images/character/char_kalab_santai.png"
image char_kalab_netics = "images/character/char_kalab_netics.png"
image char_kalab_kbj_male = "images/character/char_kalab_kbj_male.png"
image char_kalab_kcv = "images/character/char_kalab_kcv.png"
image char_kalab_pkt = "images/character/char_kalab_pkt.png"
image char_kalab_mci = "images/character/char_kalab_mci.png"
image char_kalab_giga = "images/character/char_kalab_giga.png"

image maba takut = "images/character/char_maba_takut.png"
image maba marah = "images/character/char_maba_marah.png"
image maba senang = "images/character/char_maba_senang.png"
image tc senyum = "images/character/char_tersenyum.png"
image char_maba_takut = "images/character/char_maba_takut.png"
image char_maba_marah = "images/character/char_maba_marah.png"
image char_maba_senang = "images/character/char_maba_senang.png"
image char_tersenyum = "images/character/char_tersenyum.png"

image kating normal = "images/character/char_kating_normal.png"
image kating puas = "images/character/char_kating_puas.png"
image kating marah = "images/character/char_kating_marah.png"
image char_kating_normal = "images/character/char_kating_normal.png"
image char_kating_puas = "images/character/char_kating_puas.png"
image char_kating_marah = "images/character/char_kating_marah.png"

## === DEFINISI KARAKTER ===
define masta = Character("Masta", color="#4FC3F7")
define tc = Character("Bapak TC", color="#EF5350")

define aslab_alpro = Character("Aslab Alpro", color="#81C784")
define aslab_rpl = Character("Aslab RPL", color="#64B5F6")
define aslab_tkj = Character("Aslab TKJ", color="#FFD54F")
define aslab_netics = Character("Aslab NETICS", color="#81C784")  # FIX: dipakai di lab3_netics
define aslab_kbj = Character("Aslab KBJ", color="#BA68C8")
define aslab_kcv = Character("Aslab KCV", color="#4DB6AC")
define aslab_pkt = Character("Aslab PKT", color="#FF8A65")
define aslab_mci = Character("Aslab MCI", color="#A1887F")
define aslab_giga = Character("Aslab GIGA", color="#90A4AE")
define kating = Character("Kating", color="#F48FB1")

## === SETUP TRANSISI GLOBAL ===
# FIX: Ren'Py 8.5 tidak punya config.default_transition.
# FIX: Pakai transisi global yang valid untuk menu/perpindahan layar.
define config.enter_transition = Dissolve(0.4)
define config.exit_transition = Dissolve(0.4)
define config.intra_transition = Dissolve(0.4)

define trans_fade_slow = Fade(0.5, 0, 0.5)
define trans_dissolve_fast = Dissolve(0.2)
define trans_dissolve_slow = Dissolve(0.8)
define trans_wipe_right = CropMove(0.4, "wiperight")
define trans_flash = Fade(0.1, 0.0, 0.3, color="#ffffff")

## === TRANSFORM KARAKTER ===
transform pos_left:
    xalign 0.05
    yalign 1.05
    zoom 0.78

transform pos_right:
    xalign 0.72
    yalign 1.05
    zoom 0.78

transform enter_left:
    xalign -0.3 yalign 1.05 zoom 0.78 alpha 0.0
    ease 0.35 xalign 0.05 alpha 1.0

transform enter_right:
    xalign 1.3 yalign 1.05 zoom 0.78 alpha 0.0
    ease 0.35 xalign 0.72 alpha 1.0

transform exit_left:
    ease 0.25 xalign -0.3 alpha 0.0

transform exit_right:
    ease 0.25 xalign 1.3 alpha 0.0

transform active_speak:
    zoom 0.78
    ease 0.1 zoom 0.81
    ease 0.1 zoom 0.78

transform idle_dim:
    ease 0.2 alpha 0.55 zoom 0.76

transform idle_bright:
    ease 0.2 alpha 1.0 zoom 0.78

transform char_shake:
    xoffset 0
    linear 0.04 xoffset -10
    linear 0.04 xoffset 10
    linear 0.04 xoffset -8
    linear 0.04 xoffset 8
    linear 0.04 xoffset 0

transform char_bounce:
    yoffset 0
    ease 0.1 yoffset -15
    ease 0.1 yoffset 0
    ease 0.08 yoffset -8
    ease 0.08 yoffset 0

transform fadein_char:
    alpha 0.0
    ease 0.5 alpha 1.0

## Backward-compatible aliases.
transform enter_from_left:
    contains:
        enter_left

transform enter_from_right:
    contains:
        enter_right

transform speaking:
    contains:
        active_speak

transform idle_char:
    contains:
        idle_dim

transform bounce:
    contains:
        char_bounce

transform shake:
    contains:
        char_shake

## === VARIABEL GLOBAL ===
default nyawa = 5
default lab1_done = False
default lab2_done = False
default lab3_done = False
default lab4_done = False
default lab5_done = False
default lab6_done = False
default lab7_done = False
default lab8_done = False
default hud_misi_visible = True
default hud_nyawa_visible = True
default lab_selesai = 0

## === PROLOG SAJA ===
label start:
    show screen game_hud
    scene
    show bg_siakad_flicker
    play music "audio/bgm/bgm_santai.ogg" loop

    "Pukul 14.00 WIB. Portal FRS ditutup satu jam lagi..."

    show char_maba_normal at fadein_char
    masta "Sial... Kalau begini caranya gua bisa lulus telat. Satu-satunya kelas yang sisa cuma PBO-nya Bapak TC."

    scene bg chatwa_bapaktc
    play sound "audio/sfx/sfx_phone_ring.ogg"

    "Bapak TC: Kamu masukin kelas saya karena niat belajar, atau cuma karena SKS sisa?\nSaya tidak butuh mahasiswa mental tempe.\nBuktikan logika kamu jalan.\nSaya sudah menitipkan 'sesuatu' di Lab Alpro.\nMulai dari sana, selesaikan masalah aslab di 7 lab, lalu temui saya di Lab GIGA."

    scene bg map with trans_fade_slow
    "Masta menatap peta kampus. 8 lab menunggu."

    jump lab1_alpro

## === PLACEHOLDER LABEL SEMUA LAB ===
label lab1_alpro:
    scene bg lab_alpo with trans_wipe_right
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_left
    show char_kalab_ap at right with trans_dissolve_fast
    show char_kalab_ap at enter_right

    show char_maba_normal at active_speak
    show char_kalab_ap at idle_dim
    masta "Bang! Kata Bapak TC beliau nitip sesuatu buat gua di sini?"
    show char_kalab_ap at idle_bright
    show char_maba_normal at idle_dim
    aslab_alpro "Oh, lu korban FRS yang lagi diuji Bapak TC? Iya, beliau nitip file di sini. Tapi gua nggak boleh ngasih kalau logika dasar lu masih jongkok. Gua lagi stuck bikin alur robot sapu, nabrak tembok terus nggak mau belok. Mana bagian yang logikanya error?"

    jump lab1_puzzle

label lab1_puzzle:
    scene bg flowchart_blok_kode with trans_dissolve_slow

    menu:
        # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
        "Blok [[Tetap Jalan Maju]] — ini yang salah!":
            jump lab1_benar
        # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
        "Blok [[Nabrak Tembok?]] — ini yang error":
            jump lab1_salah
        # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
        "Blok [[Jalan Maju]] — harusnya dihapus":
            jump lab1_salah

label lab1_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at char_bounce
    show char_kalab_santai at right with trans_dissolve_fast
    aslab_alpro "Bener! Harusnya 'Belok', bukan lanjut maju. Logika lu masih lurus, Ta. Nih titipan dari Bapak TC. File formatnya .fig, bawa ke anak Lab RPL."
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: File Soal Bapak TC (.fig) didapat!]]"
    jump lab2_rpl

label lab1_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_ap at char_shake
    aslab_alpro "Masta, kalau disuruh maju terus ya jebol itu robot! Fokus dong, katanya mau ACC FRS!"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab1_puzzle

label lab2_rpl:
    scene bg lab_rpl with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kating_normal at right with trans_dissolve_fast
    show char_kating_normal at enter_from_right

    show char_maba_normal at speaking
    show char_kating_normal at idle_char
    masta "Bang, tolong bukain file desain ini dong. Ini syarat ujian dari Bapak TC buat ACC FRS gua."
    show char_kating_normal at speaking
    show char_maba_normal at idle_char
    kating "Bapak TC ngasih soal pake format Figma? Absurd. Bisa gua bukain, tapi barter dulu. Tombol 'Delete' ini harus kelihatan bahaya tapi tetap Earth Tone. Menurut lu yang mana?"

    scene bg terracota_tekateki with trans_dissolve_slow
    jump lab2_puzzle

label lab2_puzzle:
    menu:
        "Terracotta (coklat kemerahan hangat)":
            jump lab2_benar
        "Kuning Stabilo (neon terang)":
            jump lab2_salah
        "Merah Neon (bright red)":
            jump lab2_salah

label lab2_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at bounce
    show char_kating_puas at right with trans_dissolve_fast
    kating "Nah, ini baru estetika! Ada password-nya nih... bawa ke anak Lab Siber buat di-crack."
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Flashdisk ZIP didapat!]]"
    jump lab3_netics

label lab2_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kating_marah at right
    show char_kating_marah at shake
    kating "Masta, lu ngerusak harmoni desain gua! Warna neon di tema bumi itu dosa besar!"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab2_puzzle

label lab3_netics:
    scene bg lab_tkj with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kalab_netics at right with trans_dissolve_fast
    show char_kalab_netics at enter_from_right

    show char_maba_normal at speaking
    show char_kalab_netics at idle_char
    masta "Bang, tolongin gua nembus password file ZIP ini."
    show char_kalab_netics at speaking
    show char_maba_normal at idle_char
    aslab_netics "Kelemahan sistem selalu ada di penggunanya. Tuh liat sticky note di bawah monitor. Tebak sendiri, Masta."

    scene bg mengetik_sciten with trans_dissolve_slow
    "Sticky note bertuliskan: PASSWORD = NAMA LAB INI (DIBALIK). Masta melihat papan nama: NETICS"
    jump lab3_puzzle

label lab3_puzzle:
    menu:
        "Ketik: SCITEN":
            jump lab3_benar
        "Ketik: NETICS":
            jump lab3_salah
        "Ketik: CITEN":
            jump lab3_salah

label lab3_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at bounce
    aslab_netics "Tembus! Tapi isinya shortcut ke server lokal. Internet lab mati total. Lari ke Lab KBJ, suruh benerin jaringan!"
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Akses File Server (belum terhubung)]]"
    jump lab4_kbj

label lab3_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_netics at shake
    aslab_netics "Gagal. Nama lab ini NETICS, tinggal dibalik doang!"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab3_puzzle

label lab4_kbj:
    scene bg lab_kbj with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kalab_kbj_male at right with trans_dissolve_fast
    show char_kalab_kbj_male at enter_from_right

    show char_maba_normal at speaking
    show char_kalab_kbj_male at idle_char
    masta "Bang! Internet nyalain dong, gua harus narik file ujian Bapak TC dari server lokal, buruan!"
    show char_kalab_kbj_male at speaking
    show char_maba_normal at idle_char
    aslab_kbj "Router-nya merah semua. Bantuin benerin dulu. Apa langkah pertama paling ampuh buat benerin alat yang nge-hang?"

    scene bg kabel_power_router with trans_dissolve_slow
    jump lab4_puzzle

label lab4_puzzle:
    menu:
        "Cabut dan colok ulang kabel power (hard reset)":
            jump lab4_benar
        "Tarik antena routernya":
            jump lab4_salah
        "Reset via tombol admin web browser":
            jump lab4_salah

label lab4_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at bounce
    aslab_kbj "Internet nyala! File berhasil ditarik tapi fotonya buram banget. Bawa ke anak KCV, suruh AI mereka yang baca."
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Foto Scan Soal Buram didapat!]]"
    jump lab5_kcv

label lab4_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_kbj_male at shake
    aslab_kbj "Ngapain narik antena? Emang ini TV cembung? Fokus ke sumber listriknya!"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab4_puzzle

label lab5_kcv:
    scene bg lab_kcv with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kalab_kcv at right with trans_dissolve_fast
    show char_kalab_kcv at enter_from_right

    show char_maba_normal at speaking
    show char_kalab_kcv at idle_char
    masta "Bang, tolong scan foto buram ini pake AI OCR lu. Waktu gua mepet!"
    show char_kalab_kcv at speaking
    show char_maba_normal at idle_char
    aslab_kcv "AI gua lagi rewel. Cuma kenal maba rambut rapi, pas liat mahasiswa gondrong malah dibilang sapu ijuk. Mana data yang harus ditambah ke dataset?"

    scene bg mahasiswa_gondrong_dataset with trans_dissolve_slow
    jump lab5_puzzle

label lab5_puzzle:
    menu:
        "Tambahkan foto mahasiswa berambut gondrong ke dataset":
            jump lab5_benar
        "Tambahkan lebih banyak foto mahasiswa rambut rapi":
            jump lab5_salah
        "Hapus semua data dan mulai ulang":
            jump lab5_salah

label lab5_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at bounce
    aslab_kcv "Mantap! AI-nya sekarang kenal variasi manusia. Foto scan sudah dijernihin... tapi ini rumus deret matematika! Bawa ke Lab Pemodelan."
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Rumus Deret Matematika didapat!]]"
    jump lab6_pkt

label lab5_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_kcv at shake
    aslab_kcv "Lu kasih data seragam lagi, AI-nya makin rabun, Ta!"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab5_puzzle

label lab6_pkt:
    scene bg lab_pkt with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kalab_pkt at right with trans_dissolve_fast
    show char_kalab_pkt at enter_from_right

    show char_maba_normal at speaking
    show char_kalab_pkt at idle_char
    masta "Bang, gua dapet rumus dari rentetan file Bapak TC. Katanya lu bisa bantuin?"
    show char_kalab_pkt at speaking
    show char_maba_normal at idle_char
    aslab_pkt "Deret Bapak TC? Khas beliau. Ini buat nyari batas iterasi program. Lanjutin polanya dulu: 2, 4, 8, 16... angka berikutnya berapa?"

    scene bg angka_32 with trans_dissolve_slow
    jump lab6_puzzle

label lab6_puzzle:
    menu:
        "32":
            jump lab6_benar
        "24":
            jump lab6_salah
        "18":
            jump lab6_salah

label lab6_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    show char_maba_senang at left
    show char_maba_senang at bounce
    aslab_pkt "Pas! Ini snippet kode solusinya, O(1). Tapi beliau daritadi muter-muter gedung. Lari ke anak MI, suruh lacak pake CCTV."
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Snippet Kode Solusi O(1) didapat!]]"
    jump lab7_mci

label lab6_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_pkt at shake
    aslab_pkt "16 dikali dua, Masta! Matematika lu ngulang di semester satu ya?"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab6_puzzle

label lab7_mci:
    scene bg lab_mci with trans_dissolve_fast
    show char_maba_normal at left with trans_dissolve_fast
    show char_maba_normal at enter_from_left
    show char_kalab_mci at right with trans_dissolve_fast
    show char_kalab_mci at enter_from_right

    show char_maba_normal at speaking
    show char_kalab_mci at idle_char
    masta "Bang! Lacakin posisi Bapak TC sekarang pake sistem lu. Gua udah dapet solusinya, tinggal nyetor orangnya!"
    show char_kalab_mci at speaking
    show char_maba_normal at idle_char
    aslab_mci "Bisa, tapi alur kerjanya masih kebolak-balik. Mana kotak yang harus ditaruh paling awal sebagai pemicu?"

    scene bg nodeWa_dan_cctv with trans_dissolve_slow
    jump lab7_puzzle

label lab7_puzzle:
    menu:
        "CCTV Rekam Wajah dulu, baru Kirim Notif WA":
            jump lab7_benar
        "Kirim Notif WA dulu, baru CCTV Rekam":
            jump lab7_salah

label lab7_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    play sound "audio/sfx/sfx_phone_ring.ogg"
    show char_maba_senang at left
    show char_maba_senang at bounce
    aslab_mci "Flow jalan! Notif masuk: 'Bapak TC terpantau masuk ke Lab GIGA'. Buruan samperin sebelum portal FRS tutup, Ta!"
    # FIX: Escape [] agar tidak dianggap interpolasi Ren'Py.
    "[[Reward: Lokasi Bapak TC — Lab GIGA!]]"
    jump lab8_giga

label lab7_salah:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    $ nyawa -= 1
    show char_kalab_mci at shake
    aslab_mci "Logika lu kebalik! Masa WA ngirim notifikasi padahal CCTV-nya belum nangkep apa-apa?"

    if nyawa <= 0:
        jump ending_tle
    else:
        jump lab7_puzzle

label lab8_giga:
    stop music fadeout 1.0
    play music "audio/bgm/bgm_ending.ogg" loop

    scene bg lab_giga with trans_dissolve_fast
    show char_maba_takut at left with trans_dissolve_fast
    show char_maba_takut at enter_from_left
    show char_kalab_giga at right with trans_dissolve_fast
    show char_kalab_giga at enter_from_right

    show char_maba_takut at speaking
    show char_kalab_giga at idle_char
    masta "Pak... Bapak TC... Ini snippet kode solusi yang Bapak minta. Saya sudah menyelesaikan ujian dari 7 lab."
    pause 1.2
    show char_kalab_giga at speaking
    show char_maba_takut at idle_char
    tc "Tepat waktu, Masta. Kamu berhasil memecahkan rantai ujian itu. Tapi di kelas saya, solusi yang asal jalan tapi lambat itu sampah. Sama saja dengan TLE. Pertanyaan terakhir."

    scene bg pilih_a_atau_b with trans_dissolve_slow
    tc "Ada 10.000 data mahasiswa acak. Kamu butuh mencari satu nama spesifik. Mana pendekatan yang pantas masuk kelas saya?"
    jump lab8_puzzle

label lab8_puzzle:
    menu:
        "A — Urutkan dulu (Sorting), lalu cari dengan Binary Search":
            jump lab8_benar
        "B — Cek satu per satu dari atas ke bawah (Linear Search)":
            jump lab8_salah_instant

label lab8_benar:
    play sound "audio/sfx/sfx_correct.ogg"
    with trans_flash
    $ lab_selesai = 8

    if nyawa == 5:
        jump ending_chosen_one
    else:
        jump ending_a_or_d

label lab8_salah_instant:
    play sound "audio/sfx/sfx_wrong.ogg"
    with Shake(0.3, 3)
    show char_kalab_giga at shake
    tc "Pola pikir kuli. Kamu tidak cocok jadi Engineer. Keluar dari lab saya."
    jump ending_tle

label ending_a_or_d:
    # FIX: Pastikan musik berhenti sebelum ending.
    $ renpy.music.stop()
    scene bg lab_giga with trans_fade_slow
    show char_tersenyum at right with trans_dissolve_fast
    show char_maba_senang at left with trans_dissolve_fast

    play sound "audio/sfx/mouse_clicks.wav"
    "Bapak TC mengambil ponselnya, lalu mengklik tombol ACC di web Siakad Doswal."
    tc "Logika kamu masih banyak bocornya, tapi nyali kamu lumayan. Saya ACC. Tapi ingat... di kelas saya cuma ada nilai A atau D. Jangan sampai kamu menyesal masuk kelas saya."

    show char_maba_takut at left with trans_dissolve_fast
    "Masta merinding. Perang sesungguhnya di kelas PBO baru saja dimulai."
    "🎲 ENDING: The A or D Roulette"

    menu:
        "Main Lagi":
            jump start
        "Keluar":
            return

label ending_chosen_one:
    # FIX: Pastikan musik berhenti sebelum ending.
    $ renpy.music.stop()
    scene bg lab_giga with trans_fade_slow
    show char_tersenyum at right with trans_dissolve_fast
    show char_maba_senang at left with trans_dissolve_fast

    "Bapak TC tersenyum tipis. Sebuah pemandangan langka."
    tc "Sempurna. Kamu melewati semua lab tanpa satu pun cacat logika. Sepertinya kelas PBO saya punya satu bintang semester ini."

    play sound "audio/sfx/sfx_correct.ogg"
    play sound "audio/sfx/email.wav"
    "Bapak TC bahkan menawarinya posisi asisten dosen semester depan."
    "Masta keluar lab sebagai legenda kampus."
    "⭐ TRUE ENDING: The Chosen One — Perfect Run!"

    scene bg fsm_diagram with trans_fade_slow
    menu:
        "Main Lagi":
            jump start
        "Keluar":
            return

label ending_tle:
    # FIX: Pastikan musik berhenti sebelum ending.
    $ renpy.music.stop()
    scene bg plaza_supeno with trans_fade_slow
    show char_maba_marah at fadein_char

    "Pukul 15.01. Portal FRS tertutup."
    "Masta tertunduk di depan Lab GIGA. Bapak TC menolak memberikan ACC. Semester ini Masta terpaksa mengambil mata kuliah sisa yang tidak ia sukai. Rencana lulus tepat waktu pun hancur."
    "{size=48}💀 ENDING: TLE — Time Limit Exceeded{/size}"

    menu:
        "Coba Lagi":
            jump start
        "Keluar":
            return

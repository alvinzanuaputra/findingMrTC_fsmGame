# PROMPT BERTAHAP — Finding MrTC (RenPy Game)
> Digunakan di: Codex / GPT-4.5 Very High di VSCode  
> Cara pakai: Kirim satu tahap, tunggu selesai, debug, lanjut ke tahap berikutnya.

---

## KONTEKS AWAL (Tempel di AWAL setiap sesi baru sebagai referensi)

```
Kamu adalah developer RenPy. Kamu akan membuat visual novel berjudul "Finding MrTC".
Struktur folder project sudah ada di:
  images/character/   → sprite karakter
  images/places/      → background tiap lab
  audio/bgm/          → musik latar
  audio/sfx/          → efek suara

Nama file aset yang tersedia:
KARAKTER:
  char_maba_normal.png, char_maba_senang.png, char_maba_marah.png, char_maba_takut.png
  char_kating_normal.png, char_kating_marah.png, char_kating_puas.png
  char_kalab_ap.png, char_kalab_rpl.png, char_kalab_netics.png, char_kalab_kbj_male.png,
  char_kalab_kbj_female.png, char_kalab_kcv.png, char_kalab_pkt.png, char_kalab_mci.png,
  char_kalab_giga.png, char_kalab_santai.png, char_tersenyum.png

BACKGROUND:
  lab_alpo.jpg, lab_rpl.jpg, lab_kbj.jpg, lab_kcv.jpg, lab_pkt.jpg,
  lab_mci.jpg, lab_giga.jpg, lab_tkj.jpg, plaza_supeno.jpg, map.jpg

BGM:
  bgm_santai.ogg, bgm_ending.ogg

SFX:
  sfx_click.ogg, sfx_correct.ogg, sfx_wrong.ogg, sfx_phone_ring.ogg,
  email.wav, gulp.wav, mouse_clicks.wav, park.mp3, sound.wav

Aturan penamaan path aset di RenPy:
  "images/character/char_maba_normal.png"  → define maba_normal = Character(...)
  "images/places/lab_alpo.jpg"             → scene lab_alpo with dissolve
```

---

## TAHAP 1 — Struktur Dasar & Prolog

**Tujuan:** Buat file `script.rpy` dengan struktur label lengkap dan prolog yang bisa dijalankan.

**Instruksi:**

```
Buat file `game/script.rpy` untuk game RenPy berjudul "Finding MrTC".

KETENTUAN:
1. Definisikan semua karakter berikut dengan nama variabel yang jelas:
   - masta = Character("Masta", color="#4fc3f7")
   - bapak_tc = Character("Bapak TC", color="#ef5350")
   - aslab_alpro = Character("Aslab Alpro", color="#a5d6a7")
   - kating_rpl = Character("Kating RPL", color="#ce93d8")
   - aslab_netics = Character("Aslab NETICS", color="#80cbc4")
   - aslab_kbj = Character("Aslab KBJ", color="#ffcc02")
   - aslab_kcv = Character("Aslab KCV", color="#ffab40")
   - aslab_pkt = Character("Aslab PKT", color="#bcaaa4")
   - aslab_mci = Character("Aslab MCI", color="#90caf9")
   - aslab_giga = Character("Aslab GIGA", color="#b0bec5")
   - narrator = Character(None, what_color="#ffffff")

2. Definisikan variable global berikut di blok `define` atau `default`:
   - default baterai = 5   # nyawa/baterai pemain

3. Buat label berikut sebagai STUB (isinya hanya "pass" atau placeholder):
   start, lab_alpro, lab_rpl, lab_netics, lab_kbj, lab_kcv, lab_pkt, lab_mci, lab_giga,
   ending_tle, ending_normal, ending_true

4. Isi label `start` dengan konten PROLOG lengkap sesuai naskah berikut:
   - Tampilkan background: "images/places/plaza_supeno.jpg"
   - Mainkan BGM: "audio/bgm/bgm_santai.ogg" (loop)
   - Tampilkan sprite masta: "images/character/char_maba_normal.png" di center
   - Narasi & dialog sesuai naskah prolog (sampai Masta membaca balasan WA dari Bapak TC)
   - Mainkan SFX: "audio/sfx/sfx_phone_ring.ogg" saat scene WA muncul
   - Di akhir prolog, lompat ke label `lab_alpro` dengan perintah: jump lab_alpro

5. Tampilkan nilai baterai saat ini di layar menggunakan screen sederhana:
   screen hud():
       text "🔋 Baterai: [baterai]/5" xalign 0.98 yalign 0.02 size 22

   Panggil screen ini dengan: show screen hud

6. Jangan isi label selain `start` dulu. Tulis komentar # TODO di setiap stub label.

OUTPUT: Satu file lengkap `game/script.rpy` yang bisa langsung dijalankan di RenPy Launcher tanpa error.
```

---

## TAHAP 2 — Lab 1: Alpro (Puzzle + Reward)

**Tujuan:** Implementasi satu lab lengkap sebagai template untuk lab-lab berikutnya.

**Instruksi:**

```
Lanjutkan file `game/script.rpy`. Isi label `lab_alpro` dengan konten lengkap berikut:

KETENTUAN:
1. Tampilkan background: "images/places/lab_alpo.jpg" with dissolve
2. Tampilkan sprite aslab: "images/character/char_kalab_ap.png" di right
3. Tampilkan sprite masta: "images/character/char_maba_normal.png" di left
4. Jalankan dialog sesuai naskah Lab Alpro
5. Implementasi PUZZLE berupa menu pilihan. Deskripsi visualnya ganti jadi teks dulu (gambar flowchart belum ada):
   "Aslab menunjuk layar: [Jalan Maju] → [Nabrak Tembok?] → ??? Blok mana yang salah?"
   menu:
       "A. Tetap Jalan Maju (blok ke-3)":
           # BENAR
           ...
       "B. Balik Arah (blok ke-2)":
           # SALAH
           ...
       "C. Berhenti Total (blok ke-2)":
           # SALAH
           ...

6. Jika BENAR:
   - Mainkan SFX: "audio/sfx/sfx_correct.ogg"
   - Tampilkan dialog reward sesuai naskah
   - Set variabel: $ masta_file_fig = True  (buat default False di bagian atas file)
   - Ubah sprite masta jadi: "images/character/char_maba_senang.png"
   - jump lab_rpl

7. Jika SALAH:
   - Mainkan SFX: "audio/sfx/sfx_wrong.ogg"
   - Tampilkan dialog penolakan sesuai naskah
   - Kurangi baterai: $ baterai -= 1
   - Cek kondisi: if baterai <= 0: jump ending_tle
   - Ubah sprite masta jadi: "images/character/char_maba_marah.png"
   - Kembali ke awal puzzle (gunakan label internal lab_alpro_puzzle dan jump ke sana)

CATATAN: Ikuti pola TAHAP 2 ini sebagai template untuk lab 3–7.
OUTPUT: Hanya isi label lab_alpro yang diperbarui. Jangan ubah label lain.
```

---

## TAHAP 3 — Lab 2 sampai 7 (Semua Lab Tengah)

**Tujuan:** Isi semua lab yang tersisa (RPL, NETICS, KBJ, KCV, PKT, MCI) mengikuti pola TAHAP 2.

**Instruksi:**

```
Isi label lab_rpl, lab_netics, lab_kbj, lab_kcv, lab_pkt, dan lab_mci
masing-masing dengan pola yang sama persis seperti lab_alpro di TAHAP 2.

Petunjuk per lab:

--- LAB RPL (label: lab_rpl) ---
Background: "images/places/lab_rpl.jpg"
Sprite aslab: "images/character/char_kalab_rpl.png" di right
Puzzle: Pilih warna tombol Delete yang cocok untuk tema Earth Tone
  menu:
    "A. Merah Neon": SALAH
    "B. Terracotta (Oranye Kecoklatan)": BENAR
    "C. Kuning Stabilo": SALAH
Reward variable: $ masta_flashdisk = True
Jump berikutnya: lab_netics

--- LAB NETICS (label: lab_netics) ---
Background: tidak tersedia, gunakan: scene black  (atau lab_tkj.jpg sebagai alternatif)
Sprite aslab: "images/character/char_kalab_netics.png" di right
Puzzle: Tebak password. Tampilkan hint: "Sticky note: PASSWORD = NAMA LAB INI (DIBALIK)"
  Nama lab: NETICS → password: SCITEN
  menu:
    "Ketik: SCITEN": BENAR
    "Ketik: NETICS": SALAH
    "Ketik: CYBER": SALAH
Reward variable: $ masta_server_access = True
Jump berikutnya: lab_kbj

--- LAB KBJ (label: lab_kbj) ---
Background: "images/places/lab_kbj.jpg"
Sprite aslab: "images/character/char_kalab_kbj_male.png" di right
Puzzle: Apa langkah pertama memperbaiki router hang?
  menu:
    "A. Cabut dan colok ulang kabel power (Hard Reset)": BENAR
    "B. Tarik antena router": SALAH
    "C. Restart komputer": SALAH
Reward variable: $ masta_foto_buram = True
Jump berikutnya: lab_kcv

--- LAB KCV (label: lab_kcv) ---
Background: "images/places/lab_kcv.jpg"
Sprite aslab: "images/character/char_kalab_kcv.png" di right
Puzzle: Tambahkan data apa ke dataset AI agar bisa kenali variasi wajah mahasiswa?
  menu:
    "A. Foto mahasiswa berseragam rapi saja": SALAH
    "B. Foto mahasiswa gondrong (variasi baru)": BENAR
    "C. Foto dosen saja": SALAH
Reward variable: $ masta_rumus = True
Jump berikutnya: lab_pkt

--- LAB PKT (label: lab_pkt) ---
Background: "images/places/lab_pkt.jpg"
Sprite aslab: "images/character/char_kalab_pkt.png" di right
Puzzle: Lanjutkan pola deret: 2, 4, 8, 16, ...
  menu:
    "A. 24": SALAH
    "B. 32": BENAR
    "C. 20": SALAH
Reward variable: $ masta_snippet = True
Jump berikutnya: lab_mci

--- LAB MCI (label: lab_mci) ---
Background: "images/places/lab_mci.jpg"
Sprite aslab: "images/character/char_kalab_mci.png" di right
Puzzle: Urutan node n8n yang benar sebagai pemicu sistem otomatis?
  menu:
    "A. [Kirim Notif WA] → [CCTV Rekam Wajah]": SALAH
    "B. [CCTV Rekam Wajah] → [Kirim Notif WA]": BENAR
    "C. [Kirim Notif WA] → [Simpan Database]": SALAH
Reward variable: $ masta_lokasi_tc = True
Jump berikutnya: lab_giga

KETENTUAN GLOBAL (berlaku semua lab):
- Setiap jawaban BENAR: mainkan sfx_correct.ogg, ganti sprite masta ke senang
- Setiap jawaban SALAH: mainkan sfx_wrong.ogg, baterai -= 1, cek if baterai <= 0: jump ending_tle
  kemudian kembali ke puzzle via jump ke label_puzzle internal
- Tampilkan narasi transisi singkat sebelum jump ke lab berikutnya
- Jangan ubah label lain di luar 6 lab ini

OUTPUT: Semua 6 label lab diisi penuh. Tidak ada label yang masih berisi pass.
```

---

## TAHAP 4 — Lab 8: GIGA (Final Boss + Sistem Ending)

**Tujuan:** Implementasi Lab GIGA sebagai ujian final dan tiga sistem ending.

**Instruksi:**

```
Isi label lab_giga dan ketiga label ending sesuai naskah.

--- LAB GIGA (label: lab_giga) ---
Background: "images/places/lab_giga.jpg" with dissolve
Sprite Bapak TC: "images/character/char_tersenyum.png" di right (muncul perlahan)
Sprite Masta: "images/character/char_maba_takut.png" di left

1. Mainkan BGM baru: "audio/bgm/bgm_ending.ogg" (stop bgm sebelumnya dengan fadeout 1.0)
2. Dialog lengkap sesuai naskah (Masta menyerahkan snippet, Bapak TC memberikan pertanyaan final)
3. PUZZLE FINAL:
   "10.000 data mahasiswa acak. Kamu harus cari satu nama. Pendekatan mana?"
   menu:
       "A. Urutkan dulu (Sort), lalu cari dengan Binary Search":
           # BENAR → cek baterai untuk tentukan ending
           if baterai == 5:
               jump ending_true
           else:
               jump ending_normal
       "B. Cek satu per satu dari atas (Linear Search)":
           # SALAH INSTANT GAME OVER
           jump ending_tle

--- ENDING: TLE / Bad Ending (label: ending_tle) ---
Background: scene black with dissolve
1. Narasi lengkap sesuai naskah ending TLE
2. Tampilkan teks merah besar: "GAME OVER — TLE (Time Limit Exceeded)"
3. Mainkan SFX: "audio/sfx/sfx_wrong.ogg"
4. Di akhir: return   (kembali ke main menu RenPy)

--- ENDING: Normal / A or D Roulette (label: ending_normal) ---
Background: "images/places/lab_giga.jpg"
Sprite Bapak TC: "images/character/char_kalab_giga.png" di right
1. Narasi dan dialog lengkap sesuai naskah ending normal
2. Mainkan SFX: "audio/sfx/sfx_correct.ogg"
3. Tampilkan teks: "ENDING: The A or D Roulette"
4. Di akhir: return

--- ENDING: True / The Chosen One (label: ending_true) ---
Background: "images/places/lab_giga.jpg" with dissolve
Sprite Bapak TC: "images/character/char_tersenyum.png" di right
Sprite Masta: "images/character/char_maba_senang.png" di left
1. Narasi dan dialog lengkap sesuai naskah true ending
2. Mainkan SFX: "audio/sfx/sfx_correct.ogg" dua kali berurutan
3. Tampilkan teks emas besar: "TRUE ENDING: The Chosen One ⭐"
4. Di akhir: return

OUTPUT: Label lab_giga, ending_tle, ending_normal, ending_true semuanya terisi penuh.
```

---

## TAHAP 5 — UI/HUD & Polish

**Tujuan:** Perindah tampilan baterai, tambahkan screen map progress, dan animasi transisi.

**Instruksi:**

```
Buat file terpisah: `game/screens_custom.rpy`

ISI FILE INI:

1. SCREEN HUD (gantikan versi sederhana di script.rpy):
   screen hud():
       frame:
           xalign 0.98 yalign 0.02
           background Frame("gui/frame.png", 5, 5)   # pakai default RenPy jika tidak ada
           hbox spacing 6:
               text "🔋" size 20
               for i in range(5):
                   if i < baterai:
                       text "■" color "#4fc3f7" size 18
                   else:
                       text "□" color "#555555" size 18

2. SCREEN MISI (tampilkan progress lab):
   default labs_done = []   # tambahkan ini di script.rpy bagian default
   
   screen misi():
       frame:
           xalign 0.01 yalign 0.02
           vbox spacing 4:
               text "📍 MISI AKTIF" size 16 bold True color "#ffcc02"
               for lab in ["Alpro","RPL","NETICS","KBJ","KCV","PKT","MCI","GIGA"]:
                   if lab in labs_done:
                       text "✅ Lab [lab]" size 14 color "#a5d6a7"
                   else:
                       text "⬜ Lab [lab]" size 14 color "#aaaaaa"

   Panggil screen ini: show screen misi
   Di setiap label lab setelah puzzle benar, tambahkan: $ labs_done.append("NamaLab")

3. TRANSISI ANTAR LAB:
   Setelah setiap jump antar lab, tambahkan dengan dissolve:
   scene [background] with dissolve

4. Pastikan kedua screen (hud dan misi) dipanggil di label start setelah prolog.

OUTPUT: File baru `game/screens_custom.rpy` yang bisa langsung diimport RenPy tanpa error.
Jangan ubah `game/script.rpy` kecuali menambahkan pemanggilan show screen misi di label start
dan menambahkan $ labs_done.append(...) di setiap lab.
```

---

## TAHAP 6 — File Konfigurasi & Packaging

**Tujuan:** Pastikan game bisa dibuild dan berjalan bersih.

**Instruksi:**

```
Lakukan pengecekan dan perbaikan pada konfigurasi RenPy project:

1. Cek file `game/options.rpy`:
   - Ubah config.name = "Finding MrTC"
   - Ubah config.version = "1.0"
   - Ubah config.window_title = "Finding MrTC — FRS War Edition"
   - Pastikan config.has_music = True dan config.has_sound = True

2. Cek file `game/gui.rpy` (jika ada):
   - Pastikan resolusi: define config.screen_width = 1280 dan config.screen_height = 720

3. Buat file `game/audio.rpy` untuk mendefinisikan semua aset audio agar mudah direferensikan:
   define audio.bgm_santai = "audio/bgm/bgm_santai.ogg"
   define audio.bgm_ending = "audio/bgm/bgm_ending.ogg"
   define audio.sfx_correct = "audio/sfx/sfx_correct.ogg"
   define audio.sfx_wrong = "audio/sfx/sfx_wrong.ogg"
   define audio.sfx_click = "audio/sfx/sfx_click.ogg"
   define audio.sfx_phone = "audio/sfx/sfx_phone_ring.ogg"

4. Lakukan syntax check pada semua file .rpy:
   - Semua label harus memiliki minimal satu statement (tidak boleh kosong)
   - Semua jump harus menuju label yang ada
   - Semua define/default harus di luar label

5. Buat file `README.md` berisi:
   - Cara menjalankan game di RenPy Launcher
   - Daftar lab dan urutan puzzle
   - Penjelasan singkat 3 ending

OUTPUT: File options.rpy yang diupdate, file audio.rpy baru, dan README.md.
Jangan ubah script.rpy di tahap ini.
```

---

## CATATAN DEBUGGING

Gunakan checklist ini setiap selesai satu tahap sebelum lanjut:

- [ ] RenPy Launcher tidak menampilkan error merah saat klik **Launch Project**
- [ ] Semua dialog muncul dengan nama karakter yang benar
- [ ] Puzzle bisa dipilih dan respons benar/salah sesuai
- [ ] Baterai berkurang saat salah jawab
- [ ] Game over redirect ke ending_tle saat baterai = 0
- [ ] Jump antar lab berjalan tanpa loop infinite
- [ ] BGM tidak overlap (stop sebelum play baru)
- [ ] Screen HUD muncul di semua scene

---

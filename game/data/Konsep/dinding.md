# 🎮 FINDING MR. TC

> **Game Design Document** — Visual Novel / Puzzle Adventure

---

## 📖 Prolog

**Visual:** Layar laptop menampilkan *website* Siakad yang *loading* lama (Error 502 Bad Gateway). Di pojok kanan atas ada UI **Baterai Laptop 100% (5 Nyawa)**.

![alt text](/game/data/screenshot/image.png)

**Narasi:** Pukul 14.00 WIB. Portal FRS ditutup satu jam lagi. **Masta** (Mahasiswa Semester Tiga) tertunduk lesu di selasar gedung. Hasil *war* SKS-nya hancur lebur; kelas Pak Irfan sudah ludes oleh kating. Jadwal Masta bolong 3 SKS.

> **Masta:** *"Sial... Kalau begini caranya gua bisa lulus telat. Satu-satunya kelas yang sisa cuma PBO-nya Bapak TC."*

**Konflik:** Kelas Bapak TC kosong karena semua orang takut dengan sistem nilai beliau: cuma ada **A atau D**. Masta nekat mengambil kelas itu, tapi butuh ACC Dosen Wali. Kebetulan, Doswal Masta adalah Bapak TC sendiri. Masta pun mengirim pesan singkat dengan tangan gemetar.

**Visual Chat WA:**
- **Masta:** *"Pak, mohon izin, saya Masta mau minta ACC kelas PBO Bapak..."*
- **Bapak TC:** *"Kamu masukin kelas saya karena niat belajar, atau cuma karena SKS sisa? Saya tidak butuh mahasiswa mental tempe. Buktikan logika kamu jalan. Saya sudah menitipkan 'sesuatu' di Lab Alpro. Mulai dari sana, selesaikan masalah aslab di 7 lab, lalu temui saya di Lab GIGA."*

![alt text](/game/data/screenshot/image-1.png)

---

## 🗺️ Alur Penjelajahan 8 Lab

### Lab 1 — Algoritma & Pemrograman (Alpro)

Masta lari ke Lab Alpro dengan napas tersengal. Aslab di sana sedang pusing menatap monitor.

- **Masta:** *"Bang! Kata Bapak TC beliau nitip sesuatu buat gua di sini?"*
- **Aslab Alpro:** *"Oh, lu korban FRS yang lagi diuji Bapak TC? Iya, beliau nitip file di sini. Tapi kata beliau, gua nggak boleh ngasih file ini ke lu kalau logika dasar lu aja masih jongkok. Kebetulan gua lagi stuck bikin alur buat robot sapu, nabrak tembok terus nggak mau belok. Tolongin gua, bagian mana yang logikanya bikin error?"*

**🧩 Teka-teki:** Klik blok kode yang salah pada gambar *flowchart*:
```
[Jalan Maju] -> [Nabrak Tembok?] -> [Tetap Jalan Maju]  ← INI YANG SALAH
```
![alt text](/game/data/screenshot/image-2.png)

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Bener! Harusnya 'Belok', bukan lanjut maju. Logika lu masih lurus ternyata, Ta. Nih, titipan berkas dari Bapak TC. Tapi aneh, file ujian kok formatnya .fig (Figma). Gua nggak punya aplikasinya. Lu bawa aja ke anak Lab RPL, suruh mereka bukain."* | **Reward: File Soal Bapak TC (.fig)** |
| ❌ Salah | *"Masta, kalau disuruh maju terus ya jebol itu robot! Fokus dong, katanya mau ACC FRS!"* | **Baterai -1** |

---

### Lab 2 — Rekayasa Perangkat Lunak (RPL)

Masta menyerahkan file `.fig` tadi ke Kating RPL yang sedang menatap layar monitor dengan mata merah.

- **Masta:** *"Bang, tolong bukain file desain ini dong. Ini syarat ujian dari Bapak TC buat ACC FRS gua."*
- **Kating RPL:** *"Bapak TC ngasih soal ujian pake format Figma? Absurd banget tuh dosen. Bisa gua bukain, tapi barter tenaga dulu, Ta. Dosen minta tombol 'Delete' ini direvisi. Harus kelihatan bahaya buat user, tapi warnanya harus tetep masuk tema Earth Tone aplikasi ini. Menurut lu yang mana?"*

![alt text](/game/data/screenshot/image-3.png)

**🧩 Teka-teki:** Klik kotak warna **Terracotta** (bukan kuning stabilo atau merah neon).

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Nah, ini baru estetika! Kelihatan tegas tapi nggak ngerusak mata. Oke, file lu udah gua buka... ada password-nya. Kalau soal crack beginian, mending lu bawa ke anak Lab Siber."* | **Reward: Flashdisk ZIP** |
| ❌ Salah | *"Masta, lu ngerusak harmoni desain gua! Warna neon di tema bumi itu dosa besar!"* | **Baterai -1** |

---

### Lab 3 — Teknologi Jaringan dan Keamanan Siber Cerdas (NETICS)

Masta memberikan flashdisk ke Aslab Siber yang sedang santai di pojok lab.

- **Masta:** *"Bang, tolongin gua nembus password file ZIP ini. Gua curiga ini sengaja dikunci sama Bapak TC buat ngetes gua."*
- **Aslab Siber:** *"Wah, ujian FRS Bapak TC ya? Beliau mah paranoid tapi pelupa. Kelemahan sistem itu selalu ada di penggunanya. Tuh liat, dia nempel sticky note di bawah monitornya buat pengingat aslab kalau mau login darurat. Coba lu tebak sendiri, Masta."*

**Visual Hint:** Sebuah kertas kecil bertuliskan:
> **"PASSWORD = NAMA LAB INI (DIBALIK)"**
> *(Masta melihat papan nama lab bertuliskan **NETICS**)*

![alt text](/game/data/screenshot/image-4.png)

**🧩 Teka-teki:** Masta mengetik: `SCITEN`

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Tembus! Emang bener, celah keamanan terbesar itu ada di manusianya sendiri. Tapi bentar, Ta. Isinya ternyata shortcut ke server lokal jurusan! Bapak TC naruh soal aslinya di sana. Gua nggak bisa narik datanya karena internet lab lagi mati total. Lu lari gih ke Lab KBJ, suruh mereka benerin jaringan!"* | **Reward: Akses File Server (Nyangkut)** |
| ❌ Salah | *"Gagal. Masta, lu bisa baca nggak? Nama lab ini SIBER, tinggal lu tulis terbalik doang!"* | **Baterai -1** |

---

### Lab 4 — Komputasi Berbasis Jaringan (KBJ)

Masta mendobrak Lab KBJ dan mendapati labnya kacau karena internet *down*. Aslab sedang jongkok di depan rak server.

- **Masta:** *"Bang! Internet nyalain dong, gua harus narik file ujian Bapak TC dari server lokal nih, buruan!"*
- **Aslab KBJ:** *"Duh Masta, lu nggak liat router-nya merah semua? Jangan nanya IP dulu, mending lu bantuin gua benerin hardware-nya. Lu kan calon engineer, apa langkah pertama yang paling ampuh buat benerin alat yang nge-hang?"*

**🧩 Teka-teki:** Klik area **Kabel Power** pada gambar router untuk melakukan *hard reset*.

![alt text](/game/data/screenshot/image-5.png)

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Internet nyala! Emang hard reset itu solusi dewa. File dari server udah berhasil ditarik dan dikirim ke PC lu. Tapi liat deh, kelakuan Bapak TC... isinya sengaja dibikin foto scan kertas kuno yang buram banget biar lu nggak bisa langsung baca. Bawa gambar ini ke anak KCV, suruh AI mereka yang baca."* | **Reward: Foto Scan Soal Buram** |
| ❌ Salah | *"Masta ngapain narik antena? Emang ini TV cembung? Fokus ke sumber listriknya!"* | **Baterai -1** |

---

### Lab 5 — Komputasi Cerdas & Visi (KCV)

Masta membawa foto buram itu ke Aslab KCV yang sedang memijat pelipisnya menatap monitor.

- **Masta:** *"Bang, tolong scan foto buram ini pake AI OCR lu. Ini soal ujian dari Bapak TC, waktu gua mepet!"*
- **Aslab KCV:** *"Mau jernihin foto? Bisa, tapi AI gua lagi rewel. Dia cuma kenal maba rambut rapi, pas liat mahasiswa gondrong malah dibilang sapu ijuk. Tolong lu perbaiki dulu logikanya. Mana data yang harus gua tambah ke dataset biar AI-nya pinteran dikit?"*

**🧩 Teka-teki:** Klik **Foto Mahasiswa Gondrong** untuk ditambahkan ke *dataset*.

![alt text](/game/data/screenshot/image-6.png)

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Mantap! AI-nya sekarang udah kenal variasi manusia. Nah, foto scan lu udah dijernihin... Tapi anjir, ini bukan teks biasa, ini rumus deret matematika! Bapak TC emang nggak pernah ngasih yang gampang. Bawa ke Lab Pemodelan, otak gua nggak nyampe kalo disuruh nyelesain ginian."* | **Reward: Rumus Deret Matematika** |
| ❌ Salah | *"Lu kasih data yang seragam lagi, AI-nya makin rabun ngenalin orang gondrong, Ta!"* | **Baterai -1** |

---

### Lab 6 — Pemodelan dan Komputasi Terapan (PKT)

Masta menunjukkan rumus deret tersebut ke aslab pemodelan yang sedang menulis di papan tulis.

- **Masta:** *"Bang, gua dapet rumus ini dari rentetan file Bapak TC. Katanya lu bisa bantuin ngerjain ini?"*
- **Aslab PKT:** *"Oh, deret Bapak TC? Khas beliau banget, pasti buat ngetes efisiensi. Ini deret buat nyari batas iterasi program supaya script-nya nggak TLE. Masta, biar lu pantes dapet snippet kodenya, coba lu lanjutin polanya: 2, 4, 8, 16... angka berikutnya berapa?"*

![alt text](/game/data/screenshot/image-7.png)

**🧩 Teka-teki:** Pilih angka **32**.

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Pas! Rumusnya jadi sangat efisien, O(1). Ini snippet kode solusinya, tinggal lu setor ke Bapak TC. Masalahnya... beliau daritadi muter-muter gedung. Nggak ada yang tahu beliau di mana. Coba lu lari ke anak MI, suruh mereka lacak posisinya pake CCTV."* | **Reward: Snippet Kode Solusi O(1)** |
| ❌ Salah | *"16 dikali dua, Masta! Matematika lu ngulang ya di semester satu?"* | **Baterai -1** |

---

### Lab 7 — Manajemen Cerdas Informasi (MCI)

Masta menghampiri Aslab MI yang sedang asyik mengatur *flow* n8n di komputernya.

- **Masta:** *"Bang! Lacakin posisi Bapak TC sekarang pake sistem lu. Gua udah dapet solusinya, tinggal nyetor orangnya doang nih!"*
- **Aslab MCI:** *"Bisa, gua lagi setting sistem deteksi wajah otomatis buat ngelacak dosen. Tapi alur kerjanya masih kebolak-balik nih, belom bisa di-run. Mana kotak yang harus ditaruh paling awal sebagai pemicu sistemnya?"*

**🧩 Teka-teki:** Klik urutan yang benar:

```
[CCTV Rekam Wajah]  →  [Kirim Notif WA]
        ↑ HARUS URUTAN INI
```

> *(Catatan desainer: buat gambar node WA dan CCTV)*

![alt text](/game/data/screenshot/image-8.png)

| Jawaban | Respons | Efek |
|---------|---------|------|
| ✅ Benar | *"Flow jalan! Barusan ada notif otomatis masuk ke grup aslab: 'Bapak TC terpantau masuk ke **Lab GIGA**'. Buruan samperin ke sana sebelum portal FRS tutup, Ta!"* | **Reward: Lokasi Bapak TC** |
| ❌ Salah | *"Logika lu kebalik! Masa WA ngirim notifikasi padahal CCTV-nya belum nangkep apa-apa?"* | **Baterai -1** |

---

### Lab 8 — Grafika, Interaksi, Gim dan Analitik (GIGA) — BOSS STAGE

Masta mendobrak pintu Lab GIGA. Bapak TC sedang duduk tenang di depan PC spesifikasi dewa sambil mantengin terminal kodingan yang jalan super cepat.

- **Masta:** *"Pak... Bapak TC... Ini snippet kode solusi yang Bapak minta. Saya sudah menyelesaikan ujian dari 7 lab yang Bapak siapkan."*
- **Bapak TC:** *(Menoleh perlahan)* *"Tepat waktu, Masta. Kamu berhasil memecahkan rantai ujian itu. Tapi di kelas saya, solusi yang 'asal jalan' tapi lambat itu sampah. Sama saja dengan TLE (Time Limit Exceeded). Pertanyaan terakhir untuk ACC FRS kamu."*

**🧩 Teka-teki Final:**
> *"Ada 10.000 data mahasiswa yang acak. Kamu butuh mencari satu nama spesifik. Mana pendekatan yang menunjukkan otak kamu pantas masuk kelas saya?"*

![alt text](/game/data/screenshot/image-9.png)

| Pilihan | Deskripsi | Hasil |
|---------|-----------|-------|
| **A ✅** | Urutkan dulu *(Sorting)*, lalu potong dua tumpukan data berulang kali *(Binary Search)* | **BENAR** |
| **B ❌** | Cek satu per satu dari atas sampai bawah *(Linear Search)* | **SALAH — Instant Game Over** |

> **Bapak TC (jika pilih B):** *"Pola pikir kuli. Kamu tidak cocok jadi Engineer. Keluar dari lab saya."*

---

## 🏆 Sistem Ending

### 💀 Ending 1 — TLE *(Bad Ending)*

**Kondisi:** Baterai 0% **atau** salah jawab di Lab GIGA.

> Pukul 15.01. Portal FRS tertutup. Masta tertunduk di depan lab GIGA. Bapak TC menolak memberikan ACC karena menganggap logika Masta cacat. Semester ini Masta terpaksa mengambil mata kuliah sisa yang tidak ia sukai. Rencana lulus tepat waktu pun hancur lebur.

---

### 🎲 Ending 2 — The A or D Roulette *(Normal Ending)*

**Kondisi:** Benar di Lab GIGA, tapi Baterai sisa **20%–80%** (pernah salah di lab lain).

> Bapak TC mengambil ponselnya, lalu mengklik tombol **[ACC]** di web Siakad Doswal. *"Logika kamu masih banyak bocornya, tapi nyali kamu lumayan. Saya ACC. Tapi ingat... di kelas saya cuma ada nilai A atau D. Jangan sampai kamu menyesal masuk kelas saya."* Masta merinding, perang sesungguhnya di kelas PBO baru saja dimulai.

---

### ⭐ Ending 3 — The Chosen One *(True Ending)*

**Kondisi:** Benar di Lab GIGA, Baterai tetap **100%** *(Perfect Run — tanpa satu pun kesalahan)*.

> Bapak TC tersenyum tipis, sebuah pemandangan langka di jurusan ini. Beliau langsung mengklik **[ACC]** di sistem. *"Sempurna. Kamu melewati semua lab tanpa satu pun cacat logika. Sepertinya kelas PBO saya punya satu bintang semester ini."* FRS Masta sukses, dan Bapak TC bahkan menawarinya posisi asisten dosen semester depan. Masta keluar lab sebagai legenda kampus.

---

## ⚙️ Mekanik Permainan

| Elemen | Deskripsi |
|--------|-----------|
| 🔋 Baterai / Nyawa | Mulai dari **100% (5 Nyawa)**. Setiap jawaban salah: **-1 nyawa** |
| ⏱️ Batas Waktu | Portal FRS tutup pukul **15.00 WIB** |
| 🗺️ Progesi | Linear — harus menyelesaikan lab secara berurutan (1→8) |
| 🔑 Reward Chain | Setiap lab menghasilkan item yang dibutuhkan di lab berikutnya |

---

## 📊 Ringkasan Teka-teki Per Lab

| Lab | Tema | Jawaban Benar | Reward |
|-----|------|---------------|--------|
| 1 — Alpro | Logika Flowchart | Klik blok `[Tetap Jalan Maju]` | File Soal (.fig) |
| 2 — RPL | UI/UX Color Theory | Pilih warna **Terracotta** | Flashdisk ZIP |
| 3 — NETICS | Keamanan Siber | Ketik `SCITEN` | Akses File Server |
| 4 — KBJ | Troubleshooting Hardware | Klik **Kabel Power** | Foto Scan Soal |
| 5 — KCV | Machine Learning Dataset | Klik **Foto Mahasiswa Gondrong** | Rumus Deret |
| 6 — PKT | Pola Deret Matematika | Pilih angka **32** | Snippet Kode O(1) |
| 7 — MCI | Alur Kerja Otomasi | **CCTV** dulu, baru **WA** | Lokasi Bapak TC |
| 8 — GIGA | Algoritma Pencarian | Pilih **A (Binary Search)** | ACC FRS ✅ |

---

*FSM — Game Design Document v1.0*

![alt text](/game/data/screenshot/image-10.png)
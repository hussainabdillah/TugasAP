# Tugas matakuliah Algoritma dan Pemrograman, Kelas x 2021

Project ini adalah bagian dari tugas besar matakuliah Algoritma dan Pemrograman, Teknik Informatika, Universitas Muhammadiyah Surakarta, tahun 2021.

Dosen : Fajar Suryawan, Ph.D

## Bagaimanakah struktur kode aplikasi ini?
Struktur kode 
Langkah awal membuat class di apps.py lalu dipanggil di settings.py . Kemudian membuat beberapa fungsi yang berkaitan dengan aplikasi di myutils.py untuk dipanggil di views.py, dengan cara mengimport nya ke views dari my utils .
Kemudian membuat definisi fungsi yang berisi beberapa list di views.py untuk di panggil di template html . Setelah itu membuat definisi untuk bisa mereturn hasil yang kita inginkan , lalu hasilnya dipanggil di template html .
Untuk membuat link untuk bisa berpindah-pindah page, membuat definisi terlebih dahulu di views.py dan mereturn render, lalu membuat path di urls.py dengan menyantumkan nama path yang mau kita panggil nanti, lalu nama dari definisi yang telah dibuat di views.py, lalu nama url yang akan ditampilkan . Setelah itu dipanggil di template html dengan memangil url dan nama path .
Untuk mengimport gambar dengan cara meng-hosting terlebih dahulu gambar tersebut ke web, lalu menyalinkan linknya ke template html. Selain mengimport gambar kita juga mengimport font dari google font. Untuk css dibuat di dalam file html itu sendiri.
Untuk settings.py time zone diubah menjadi Asia/Jakarta supaya jam nya bisa mengikuti sesuai dengan zona waktu WIB . 

Maka strukturnya jika dijabarkan :
    apps-->settings-->myutils-->views-->urls-->templates-->index dan about .

Setelah semua itu selesai lalu membuat file readme untuk informasi lalu merge semua file yang berada di branch saat ini ke branch master . Setelah itu deploy aplikasi ke heroku dengan cara membuat procfile terlebih dahulu lalu push lewat git push heroku master.

Definisi dan fungsi setiap file :
Apps      : Berisi app config .
Settings  : Untuk pengaturan berkaitan dengan config project .
Myutils   : Untuk menyimpan kode fungsi yang dibutuhkan untuk menghitung pajak. 
Views     : Untuk menyimpan kode fungsi terusan dari myutils .Dan untuk diteruskan ke index, about dan urls . Didalam views juga ada fungsi exception dan error handling .
Urls      : Untuk menyimpan kode yang berhubungan dengan routing atau link supaya bisa mengganti page dan merefresh page .
Procfile  : digunakan untuk deploy ke Heroku .
Templates : Menyimpan file html untuk ditampilkan di web. terdapat dua file di dalam folder templates .
            1. index.html : untuk menampilkan halaman utama yang berisi fungsi untuk menghitung pajak progresif berupa table, identitas anggota kelompok, dosen dan waktu .
            2. about.html : untuk menampilkan about page , berisi pengertian dan diagram dari pajak progresif , dan tentang kontribusi anggota . 



## Akses Aplikasi di Heroku:

https://dashboard.heroku.com/apps/pajak-2021-hussain-ilham-pandu/deploy/heroku-git

https://pajak-2021-hussain-ilham-pandu.herokuapp.com/

## Anggota Kelompok:
1. Hussain Abdillah Tugas Kelarno, L200214201
2. Ilham Aufal Hadad, L200214071
3. Pandu Putra Wijaya, L200214174

## Daftar kontribusi :
1. Hussain   : Mengedit kode python, Membuat tabel diagram, Mengubah indeks .
2. Ilham     : Membuat about page, mencari referensi, Mengedit gambar .
3. Pandu     : Mengedit CSS dan mengupload ke heroku .

## Kontribusi dari luar kelompok :
 1. Aldin    : Memberikan penjelasan tentang routing (menghubungkan homepage ke about page)
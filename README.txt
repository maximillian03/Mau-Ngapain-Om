IF2211-Strategi-Algoritma
Tugas Kecil 3
Semester II Tahun 2020/2021

Mesin pencarian lintasan terpendek dengan algoritma A star Bernama “Mau Ngapain Om” dalam Bahasa Python

Description :
Sebuah program kecil (sederhana) dalam bahasa Python yang dapat mencari lintasan terpendek dari input graf dengan 
mengimplementasikan algoritma A star. 

Requirement :
- Download and install Python (https://www.python.org/downloads/))
- Install networkx (https://riptutorial.com/networkx/example/18973/installation-or-setup)
- Install matplotlib (https://ehmatthes.github.io/pcc/chapter_15/README.html)

Setup and Run :
- Pastikan sudah memiliki Python dengan versi yang tidak terlalu lama pada komputer Anda.
- Ekstrak dan tempatkan folder pada directory yang diinginkan.
- Sebelum menjalankan program, perhatikan directory tempat menyimpan folder karena directory path dari file test yang diakses pada source code harus diubah secara manual.
- Setelah mendapatkan alamat directory dari file test pada komputer, salin alamat tersebut dan ubah directory path dalam source code pada variabel 'path' dengan alamat tersebut.
- Perhatikan bahwa alamat yang dipakai harus menggunakan '/' bukan '\' dan diakhiri dengan '{}.txt'. (Contoh : "C:/Users/Windows/Desktop/Tucil3_13519103/test/{}.txt")
- Setelah directory path dari file test telah diubah, program dapat langsung dijalankan melalui text editor ataupun Command Prompt.
- Apabila menggunakan Command Prompt, pertama-tama arahkan dahulu menjadi directory tempat menyimpan source code yaitu 'src' pada folder 'Tucil3_13519103'.
- Setelah berada pada directory 'src', ketikkan 'python MauNgapainOm.py' dan program berhasil dijalankan.
- Perlu diingat bahwa program tidak bisa dijalankan melalui executable (.exe) dikarenakan directory path yang berbeda dan tidak menggunakan library os pada source code.

Features : 
- Input file graf dengan format (.txt)
- Menampilkan graf yang telah di input
- Mencari jalur terpendek dengan algoritma A star melalui input simpul asal dan simpul tujuan 
- Menampilkan graf dengan jalur terpendek berdasarkan input yang telah dilakukan 
(warna kuning pada node berarti node tersebut dilalui, warna merah pada edge berarti edge tersebut dilalui)  

NB: 
Jika ingin memasukkan test case milik sendiri, harap untuk mengikuti test case yang sudah diberikan secara sama persis dikarenakan case sensitive. (format .txt)
contoh penulisan file input: 

2 			-> banyak simpul 
Dago 30 40		-> nama jalan, koordinat X, koordinat Y (dipisah dengan spasi)
ITB 50 60		-> nama jalan, koordinat X, koordinat Y (dipisah dengan spasi)
1 0			-> adjacency matrix yang menguhubungkan (case ini dago terhubung dengan ITB)
0 1			-> adjacency matrix yang menguhubungkan (case ini ITB terhubung dengan dago)

Author :
- Bryan Rinaldo/13519103/K-02 IF2019
- Maximillian Lukman/13519153/K-03 IF2019
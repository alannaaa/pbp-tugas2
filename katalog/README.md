# Assignment 2

Lihat hasil deploy [di sini](https://pbp-tugas2-alanna.herokuapp.com/) <br>
Lihat hasil deploy aplikasi Katalog [di sini](https://pbp-tugas2-alanna.herokuapp.com/katalog/)

## Bagan
![Untitled presentation](https://user-images.githubusercontent.com/88122697/190184684-bb4c2ab8-3cc1-4bc3-b935-b56a152eb4c2.png)

### Deskripsi
1. Saat client mengakses aplikasi dengan path `katalog`, Django akan mengakses file `urls.py` pada folder `project_django/urls.py` lalu mencari route `katalog/` pada list `urlpatterns`. Pada list tersebut, tercantum `include('katalog.urls')`, maka routing katalog di handle oleh file `katalog/urls.py`
2. Setelah mengakses `katalog/urls.py`, ditemukan bahwa route yang di-request di handle oleh view  `show_katalog` yang diimport dari `katalog/views`
3. `show_katalog` akan me-render HTML sesuai request user yaitu `katalog.html` termasuk: melibatkan _context_ yang akan ikut di-render. Fungsi ini pun akan membuat _list_ berisi `CatalogItem` yang di-import dari `katalog/models`, yang kemudian akan me-retrieve data dari database agar dapat men-display data benda-benda katalog pada laman HTML.
4. Laman HTML ter-render dan dapat diakses client.

## Kenapa menggunakan _virtual environment?_
   _virtual environment_ dari python merupakan _environment manager_ yang membuat environment virtual yang terisolasi dari project lainnya (agar dependencies dan packages tidak tercampur antar project satu dengan yang lainnya). _virtual environment_ akan menjaga agar data-data pada library project hanya ter-update/diubah di env tersebut dan tidak pada local storage. Hal ini dapat bermanfaat apabila, contohnya, dua project membutuhkan library yang sama dengan version yang berbeda.

### Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?
Ya, tanpa menggunakan _virtual environment_, kita tetap dapat membuat aplikasi web berbasis Django. Namun, seperti yang sudah dibahas sebelumnya, _practice_ ini tidak direkomendasikan dan tidak menguntungkan bagi kita.

## Implementasi poin 1–4
1. **Membuat fungsi pada `views.py`**<br>
Saya menambahkan function bernama `show_katalog` pada template yang akan mengakses data dari model (`CatalogItem` dari `katalog/models`) serta membuat variabel yang diperlukan (nama, npm). Data `CatalogItem` yang disimpan ke dalam `list` serta variabel-variabel tadi disimpan dalam dictionary bernama `context`. Fungsi ini mengembalikan HttpResponse dengan memanggil fungsi render dan mengikutsertakan `context` di dalamnya.
2. **Routing (`urls.py`)**<br>
Pada file  `urls.py` yang terletak di folder utama (project_django), ditambahkan route `/katalog` yang akan di-handle oleh file `katalog/urls.py` dengan menambahkan potongan kode berikut pada list `urlpatterns`
   
   ```
    ...
    path('katalog/', include('katalog.urls')),
    ...
   ```
   File `katalog/urls.py` kemudian akan menjalankan function `show_katalog` yang terdapat di file `katalog/views.py`

3. **Memetakan data ke HTML (`katalog.html`)**<br>
Function render yang dipanggil fungsi `show_katalog` menerima argumen bahwa _template name_-nya yaitu `katalog.html`. Pada template ini, saya menggunakan kembali variabel dari `context` dengan menggunakan `{{nama}}`, `{{student_id}}`, kemudian mengiterasi list `list_barang` yang berisi data barang dengan for loop dan menampilkannya pada tabel sesuai urutan.

4. **Deploy ke Heroku**<br>
Di Heroku, saya membuat aplikasi baru dan menghubungkannya dengan repository github yang bersangkutan dengan aplikasi. Kemudian, saya menambahkan Repository Secrets berupa API key Heroku saya serta nama aplikasi yang akan saya gunakan pada repository tersebut.  Setelah menjalankan kembali _workflow_ yang gagal, aplikasi pun ter-deploy!

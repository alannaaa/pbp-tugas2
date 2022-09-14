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

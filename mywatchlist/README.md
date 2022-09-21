# Tugas 3: My Watchlist
🔗 [Link to Deployment](https://pbp-tugas2-alanna.herokuapp.com/mywatchlist/)

## Perbedaan JSON, XML, dan HTML
* **JSON** <br>
JSON (JavaScript Object Notation) digunakan untuk menyimpan dan mengirimkan data dan termasuk sangat mudah untuk dimengerti. Sintaks JSON merupakan turunan dari Object JavaScript. Akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat dibanyak bahasa pemrograman. JSON lebih singkat dan lebih cepat untuk ditulis dan dibaca. JSON juga tidak membutuhkan _end tag_ dan bisa menggunakan array.
* **XML** <br>
Seperti JSON, XML (eXtensible Markup Language) juga digunakan untuk menyimpan dan mengirimkan data. XML juga didesain menjadi self-descriptive,sehingga informasi yang disajikan mudah dimengerti. XML hanyalah informasi yang dibungkus di dalam tag. Salah satu perbedaan dari JSON dan XML adalah XML harus di-_parse_ menggunakan XML parser, sementara JSON dapat di-_parse_ menggunakaan function JavaScript biasa.
* **HTML** <br>
HTML (Hypertext Markup Language) merupakan markup languange yang dapat digunakan untuk merepresentasikan data dalam element tree. Data-data ini kemudian dapat ditampilkan dalam bentuk web page yang tampilannya dapat dikustomisasi.

## Alasan dibutuhkannya _data delivery_ dalam pengimplementasian sebuah platform
Penggunaan data delivery akan menjadi hal yang menguntungkan saat mengimplementasikan suatu platform. Dalam penggunaan sebuah platform, pertukaran data antara client dan server pasti terjadi, misalnya untuk melakukan CRUD (Create, Read, Update, Delete). Pertukaran ini akan dipermudah dan komunikasinya dapat diterima dengan baik dengan _data delivery_ ini. Untuk melakukan _data delivery_, dapat digunakan format tertentu seperti HTML, JSON, dan XML.

## Implementasi
1. Mengaktivasi virtual environment di directory project lalu menjalankan `python manage.py startapp mywatchlist` untuk membuat aplikasi Django baru bernama mywatchlist.
2. Menambahkan path `mywatchlist` di file `/project_django/urls.py` dengan kode:
```
urlpatterns = [
    ...
    path('mywatchlist/', include('mywatchlist.urls')),
]
```
Menambahkan `'mywatchlist'` ke `INSTALLED_APPS` di file `/project_django/settings.py` dengan kode:
```
INSTALLED_APPS = [
    ...,
    'mywatchlist',
]
```
3. Membuat model MyWatchlist di `/mywatchlist/models.py` dengan atribut-atribut yaitu `watched`, `title`, `rating`, `release_date`, `review` dan field yang sesuai. Kemudian, melakukan migrasi dengan menjalankan `python manage.py makemigration` dan `python manage.py migrate`
4. Membuat direktori baru `/mywatchlist/fixtures/movies_catalog.json` dan menambahkan data berupa 10 film yang ingin dimasukkan ke database.
5. Membuat fungsi untuk menampilkan data-data tersebut dengan format HTML, JSON, dan XML di `mywatchlist/views.py`, kemudian melakukan routing untuk menampilkan masing-masing format dengan menambahkan path pada list `urlpatterns` di `/mywatchlist/urls.py`.
6. Menambahkan `&& python manage.py loaddata movies_catalog.json` di baris pertama Procfile. Setelah semua selesai, melakukan `git pull, commit, push` lalu menjalankan workflow yang gagal agar aplikasi mywatchlist ter-deploy di aplikasi Heroku.

## Screen capture Postman
### /html
![HTML](https://user-images.githubusercontent.com/88122697/191400030-922e01fc-d14a-48ad-bd19-daef677ff9e7.png)
### /xml
![XML](https://user-images.githubusercontent.com/88122697/191400069-9b29f0bf-240e-4038-abc8-c9b15b651514.png)
### /json
![JSON](https://user-images.githubusercontent.com/88122697/191399872-9bad0239-43e6-445d-88fb-c91128e250ce.png)

# TUGAS 4: To-Do List
🔗 [Link to Deployment](https://pbp-tugas2-alanna.herokuapp.com/todolist/)

## Apa kegunaan {% csrf_token %} pada elemen `<form>`?
Tag {% csrf_token %} dari Django dapat diimplementasikan untuk menghindari Cross Site Request Forgery (CSRF) attack, yaitu attack yang membuat end-user mengeksekusi suatu action yang tidak diinginkan pada aplikasi web di mana mereka telah terautentikasi. Tag ini akan men-generate sebuah token khusus pada server-side saat me-render laman. Setelahnya, saat menerima request, server-side application akan membandingkan kedua token yang ada di user session dan di request tersebut. Request yang masuk hanya akan dieksekusi apabila mengandung token khusus tadi. Jika token tidak ditemukan atau kedua token berbeda, request akan ditolak dan user session akan di-terminate serta event-nya di-log sebagai potential CSRF attack.</br>
Apabila kita tidak menggunakan {% csrf_token %}, maka akan terdapat ancaman CSRF yang besar. Attacker dapat mengelabui user (misalnya dengan mengirim link) agar membuat request yang tidak diinginkan. Apabila korbannya user normal, maka CSRF attack dapat melakukan state-changing request seperti menghapus akun user, mengubah alamat surel yang terdaftar, mentransfer dana ke akun lain, dan sebagainya. Apabila korbannya akun administratif, attack ini dapat membahayakan keseluruhan aplikasi web.

## Apakah kita dapat membuat elemen `<form>` secara manual?
Bisa. Saya mencontohkan pembuatan elemen `<form>` tanpa generator seperti `{{ form.as_table }}` pada template `create_task.html`. Caranya tidak jauh berbeda – pada template, kita letakkan tag `<form method="POST" action="">`, kemudian `{% csrf_token %}`. Hanya saja, setelah itu kita perlu men-_specify_ baris per baris yang berisikan prompt serta field untuk input. Misalnya dibutuhkan prompt serta field untuk meminta judul task, maka kita letakkan kode sebagai berikut di dalam tag `<table>`:
```         
<tr>
    <td>Task Title: </td>
    <td><input type="text" name="title" placeholder="Title" class="form-control"></td>
</tr>
```
Untuk selebihnya, kode yang dibutuhkan sama saja. Contohnya, untuk membuat tombol submit yang mengirimkan data ke form-handler, kita memakai tag `input` dengan type `submit`, contohnya `<input type="submit" name="submit" value="Create Task"/>`.
Kemudian, setelah data di-submit, data dapat diakses oleh function dalam `views` yang tadi memanggil render form dengan memanfaatkan method `request.POST.get(name)`. Contohnya, jika kita ingin mengambil judul task dari potongan kode template di atas, maka kita dapat memanggil `request.POST.get("title")`.

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

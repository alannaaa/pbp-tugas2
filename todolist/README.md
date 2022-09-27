# TUGAS 4: To-Do List
🔗 [Link to Deployment](https://pbp-tugas2-alanna.herokuapp.com/todolist/)

## Apa kegunaan {% csrf_token %} pada elemen `<form>`?
Tag `{% csrf_token %}` dari Django dapat diimplementasikan untuk menghindari Cross Site Request Forgery (CSRF) attack, yaitu attack yang membuat end-user mengeksekusi suatu action yang tidak diinginkan pada aplikasi web di mana mereka telah terautentikasi. Tag ini akan men-generate sebuah token khusus pada server-side saat me-render laman. Setelahnya, saat menerima request, server-side application akan membandingkan kedua token yang ada di user session dan di request tersebut. Request yang masuk hanya akan dieksekusi apabila mengandung token khusus tadi. Jika token tidak ditemukan atau kedua token berbeda, request akan ditolak dan user session akan di-terminate serta event-nya di-log sebagai potential CSRF attack.</br>
Apabila kita tidak menggunakan `{% csrf_token %}`, maka akan terdapat ancaman CSRF yang besar. Attacker dapat mengelabui user (misalnya dengan mengirim link) agar membuat request yang tidak diinginkan. Apabila korbannya user normal, maka CSRF attack dapat melakukan state-changing request seperti menghapus akun user, mengubah alamat surel yang terdaftar, mentransfer dana ke akun lain, dan sebagainya. Apabila korbannya akun administratif, attack ini dapat membahayakan keseluruhan aplikasi web.

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

## Proses alur data
Contoh: kita ingin membuat instance dari model bernama Task yang terdapat di `todolist/models.py`. User memberikan input berupa judul task dengan `name = "title"`
* Submit button diklik
* Input dapat diakses oleh function dalam `views` yang tadi memanggil function untuk merender form dengan memanfaatkan method `request.POST.get(name)`
* Data dapat disimpan dengan menginstansiasi object baru menggunakan keyword arguments ke model class-nya, lalu memanggil save() untuk menyimpan ke database. Contohnya:
```
from todolist.models import Task
t = Task(title=request.POST.get("title"))
t.save()
```
* Cara lain adalah dengan menggunakan method `create()` (tidak perlu memanggil `save()`) 
* Dalam fungsi yang akan memanggil function render untuk laman yang akan memuat data, data yang ingin ditampilkan disertakan dalam `context`. Contohnya, jika ingin menyertakan data sesuai user yang membuat request maka kita dapat mem-filter database, sehingga kode akan seperti berikut:
```
context = {
        "todolist" : Task.objects.filter(user=request.user),
    }
```
* Context dijadikan argument saat pemanggilan method render, maka pada template kita dapat menggunakan variabel `todolist`. Contohnya, kita dapat menampilkan nama dari setiap task dalam todolist dengan kode berikut:
```
{% for task in todolist %}
  <tr>
      <td>{{ task.title }}</td>
  </tr>
{% endfor %}
```
* Data berhasil ditampilkan di halaman HTML

## Implementasi
1. Menjalankan perintah `python manage.py startapp todolist` di folder root.
2. Menambahkan `path('todolist/', include('todolist.urls')),` di urlpatterns pada file `project_django/urls.py` dan `path('', show_todolist, name='show_todolist'),` di urlpatterns pada file `todolist/urls.py`. 
3. Membuat class Task pada `todolist/models.py` dengan atribut `user` dengan ForeignKey berupa User dan `date, title, description` dengan fields yang sesuai
4. Membuat fungsi register, login, dan logout pada `todolist/views.py`, kemudian membuat template HTML untuk masing-masing fungsi
5. Membuat fungsi show_todolist untuk memanggil render template HTML dengan context yang sesuai, kemudian membuat template HTML untuk menampilkan username pengguna, tombol untuk menambahkan task baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
6. Membuat form pada template HTML create_task yang menerima input judul dan deskripsi task yang ingin ditambahkan, kemudian membuat fungsi create_task pada `todolist/views.py` yang akan me-render halaman pembuatan task, lalu menambahkan data yang di-input ke database.
7. Menambahkan routing yang sesuai dengan fungsinya pada file `todolist/urls.py` dengan kode sebagai berikut:
```
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
```
8. Melakukan git pull, add, commit, lalu push ke repository yang terhubung dengan aplikasi Heroku.
9. Melakukan mekanisme registrasi dan login di aplikasi Heroku hingga 2 pengguna. Pada akun masing-masing pengguna, melakukan mekanisme "create task" 3 kali.

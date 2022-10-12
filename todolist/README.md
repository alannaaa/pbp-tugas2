## Jump to:
➡️ [TUGAS 4](#tugas-4-to-do-list) </br>
➡️ [TUGAS 5](#tugas-5)

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


# TUGAS 5
🔗 [Link to Deployment](https://pbp-tugas2-alanna.herokuapp.com/todolist/)
## Perbedaan serta Kelebihan-Kekurangan dari Inline, Internal, dan External CSS
**Inline Style** <br>
Berisi Cascading Style Sheet (CSS) properties pada bagian body, dilampirkan inline/sebaris dengan elemen HTML dengan atribut `style`. Penerapannya bersifat unik terhadap satu elemen HTML.
- Kelebihan <br>
Karena dilampirkan dalam dokumen yang sama dengan HTML, tidak perlu membuat dan mengunggah dokumen terpisah. Selain itu, Inline Style dapat dengan mudah dan cepat membuat properti CSS ke dalam halaman HTML. <br>
- Kekurangan <br>
Pada kasus tertentu, inline styling dapat mempengaruhi ukuran HTML file serta waktu download-nya. Selain itu, apabila terlalu banyak digunakan, struktur dari file HTML akan menjadi lebih berantakan. </br>

**Internal Style** <br>
Cascading Style Sheet (CSS) properties dilampirkan di dalam file HTML yang di-style pada bagian head. Internal style bersifat akan berlaku untuk halaman HTML tersebut. Internal Style menggunakan elemen `<style>` di bagian `<head>`.
- Kelebihan <br>
Properti CSS berada pada file HTML yang sama sehingga tidak perlu mengunggah banyak file dan struktur halaman lebih rapi dibanding menggunakan inline style. Selain itu, kita dapat menggunakan class dan ID selector. <br />
- Kekurangan <br>
Ukuran halaman HTML serta waktu loading dapat meningkat karena adanya property CSS. Style yang didefinisikan pada Internal Style akan di-override oleh Inline Style.</br>

**External Style** <br>
Menggunakan file CSS yang terpisah dengan extension `css`, berisi style properties dengan bantuan tag atribut. File ini akan di-link oleh dokumen HTML yang mau menerapkan dengan menggunakan tag link. External style dapat digunakan untuk banyak halaman HTML. <br>
- Kelebihan <br>
Cenderung lebih efisien untuk menerapkan style pada web berskala besar. Selain struktur HTML files yang akan lebih rapi, ukuran file dan waktu loading nya juga lebih kecil.
- Kekurangan <br>
Apabila kita menggunakan beberapa file CSS, waktu loading dapat meningkat. Selain itu, terdapat kemungkinan halaman tidak berhasil dirender secara sempurna hingga file CSS berhasil dimuat.</br>

## Tag HTML5
- `<a>` : Mendefinisikan Hyperlink
- `<b>` : Menampilkan teks dalam style tebal atau bold <br />
- `<body>` : Mendefinisikan bagian body suatu dokumen <br />
- `<br>` : Menghasilkan sebuah line break <br />
- `<button>` : Membuat sebuah tombol yang dapat di klik <br />
- `<code>` : Menspesifikasikan teks sebagai kode komputer <br />
- `<div>` : Menspesifikasikan sebuah bagian atau divisi dalam dokumen <br />
- `<embed>` : Meletakkan aplikasi eksternal seperti konten media ke dalam dokumen HTML
- `<footer>` : Merepresentasikan footer sebuah dokumen atau bagian <br />
- `<form>` : Mendefinisikan sebuah form HTML untuk input user <br />
- `<head>` : Mendefinsikan bagian head dokumen seperti judul <br />
- `<h1>` to `<h6>` : Mendefinisikan header HTML <br />
- `<html>` : Mendefinisikan root dari suatu dokumen HTML <br />
- `<img>` : Merepresentasikan suatu gambar <br />
- `<input>` : Mendefinisikan sebuah kontrol input <br />
- `<input>` : Mendefinisikan sebuah kontrol input <br />
- `<label>` : mendefinisikan sebuah label untuk kontrol input <br />
- `<li>` : Mendefiniskan sebuah list <br />
- `<link>` : Mendefinisikan hubungan antara dokumen dan sumber eksternal <br />
- `<nav>` : Mendefinsikan sebuah bagian mengenai link navigasi <br />
- `<p>` : Mendefinisikan paragraf <br />
- `<source>` : Mendefinisikan sumber media alternatif untuk elemen media <br />
- `<style>` : Merepresentasikan informasi style ke dalam head dokumen <br />
- `<svg>` : Meletakkan konten SVG dalam dokumen HTML <br />
- `<table>` : Mendefinisikan sebuah tabel <br />
- `<tbody>` : Mengelompokkan sekumpulan baris yang mendefinisikan isi utama tabel <br />
- `<td>` : Mendefinisikan cell dalam tabel <br />
- `<th>`: Mendefiniskan table header

## Jelaskan tipe-tipe CSS selector yang kamu ketahui
1. **Element selector** <br>
Menyeleksi elemen HTML berdasarkan nama elemennya. 
2. **ID selector** <br>
Menyeleksi satu elemen HTML yang unik menggunakan attribute id nya
3. **Class selector** <br>
Memilih elemen HRML dengan atribut spesifik class tertentu.
4. **Combinator selector** <br>
Menyeleksi elemen berdasarkan hubungan spesifik antarelemen, contohnya descendant selector (memilih semua elemen yang merupakan keturunan dari elemen yang di-specify), dan child selector (memilih semua elemen yang merupakan anak dari elemen yang di-specify)
5. **Universal selector** <br>
Menyeleksi seluruh elemen HTML pada halaman tersebut.

## Implementasi
1. Menginject CSS Bootstrap pada `base.html` dengan meletakkan tag <link> pada <head> in the `<head>`, dan tag `<script>` untuk bundle JSS sebelum closing `</body>`.
```
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
```
```
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
```
2. Meng-kustomisasi template `todolist.html`, `login.html`, `register.html`, `create_task.html` dengan menambahkan internal CSS styling dan memanfaatkan Bootstrap (menambahkan font, menyesuaikan ukuran, mengubah warna dan background, dst) 
3. Mengubah tabel menjadi bentuk `cards` menggunakan Bootstrap. Saya menggunakan divider dengan class row, lalu memanfaatkan grid system di mana di dalamnya menggunakan class `card`. 
4. Membuat keempat halaman responsive dengan memanfaatkan Bootstrap, serta menggunakan CSS media query untuk mendefinisikan breakpoint. Contohnya:
```
/* Pada screen sama dengan atau kurang dari 490px, sesuaikan font size sebagai berikut.
@media screen and (max-width: 490px) {
    h1 {
      font-size:7vw;
    }
    th {
      font-size:4vw;
    }
    td {
      font-size:3vw;
    }
  }
```
5. Melakukan pull, commit, push ke GitHub repository,

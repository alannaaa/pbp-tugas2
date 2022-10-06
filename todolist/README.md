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
Pada kasus tertentu, inline styling dapat mempengaruhi ukuran HTML file serta waktu download-nya. Selain itu, apabila terlalu banyak digunakan, struktur dari file HTML akan menjadi lebih berantakan.
**Internal Style** <br>
Berisikan properti Cascading Style Sheet (CSS) di dalam file HTML pada bagian head dimana properti CSS menempel di dalam file HTML tersebut. Penerapannya bersifat untuk satu halaman HTML. Internal Style menggunakan elemen ‘<style>’ pada bagian ‘<head>’. <br />
-- Kelebihan : Karena properti CSS berada pada file HTML yang sama, maka tidak perlu mengunggah banyak file. Selain itu, Inline Style dapat menggunakan class dan ID selector. <br />
-- Kekurangan : Menambahkan kode atau property ke dokumen HTML dapat meningkatkan ukuran halaman dan waktu loading web. Selain itu, karena Inline Style memiliki prioritas yang lebih tinggi, semua style yang berada pada Internal Style akan di-override oleh Inline Style. <br />
**External Style** <br />
Berisikan file CSS yang terpisah yang hanya berisi properti style dengan bantuan tag atribut. Properti CSS ditulis dalam file terpisah yang memiliki ekstensi .css yang kemudian di-link ke dokumen HTML menggunakan tag link. Untuk setiap elemen, style hanya dapat diatur sekali dan akan diterapkan di seluruh halaman web. Penerapannya bersifat untuk banyak halaman HTML. External Style menggunakan elemen ‘<link>’ untuk me-link¬ ke sebuah eksternal file CSS. <br />
-- Kelebihan : Karena properti CSS berada pada file yang terpisah, file HTML akan memiliki struktur yang lebih bersih dan berukuran lebih kecil. Selain itu, External Style dapat menggunakan file .css yang sama untuk beberapa halaman web. <br />
-- Kekurangan : Karena Inline dan Internal Style memiliki prioritas yang lebih tinggi, semua style yang berada pada External Style akan di-override oleh Inline dan Internal Style. Selain itu, mengunggah atau menautkan beberapa file CSS dapat meningkatkan waktu download web. Halaman web juga mungkin tidak di render dengan benar sampai CSS eksternal dimuat. <br />

## Tag HTML5
#### Jelaskan tag HTML5 yang kamu ketahui.
`<a>` : Mendefinisikan Hyperlink <br />
`<abbr>` : Mendefinisikan bentuk singkatan suatu kata atau frase yang lebih panjang <br />
`<address>` : Menspesifikasikan informasi kontak author <br />
`<area>` : Mendefinsikan sebuah spesifik area dalam image map <br />
`<article>` : Mendefinisikan sebuah artikel <br />
`<aside>` : Mendefinisikan beberapa konten yang berhubungan dengan konten halaman web <br />
`<audio>` : Memasukkan sound atau audio dalam dokumen HTML <br />
`<b>` : Menampilkan teks dalam style tebal atau bold <br />
`<base>` : Mendefiniskan URL dasar untuk semua URL relatif dalam dokumen <br />
`<bdi>` : Merepresentasikan teks yang terisolasi dengan tujuan text formatting <br />
`<bdo>` : Override teks direction <br />
`<blockquote>` : Merepresentasikan sebuah bagian yang diambil dari sumber lain <br />
`<body>` : Mendefinisikan bagian body suatu dokumen <br />
`<br>` : Menghasilkan sebuah line break <br />
`<button>` : Membuat sebuah tombol yang dapat di klik <br />
`<canvas>` : Mendefinisikan bagian atau wilayah dalam dokumen <br />
`<caption>` : Mendefinisikan caption atau judul suatu tabel <br />
`<cite>` : Menunjukkan kutipan atau referensi ke sumber lain <br />
`<code>` : Menspesifikasikan teks sebagai kode komputer <br />
`<col>` : Mendefinsikan nilai atribut untuk satu atau lebih kolom dalam tabel <br />
`<colgroup>` : Menentukan atribut untuk beberapa kolom dalam tabel <br />
`<data>` : Meletakkan konten yang memiliki terjemahan yang machine-readable <br />
`<datalist>` : Merepresentasikan set opsi yang telah ditentukan untuk suatu elemen input <br />
`<dd>` : Menspesifikasikan deskripsi pada dt dan dl <br />
`<del>` : Merepresentasikan teks yang telah dihapus dari dokumen <br />
`<details>` : Merepresentasikan widget dimana user dapat memperoleh informasi <br />
`<dfn>` : Menspesifikasikan sebuah definisi <br />
`<dialog>` : Mendefinsikan sebuah dialog box atau subwindow <br />
`<div>` : Menspesifikasikan sebuah bagian atau divisi dalam dokumen <br />
`<dl>` : Mendefinisikan sebuah list deskripsi <br />
`<dt>` : Mendefinsikan sebuah item pada list deskripsi <br />
`<em>` : Mendefinisikan teks yang ditekankan <br />
`<embed>` : Meletakkan aplikasi eksternal seperti konten media ke dalam dokumen HTML <br />
`<fieldset>` : Menentukan sebuah set mengenai form <br />
`<figcaption>` : Mendefinisikan sebuah keterangan atau legend untuk gambar <br />
`<figure>` : Merepresentasikan gambar yang diilustrasikan <br />
`<footer>` : Merepresentasikan footer sebuah dokumen atau bagian <br />
`<form>` : Mendefinisikan sebuah form HTML untuk input user <br />
`<head>` : Mendefinsikan bagian head dokumen seperti judul <br />
`<header>` : Merepresentasikan heade sebuah dokumen atau bagian <br />
`<hgroup>` : Mendefinsikan grup yang berisi header <br />
`<h1>` to `<h6>` : Mendefinisikan header HTML <br />
`<hr>` : Menghasilkan sebuah garis mendatar atau horizontal <br />
`<html>` : Mendefinisikan root dari suatu dokumen HTML <br />
`<i>` : Menampilkan teks dalam style miring atau italic <br />
`<iframe>` : Menampilkan sebuah url dalam Inline frame <br />
`<img>` : Merepresentasikan suatu gambar <br />
`<input>` : Mendefinisikan sebuah kontrol input <br />
`<ins>` : Mendefinisikan sebuah blok teks yang telah dimasukkan ke dalam dokumen <br />
`<kbd>` : Menentukan teks sebagai input keyboard <br />
`<keygen>` : Merepresentasikan kontrol untuk public-private key <br />
`<label>` : mendefinisikan sebuah label untuk kontrol input <br />
`<legend>` : Mendefinisikan caption untuk elemen fieldset <br />
`<li>` : Mendefiniskan sebuah list <br />
`<link>` : Mendefinisikan hubungan antara dokumen dan sumber eksternal <br />
`<main>` : Merepresentasikan bagian utama atau main dari program <br />
`<map>` : Mendefinisikan peta gambar dari sisi user <br />
`<mark>` : Merepresentasikan teks yang di-highlight untuk tujuan referensi <br />
`<menu>` : Merepresentasikan sebuah list commands <br />
`<menuitem>` : Mendefinsikan sebuah list commands yang dapat dilakukan oleh user <br />
`<meta>` : Menyediakan metadata terstruktur mengenai konten dalam dokumen <br />
`<meter>` : Merepresentasikan pengukuran skalaran dalam suatu range <br />
`<nav>` : Mendefinsikan sebuah bagian mengenai link navigasi <br />
`<noscript>` : Mendefinisikan konten alternative yang tidak mensupport frames <br />
`<object>` : Mendefinisikan sebuah object <br />
`<ol>` : Mendefinisikan list yang sudah terurut <br />
`<optgroup>` : Mendefinsikan sebuah kelompok yang berisi opsi yang saling berhubungan dalam section list <br />
`<option>` : Mendefinisikan opsi dalam selection list <br />
`<output>` : Merepresentasikan hasil dari suatu perhitungan <br />
`<p>` : Mendefinisikan paragraf <br />
`<param>` : Mendefinisikan sebuah parameter untuk suatu object <br />
`<picture>` : Mendefinisikan tempat untuk beberapa gambar <br />
`<pre>` : Mendefinisikan teks yang telah diformat <br />
`<progress>` : Merepresentasikan kemajuan penyelesaian suatu task <br />
`<q>` : Mendefinisikan kutipan Inline pendek <br />
`<rp>` : Menyediakan fall-bak parenthesis untuk browser yang tidak mensupport anotasi ruby <br />
`<rt>` : Mendefinisikan pengucapan suatu karakter yang direpresentasikan dalam anotasi ruby <br />
`<ruby>` : Mewakili anotasi ruby <br />
`<s>` : Mewakili konten yang sudah tidak akurat atau relevan <br />
`<samp>` : Menentukan teks sebagai output sampel dari suatu program <br />
`<script>` : Menempatkan skrip dalam dokumen untuk pemrosesan dari sisi klien <br />
`<section>` : Mendefinisikan bagian – bagian dari dokumen HTML <br />
`<select>` : Mendefinisikan daftar yang dipilih dalam suatu formulir <br />
`<small>` : Menampilkan teks dalam ukuran yang lebih kecil <br />
`<source>` : Mendefinisikan sumber media alternatif untuk elemen media <br />
`<span>` : Mendefinisikan bagian Inline Style <br />
`<strong>` : Menunjukkan teks yang ingin ditekankan <br />
`<tyle>` : Merepresentasikan informasi style ke dalam head dokumen <br />
`<sub>` : Mendefinisikan teks subscript <br />
`<summary>` : Mendefinisikan ringkasan untuk elemen details <br />
`<sup>` : Mendefinisikan teks superscript <br />
`<svg>` : Meletakkan konten SVG dalam dokumen HTML <br />
`<table>` : Mendefinisikan sebuah tabel <br />
`<tbody>` : Mengelompokkan sekumpulan baris yang mendefinisikan isi utama tabel <br />
`<td>` : Mendefinisikan cell dalam tabel <br />


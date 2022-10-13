# Tugas 6: Javascript dan AJAX
### 🔗 [See deployment](https://tugaspbp-alanna.herokuapp.com/todolist/)

### Asynchronous vs Synchronous Programming
* Pada **asynchronous programming**, requests dan responses dilayani menggunakan protokol I/O yang bersifat non-blocking. Artinya, saat mengeksekusi sesuatu, eksekusi proses lain tidak terblokir (tidak harus menunggu eksekusi sebelumnya selesai) dan bisa berjalan beriringan. Program asinkronus tidak dieksekusi secara hierarchical atau sequential. Request yang gagal tidak memengaruhi request lainnya dan program dapat berindah ke task selanjutnya walaupun yang sebelumnya belum sepenuhnya selesai.
* Pada **synchronous programming**, resource di-load satu per satu secara sekuensial. Apabila ada resource atau component yang secara hirarki lebih tinggi gagal dimuat, maka resource/component yang berada di bawahnya juga tidak akan respond. Request yang dibuat secara sinkronus akan beroperasi dengan protokol multi-threaded, di mana masing-masing thread meng-handle request secara terpisah. Masing-masing thread harus dimuat sampai selesai sebelum berpindah mengeksekusi yang lainnya. Pengeksekusian suatu event dalam thread akan memblokir thread lain (dan seuruh user interface) sepanjang prosesnya.

### Event-Driven Programming
Event-driven programming merupakan suatu paradigma pemrograman di mana flow dari program ditentukan oleh **events**, misalnya user actions seperti pergerakan kursor atau pemencetan sebuah button, atau penerimaan message dari program atau thread lain. Paradigma ini digunakan untuk mengsinkronuskan munculnya banyak event sekaligus menyederhanakan program. Komponen penting yang ada dalam event-driven programming adalah:
- Callback functions (disebut juga event handler) yang dipanggil setiap event yang berkaitan terjadi.
- Event loop yang mendengarkan saat event ter-trigger dan memanggil event-handler yang sesuai 
</br>
Salah satu contoh penerapan event-driven programming dalam tugas 6 adalah saat menekan button 'Add' dengan id `submit-btn` pada modal 'Add new task', akan dijalankan function yang mengambil value nama task serta deskripsi dari input user, kemudian membuat card task dan menampilkannya. 

### Penerapan asynchronous programming pada AJAX
Pada AJAX diterapkan asynchronous programming di mana request baru dari user yang tidak terlalu besar dapat diproses tanpa harus memuat ulang halaman. AJAX mengirimkan hanya informasi yang ter-update kepada server dan begitu juga sebaliknya. Informasi yang di-request diproses di _background_ kemudian response nya akan tercermin pada laman saat response tersebut diterima. Data dapat dikirimkan menggunakan method HTTP POST dan diterima menggunakan method HTTP GET.

### Implementasi checklist
AJAX GET:
1. Membuat function `show_json` dengan parameter request dan mengembalikan HttpResponse berupa data yang di-serialize dalam bentuk JSON.
2. Menambahkan `path('json/', show_json, name='show_json'),` pada `url_patterns` di `todolist/urls.py`
3. Mengambil data dari `/todolist/json/` menggunakan AJAX GET, kemudian membuat card untuk masing-masing data object lalu meng-appendnya ke container yang akan menampilkan seluruh cards. <br>

AJAX POST:
1. Membuat button 'Add Task' yang akan men-trigger modal dengan menghubungkannya ke modal menggunakan `data-bs-toggle = "modal"` dan memasang target-nya ke modal dengan id `createTaskModal` menggunakan `data-bs-target = "#createTaskModal`.
2. Membuat modal yang menerima input berupa nama dan deskripsi task baru (source code dari https://getbootstrap.com/docs/5.2/components/modal/). Ketika button 'Add' dengan id `submit_btn` diklik, action listener akan memanggil event handler nya yang akan mengirimkan response AJAX POST ke `/todolist/add` yang akan memanggil fungsi `create_json`. Fungsi ini akan mengembalikan JsonResponse berisi object Task yang baru dibuat serta pk-nya, kemudian dari response tersebut akan dibuat card baru berisi task yang baru ditambahkan dan di-append ke container berisi cards lainnya. 

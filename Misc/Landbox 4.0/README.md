# Haruka
inspired by the recent Top 7 Google's VRP 2023, now comes in Lua!
this was made using Lua's sandbox function, `pcall`!
why not give it a shot? maybe you can get something in Return!

# FLAG
INTECHFEST{congrats_you_just_did_blind_pwn_or_maybe_blind_sandbox_but_who_cares_its_all_about_RSA_after_all}

# Solution
Simplified:
Challenge ini intinya execute kode Lua lewat `load` dan `pcall`, yang dimana si kode yang akan diload ini sebelumnya diconcat dengan input dari user, yang dimana input ini unsafe dan menyebabkan Code Injection, yang akan kita escalate menjadi source code leak.

Complex:
Tipikal challenge dengan hint terdapat pada deskripsi, setiap kata yang diawali huruf kapital bisa jadi referensi yang cukup buat ngebantu ngesolve challengenya. Dan, yak challenge ini ngambil inspirasi dari #7 VRP by Google.
Kita bisa mulai coba dari masukkin single quote `'` ke inputnya dan bakal munculin error. Disini pesan dari errornya cukup penting, tapi kita juga harus paham juga basic dari bahasa Lua. Contohnya dalam Lua, if-statement itu contohnya kayak gini:
```lua
if a == b then
-- Something
else
-- Something
end
```

Error yang didapetin pas input `'`:
<image>

Disini, string "xxx" itu merupakan kode yang diload oleh fungsi `load` si Lua, sementara dikanan itu penyebab dari kenapa si `load` ini gabisa ngejalanin kode yang diberikan. Kalo kita liat, di error nya ada kata `then` yang berarti ini errornya berada pada baris yang punya if-statement, sementara disini kita juga udah tau kalo ada fungsi `check_flag`, kita bisa asumsi bahwa flow dari pengecekan flag setelah input kurang lebih seperti ini:
```
if check_flag(xxx) then
```

Tapi sekarang pertanyaannya, kenapa error ketika kita input `'`?
Well, disini kita bisa ambil contoh dari SQL Injection, ketika ada unescaped single quote dalam query, maka akan dianggap error karena belum single quotenya diclose. Jadi disini kode gabisa dijalanin di `load` karena ada unclosed single quote alias invalid Lua code. Yes, this challenge is similar to SQL Injection.

Kalo kita coba input seperti:
```
' or 1==1 then--
```
<image>

Kita bakal tetep dapetin error, tapi inget! Disini kita udah asumsiin kalo flow pengecekan flagnya memanggil sebuah fungsi, yaitu `check_flag`, jadi input yang seharusnya bakal work kurang lebih kayak gini:
```
') or 1==1 then--
```
<image>
Boom, injected!

Oke, kita udah punya code injection, sekarang apa?
Well, did you know that you can dump a function code in Lua! Yes, the full source code!

Selama debug informationnya ga distrip ketika compilation, fungsi apapun bisa kita dump menggunakan fungsi `debug.getinfo`.
Disini karena kode Lua nya dijalankan didalam si Lua itu sendiri, otomatis kode yang diberikan pada `load` juga harus berupa string. Disini karena kita udah tau ada fungsi `check_flag`, goal utama kita adalah nge-dump source dari fungsi tersebut.

Okay, but how?
Di Lua Environment dalam `pcall`, kita bisa return kapan aja, yang dimana return tersebut akan diberikan/disimpan ke hasil return si `pcall`, yang dimana disini secara sengaja output dari `pcall` sengaja aku print ke terminal/consolenya.

Payload:
```
') or 1==1 then return debug.getinfo(check_flag, 'S').source elseif 1==2 then--
```
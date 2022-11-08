kata_negasi = ["Tidak bisa melakukan transaksi", "Belum bisa transaksi",
               "jangan dipake aplikasinya", "tidak murah barangnya"]

kata_negasi_baru = []
for kata in kata_negasi:
    kata = kata.replace("Tidak bisa", "gagal")
    kata = kata.replace("Belum bisa", "gagal")
    kata = kata.replace("jangan dipake", "yang lain")
    kata = kata.replace("tidak murah", "mahal")
    kata_negasi_baru.append(kata)

print(kata_negasi_baru)

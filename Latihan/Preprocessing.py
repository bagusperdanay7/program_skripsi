# menginstall library yang dibutuhkan
# pip install PySastrawi
# pip install nltk
# import nltk
# nltk.download()

# mengimport library yang dibutuhkan
import string
from pydoc import doc
import re
import math
import pandas as pd
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# membaca file text
file = 'Benar2 mengecewakan.Respon sangat lama.pokok nya tidak d rekomended'

print('----------------------------------------------------')
print('|                  Dokumen Kotor                   |')
print('----------------------------------------------------')
print('Dokumen 1 : ', file)


# Tahapan Tokenisasi
# Menghilangkan angka
tokenisasi_doc1 = re.sub('[0-9]+', '', file)
print('----------------------------------------------------')
print('|                 Penghilangan Angka               |')
print('----------------------------------------------------')
print('Dokumen 1 : ', tokenisasi_doc1)

# Menghilangkan karakter khusus
tokenisasi_doc1 = re.sub('[^a-zA-Z0-9\n\.]', ' ', tokenisasi_doc1)

print('-----------------------------------------------------------')
print('|              Menghilangkan Karakter Khusus              |')
print('-----------------------------------------------------------')
print('Dokumen 1 : ', tokenisasi_doc1)


# Menghilangkan spasi
tokenisasi_doc1 = re.sub('\s+', ' ', tokenisasi_doc1)
print('-------------------------------------------------------')
print('|              Menghilangkan Spasi Lebih              |')
print('-------------------------------------------------------')
print('Dokumen 1 : ', tokenisasi_doc1, '\n')

# Case folding
tokenisasi_doc1 = tokenisasi_doc1.lower()
print('-------------------------------------------------------')
print('|                     Case Folding                    |')
print('-------------------------------------------------------')
print('Dokumen 1 : ', tokenisasi_doc1)

# Tahapan Stemming
# membuat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# proses stemmingpd
stemming_doc1 = stemmer.stem(tokenisasi_doc1)
print('-------------------------------------------------------')
print('|                       Stemming                      |')
print('-------------------------------------------------------')
print('Dokumen 4 : ', stemming_doc1, '\n')

# tokenisasi kalimat
tokenisasi_doc1 = stemming_doc1.split()
print('-------------------------------------------------------')
print('|                       Tokenisasi                      |')
print('-------------------------------------------------------')
print('Dokumen 1 : ', tokenisasi_doc1, '\n')


# Tahapan Filtering
# Stopword list dengan nltk
stopword_document = set(stopwords.words('indonesian'))

# stopword dokumen 1
clean_doc1 = []
for kata in tokenisasi_doc1:
    if kata not in stopword_document:
        clean_doc1.append(kata)

# menggabungkan hasil stopword semua dokumen
kumpulan_document = set(clean_doc1)
print('-------------------------------------------------------')
print('|                       Stopword                      |')
print('-------------------------------------------------------')
print(kumpulan_document, '\n')

# # Tahapan Pembobotan TF-IDF

# # inisialisasi variabel tf setiap dokumen
# jumlah_tf_doc1 = dict.fromkeys(kumpulan_document, 0)
# jumlah_tf_doc2 = dict.fromkeys(kumpulan_document, 0)
# jumlah_tf_doc3 = dict.fromkeys(kumpulan_document, 0)
# jumlah_tf_doc4 = dict.fromkeys(kumpulan_document, 0)

# # Perhitungan Jumlah TF
# for term in clean_doc1:
#     jumlah_tf_doc1[term] += 1

# for term in clean_doc2:
#     jumlah_tf_doc2[term] += 1

# for term in clean_doc3:
#     jumlah_tf_doc3[term] += 1

# for term in clean_doc4:
#     jumlah_tf_doc4[term] += 1

# # Perhitungan DF
# jumlah_df = dict.fromkeys(kumpulan_document, 0)
# for term in kumpulan_document:
#     term_unik = term
#     for term, nilai_df in jumlah_tf_doc1.items():
#         if term_unik == term:
#             jumlah_df[term] += nilai_df
#     for term, nilai_df in jumlah_tf_doc2.items():
#         if term_unik == term:
#             jumlah_df[term] += nilai_df
#     for term, nilai_df in jumlah_tf_doc3.items():
#         if term_unik == term:
#             jumlah_df[term] += nilai_df
#     for term, nilai_df in jumlah_tf_doc4.items():
#         if term_unik == term:
#             jumlah_df[term] += nilai_df

# # Perhitungan IDF
# nilai_idf = dict.fromkeys(kumpulan_document, 0)
# for key, value in jumlah_df.items():
#     frekuensi = int(value)
#     total_dokumen = 4
#     pembagian_dokumen_dan_frekuensi = (total_dokumen/frekuensi)
#     idf = math.log10(pembagian_dokumen_dan_frekuensi)
#     nilai_idf[key] = round(idf, 4)

# # membentuk tabel
# tabel_tf = pd.DataFrame(kumpulan_document, columns=['term'])
# tabel_tfidf = pd.DataFrame(kumpulan_document, columns=['term'])

# # Memasukkan hasil perhitungan TF, DF, dan IDF ke dalam tabel TF
# tabel_tf['doc1'] = tabel_tf['term'].map(jumlah_tf_doc1)
# tabel_tf['doc2'] = tabel_tf['term'].map(jumlah_tf_doc2)
# tabel_tf['doc3'] = tabel_tf['term'].map(jumlah_tf_doc3)
# tabel_tf['doc4'] = tabel_tf['term'].map(jumlah_tf_doc4)
# tabel_tf['df'] = tabel_tf['term'].map(jumlah_df)
# tabel_tf['idf'] = tabel_tf['term'].map(nilai_idf)

# print('----------------------------------------------------')
# print('|                   TABEL TF                       |')
# print('----------------------------------------------------')
# print(tabel_tf, '\n')

# # Perhitungan TF IDF
# tabel_tfidf['doc1'] = tabel_tf['doc1'] * tabel_tf['idf']
# tabel_tfidf['doc2'] = tabel_tf['doc2'] * tabel_tf['idf']
# tabel_tfidf['doc3'] = tabel_tf['doc3'] * tabel_tf['idf']
# tabel_tfidf['doc4'] = tabel_tf['doc4'] * tabel_tf['idf']

# print('----------------------------------------------------')
# print('|                  TABEL TF-IDF                    |')
# print('----------------------------------------------------')
# print(tabel_tfidf)

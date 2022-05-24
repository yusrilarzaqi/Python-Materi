# ++++3----10+++++
user=float(input("Masukan angka yang berisi \nKurang dari 3 \natau \nLebih dari 10"))
#++++3-----
isKurangDari=user<3
print("Kurang dari 3 :",isKurangDari)
# -----10+++++
isLebihDari=user>10
# ++++3----10++++
isCorrect=isKurangDari or isLebihDari
print("Angka yang anda Masukan :",isCorrect)

# ----3++++10----
user=float(input("Masukan angka yang berisi \nLebih dari 3 \ndan \nKurang dari 10"))
# ----3++++
isLebihDari=user>3
print("Lebih dari 3 :",isLebihDari)
# ++++10----
isKurangDari=user<10
# ----3++++10----
isCorrect=isKurangDari and isLebihDari
print("Angka yang anda Masukan :",isCorrect)


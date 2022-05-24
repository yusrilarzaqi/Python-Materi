# ++++0----5++++8----11++++
print("++++0----5++++8----11++++")
user=float(input("Masukan :"))
# +++0----
isKurang0=user<0
print("Kuang dari 0 :",isKurang0)
# ----5++++
isLebih5=user>5
print("Lebih dari 5 :",isLebih5)
# ++++8----
isKurang8=user<8
print("Kurang dari 8 :",isKurang8)
# ----11++++
isLebih11=user>11
print("Lebih dari 11 :",isLebih11)
# ++++0----5++++8----11++++
isCorrect=(isKurang0 or isLebih5)and(isKurang8 or isLebih11)
print("Angka yang anda masukan :",isCorrect)


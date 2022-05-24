## ----0++++5----8++++11----
print("----0++++5----8++++11----")
user=float(input("Inputkan :"))
# ----0++++
isLebih0=user>0
print("Lebih dari 0 :",isLebih0)
# ++++5----
isKurang5=user<5
print("Kurang dari 5 :",isKurang5)
# ----8++++
isLebih8=user>8
print("Lebih dari 8 :",isLebih8)
# ++++11----
isKurang11=user<11
print("Kurang dari 11 :",isKurang11)
## ----0++++5----8++++11----
isCorrect=(isLebih0 and isKurang5) or (isLebih8 and isKurang11)
print("Angka yang anda masukan :",isCorrect)


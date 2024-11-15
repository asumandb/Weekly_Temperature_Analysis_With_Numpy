import numpy as np

np.random.seed(42)
gun = 7
sicaklik = np.random.randint(0, 31, size = gun)

ort_sicaklik = np.mean(sicaklik)
min_sicaklik = np.min(sicaklik)
max_sicaklik = np.max(sicaklik)
sicaklik_std = np.std(sicaklik)

print("7 Günlük Hava Sıcaklığı Verisi:")
print(sicaklik)
print("\nHaftalık Analiz:")
print("Ortalama Sıcaklık:", ort_sicaklik)
print("Maksimum Sıcaklık:", max_sicaklik)
print("Minimum Sıcaklık:", min_sicaklik)

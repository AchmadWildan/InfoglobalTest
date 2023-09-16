import numpy as np


# Matriks A
A = np.array([
    [91, -91, -91, 91],
    [-106, -25, -126, -71],
    [-49, 118, -118, 49],
    [126, -106, 71, -25]
])

# Batasan nilai X (0 hingga 255)
nilai_minimal = 0
nilai_maksimal = 255

# Inisialisasi nilai minimum dan maksimum Y
nilai_minimum_Y = float('inf')
nilai_maksimum_Y = float('-inf')

# Perulangan untuk menghasilkan berbagai kombinasi nilai X
for x1 in range(nilai_minimal, nilai_maksimal + 1):
    for x2 in range(nilai_minimal, nilai_maksimal + 1):
        for x3 in range(nilai_minimal, nilai_maksimal + 1):
            for x4 in range(nilai_minimal, nilai_maksimal + 1):
                # Vektor X
                X = np.array([x1, x2, x3, x4])
                
                # Menghitung Y = X^T * A * X
                Y = np.dot(X, np.dot(A, X))
                
                # Memperbarui nilai minimum dan maksimum Y
                nilai_minimum_Y = min(nilai_minimum_Y, Y)
                nilai_maksimum_Y = max(nilai_maksimum_Y, Y)

# Hasil
print("Nilai Minimum Y:", nilai_minimum_Y)
print("Nilai Maksimum Y:", nilai_maksimum_Y)


# Nhập hai số nguyên từ người dùng
a = int(input("Nhập một số A: "))
b = int(input("Nhập một số B: "))

# Tăng hoặc giảm giá trị của a tùy điều kiện
if a < 5:
    a *= 0.5
elif a > 10:
    a -= 1

# Tính kết quả và in ra màn hình
ket_qua = a * b
print("Kết quả là", ket_qua)
print("Kết thúc chương trình")


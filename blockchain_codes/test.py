from hashlib import sha256

x = 12
y = 0  # y未知
while sha256(f'{x*y}'.encode()).hexdigest()[-1] != "00":
    y += 1
print(f'The solution is y = {y}')
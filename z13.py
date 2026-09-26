# Write a python program to Generate a random OTP
import random
otp = "".join(random.choices("0123456789", k=6))
print("Your 6-digit OTP is:", otp)

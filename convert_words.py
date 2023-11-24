def encode(text):
    encoded_text = ''
    for char in text:
        if char.islower():  # ตรวจสอบว่าตัวอักษรเป็นตัวพิมพ์เล็กหรือไม่
            encoded_text += chr(219 - ord(char))  # หาตัวอักษรที่อยู่ในตำแหน่งเดียวกันเมื่อกลับด้าน
        else:
            encoded_text += char
    return encoded_text

# รับค่าจากผู้ใช้
user_input = input("Enter 5 characters: ")

# ตรวจสอบว่ามีตัวอักษร 5 ตัวหรือไม่
if len(user_input) == 5:
    result = encode(user_input.lower())
    print("Encryption is", result)
else:
    print("Enter 5 characters: ")

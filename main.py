users_info = []

def is_int(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def is_phone(phone):
  return phone.startswith("+998")

while True:
  name = input("Ism kiriting: ")
  last_name = input("Familiya kiritin: ")
  str_age = input("Yoshini kiriting: ")

  while not is_int(str_age):
    str_age = input("Yoshni faqat raqamda kiriting: ")
  age = int(str_age)

  phone = input("Tel nomerini kiriting: ")
  while not is_phone(phone):
    phone = input("Tel nomerini kodi +998 bolishi kerak!")

  email = input("Emailini kiriting: ")
  address = input("Adresini kiriting: ")

  user_id = len(users_info) + 1

  users_info.append({
    "id": user_id,
    "name": name,
    "last_name": last_name,
    "age": age,
    "phone": phone,
    "email": email,
    "address": address
  })

  with open("users_info.txt", "w") as file:
    for user in users_info:
      file.write(f"{user}\n")
  yes_no = input("Yana user kiritasizmi? yes/no: ")
  if yes_no.lower() == "no":
    break

print("Dastur tohtadi!")
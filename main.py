import json
import hashlib

def save_data(file: str, data: dict | list) -> None:
  with open(file, "w", encoding="utf-8") as file:
    new_data = json.dumps(data)
    file.write(new_data)

def load_data(file_path: str) -> dict | list:
  with open(file_path) as file:
    content = file.read()
    data = json.loads(content)
    return data

def encrypt_password(password: str) -> str:
  return hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest()

def save_user(data: list, login: str, password: str) -> None:
  data.append({
    "login": login,
    "password": encrypt_password(password)
  })
  
  save_data("data.json", data)

def modify_password(data: dict | list, login: str, new_password) -> None:
  for user in data:
    if user["login"] == login:
      user["password"] = encrypt_password(new_password)
      break
  
  save_data("data.json", data)

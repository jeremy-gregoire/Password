from tkinter import *
import json
import hashlib

def from_json(file_path: str) -> dict | list:
  """
  Gets the data from a file json file.

  #### Parameters
   - file_name : str > A string that corresponding to the name of the file.
  
  #### Returns
  dict | list > A dictionnary or a list which contains the data inside.
  """
  with open(file_path) as file:
    content = file.read()
    data = json.loads(content)
    return data

def to_json(file_path: str, data: dict | list) -> None:
  """
  Saves data into a json file.

  #### Parameters
   - file_name : str > A string that corresponding to the name of the file.
   - data : dict | list > A data structure that corresponding to the data that would be registered inside the file.
  """

  with open(file_path, "w", encoding="utf-8") as file_path:
    new_data = json.dumps(data)
    file_path.write(new_data)

def encrypt_password(password: str) -> str:
  return hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest()

def save_user(data: list, login: str, password: str) -> None:
  data.append({ "login": login, "password": encrypt_password(password) })
  to_json("data.json", data)

def modify_password(data: dict | list, login: str, new_password) -> None:
  for user in data:
    if user["login"] == login:
      user["password"] = encrypt_password(new_password)
      break
  
  to_json("data.json", data)

def exist_login(data: dict | list, login: str) -> bool:
  for user in data:
    if login == user["login"]:
      return True

  return False

window = Tk()
window.title("Password Generator")
window.geometry("480x480")
window.resizable(False, False)

paned_window = PanedWindow(window, orient="vertical")
paned_window.pack(side="top", pady=50, padx=75)

login_label = Label(paned_window, text="Login")
paned_window.add(login_label)

login_entry_value = StringVar()
login_entry = Entry(paned_window, textvariable=login_entry_value, width=30)
paned_window.add(login_entry)

password_label = Label(paned_window, text="Password")
paned_window.add(password_label)

password_entry_value = StringVar()
new_password_entry = Entry(paned_window, textvariable=password_entry_value, width=33)
paned_window.add(new_password_entry)

def register() -> None:
  data = from_json("data.json")
  login = login_entry.get()
  password = new_password_entry.get()

  if login != "" and password != "" and not exist_login(data, login):
    save_user(data, login, password)
  else:
    error_message = Label(paned_window, text="The login or password is empty!", foreground="red")
    paned_window.add(error_message)

register_btn = Button(paned_window, text="Register", command=register)
paned_window.add(register_btn)

def reset_password_window() -> None:
  reset_window = Toplevel()
  reset_window.title("Reset your password")
  reset_window.resizable(False, False)

  paned_window = PanedWindow(reset_window, orient="vertical")
  paned_window.pack(side="top", pady=50, padx=75)

  login = Label(paned_window, text="Login")
  paned_window.add(login)

  login_entry_value = StringVar()
  login_entry = Entry(paned_window, textvariable=login_entry_value, width=30)
  paned_window.add(login_entry)

  new_password = Label(paned_window, text="New password")
  paned_window.add(new_password)

  new_password_entry_value = StringVar()
  new_password_entry = Entry(paned_window, textvariable=new_password_entry_value, width=30)
  paned_window.add(new_password_entry)

  def modify() -> None:
    data = from_json("data.json")
    login = login_entry.get()
    new_password = new_password_entry.get()

    if login != "" and new_password != "" and exist_login(data, login):
      modify_password(data, login, new_password)
      reset_window.destroy()
    else:
      error_message = Label(paned_window, text="The username doesn't exist!", foreground="red")
      paned_window.add(error_message)


  modify_btn = Button(paned_window, text="Modify your password", command=modify)
  paned_window.add(modify_btn)

  paned_window.pack()

reset_password_btn = Button(paned_window, text="Reset password", command=reset_password_window)
paned_window.add(reset_password_btn)

paned_window.pack()
window.mainloop()

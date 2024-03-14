import hashlib, random, string, re
from tkinter import *
from json_utility import JSONUtility

class App(Tk):
  def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
    super().__init__(screenName, baseName, className, useTk, sync, use)

    self.data = JSONUtility.from_json("data.json")
    self.is_pw_auto_generate = False
    self.visibility = False
    self.pi_visibility_on = PhotoImage(file=f"images/png/visibility_on.png")
    self.pi_visibility_off = PhotoImage(file=f"images/png/visibility_off.png")

    # Basic to the application
    self.title("Mot de passe")
    self.resizable(False, False)

    self.self_paned = PanedWindow(self, orient="vertical")
    self.self_paned.pack(side="top", pady=75, padx=75, fill="both")

    # Login section
    lbl_login = Label(master=self, text="Nom d'utilisateur")
    self.self_paned.add(lbl_login)

    entry_login = Entry(master=self)
    self.self_paned.add(entry_login)

    # Password section
    password_section = Frame(self)
    password_section.pack(fill='both', expand=True)
    password_section.columnconfigure(2, weight=1)
    password_section.rowconfigure(0, weight=1)

    lbl_password = Label(master=self, text="Mot de passe")
    self.self_paned.add(lbl_password)

    entry_password_value = StringVar()
    entry_password_value.trace_add("write", callback=self.on_entry_pw_changed)
    entry_password = Entry(master=password_section, textvariable=entry_password_value, show="*")
    entry_password.grid(row=0, column=0, sticky="WE", padx=(0, 5))

    btn_show_password = Button(master=password_section, image=self.pi_visibility_on, command=lambda: self.on_visibility_btn_click(btn_show_password, entry_password))
    btn_show_password.grid(row=0, column=1, sticky="WE", padx=(0, 5))
    
    btn_clear_password = Button(master=password_section, text="X", command=lambda: entry_password_value.set(""))
    btn_clear_password.grid(row=0, column=2, sticky="WE")

    self.self_paned.add(password_section)

    # Generate Random Password button
    lbl_nb_character_random = Label(master=self, text="Nombre de caractère")
    self.self_paned.add(lbl_nb_character_random)

    sb_nb_random_character = Spinbox(master=self, from_=8, to=255)
    self.self_paned.add(sb_nb_random_character)
    
    btn_random_generate_password = Button(master=self, text="Générer un mot de passe aléatoire", command=lambda: self.on_generate_rand_pw_btn_clicked(sb_nb_random_character.get(), entry_password_value))
    self.self_paned.add(btn_random_generate_password)

    # Register account button
    btn_register = Button(master=self, text="Enregistrer un compte", command=lambda: self.on_register_btn_clicked(entry_login.get(), entry_password.get()))
    self.self_paned.add(btn_register)

    # Reset password button
    btn_reset = Button(master=self, text="Mot de passe oublié", command=self.show_app_reset_password)
    self.self_paned.add(btn_reset)

    # Connexion button
    btn_connexion = Button(master=self, text="Se connecter", state="disabled")
    self.self_paned.add(btn_connexion)

    # Error message
    self.lbl_error_message = Label(master=self, text="", justify="left", foreground="red")

    self.self_paned.pack()
    self.mainloop()
  
  def show_app_connexion(self, user: dict) -> None:
    login = user["login"]

    sub_window = Toplevel()
    sub_window.title("Connexion")
    sub_window.resizable(False, False)

    lbl_welcome = Label(master=sub_window, text=f"Bienvenue {login}! Tu a été connecter avec succès !")
    lbl_welcome.pack()

  def show_app_reset_password(self) -> None:
    sub_window = Toplevel()
    sub_window.title("Réinitialisé le mot de passe")    # if self.is_pw_auto_generate:
    #   self.save_user(self.data, login, password)
    # elif len(password) >= 8 and bool(re.search(r"[a-zA-Z0-9]", password)):
    #   self.save_user(self.data, login, password)
    # else:
    #   pass
    sub_window.resizable(False, False)

    sub_paned_window = PanedWindow(master=sub_window, orient="vertical")
    sub_paned_window.pack(side="top", pady=50, padx=75)

    # Login section
    lbl_login = Label(master=sub_paned_window, text="Nom d'utilisateur")
    sub_paned_window.add(lbl_login)    # if self.is_pw_auto_generate:
    #   self.save_user(self.data, login, password)
    # elif len(password) >= 8 and bool(re.search(r"[a-zA-Z0-9]", password)):
    #   self.save_user(self.data, login, password)
    # else:
    #   pass
    entry_login = Entry(master=sub_paned_window)
    sub_paned_window.add(entry_login)

    # New password section
    lbl_new_password = Label(master=sub_paned_window, text="Nouveau mot de passe")
    sub_paned_window.add(lbl_new_password)

    entry_new_password = Entry(master=sub_paned_window)
    sub_paned_window.add(entry_new_password)

    # Modify password section
    btn_modify = Button(master=sub_paned_window, text="Changer le mot de passe", command=lambda: self.modify_password_user(self.data, entry_login.get(), entry_new_password.get()))
    sub_paned_window.add(btn_modify)

  def hash_password(self, password: str) -> str:
    """
    Method to hash a password using SHA-256 algorithm.

    #### Parameters:  def on_visibility_btn_click(self, btn_visibility: Button, entry_password: Entry) -> None:
    if self.visibility:
      btn_visibility.configure(image=self.pi_visibility_on)
      entry_password.configure(show="*")
      self.visibility = False
    else:
      btn_visibility.configure(image=self.pi_visibility_off)
      entry_password.configure(show="")
      self.visibility = True
  
  def get_random_password(self, nb_character: int = 8) -> str:
    return "".join(random.sampl    # if self.is_pw_auto_generate:
    #   self.save_user(self.data, login, password)
    # elif len(password) >= 8 and bool(re.search(r"[a-zA-Z0-9]", password)):
    #   self.save_user(self.data, login, password)
    # else:
    #   pass
    str : The hashed password in hexadecimal format.
    """
    # Convert the password string to bytes using UTF-8 encoding,
    # then hash it using SHA-256 algorithm, and finally return
    # the hexadecimal representation of the hashed value.
    return hashlib.sha256(bytes(password, encoding="utf-8")).hexdigest()

  def save_user(self, data: list, login: str, password: str) -> None:
    if login == "" or password == "":
      return
    
    data.append({ "login": login, "password": self.hash_password(password) })
    JSONUtility.to_json("data.json", data)

  def modify_password_user(self, data: list, login: str, new_password: str) -> None:
    for user in data:
      if user["login"] == login:
        user["password"] = self.hash_password(new_password)
        JSONUtility.to_json("data.json", data)
        break

  def exist_user(self, data: list, login: str) -> bool:
    for user in data:
      if login == user["login"]:
        return True
    
    return False

  def on_register_btn_clicked(self, login: str, password: str) -> None:
    password_can_pass = len(password) >= 8 and any(c in string.ascii_lowercase for c in password) and any(c in string.ascii_uppercase for c in password) and any(c in string.punctuation for c in password)

    if self.is_pw_auto_generate == True or password_can_pass:
      self.save_user(self.data, login, password)
    else:
      self.lbl_error_message.configure(text="\n".join([
        "Le mot de passe doit correspondre aux critères si dessous:",
        " - Il doit contenir au moins 8 caractères.",
        " - Il doit contenir au moins une lettre majuscule.",
        " - Il doit contenir au moins une lettre minuscule.",
        " - Il doit contenir au moins un chiffre.",
        " - Il doit contenir au moins un caractère spéciaux."
      ]))
      self.self_paned.add(self.lbl_error_message)

  def on_entry_pw_changed(self, var, index, mode):
    if self.is_pw_auto_generate:
      self.is_pw_auto_generate = False

  def on_generate_rand_pw_btn_clicked(self, nb_character: str, entry_password_value: StringVar) -> None:
    entry_password_value.set(self.get_random_password(int(nb_character)))
    self.is_pw_auto_generate = True
  
  def on_visibility_btn_click(self, btn_visibility: Button, entry_password: Entry) -> None:
    if self.visibility:
      btn_visibility.configure(image=self.pi_visibility_on)
      entry_password.configure(show="*")
      self.visibility = False
    else:
      btn_visibility.configure(image=self.pi_visibility_off)
      entry_password.configure(show="")
      self.visibility = True
  
  def get_random_password(self, nb_character: int = 8) -> str:
    return "".join(random.sample(string.ascii_letters + string.digits + string.punctuation, nb_character))

if __name__ == "__main__":
  App()
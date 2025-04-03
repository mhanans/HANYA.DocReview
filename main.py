from auth import login_user
from database import User, Session, engine

# Menambahkan pengguna untuk pengujian (opsional)
with Session(engine) as session:
    new_user = User(id="1", username="admin", password="hashedpassword123")
    session.add(new_user)
    session.commit()

# Menguji fungsi login
user_id = login_user("admin", "password123")
if user_id:
    print(f"Login berhasil, ID pengguna: {user_id}")
else:
    print("Login gagal")
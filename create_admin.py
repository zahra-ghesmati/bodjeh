# create_admin.py  (در ریشه پروژه reports)

from app.database import SessionLocal
from app.models.user_models import User, Role
from app.services.auth_service import get_password_hash

def main():
    db = SessionLocal()
    try:
        admin_role = db.query(Role).filter(Role.name == 'ADMINISTRATOR').first()
        if not admin_role:
            print("نقش ADMINISTRATOR پیدا نشد. ابتدا نقش‌ها را در جدول roles درج کنید.")
            return

        # چک نکنیم ادمین قبلی وجود دارد یا نه
        existing = db.query(User).filter(User.username == "admin").first()
        if existing:
            print("کاربری با نام admin قبلاً وجود دارد.")
            return

        admin_user = User(
            username="admin",
            hashed_password=get_password_hash("123456"),  # رمز عبور
            role_id=admin_role.id,
            full_name="مدیر سیستم"
        )
        db.add(admin_user)
        db.commit()
        print("ادمین با موفقیت ساخته شد.")
    finally:
        db.close()

if __name__ == "__main__":
    main()

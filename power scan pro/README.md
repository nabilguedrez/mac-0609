# PowerScan Pro

نسخة احترافية من التطبيق مع اسم وأيقونة مخصصة.

## 🚀 البناء التلقائي (GitHub Releases)
- عند كل push، GitHub يبني APK جديد ويضيفه في قسم Releases.

### التحميل
1. افتح المستودع على GitHub.
2. اذهب إلى تبويب **Releases**.
3. حمل آخر ملف APK.

---

## ⚠️ ملاحظة مهمة
- في هذا المشروع، المجلد اسمه `GITHUB_WORKFLOWS/` حتى لا يختفي عند الرفع.
- بعد رفع المشروع على GitHub:
  1. افتح المستودع.
  2. غير اسم المجلد من `GITHUB_WORKFLOWS` إلى `.github/workflows`.
  3. بعد ذلك سيظهر الـ **Actions** ويعمل تلقائي.

---

## 📌 البناء المحلي (اختياري)

### على ويندوز (EXE)
```bash
pip install kivy pyinstaller
pyinstaller --onefile main.py
```

### على لينكس (APK)
```bash
pip install buildozer
buildozer init
buildozer -v android debug
```

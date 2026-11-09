TAYYAB MUNEER - DJANGO PORTFOLIO
================================

WINDOWS SETUP (PowerShell)
1. Extract this ZIP file.
2. Open PowerShell in the extracted tayyab_portfolio folder.
3. Run:

   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python manage.py makemigrations portfolio
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

4. Open http://127.0.0.1:8000/
5. Admin: http://127.0.0.1:8000/admin/

If PowerShell blocks activation, run:
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Then activate the venv again.

IMPORTANT PERSONALIZE BEFORE PUBLISHING
- In templates/portfolio/home.html replace tayyab@example.com with your real public business email.
- Add your real Fiverr profile URL and GitHub / LinkedIn links if desired.
- Replace project descriptions with accurate details and add genuine screenshots/demo links.
- Only describe features that are actually implemented and tested.
- The lung image classifier is an educational prototype, not a medical diagnostic product.

CONTACT FORM
Submitted messages are saved in the Django database and visible in Django admin.
For a public production deployment, set DEBUG=False, use a strong environment-based SECRET_KEY,
configure ALLOWED_HOSTS, HTTPS, secure cookies, and a production database / email service.
Do not deploy with the development SECRET_KEY or DEBUG=True.

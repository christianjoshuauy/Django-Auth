# Django and React Authentication Project

Just a simple user authentication with user types Student and Teacher. This project uses Django as its server and MySQL as its backend and ReactTS as its client/frontend. Authentication includes password hashing, and sessions via JWT tokens.

## Installation & Setup
### Backend
1. Modify settings.py DATABASES to your database settings
2. Change to server directory and to the project directory
   ```
   cd server/authproject
   ```
3. Install dependencies
   ```
   pip install -r requirements.txt
   ```
4. Run migrations
   ```
    python manage.py migrate
    ```
5. Run server
    ```
    python manage.py runserver
    ```
### Frontend
1. Change to client directory
    ```
    cd client
    ```
2. Install dependencies
    ```
    npm install
    ```
3. Run server
    ```
    npm run dev
    ```

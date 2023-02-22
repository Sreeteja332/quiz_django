from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
import psycopg2

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        conn = psycopg2.connect(
            host="hostname",
            database="database_name",
            user="user_name",
            password="password"
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM quiz WHERE user_id=%s AND password=%s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            try:
                django_user = User.objects.get(username=username)
                return django_user
            except User.DoesNotExist:
                return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

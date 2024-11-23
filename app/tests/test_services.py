import unittest
from app.services import create_user, get_user, get_all_users, update_user, delete_user, users_db

class TestServices(unittest.TestCase):

    def setUp(self):
        # Limpa o banco de dados antes de cada teste
        users_db.clear()

    def test_create_user(self):
        user = create_user(1, "user1", "password1", "User One")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.name, "User One")

    def test_create_user_duplicate_username(self):
        create_user(1, "user1", "password1", "User One")
        with self.assertRaises(ValueError):
            create_user(2, "user1", "password2", "User Two")

    def test_get_user(self):
        create_user(1, "user1", "password1", "User One")
        user = get_user(1)
        self.assertIsNotNone(user)

    def test_get_all_users(self):
        create_user(1, "user1", "password1", "User One")
        create_user(2, "user2", "password2", "User Two")
        users = get_all_users()
        self.assertEqual(len(users), 2)

    def test_update_user(self):
        create_user(1, "user1", "password1", "User One")
        user = update_user(1, "user1_updated", "password_updated", "User Updated")
        self.assertEqual(user.username, "user1_updated")

    def test_delete_user(self):
        create_user(1, "user1", "password1", "User One")
        delete_user(1)
        self.assertIsNone(get_user(1))

    def test_delete_nonexistent_user(self):
        with self.assertRaises(ValueError):
            delete_user(1)

if __name__ == "__main__":
    unittest.main()

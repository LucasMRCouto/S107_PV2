import unittest
from app.services import create_user, get_user, get_all_users, update_user, delete_user, users_db

class TestServices(unittest.TestCase):

    def setUp(self):
        # Limpa o banco de dados antes de cada teste
        users_db.clear()

    # teste de criação de user 
    def test_create_user(self):
        user = create_user(1, "user1", "password1", "User One")
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.name, "User One")

    # teste de criação de user repetido 
    def test_create_user_duplicate_username(self):
        create_user(1, "user1", "password1", "User One")
        with self.assertRaises(ValueError):
            create_user(2, "user1", "password2", "User Two")

    # teste de get 
    def test_get_user(self):
        create_user(1, "user1", "password1", "User One")
        user = get_user(1)
        self.assertIsNotNone(user)

    # teste de get all
    def test_get_all_users(self):
        create_user(1, "user1", "password1", "User One")
        create_user(2, "user2", "password2", "User Two")
        users = get_all_users()
        self.assertEqual(len(users), 2)

    # teste de update 
    def test_update_user(self):
        create_user(1, "user1", "password1", "User One")
        user = update_user(1, "user1_updated", "password_updated", "User Updated")
        self.assertEqual(user.username, "user1_updated")


    # teste de delete 
    def test_delete_user(self):
        create_user(1, "user1", "password1", "User One")
        delete_user(1)
        self.assertIsNone(get_user(1))


    # teste de delete em um usuario inxistente 
    def test_delete_nonexistent_user(self):
        with self.assertRaises(ValueError):
            delete_user(1)

# teste para obter todos os usuários quando do bd está vazio 
    def test_get_all_users_empty_db(self):
        users = get_all_users()
        self.assertEqual(users, [])

    # teste de update em usuario inexistente
    def test_update_user_not_found(self):
        create_user(1, "user1", "password1", "User One")
        with self.assertRaises(ValueError):
            update_user(0, "user0", "password0", "anotherUser")

    def test_delete_all_users(self):
        create_user(1, "user1", "password1", "User One")
        create_user(2, "user2", "password2", "User Two")
        create_user(3, "user3", "password3", "User Three")
        create_user(4, "user4", "password4", "User Four")
        create_user(5, "user5", "password5", "User Five")
        delete_user(1)
        delete_user(3)
        delete_user(5)
        self.assertNotIn(1, users_db)
        self.assertIn(2, users_db)
        self.assertNotIn(3, users_db)
        self.assertIn(4, users_db)
        self.assertNotIn(5, users_db)
        
 # Teste para excluir bd vazio
    def test_delete_user_empty_db(self):
        with self.assertRaises(ValueError):
            delete_user(1)

if __name__ == "__main__":
    unittest.main()

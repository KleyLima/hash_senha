# -*- coding: utf-8 -*-

from source.hash_senha import HashSenha
import unittest


class TesteHashSenha(unittest.TestCase):
    def test_hash_md5(self):
        self.assertEqual(HashSenha('Teste').hash_md5(), HashSenha('Teste').hash_md5())  # Uma strig gera o mesmo hash
        self.assertTrue(HashSenha('').hash_md5())  # String vazia também gera hash
        self.assertEqual(len(HashSenha('small').hash_md5()), len(HashSenha('UmaGrandeSenha123456').hash_md5()))  # Sempre 32 caracteres

    def test_hash_sha256(self):
        self.assertEqual(HashSenha('Teste').hash_sha256(), HashSenha('Teste').hash_sha256()) # Uma string gerá mesmo hash
        self.assertTrue(HashSenha('').hash_sha256())  # String vazia também gera um hash
        self.assertEqual(len(HashSenha('small').hash_sha256()), len(HashSenha('UmaGrandeSenha123').hash_sha256()))  # Sempre 64 caracteres


if __name__ == '__main__':
    unittest.main()


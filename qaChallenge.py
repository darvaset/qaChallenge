import unittest
from kambista_register import KambistaRegister

# Obtener todos los tests
kambista_register_tests = unittest.TestLoader().loadTestsFromTestCase(KambistaRegister)
# gmail_tests = unittest.TestLoader().loadTestsFromTestCase(GmailTests)

# Definir un Test Suite

qa_challenge = unittest.TestSuite([kambista_register_tests])

# Ejecutar la Suite
unittest.TextTestRunner(verbosity=2).run(qa_challenge)

import unittest
from book_recommender import generateRecommendations, hasMinimumHistory

class TestBookRecommender(unittest.TestCase):
    
    # Unit 1: generateRecommendations()
    def test_valid_history_and_preferences(self):
        history = ["Dune", "Neuromancer", "Foundation"]
        prefs = {"genre": "sci-fi"}
        self.assertTrue(len(generateRecommendations(history, prefs)) > 0)

    def test_invalid_null_history(self):
        with self.assertRaises(TypeError):
            generateRecommendations(None, {"genre": "sci-fi"})

    def test_invalid_preferences_type(self):
        with self.assertRaises(TypeError):
            generateRecommendations(["Dune"], "sci-fi")

    def test_boundary_exact_min_history(self):
        history = ["Dune", "Neuromancer", "Foundation"]
        self.assertTrue(len(generateRecommendations(history, {"genre": "sci-fi"})) > 0)

    def test_edge_empty_history(self):
        self.assertEqual(generateRecommendations([], {"genre": "sci-fi"}), [])

    def test_edge_no_matching_preferences(self):
        history = ["Dune", "Neuromancer", "Foundation"]
        self.assertEqual(generateRecommendations(history, {"genre": "nonexistent"}), [])

    # Unit 2: hasMinimumHistory()
    def test_min_history_correct(self):
        history = ["Dune", "Neuromancer", "Foundation"]
        self.assertTrue(hasMinimumHistory(history, 3))

    def test_min_history_incorrect_type(self):
        with self.assertRaises(TypeError):
            hasMinimumHistory("not-a-list", 3)

    def test_min_history_boundary_true(self):
        history = ["Dune", "Neuromancer", "Foundation"]
        self.assertTrue(hasMinimumHistory(history, 3))

    def test_min_history_boundary_false(self):
        history = ["Dune", "Neuromancer"]
        self.assertFalse(hasMinimumHistory(history, 3))

    def test_min_history_edge_empty(self):
        self.assertTrue(hasMinimumHistory([], 0))

if __name__ == '__main__':
    unittest.main()
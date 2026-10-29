import unittest
from book_recommender import generateRecommendations, hasMinimumHistory

class TestBookRecommender(unittest.TestCase):

    def test_edge_empty_history(self):
        # When history is empty, the recommender returns the default/fallback book list
        self.assertEqual(
            generateRecommendations([], {"genre": "sci-fi"}), 
            ['Dune', 'Neuromancer', 'Foundation', 'Snow Crash']
        )

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

if __name__ == '__main__':
    unittest.main()

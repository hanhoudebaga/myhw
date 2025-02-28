import unittest
import requests
from github_api import get_user_repos, get_repo_commits, get_repo_commit_counts

class TestGitHubAPI(unittest.TestCase):
    def test_get_user_repos(self):
        # Test valid user returns list
        repos = get_user_repos("hanhoudebaga")
        self.assertIsInstance(repos, list)
        
        # Test first repo has expected structure
        self.assertEqual(repos[0]["name"], "Algorithms-and-Data-Structures-in-Java")

    def test_get_repo_commits(self):
        # Test known repository
        commit_count = get_repo_commits("hanhoudebaga", "myhw")
        self.assertIsInstance(commit_count, int)
        self.assertGreaterEqual(commit_count, 1)

    def test_get_repo_commit_counts(self):
        # Test valid user response format
        results = get_repo_commit_counts("hanhoudebaga")
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        
        # Test string format and commit count validity
        for entry in results:
            self.assertTrue(entry.startswith("Repo: "))
            parts = entry.split("Number of commits: ")
            self.assertEqual(len(parts), 2)
            commit_count = int(parts[1])
            self.assertIsInstance(commit_count, int)
            self.assertGreaterEqual(commit_count, 1)

    def test_error_handling(self):
        # Test invalid user handling
        with self.assertRaises(requests.exceptions.HTTPError):
            get_user_repos("hanhoudebaga_asdwasdwasdw")
            
        # Test error message format
        result = get_repo_commit_counts("hanhoudebaga_asdwasdwasdw")
        self.assertTrue(result.startswith("Error:"))

if __name__ == '__main__':
    unittest.main()
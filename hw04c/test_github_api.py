import unittest
from unittest.mock import patch, Mock
import requests
from github_api import get_user_repos, get_repo_commits, get_repo_commit_counts

class TestGitHubAPI(unittest.TestCase):
    @patch('github_api.requests.get')
    def test_get_user_repos(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"name": "myhw"}]
        mock_get.return_value = mock_response

        repos = get_user_repos("hanhoudebaga")
        self.assertEqual(repos[0]["name"], "myhw")

    @patch('github_api.requests.get')
    def test_get_repo_commits(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = [{"sha": "1"}, {"sha": "2"}]
        mock_get.return_value = mock_response

        self.assertEqual(get_repo_commits("hanhoudebaga", "myhw"), 2)

    @patch('github_api.requests.get')
    def test_get_repo_commit_counts(self, mock_get):
        user_mock = Mock()
        user_mock.json.return_value = [{"name": "myhw"}]
        
        commit_mock = Mock()
        commit_mock.json.return_value = [{"sha": "1"}]
        
        mock_get.side_effect = [user_mock, commit_mock]

        results = get_repo_commit_counts("hanhoudebaga")
        self.assertEqual(results[0], "Repo: myhw Number of commits: 1")

    @patch('github_api.requests.get')
    def test_error_handling(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
            "404 Client Error: Not Found for url: https://api.github.com/users/hanhoudebaga_invalid/repos"
        )
        mock_get.return_value = mock_response
        
        result = get_repo_commit_counts("hanhoudebaga_invalid")
        self.assertTrue(result.startswith("Error: "))
        self.assertIn("404 Client Error", result)

if __name__ == '__main__':
    unittest.main()

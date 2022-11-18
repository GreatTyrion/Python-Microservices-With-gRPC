# recommendations/test_recommendations.py
import unittest

from recommendations import RecommendationService
from recommendations_pb2 import BookCategory, RecommendationRequest


# class TestRecommendations(unittest.TestCase):
#     def test_recommendations(self):
#         service = RecommendationService()
#         request = RecommendationRequest(
#             user_id=1, category=BookCategory.MYSTERY, max_results=1
#         )
#         response = service.Recommend(request, None)
#         assert len(response.recommendations) == 1

def test_recommendations():
    service = RecommendationService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MYSTERY, max_results=1
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 1


if __name__ == "__main__":
    test_recommendations()

from fastapi.testclient import TestClient
from app.endpoints.mutant import router, check_dna


client = TestClient(router)


def test_check_mutant_dna():
    assert check_dna(["AAAAEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "78AAAA"]) is True


def test_check_human_dna():
    assert check_dna(["AAAAEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) is False

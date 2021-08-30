from fastapi.testclient import TestClient
from app.endpoints.mutant import check_dna, check_horizontal_genes, check_vertical_genes, check_diagonal_genes, \
    check_reversed_diagonal_genes, router, parse_list


client = TestClient(router)


def test_check_horizontal_genes():
    assert check_horizontal_genes(["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == 0
    assert check_horizontal_genes(["ABCDEF", "GHIJKL", "1BOPQR", "1BUVXZ", "1B3456", "1B9ABC"]) == 0
    assert check_horizontal_genes(["AAAAEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == 1
    assert check_horizontal_genes(["AAAAEF", "GHAAAA", "MNAAAA", "STUVXZ", "123456", "789ABC"]) == 3
    assert check_horizontal_genes(["AAAAEF", "GHAAAA", "MNAAAA", "STUVXZ", "123456", "78AAAA"]) == 4
    assert check_horizontal_genes(["AAAAEF", "GHAAAA", "MNAAAA", "STUVXZ", "12AAAA", "78AAAA"]) == 5
    assert check_horizontal_genes(["AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA"]) == 6


def test_check_vertical_genes():
    assert check_vertical_genes(["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == 0
    assert check_vertical_genes(["ABCDEF", "AHIJKL", "ANOPQR", "ATUVXZ", "123456", "789ABC"]) == 1
    assert check_vertical_genes(["AACDEF", "AAIJKL", "AAOPQR", "AAUVXZ", "123456", "789ABC"]) == 2
    assert check_vertical_genes(["AACDEF", "AAIJKL", "AAOPQC", "AAUVXC", "12345C", "789ABC"]) == 3
    assert check_vertical_genes(["ABCDEF", "GHIJKL", "AAOPQR", "AAOPQR", "12OPQR", "78OPQR"]) == 4
    assert check_vertical_genes(["9ACDEF", "AAIJKL", "A8OPQR", "A8OPQR", "18OPQR", "78OPQR"]) == 5
    assert check_vertical_genes(["AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA", "AAAAAA"]) == 6


def test_check_diagonal_genes():
    assert check_diagonal_genes(["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == 0
    assert check_diagonal_genes(["ABCDEF", "GHIJKL", "MNCPQR", "STUCXZ", "1234C6", "789ABC"]) == 1
    assert check_diagonal_genes(["ABCDEF", "GABJKL", "MNABQR", "STUABZ", "1234CA", "789ABC"]) == 2
    assert check_diagonal_genes(["ABCDEF", "GABCKL", "MNABCR", "STUABC", "1234CA", "789ABC"]) == 3


def test_check_reversed_diagonal_genes():
    assert check_reversed_diagonal_genes(["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == 0
    assert check_reversed_diagonal_genes(["ABCDEA", "GHIJAL", "MNOAQR", "STAVXZ", "123456", "789ABC"]) == 1


def test_parse_list():
    assert parse_list(["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]) == ["ABCDEF", "GHIJKL", "MNOPQR", "STUVXZ", "123456", "789ABC"]


def test_parse_list_one():
    assert parse_list("AA,AA,AA,AA,AA") == "AA,AA,AA,AA,AA"


def test_parse_one():
    assert parse_list("A") == "A"


def test_parse_list_none():
    assert parse_list(None) is None


def test_check_mutant_dna():
    response = client.post(
        "/mutant?dna=['AAAAEF', 'GHIJKL', 'MNOPQR', 'STUVXZ', '123456', '78AAAA']",
    )
    assert response.status_code == 200
    assert response.json() is True


# def test_check_human_dna():
#     response = client.post(
#         "/mutant?dna=['ABCDEF', 'GHIJKL', 'MNOPQR', 'STUVXZ', '123456', '789ABC']",
#     )
#     assert response.status_code == 403


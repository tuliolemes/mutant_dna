from fastapi import Query
from typing import List, Optional


def parse_list(dna: List[str] = Query(...)) -> Optional[List]:
    """
    accepts strings formatted as lists with square brackets
    """
    def remove_prefix(text: str, prefix: str):
        return text[text.startswith(prefix) and len(prefix):]

    def remove_postfix(text: str, postfix: str):
        if text.endswith(postfix):
            text = text[:-len(postfix)]
        return text

    if dna is None:
        return

    # we already have a list, we can return
    if len(dna) > 1:
        return dna

    # if we don't start with a "[" and end with "]" it's just a normal entry
    flat_dna = dna[0]
    if not flat_dna.startswith("[") and not flat_dna.endswith("]"):
        return dna

    flat_dna = remove_prefix(flat_dna, "[")
    flat_dna = remove_postfix(flat_dna, "]")

    dna_list = flat_dna.split(",")
    dna_list = [remove_prefix(n.strip(), "\"") for n in dna_list]
    dna_list = [remove_postfix(n.strip(), "\"") for n in dna_list]

    return dna_list


def check_horizontal_genes(dna):
    horizontal_mutant_gene = 0
    for row in range(len(dna)):
        for col in range(len(dna) - 3):
            if dna[row][col] == dna[row][col + 1] == dna[row][col + 2] == dna[row][col + 3]:
                horizontal_mutant_gene += 1
                break
    return horizontal_mutant_gene


def check_vertical_genes(dna):
    vertical_mutant_genes = 0
    for col in range(len(dna)):
        for row in range(len(dna)-3):
            if dna[row][col] == dna[row + 1][col] == dna[row + 2][col] == dna[row + 3][col]:
                vertical_mutant_genes += 1
                break
    return vertical_mutant_genes


def check_diagonal_genes(dna):
    diagonal_mutant_genes = 0
    for col in range(len(dna) - 3):
        for row in range(len(dna) - 3):
            if dna[row][col] == dna[row + 1][col + 1] == dna[row + 2][col + 2] == dna[row + 3][col + 3]:
                diagonal_mutant_genes += 1
                break
    return diagonal_mutant_genes


def check_reversed_diagonal_genes(dna):
    reversed_diagonal_mutant_genes = 0
    for row in range(len(dna) - 3):
        for col in range(len(dna) - 1, 2, -1):
            if dna[row][col] == dna[row + 1][col - 1] == dna[row + 2][col - 2] == dna[row + 3][col - 3]:
                reversed_diagonal_mutant_genes += 1
                break
    return reversed_diagonal_mutant_genes

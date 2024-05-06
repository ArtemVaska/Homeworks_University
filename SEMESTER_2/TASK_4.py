# Для выровненной multiFASTA построить UPGMA дерево.

import math


def convert_multiline_fasta_to_oneline(
    input_fasta: str, output_fasta: str = None
) -> dict:
    seqs = {}
    with open(input_fasta) as multiline_fasta:
        seq = []
        for line in multiline_fasta:
            line = line.strip()
            if line.startswith(">"):
                if len(seq) != 0:
                    seqs[seq_id] = "".join(seq)
                    seq = []
                seq_id = line
            else:
                seq.extend(line)
        seqs[seq_id] = "".join(seq)

    if output_fasta is None:
        output_fasta = input_fasta.split(".")[0] + "_oneline.fasta"

    with open(output_fasta, mode="w") as oneline_fasta:
        for seq_id, seq in seqs.items():
            oneline_fasta.write(f"{seq_id}\n")
            oneline_fasta.write(f"{seq}\n")

    print(f"{output_fasta} created!")

    return seqs


def calculate_differences(seqs):
    n = len(seqs)
    matrix = [[math.inf] * n for _ in range(n)]

    seqs_id = [id for id in seqs]

    for i in range(n - 1):
        for j in range(i + 1, n):
            matrix[i][j] = sum(
                1
                for nucl_query, nucl_subject in zip(seqs[seqs_id[i]], seqs[seqs_id[j]])
                if nucl_query != nucl_subject
            )

    seqs_id_upd = [id[1:] for id in seqs_id]

    return matrix, seqs_id_upd


def find_min_values(matrix, seqs_id_upd):
    min_values_indices = []
    for j in range(len(seqs_id_upd) - 1):
        min_values_indices.append(
            [index for index, value in enumerate(matrix[j]) if value == min(matrix[j])]
        )
    print(min_values_indices)

    min_values = []
    for i in range(len(min_values_indices)):
        min_value = matrix[i][min_values_indices[i][0]]
        min_values.append(min_value)

    return min_values_indices, min_values


def compare_min_values(min_values_indices, min_values):
    if max([len(el) for el in min_values_indices]) > 1:
        print("Все сложно")


# def combine_indices(min_values_indices, matrix, seqs_id):
#     min_value = [
#         index for index, value in enumerate(min_values_indices) if value == min()
#     ]
#     pass


def upgma(matrix, seqs_id, upgma_tree=None):
    if upgma_tree is None:
        upgma_tree = []
    min_values_indices = find_min_values(matrix, seqs_id)
    new_seqs_id = combine_indices(min_values_indices, matrix, seqs_id)

    return upgma_tree


seqs = convert_multiline_fasta_to_oneline("multifasta/test.fa")
matrix, seqs_id = calculate_differences(seqs)
print(matrix)

min_values_indices, min_values = find_min_values(matrix, seqs_id)
print(min_values)

compare_min_values(min_values_indices, min_values)

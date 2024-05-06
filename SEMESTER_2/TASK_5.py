# Дано дерево в формате newick. Нужно для этого дерева посчитать среднюю длину ветвей.

# mamba remove -n phylo_tree --all
# mamba create -n phylo_tree -c conda-forge python=3.6
# mamba activate phylo_tree
# mamba install -c etetoolkit ete3

import re

from ete3 import Tree


def calculate_mean_nodes_length(input_file: str) -> float:
    # pattern = re.compile(r"\b[0-9]+(?:\.[0-9]+)?\b")
    pattern = re.compile(r"\d+\.\d+")

    with open(input_file, "r") as handle:
        tree = handle.readlines()[0].strip(";")
        nodes_dists_str = pattern.findall(tree)
        nodes_dists_int = [0.0] + [float(dist) for dist in nodes_dists_str]
        average_nodes_length = sum(nodes_dists_int) / len(nodes_dists_int)

    return average_nodes_length


def calculate_mean_nodes_length_ete3(input_file: str) -> float:
    with open(input_file, "r") as handle:
        tree = Tree(handle.readline())

    nodes = [node for node in tree.traverse()]
    nodes_dists = [node.dist for node in nodes]
    average_branch_length = sum(nodes_dists) / len(nodes_dists)

    return average_branch_length


files = ["newick/test.newick", "newick/yeast_strains.newick"]

for file in files:
    custom_result = round(calculate_mean_nodes_length(file), 17)
    lib_result = calculate_mean_nodes_length_ete3(file)
    print(f"{custom_result}\n{lib_result}\n")

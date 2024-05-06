"""
UPGMA - Unweighted pair group method using arithmetic averages
Takes as input the distance matrix of species as a numpy array
Returns tree either as a dendrogram or in Newick format
"""

import itertools
from dataclasses import dataclass
from typing import Self, Generator

import numpy as np


@dataclass
class Leaf:
    """Data structure to store leaf of a UPGMA tree"""

    name: str
    up_height: float = 0.0

    def leaves(self) -> Generator[Self, None, None]:
        yield self

    def __str__(self):
        return f"{self.name}:{self.up_height}"


@dataclass
class Node:
    """
    Data structure to store OTU node of a UPGMA tree
    """

    left: Self | Leaf
    right: Self | Leaf
    up_height: float = 0.0
    down_height: float = 0.0

    @classmethod
    def from_height(cls, left: Self | Leaf, right: Self | Leaf, height: float):
        left.up_height = height if isinstance(left, Leaf) else height - left.down_height
        right.up_height = (
            height if isinstance(right, Leaf) else height - right.down_height
        )
        return cls(left, right, down_height=height)

    def leaves(self) -> Generator[Leaf, None, None]:
        """
        Method to find the taxa under any given node, effectively equivalent to
        finding leaves of a binary tree. Only lists original taxa and not OTUs.
        """
        yield from self.left.leaves()
        yield from self.right.leaves()

    def __len__(self) -> int:
        """
        Method to define len() of a node.

        Returns the number of original taxa under any given node.
        """
        return sum(1 for taxa in self.leaves())

    def __str__(self) -> str:
        """
        Method to give readable print output
        """
        return f"({self.left},{self.right}):{self.up_height}"


def upgma_tree(dist_matrix: np.ndarray, taxa: list[str]) -> Leaf | Node:
    if not taxa:
        raise ValueError("need at least one leaf (taxon)")

    size = len(taxa)
    work_matrix = np.array(dist_matrix, dtype=float)

    if work_matrix.shape != (size, size):
        raise ValueError("distance matrix should be squared in the number of taxa")

    # creating node for each taxa
    nodes = list(map(Leaf, taxa))
    taxa_to_rc = {j: i for i, j in enumerate(taxa)}

    while size > 1:
        # set all diagonal elements to infinity for ease of finding least distance
        np.fill_diagonal(work_matrix, np.inf)

        # finding (row, col) of least dist
        least_id = np.unravel_index(work_matrix.argmin(), work_matrix.shape, "C")
        least_dist = work_matrix[least_id]

        # nodes corresponding to (row, col)
        node1, node2 = (nodes[i] for i in least_id)

        # add OTU with node1 and node2 as children. set heights of nodes
        new_node = Node.from_height(node2, node1, least_dist / 2)
        nodes.remove(node1)
        nodes.remove(node2)
        nodes.append(new_node)

        # create new working distance matrix
        size -= 1  # Removing 2 nodes but adding only one new
        work_matrix = np.zeros((size, size), dtype=float)
        for row, node1 in enumerate(nodes):
            for col, node2 in enumerate(nodes):
                work_matrix[row, col] = np.mean(
                    [
                        dist_matrix[taxa_to_rc[i.name], taxa_to_rc[j.name]]
                        for i, j in itertools.product(node1.leaves(), node2.leaves())
                    ]
                )

    return nodes[-1]


if __name__ == "__main__":
    # data from table 3 of Fitch and Margoliash, Construction of Phylogenetic trees
    taxa = ["Turtle", "Human", "Tuna", "Chicken", "Moth", "Monkey", "Dog"]
    distances = np.array(
        [
            [0, 19, 27, 8, 33, 18, 13],
            [19, 0, 31, 18, 36, 1, 13],
            [27, 31, 0, 26, 41, 32, 29],
            [8, 18, 26, 0, 31, 17, 14],
            [33, 36, 41, 31, 0, 35, 28],
            [18, 1, 32, 17, 35, 0, 12],
            [13, 13, 29, 14, 28, 12, 0],
        ]
    )
    print(upgma_tree(distances, taxa))


def combine_indices(min_values_indices, matrix, seqs_id):
    min_value = [
        index for index, value in enumerate(min_values_indices) if value == min()
    ]
    pass

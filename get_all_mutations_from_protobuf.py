import gzip
import treeswift
import parsimony_pb2
import tqdm
def preorder_traversal(node):
    yield node
    for clade in node.children:
        yield from preorder_traversal(clade)


def preorder_traversal_iter(node):
    return iter(preorder_traversal(node))


class UsherMutationAnnotatedTree:
    def __init__(self, tree_file):
        self.data = parsimony_pb2.data()
        self.data.ParseFromString(tree_file.read())
        self.condensed_nodes_dict = self.get_condensed_nodes_dict(
            self.data.condensed_nodes)
        self.tree = treeswift.read_tree(self.data.newick, schema="newick")
        self.data.newick = ''

        self.annotate_mutations()
        self.expand_condensed_nodes()

    def annotate_mutations(self):
        for i, node in enumerate(preorder_traversal(self.tree.root)):
            node.nuc_mutations = self.data.node_mutations[i].mutation

    def set_branch_lengths(self):
        for i, node in enumerate(preorder_traversal(self.tree.root)):
            node.edge_length = len(node.nuc_mutations.mutation)

    def expand_condensed_nodes(self):
        for i, node in tqdm.tqdm(enumerate(self.tree.traverse_leaves()),
                                 desc="Expanding condensed nodes",
                                 miniters=100000,mininterval=10):

            if node.label and node.label in self.condensed_nodes_dict:

                for new_node_label in self.condensed_nodes_dict[node.label]:
                    new_node = treeswift.Node(label=new_node_label)
                    new_node.nuc_mutations = []
                    new_node.aa_subs = []
                    node.add_child(new_node)
                node.label = ""
            else:
                pass

    def get_condensed_nodes_dict(self, condensed_nodes_dict):
        output_dict = {}
        for condensed_node in tqdm.tqdm(condensed_nodes_dict,
                                        desc="Reading condensed nodes dict",
                                        miniters=100000,mininterval=10):
            output_dict[
                condensed_node.node_name] = condensed_node.condensed_leaves
        return output_dict

f = open("/mnt/data/gisaid_data/optimised_trimmed.pb", "rb")


mat = UsherMutationAnnotatedTree(f)

for leaf in tqdm.tqdm(mat.tree.traverse_leaves()):
    positions_mutated = set()
    cur_node = leaf
    starting_nucs = {}
    ending_nucs = {}
    while cur_node.parent:
        for mutation in cur_node.nuc_mutations:
            positions_mutated.add(mutation.position)
            if mutation.position not in ending_nucs:
                ending_nucs[mutation.position] = mutation.mut_nuc[0]
            starting_nucs[mutation.position] = mutation.ref_nuc


        cur_node = cur_node.parent
    mutation_string = ",".join(str(pos) for pos in sorted(positions_mutated) if starting_nucs[pos] != ending_nucs[pos])
    print(f"{leaf.label}:{mutation_string}")

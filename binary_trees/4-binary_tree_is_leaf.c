#include "binary_trees.h"

/**
 * binary_tree_is_leaf - function that checks whether a node is a leaf
 * @node: pointer to the node to check
 * Return: 1 (success) 0 otherwise
*/

int binary_tree_is_leaf(const binary_tree_t *node)
{
	if (node->left == NULL && node->right == NULL)
		return (1);
	return (0);
}

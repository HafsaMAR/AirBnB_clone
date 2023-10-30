#include "binary_trees.h"

/**
 * binary_tree_is_root - function that checks whether a node is a root
 * @node: pointer to the node to check
 * Return: 1 (success) 0 otherwise
*/

int binary_tree_is_root(const binary_tree_t *node)
{
	if (node->parent == NULL)
		return (1);
	return (0);
}

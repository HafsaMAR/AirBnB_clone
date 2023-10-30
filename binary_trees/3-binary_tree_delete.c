#include "binary_trees.h"


/**
 * binary_tree_delete - function that deletes an entire tree
 * @tree: pointer to the root of the tree
 */
void binary_tree_delete(binary_tree_t *tree)
{
	binary_tree_t *node;

	if (tree == NULL)
		return;
	/*To free all the tree we need to traverse it*/
	node = tree;
	binary_tree_delete(node->left);
	binary_tree_delete(node->right);
	free(tree);
}

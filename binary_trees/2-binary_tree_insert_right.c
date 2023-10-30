#include "binary_trees.h"

/**
 * binary_tree_insert_right - function that insert a node a the right-child
 * @parent: pointer to the node to insert the right-child in
 * @value: the value to store in the new node
 * Return: pointer to the inserted node
 */
binary_tree_t *binary_tree_insert_right(binary_tree_t *parent, int value)
{
	binary_tree_t *node;

	if (!parent)
		return (NULL);
	node = binary_tree_node(parent, value);
	if (node)
	{
		if (parent->right == NULL)
		{
			parent->right = node;
		}
		else
		{
			parent->right->parent = node;
			node->right = parent->right;
			parent->right = node;
		}
	}
	return (node);
}

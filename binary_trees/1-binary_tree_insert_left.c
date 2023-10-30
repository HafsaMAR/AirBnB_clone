#include "binary_trees.h"

/**
 * binary_tree_insert_left - function that insert a node as a left-child
 * @parent: pointer to the node to insert the left-child in
 * @value: the valur of the inserted node
 * Return: pointer to the inserted node
 */
binary_tree_t *binary_tree_insert_left(binary_tree_t *parent, int value)
{
	binary_tree_t *node;

	if (!parent)
		return (NULL);
	node = malloc(sizeof(binary_tree_t));
	if (!node)
		return (NULL);
	node->n = value;
	node->right = NULL;
	node->parent = parent;

	if (parent->left == NULL)
	{
		parent->left = node;
		node->left = NULL;
	}
	else
	{
		node->left = parent->left;
		parent->left->parent = node;
		parent->left = node;
	}
	return (node);
}

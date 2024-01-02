#include "lists.h"

/**
 * insert_node - inserts a node to list
 * @head: start node
 * @number: number of nodes to be added
 * Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *arr, *old = *head;

	arr = malloc(sizeof(listint_t));

	if (arr == NULL)
		return(NULL);

	arr->n = number;

	if (old == NULL || old->n >= number)
	{
		arr->next = old;
		*head = arr;
		return (arr);
	}

	while (old && old->next && old->next->n < number)
		old = old->next;

	arr->next = old->next;
	old->next = arr;

	return (arr);
}

#include "lists.h"

/**
 * check_cycle - checks if a cycle exists in singly linked lists
 * @list: pointer to head of list
 * Return: Always 0 on success, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *second = list;

	while (first != NULL && second != NULL && second->next != NULL)
	{
		first = first->next;
		second = second->next->next;

		if (first == second)
		{
			return (1);
		}
	}
	return (0);
}


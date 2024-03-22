#include "lists.h"

/**
 * print_dlistint - prints double-linked list
 * @h: pointer of head of the list
 * Return: number of list nodes
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}

#include "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if a list has 0 or 1 element
 */
int check_cycle(listint_t *list)
{
listint_t *slow = list;
listint_t *fast = list;

 /* Check if the list is NULL or contains one node only*/
 if (!list || !list->next)
 return (0);

/* Move slow pointer 1 step and fast pointer 2 steps */
while (slow && fast && fast->next)
{
slow = slow->next;
fast = fast->next->next
/*  cycle, slow and fast pointers will meet */
if (slow == fast)
return (1);
}

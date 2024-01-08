#include <listobject.h>
#include <object.h>
#include <Python.h>

/**
 * print_python_list_info - prints info o python lists
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	int x;
	PyListObject *list = (PylistObject *)p;
	long int size = Pylist_Size(p);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", allocated);

	for (x = 0; x < size; x++)
	{
		printf("Element %i: %s\n", x, Py_TYPE(list->ob_item[x])->tp_name);

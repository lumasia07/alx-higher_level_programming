#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints bytes info
 * @p: python list
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	long int len, x, y;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	len = ((PyVarObject *)(p))->ob_size;

	printf(" size: %ld\n", len);
	printf(" trying string: %s\n", str);

	if (len >= 10)
		y = 10;
	else
		y = len + 1;

	printf(" first %ld bytes:", y);

	for (x = 0; x < y; x++)
		if (str[x] >= 0)
			printf( " %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);

	printf("\n");
}

/**
 * print_python_list - prints list info
 * @p: Python object
 * Return: none
 */
void print_python_list(PyObject *p)
{
	long int x, y;
	PyObject *obj;
	PyListObject *list;

	x = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of Python List = %ld\n", x);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (y = 0; y < x; y++)
	{
		obj = ((PyListObject *)p)->ob_item[y];
		printf("Element %ld: %s\n", y, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

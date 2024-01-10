#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - prints bytes info
 * @p: python list
 * Return: none
 */
void print_python_bytes(PyObject *p)
{
	long int l, x, y;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	str = ((PyBytesObject *)p)->ob_sval;
	l = ((PyVarObject *)(p))->ob_size;

	printf(" size: %ld\n", l);
	printf(" trying string: %s\n", str);

	y = (l >= 10) ? 10 : l + 1;

	printf(" first %ld bytes:", y);

	for (x = 0; x < y; x++)
		printf(" %02hhx", str[x]);

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

	x = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of Python List = %ld\n", x);

	for (y = 0; y < x; y++)
	{
		obj = ((PyListObject *)p)->ob_item[y];

		printf("Element %ld: %s\n", y, ((obj)->ob_type)->tp_name);

		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}

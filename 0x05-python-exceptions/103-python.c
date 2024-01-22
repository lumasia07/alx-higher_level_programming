#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints a python list
 * @p: pointer to list to be printed
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocator, j;
	const char *list_type;
	PyListObject *x = (PyListObject *)p;
	PyVarObject *y = (PyVarObject *)p;

	size = y->ob_size;
	allocator = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf(" [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocator);

	for (j = 0; j < size; j++)
	{
		list_type = x->ob_item[j]->ob_type->tp_name;
		printf("Element %ld: %s\n", j, list_type);
		if (strcmp(list_type, "bytes") == 0)
			print_python_bytes(x->ob_item[j]);
		else if (strcmp(list_type, "float") == 0)
			print_python_float(x->ob_item[j]);
	}
}

/**
 * print_python_bytes - prints python bytes
 * @p: pointer to python byte objects
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, j;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf(" size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf(" trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;


	printf(" first %ld bytes: ", size);
	for (j = 0; j < size; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints basic info on python float objects
 * @p: python float object
 */
void print_python_float(PyObject *p)
{
	char *bf = NULL;

	PyFloatObject *f_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}

	bf = PyOS_double_to_string(f_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);

	printf(" value: %s\n", bf);
	PyMem_Free(bf);
}

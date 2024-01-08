#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints info on lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	long int n = PyList_Size(p);
	int idx;
	PyListObject *m = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", n);
	printf("[*] Allocated = %li\n", m->allocated);

	for (idx = 0; idx < n; idx++)
	{
		printf("Element %i: %s\n", idx, Py_TYPE(m->ob_item[idx])->tp_name);
	}
}

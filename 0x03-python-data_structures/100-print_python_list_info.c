#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>

#define PY_SSIZE_T_CLEAN

/**
 * print_python_list_info - printd info on lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	long int n = PyList_Size(p);
	int idx;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", n);
	printf("[*] Allocated = %li\n", obj->allocated);

	for (idx = 0; idx < n; idx++)
	{
		printf("Element %i: %s\n", idx, Py_TYPE(obj->ob_item[idx])->tp_name);
	}
}

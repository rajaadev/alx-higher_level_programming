#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <floatobject.h>
#include <stdlib.h>


/*
 * print_python_list - Prints information about Python list.
 * p: pointer to a Python object.
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;

    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, alloc);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

/*
 * print_python_bytes - Prints information about Python bytes.
 * p: pointer to a Python object.
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *bytes_str;

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    bytes_str = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %ld\n  ", size);
    printf("trying string: %s\n  ", bytes_str);
    printf("first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x ", (unsigned char)bytes_str[i]);
    }
    printf("\n");
}

/*
 * print_python_bytes - Prints information about Python float.
 * p: pointer to a Python object.
 */
void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);
    printf("[.] float object info\n  value: %f\n", value);
}

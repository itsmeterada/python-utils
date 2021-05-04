//
// A simple example of calling python code from C/C++.
// - only tested on Linux Mint 20.04 / gcc9.3 / Anaconda / python3.9 environment
// 

#include <stdio.h>
#include <Python.h>

int main(int argc, char *argv[])
{
	wchar_t *program = Py_DecodeLocale(argv[0], NULL);
	if (program == NULL) {
		fprintf(stderr, "Fatal error: can not decode argv[0]\n");
		exit(1);
	}
	Py_SetProgramName(program);
	Py_Initialize();
	PyRun_SimpleString("from time import time, ctime\n"
					   "print('Today is', ctime(time()))\n");
	if (Py_FinalizeEx() < 0) {
		exit(1);
	}
	PyMem_RawFree(program);
	return 0;
}

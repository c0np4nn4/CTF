#include <stdio.h>
#include <unistd.h>

int main() {
  // buffer for storing shellcode
  char shellcode[] = "";

  read(0, shellcode, 1024);

  void (*func)();

  // type conversion; char[] to function pointer
  func = (void (*)())shellcode;

  // execute shellcode
  func();

  return 0;
}

#include <stdio.h>
#include "bitcoin_lib.h"
#include <cstdlib>
#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
  Bitcoin b;
  b.createAddress();
  b.printAddress();
  return 0;
}

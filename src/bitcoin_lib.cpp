#include "bitcoin_lib.h"
#include <iostream>

Bitcoin::Bitcoin()
{
  std::cout<<"Constructor runs"<<std::endl;
}
Bitcoin::~Bitcoin()
{
  std::cout<<"Destructor runs"<<std::endl;
}
void Bitcoin::initializeAddress()
{
  for (char x : address) {
    x = '0';
  }
  for (char a : address) {
    std::cout<<a;
  }
}

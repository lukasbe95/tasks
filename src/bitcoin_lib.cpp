#include "bitcoin_lib.h"
#include <iostream>
#include <cstdlib>
#include <sstream>

using namespace std;

Bitcoin::Bitcoin()
{
  cout<<"Constructor runs"<<endl;
}
Bitcoin::~Bitcoin()
{
  cout<<"Destructor runs"<<endl;
}
void Bitcoin::initializeAddress()
{
  srand(static_cast <unsigned int> (time(0)));
  address = "0";
  for (int i=1;i<21;i++) {
    int temp = rand()%t.length();
    address += t[temp];
  }
  size_t hashResult = std::hash<string>{}(address);
  stringstream ss;
  ss << hashResult;
  address += ss.str().substr(0,4);  
}

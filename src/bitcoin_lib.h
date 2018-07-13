#include <string>
#ifndef BIT_H
#define BIT_H

class Bitcoin
{
private:
  std::string address;
  std::string t = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
public:
  Bitcoin ();
  void createAddress();
  void printAddress();
  ~Bitcoin ();
};
#endif

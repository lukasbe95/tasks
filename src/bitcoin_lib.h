#include <string>
#ifndef BIT_H
#define BIT_H

class Bitcoin
{
private:
  std::string address;
  std::string t = "01234567890abcdefghijklmnoprstuxwvABCDEFGHIJKLMNOPRSTUWXV";
public:
  Bitcoin ();
  void initializeAddress();
  ~Bitcoin ();
};
#endif

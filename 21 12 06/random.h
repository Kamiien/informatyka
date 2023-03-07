#include <cstdlib>
#include <ctime>

#ifndef RANDOMH
#define RANDOMH

int randr(int min, int max)
{
  timeval t;
  mingw_gettimeofday(&t, NULL);
  srand(t.tv_usec * t.tv_sec);
  return rand() % (max + 1 - min) + min;
}

float randfr(int min, int max)
{
  timeval t;
  mingw_gettimeofday(&t, NULL);
  srand(t.tv_usec * t.tv_sec);
  return (float) ((rand() % (max - min) + min) + ((float)(rand() % 10) / 10));
}

#endif
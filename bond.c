#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double dWT(){
    int num = 3;
    return (rand() % (2*num + 1)) - num;
}

double InterestRate(double alpha, double mu, double sigma, double ir, double dt, int N, int P){
    srand(time(NULL));
    double r0 = ir;
    for(int p = 0; p < P; ++p){
        for(int t = 0; t < N; ++t){
            r0 += alpha*(mu - r0)*dt + sigma*pow(r0, 0.5)*dWT();
        }
    }
    return r0;
}
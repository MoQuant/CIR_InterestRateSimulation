#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Generates the dWT parameter for the stochastic equation
double dWT(){
    int num = 3;
    return (rand() % (2*num + 1)) - num;
}

// Simulates the interest rate with a stochastic model
double InterestRate(double alpha, double mu, double sigma, double ir, double dt, int N, int P){
    srand(time(NULL));
    double r0 = ir;
    for(int p = 0; p < P; ++p){
        for(int t = 0; t < N; ++t){
            // Interest rate is updated based on its previous rate and the mean reversion parameters
            r0 += alpha*(mu - r0)*dt + sigma*pow(r0, 0.5)*dWT();
        }
    }
    return r0;
}

package com.primes.primes;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@SpringBootApplication
public class PrimesApplication {

    @RequestMapping("/")
    String spring() {
        int numPrimes = 0;                                                      
        for (int i=2;i<250001;i++) {                                            
            numPrimes += isPrime(i);                                            
        }                                                                       
        System.out.println(numPrimes);                                          
        return Integer.toString(numPrimes);
    }

	public static void main(String[] args) {
		SpringApplication.run(PrimesApplication.class, args);
	}

    public static int isPrime(int n) {                                          
        for (int i=2;i<=n/2;i++)                                                
            if((n%i) == 0)                                                      
                return 0;                                                       
        return 1;                                                               
    }                                                                           

}

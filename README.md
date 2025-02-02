# Diffie-Hellman-Algorithm
This an explanation and implementation for Diffie-Hellman algorithm. 



Diffie-Hellman algorithm is an algorithm used for key exchange between two parties, and primarly used when no secure channel is found to share a secret key between two parties. This is an explanation of how this algorithm works, and implementation for it. 


1- the communication parties (Bob & Alice) agree on two large numbers p,g. Where p is a large prime number, and g is an integer such that 1 < g < p. 

2- Bob chooses a large random integer b and performs --> B = g^b mod p 

3- Alice also do the same performing --> A = g^a mod p 

4- Bob sends B to Alice, and Alice sends A to Bob.

5- Bob then performs the following calculation --> K = S^b mod p 

6- Alice also does the same --> K = B^a mod p 

At this point both Bob and Alice have the same key. 




# Example of how Diffie-Hellman works: 



let's say that Alice and Bob chose p=32, and g=5.


Alice chose a=6, and Bob chose b=15


Alice computes --> 5^6 mod 23 = 8
Bob computes --> 5^15 mod 23 = 19

Alice sent 8 to Bob 
Bob sent 19 to Alice


Alice computes --> s = 19^6 mod 23 = 2
Bob computes --> s = 8^15 mod 23 =2 

Now both Alice and Bob have the same key, to initiate their symmetric key encryption algorithm. 



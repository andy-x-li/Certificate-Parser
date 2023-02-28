# Certificate-Parser

A program I wrote in Python for a Computer Security course. 

The file tranco-top-1m.csv contains the top million most popular websites and orders them by rank. 

Certificate_Parser.py takes in this file and attempts to revieve the certificates to the top 1000 cites. Certificate_Parser.py then analyzes these certificates to answer the following problems: 

1) What are most common certificate authorities?
2) What is the range of valid certificate times?
3) What is the most common issuer country?
4) Are there any patterns in CA state/province names?
5) What are the types and most common public keys?
6) What are the key lengths for each type of public keys?
7) Are there any patterns in the associated exponent of public keys?
8) What is the most common signature algorithm?
9) Are there any connections between the number of extensions of a certificate to its webpage or CA?
10) What is the most common organization name for all 1000 and is it the same for the top 50? 

To run this code:
  1) Create a folder with both Certificate_Parser.py and tranco-top-1m.csv
  2) Run via cmd line ("python3 Certificate_Parser.py")
  
Note: There are comments in the code highlighting which sections answer which problems. Please comment out all other problems besides your problem of interest. If the comments don't specify what to set as x in the for loop (int(row[0]) <= x), please set x as 1000 (x represents how many websites are analyzed starting from the top of the list). Remember to also comment out the corresponding print sections found at the bottom of the code. 

Below is the code run on its current state without any changes to the comments. It outputs the answer to question 10. 

<img width="455" alt="Screen Shot 2023-02-28 at 1 33 54 PM" src="https://user-images.githubusercontent.com/125074849/221959704-973a0130-291e-4613-b93a-7fb003ad2607.png">

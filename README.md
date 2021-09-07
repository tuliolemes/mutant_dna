# mutant_dna
This is a FastAPI application. 
I used SQLAlchemy ORM, Docker and Cloudformation (SAM) to create a structure in AWS (PostgreSQL, API Gateway and Lambda) and solve the problem below. 

## Synopsis
```
Magneto wants to recruit as many mutants as possible so he can fight the X-Men.
He has hired you to develop a project that detects if a human is a mutant based on his DNA
sequence.
For that he has asked you to create a program with a method or function with the following
signature:
• boolean isMutant (String [] dna); // Java example
Where you will receive as a parameter an array of Strings that represent each row of a table of
(NxN) with the DNA sequence. The letters of the Strings can only be: (A, T, C, G), which
represents each nitrogenous base of DNA.
No-Mutant
A T G C G A
C A G T G C
T T A T T T
A G A C G G
G C G T C A
T C A C T G
Is-Mutant
A T G C G A
C A G T G C
T T A T G T
A G A A G G
C C C C T A
T C A C T G
You will know if a human is a mutant, if you find more than one sequence of four equal letters,
obliquely, horizontally or vertically. Example (Mutant case):
String [] dna = {"ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"};
In this case the call to the isMutant (dna) function returns "true". Develop the algorithm as
efficiently as possible
```
## Files
```
.
├── app
|   ├── __init__.py
|   ├── main.py
│   ├── endpoints
│   │   ├── __init__.py
│   │   ├── mutant.py
│   │   └── utils.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── crud.py
│   │   └── database.py
│   │   └── models.py
│   │   └── schemas.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── mutant_test.py
├── Dockerfile
├── README.md
├── requirements.txt
└── template.yml
```

- `main.py`: Main, unifies routers
- `crud.py`: Create CRUD operations utils as in the SQLAlchemy
- `database.py`: Sets up connection with PostgreSQL
- `models.py`: Create the database models
- `schemas.py`: Create the Pydantic models
- `enpoints/`: Folder containing the APIs endpoints
- `requirements.txt`: python packages required to run the project
- `Dockerfile`: Dockerfile with all commands to run a container locally
- `template.yml`: Cloudformation responsible for deploying the project at AWS

## Prerequisites
```
Make sure you have installed:
* Python
* PostgreSQL
* Docker
```
```
Change the dbconnection at database.py:
user = "TBD"
password = "TBD"
host = "localhost"
port = "5432"
database = "TBD"
```
## Clone project and test locally
```
git clone https://github.com/tuliolemes/mutant_dna
cd mutant_dna
# Build and run Dockerfile to test locally
docker build -t mutant-image .
docker run -d --name mutant-container -p 8000:8000 mutant-image
Open the browser at http://127.0.0.1:8000/docs#/default
```

## Local endpoints
```
/stats [GET]
/mutants [POST]
```

## Or try the endpoints above:
```
https://7o0dchybgl.execute-api.us-east-2.amazonaws.com/dev/api/v1/mutant?dna=["ABCDEF", "GHIJKL", "SDSADS", "STUVXZ", "ZZZZZZ", "AAAAAA"] [POST]
https://7o0dchybgl.execute-api.us-east-2.amazonaws.com/dev/api/v1/stats [GET]
```

## Next Steps
```
- stress tests
- introduce AWS SQS to decouple the application (APIs calls and DB connection)
```
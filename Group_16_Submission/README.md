Group 16<br />
SU17<br />
CS325 TSP Competition<br />
These two programs use the 2-OPT algorithm to find a near optimal solution to the
traveling salesperson problem.  The first program was used to generate tours for
the example problems with an unlimited time limit.  The second program was used
to generate tours for the competition and includes conditional clauses in the
main function to account for specific test input.  To run either program, type
the following:  python3 TSP_OPT.py [filename] for the three example problems or
python3 TSP_OPT_COMP.py [filename] for the Competition input problems.  Filename
represents the name of the file containing the city data without the extention.
When the program is executed it will return a file named [filename].txt.tour.  
Competition Time Results file contains the results from our competition runs
while the Unlimited Time file holds the solutions to the examples and
test-input-4 which had a time of 17min vs the 18s in the competion run.

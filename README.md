# code_challenge
Code Challenge Solution

Problem 1
---------

Alex and Bob are high-school friends. They are enthusiastic about secret messages.
They design their own algorithm for encrypting messages.
Suppose Alex wants to send Bob the message: "canyoudecryptthismessage?", he starts out
by deciding on a number, `X` [ 0 < X < the length of the message ], as the number of columns
and generates a matrix, by writing each character top-to-down in columns, starting
with the first cell, then the second column, and so on to form a matrix.
Then he writes the output string on a single line by copying characters from this matrix,
left-to-right and right-to-left, in odd and even rows.

         input:    "canyoudecryptthismessage?"

transformation:    c u y i s       // X = number_of_columns = 5
                   a d p s a
                   n e t m g
                   y c t e e
                   o r h s ?

        output:    "cuyisaspdanetmgeetcyorhs?"

Given the output, write a program that calculates the possible `X` (number_of_columns), and
also decrypts the message to obtain the possible original message.


Problem 2
---------

In Lumberville, there is a company running a fleet of lumber trucks. The main-road
to their garage is rather narrow and allows only one truck to pass at once.
As a saving grace, there happens to be an equally narrow side-road,
making a `T` section with the main road.
The garage requires that the trucks come in order, for their parking to be fully accommodated.
But the trucks can come in any order to the office at the junction.

                                        main-road
      from the city: --------------------------------------------------  garage:
trucks can come out-of-order  [6] [2] [3]       [1]                      trucks have to come in order
                     --------------------       -----------------------
                                    |^^^|| [4] |
                             office |___|| [5] |
                                         |     |
                                         |     |
                                         |     |
                                         |_____| side-road

For example, if the trucks are lined up in order: 623451, then the following may occur:

step  operation                                           side-road       final order
  1.  [1] passes on                                       -               [1]
  2.  [5] is made to wait on the side-road                [5]             [1]
  3.  [4] is made to wait on the side-road                [4][5]          [1]
  4.  [3] is made to wait on the side-road                [3][4][5]       [1]
  5.  [2] passes on                                       [3][4][5]       [2][1]
  6.  [3] waiting on the side-road is made to pass on     [4][5]          [3][2][1]
  7.  [4] waiting on the side-road is made to pass on     [5]             [4][3][2][1]
  8.  [5] waiting on the side-road is made to pass on     -               [5][4][3][2][1]
  9.  [6] passes on                                       -               [6][5][4][3][2][1]

Given a sequence of truck numbers, write a function to output whether the sequence will result
in a completely ordered final garage or not, in #true or #false.


Problem 3
---------

In Laxmitown, one can exchange a coin of amount X, with three coins of amounts X/2, X/3 and X/4.
But coins cannot be converted if the result is a fractional value. Only whole numbers are valid.

For example, if one deposits a coin worth 36, he get back 3 coins: 18, 12 and 9, with a value of 39
Further 12 can be exchanged for coins: 6, 4 and 3, totalling to 13. The final value being 39 + 13 = 52.
Note that 18 cannot be exchanged further, because 18/4 does not result in a whole number.

Given a number X, write a program to find the maximum value it can be exchanged for.

# CSC 4330: Extra Credit
By Vincent Kim<br>
CSC 4330: Programming Language Concepts

## Syntax Rules
```
<program> --> INIT : <stmt_ls> ;
<stmt_ls> --> <stmt> ;
<stmt> --> <if_stmt> | <while_stmt> | <as_s> | <block> | <dec>
<if_stmt> --> given ( <bool_exp> ) { <stmt> ; }
<while_stmt> --> during ( <bool_exp> ) { do <stmt> ; }
<as_s> --> id = <exp> ;
<block> --> { <stmt_ls> }
<dec> --> var id ;
<exp> --> <term> { ( * | / ) } <term>
<term> --> <fctr> { ( + | - ) } <fctr>
<fctr> --> id | int | ( <expr> )
<bool_exp> --> <rel> { ( := | /= ) } <rel>
<rel> --> <b_ex> { ( < | > | <= | >= ) } <b_ex>
<b_ex> --> <b_term> { ( * | / ) } <b_term>
<b_term> --> <b_fctr> { ( + | - ) } <b_fctr>
<b_fctr> --> id | int | bool | ( <b_ex> )
```

## Keywords/Token Table
### Operators
| Operator           | Regex | Token |
| ------------------ | ----- | ----- |
| Addition           | +     | PLUS  |
| Subtraction        | -     | MNUS  |
| Multiplication     | \*    | MULT  |
| Division           | /     | DIVS  |
| Open Parenthesis   | (     | STRP  |
| Closed Parenthesis | )     | ENDP  |
| Assignment         | =     | SIGN  |

### Relationals
| Relational               | Regex | Token |
| ------------------------ | ----- | ----- |
| Less Than                | <     | LESS  |
| Greater Than             | >     | MORE  |
| Less Than or Equal To    | <=    | LEEQ  |
| Greater Than or Equal To | >=    | MOEQ  |
| Equal To                 | :=    | EQTO  |
| Not Equal To             | /=    | NOEQ  |
| And                      | and   | AND   |
| Or                       | or    | OR    |
| Code Block Start         | :     | BLKS  |
| Code Block End           | ;     | BLKE  |

### Data Types
| Data Type | Token | Regex |
| --------- | ----- | ----- |
| int       | INUM  | \d+   |
| real      | RNUM  | \d+   |
| string    | WRDS  | \d+   |

### Keywords
| Keyword  | Regex           | Token |
| -------- | --------------- | ----- |
| Variable | [a-z][A-Z]{6-8} | id    |
| While    | during          | DRNG  |
| Do       | exec            | EXEC  |
| For      | given           | GIVN  |
| Else     | ifnot           | IFNO  |
| Start    | init            | INIT  |
| End      | term            | TERM  |

## Structure Rules
### Declaring a string
A string (WRDS) is a sequence of characters used to store text. It can also include digits and symbols, though it will be treated as text. A string must be enclosed in double quotation marks ("").

```
WRDS str ;
WRDS str = " Hello World " ;
```

### Number Rules
An int (INUM) is a numeric data type used to store numbers without a fractional component (i.e. whole numbers).

```
INUM numTest ;
INUM numTest = 100 ;
```

A real (RNUM) is a numeric data type used to store numbers with fractional components (i.e. decimals).

```
RNUM numTest ;
RNUM numTest = 100.001 ;
```

### Boolean Rules
Boolean values represent "true" and "false" for conditional statements such as if statements (given) and while loops (during).

```
-- if the condition is true (W)
if x := W {
    -- insert statement here
}

-- while the condition is false (L)
while y := L {
    -- insert statement here
}
```

### If Statement Rules
An if statement (given) is a conditional statement that, if proved true, performs a function or displays information. Otherwise, a different function is executed or other information is displayed instead via the else statement (ifnot).

```
-- If x equals to 1, then y = 2. Else (if x is not equal to 1), then y = 1.
given (x := 1) {
    y = 2 ;
}
ifnot {
    y = 1 ;
}
```

### While Loop Rules
A while loop (during) loops through a block of code as long as a specific condition is true (exec).

```
-- While x is true, execute the statement. 
during x := W {
    exec ( <stmt> ) ;
}
```

### Semantic Rules
given/ifnot (If/Else):
```
<if_stmt> --> given ( <bool_exp> ) { <stmt> ; }

M_if(given (bool_exp) <stmt>, s) -->

    given ( <bool_exp>, s ) := error {
        return error ;
    }
    
    given ( <bool_exp>, s ) {
        given M_stmt( <stmt>, s ) := error {
            return error ;
        }
        return M_stmt( <stmt>, s ) ;
    }
       
M_if( given (bool_exp) <stmt1>, & <stmt2>, s ) -->
    
    given M_b( <bool_exp>, s ) := error {
        return error ;
    }
     
    given M_b ( <bool_exp>,s ) {
        given M_stmt( <stmt1>, s ) := error {
            return error ;
        }
        return M_stmt( <stmt1>, s ) ;
    }
       
    ifnot {
        given M_stmt( <stmt2>, s ) := error {
            return error ;
        }
        return M_stmt( <stmt2>, s ) ;
    }
```

during/exec (While/Do):
```
<while_stmt> --> during ( <bool_exp> ) { do <stmt> ; }

M_while( during (bool_exp) <stmt>, s ) -->

    during M_b( <bool_exp>, s ) := error {
        return error ;
    }
    
    during M_b( <bool_exp>, s ) {
        given M_stmt( <stmt>, s ) := error {
            return error ;
        }
        return exec M_stmt( <stmt>, s ) ;
    }
```

<as_s> (Assignment):
```
<as_s> --> id = <exp> ;

M_as ( id <exp>, s ) -->
    given M_op( =, s ) := error {
        return error ;
    }

    given M_op( =, s ) {
        given M_exp( <exp>, s ) {
            return error ;
        }
        return M_exp( <exp>, s ) ;
        
        given M_e( ;, s ) := error {
            return error ;
        }
        return M_e( ;, s ) ;
    }
```

<block> (Block):
```
<block> --> { <stmt_ls> }

M_block( { <stmt_ls> }, s ) -->

    given M_s ( {, s ) := error {
        return error;
    }
    given M_s ( {, s ) {
        given ( M_stmt_ls ( <stmt_ls>, s ) := error {
            return error ;
        }
        return M_stmt_ls( <stmt_ls>, s ) ;
    
        given M_e( }, s ) := error {
            return error ;
        }
        return M_e( }, s )
    }
```

<dec> (Declaration):
```
<dec> --> var id ;

M_dec(var id, s) -->
    given M_var( var, s ) := error {
        return error ;
    }
    given M_var ( var, s) {
        given M_id( id, s ) := error {
            return error ;
        }
        return M_id( id, s ) ;
        
        given M_c ( ;, s ) := error {
            return error ;
        }
        return M_c ( ;, s ) ;
    }
```

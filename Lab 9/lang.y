%{
#include "lex.yy.c"
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1

int yyerror(const char *s);
%}

%token MILNUMAR
%token MILSIR
%token IDENTIFIER
%token INTCONSTANT
%token STRINGCONSTANT
%token PLUS
%token MINUS
%token TIMES
%token DIV
%token EQ
%token EQEQ
%token LT
%token LTEQ
%token GT
%token GTEQ
%token SEMICOLON
%token MILINTREBI
%token MILALTFEL
%token MILTIMP
%token MILRETURN
%token MILAFISEZI
%token MILCITESTI
%token OPEN_BRACE
%token CLOSE_BRACE
%token OPEN_PAREN
%token CLOSE_PAREN
%token COMMA

%start program

%%
program : statement                      { printf("program -> statement\n"); }
        ;

statement : decl_statement SEMICOLON   { printf("statement -> decl_statement ;\n"); }
          | arr_statement SEMICOLON    { printf("statement -> arr_statement ;\n"); }
          | assign_statement SEMICOLON { printf("statement -> assign_statement ;\n"); }
          | if_statement               { printf("statement -> if_statement\n"); }
          | while_statement            { printf("statement -> while_statement\n"); }
          | return_statement SEMICOLON { printf("statement -> return_statement ;\n"); }
          | function_call_statement SEMICOLON { printf("statement -> function_call_statement ;\n"); }
          ;

types : MILNUMAR | MILSIR               { printf("types -> %s\n", yytext); }
      ;

decl_statement : types                   { printf("decl_statement -> types\n"); }
               | identifier_list         { printf("decl_statement -> identifier_list\n"); }
               ;

arr_statement : types IDENTIFIER "[" INTCONSTANT "]" clean_identifier_list { printf("arr_statement -> types IDENTIFIER [ INTCONSTANT ] clean_identifier_list\n"); }
              ;

clean_identifier_list : IDENTIFIER COMMA IDENTIFIER  { printf("clean_identifier_list -> IDENTIFIER { , IDENTIFIER }\n"); }
                    ;

identifier_list : IDENTIFIER EQ expression COMMA identifier_list { printf("identifier_list -> IDENTIFIER { = expression } { , IDENTIFIER { = expression } }\n"); }
                | IDENTIFIER EQ expression  { printf("identifier_list -> IDENTIFIER = expression\n"); }
		;

expression : int_expression             { printf("expression -> int_expression\n"); }
           | string_expression          { printf("expression -> string_expression\n"); }
           ;

int_expression : INTCONSTANT             { printf("int_expression -> INTCONSTANT\n"); }
               | IDENTIFIER              { printf("int_expression -> IDENTIFIER\n"); }
               | int_expression PLUS int_expression { printf("int_expression -> int_expression + int_expression\n"); }
               | int_expression MINUS int_expression { printf("int_expression -> int_expression - int_expression\n"); }
               | int_expression TIMES int_expression { printf("int_expression -> int_expression * int_expression\n"); }
               | int_expression DIV int_expression   { printf("int_expression -> int_expression / int_expression\n"); }
               | OPEN_PAREN int_expression CLOSE_PAREN { printf("int_expression -> ( int_expression )\n"); }
               ;

string_expression : STRINGCONSTANT        { printf("string_expression -> STRINGCONSTANT\n"); }
                  | IDENTIFIER             { printf("string_expression -> IDENTIFIER\n"); }
                  | string_expression PLUS string_expression { printf("string_expression -> string_expression + string_expression\n"); }
                  ;

expression_list : expression COMMA expression  { printf("expression_list -> expression { , expression }\n"); }               
		| expression {printf("expression_list -> expression\n"); }
		;

assign_statement : IDENTIFIER EQ expression { printf("assign_statement -> IDENTIFIER = expression\n"); }
                ;

if_statement : MILINTREBI OPEN_PAREN condition CLOSE_PAREN OPEN_BRACE statement CLOSE_BRACE 
             | MILINTREBI OPEN_PAREN condition CLOSE_PAREN OPEN_BRACE statement CLOSE_BRACE MILALTFEL OPEN_BRACE statement CLOSE_BRACE { printf("if_statement -> milintrebi ( condition ) { statement } milaltfel { statement }\n"); }
             ;

condition : expression EQEQ expression   { printf("condition -> expression == expression\n"); }
          | expression LT expression    { printf("condition -> expression < expression\n"); }
          | expression LTEQ expression   { printf("condition -> expression <= expression\n"); }
          | expression GT expression    { printf("condition -> expression > expression\n"); }
          | expression GTEQ expression   { printf("condition -> expression >= expression\n"); }
          ;

while_statement : MILTIMP OPEN_PAREN condition CLOSE_PAREN OPEN_BRACE statement CLOSE_BRACE { printf("while_statement -> miltimp ( condition ) { statement }\n"); }
                ;

return_statement : MILRETURN expression { printf("return_statement -> milreturnezi expression\n"); }
                 ;

function_call_statement : MILAFISEZI OPEN_PAREN expression_list CLOSE_PAREN { printf("function_call_statement -> milafisezi ( expression_list )\n"); }
                      ;

%%

int yyerror(const char *s) {
    printf("%s\n", s);
    return 0;
}

extern FILE *yyin;

int main(int argc, char** argv) {
    if (argc > 1)
        yyin = fopen(argv[1], "r");
    if (!yyparse())
        fprintf(stderr, "\tOK\n");
}


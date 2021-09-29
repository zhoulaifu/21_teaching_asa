
%{
#include <stdio.h>
#include <assert.h>
int n_var=0;
int n_var_phase1=0;
int phase=0; //on phase 0, only count numbers
FILE *in_file;
%}
%option noyywrap
%%
"int"[ \t\n]+"main"[ \t\n]*\([^)]*\)[ \t\n]*\{ { 

if (phase==1) {
  if (getenv("LANG_LEX")==NULL){ 
              printf("%s\n  std::cin",yytext); 
              for (int i=0; i<n_var;i++) printf(">>__x%d",i); 
              printf(";");
  }
  else {
            printf("%s\n  int __passed=scanf (\"",yytext); 
            for (int i=0; i<n_var-1;i++) printf("%%lf ");
	    printf("%%lf\""); 
            for (int i=0; i<n_var;i++) printf(",&__x%d",i); 
              printf(");");
	    printf("\nif (__passed!=%d) return 2;\n", n_var); 
		     } 
		     
//by default: no such 'error_handerler_off'. 		     
if (getenv("GSL")==NULL) printf("\n  gsl_set_error_handler_off();");
}
}


\"(\\.|[^"\\])*\" {if (phase==1) printf("%s",yytext);/*not counting fp numbers in strings*/}
"//".*  {if (phase==1) printf("%s",yytext);/*not counting fp numbers in double-slash comments*/}
"/"\*[.*\n]*.*\*"/"  {if (phase==1) printf("%s",yytext);/*not counting fp numbers in slash-star comments*/}
([-+]?[0-9]*\.[0-9]+)|([-+]?[0-9]*\.?[0-9]+[eE][-+]?[0-9]+) {
    if (phase==0) ++n_var;
    else if (phase==1) {printf("__x%d",n_var_phase1++); fprintf(in_file, "%s\n", yytext); } 
    else assert (0);
                 }
(.|\n) {if (phase==1) printf("%s",yytext);}
%%
int main() { 



 in_file = fopen("shape_parameters.txt", "w");
if (in_file == NULL) 
            {   
              printf("Error! Could not open file\n"); 
             // exit(-1); // must include stdlib.h 
            } 
phase=0;
while(yylex());

if (n_var==0) return -1;

fprintf(in_file, "%d\n", n_var); // write to file 

fclose(in_file);
 in_file = fopen("shape_parameters.txt", "a");
if (in_file == NULL) 
            {   
              printf("Error! Could not open file\n"); 
             // exit(-1); // must include stdlib.h 
            } 
rewind(stdin);

phase=1;

              printf("double "); for (int i=0; i<n_var-1;i++){printf("__x%d,",i);} printf("__x%d;\n%s",n_var-1, yytext);

//by default: no such 'include'. 
if (getenv("GSL")==NULL) printf ("#include <gsl/gsl_errno.h>\n");

if (getenv("LANG_LEX")==NULL) printf ("#include <iostream>\n");
else printf ("#include <stdio.h>\n");


while(yylex());
printf ("//Expect variables no.  counted in two rounds are equal: %d == %d\n",n_var, n_var_phase1);

fclose(in_file);
return 0;
}

usage:
	@echo Purpose:  To parameterize a program involving FP numbers
	@echo
	@echo How:  Run \"make main_tool\" to get a lexer, named main_tool. Then, run \"make run IN=my_cpp_file\" to run the lexer on the cpp file. A FP number will be shown in stdout. By default, C++ style and GSL err handler is put there. Two environment variables can be set: LANG_LEX, and GSL. If LANG_LEX is set to anything, C stuff is instrumented. If GSL is set to anything, then "include <gsl_error_handler" stuff will be inserted. The name LANG_LEX is confusing, it should be considered as "is c".
	@echo Now: two use cases. For ROS, LANG_LEX=" ", although ROS uses C++. For GSL, use LANG_LEX= " " GSL=" ".
	@echo Example: Run \"make eg\"

main_tool: hello.l
	flex hello.l
	gcc lex.yy.c -o $@
run:	main_tool
	./main_tool < $(IN)


eg: main_tool

	@echo "=======targeted cpp file======"
	@cat maketest/in1.cpp
	@echo
	@echo "=======modified one======"
	@./main_tool < maketest/in1.cpp
	@echo
	@echo "====end===="

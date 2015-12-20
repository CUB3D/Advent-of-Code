// Day-7.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <map>
#include <vector>
#include <sstream>
#include <string>
#include <fstream>

enum op
{
	SET, AND, OR, LSHIFT, RSHIFT, NOT
};

struct command
{
	std::string var1;
	std::string var2;
    op op;
	std::string dest;
};

std::vector<std::string> splitStr(std::string input, const char dlim)
{
	std::vector<std::string> ret;

	std::string s;

	for (int i = 0; i < input.length(); i++)
	{
		char c = input.c_str()[i];

		if (c == dlim)
		{
			ret.push_back(s);
			s = "";
			continue;
		}

		s += c;
	}

	ret.push_back(s);

	return ret;
}

int findArrowIndex(std::vector<std::string> input)
{
	for (int i = 0; i < input.size(); i++)
	{
		if (input[i] == "->")
		{
			return i;
		}
	}

	return -1;
}

int integer(std::string input)
{
	std::stringstream ss;

	ss << input;

	int c;

	ss >> c;

	return c;
}

// map wires to values
std::map<std::string, unsigned short> wires;

//returns true if the value can be obtained
bool hasVar(std::string var)
{
	char c = var.c_str()[0];

	//dosen't exist, value is known
	if (var.length() == 0)
	{
		return true;
	}

	//we know the value of a number
	if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
	{
		return true;
	}
	else
	{
		//depends on the wire value
		if (wires.find(var) != wires.end())
		{
			return true;
		}
		else
		{
			return false;
		}
	}
}

short getVar(std::string var)
{
	if (var.length() == 0)
	{
		//dosen't matter as the value should never be needed
		return 0;
	}

	char c = var.c_str()[0];

	if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9')
	{
		return (unsigned short) integer(var);
	}
	else
	{
		return wires[var];
	}
}

std::vector<command> readData()
{
	std::vector<command> commands;

	std::ifstream data("Data.txt");

	std::string input = "";

	while (std::getline(data, input))
	{
		command c;


		std::vector<std::string> split = splitStr(input, ' ');

		int arrowIndex = findArrowIndex(split);

		if (arrowIndex == 1) // setting value for wire
		{
			c.op = op::SET;
			c.dest = split[2];
			c.var1 = split[0];
		}
		else
		{
			if (arrowIndex == 2) // preform a NOT
			{
					std::string command = split[0];

					if (command == "NOT")
					{
						c.op = op::NOT;
						c.dest = split[3];
						c.var1 = split[1];
					}
			}
			else
			{
				if (arrowIndex == 3) // preform a gate
				{
					std::string command = split[1];

					std::string wireOut = split[4];

					if (command == "AND")
					{
						c.op = op::AND;
						c.dest = split[4];
						c.var1 = split[0];
						c.var2 = split[2];
					}

					if (command == "OR")
					{
						c.op = op::OR;
						c.dest = split[4];
						c.var1 = split[0];
						c.var2 = split[2];
					}

					if (command == "LSHIFT")
					{
						c.op = op::LSHIFT;
						c.dest = split[4];
						c.var1 = split[0];
						c.var2 = split[2];
					}

					if (command == "RSHIFT")
					{
						c.op = op::RSHIFT;
						c.dest = split[4];
						c.var1 = split[0];
						c.var2 = split[2];
					}
				}
			}
		}

		commands.push_back(c);
	}

	for (command c : commands)
	{
		printf("%s %i %s -> %s\n", c.var1.c_str(), c.op, c.var2.c_str(), c.dest.c_str());
	}

	printf("Size: %i\n", commands.size());

	return commands;
}

int main()
{
	std::vector<command> commands = readData();

	while (true)
	{
		for (command c : commands)
		{
			//if a is found
			if (wires.find("a") != wires.end())
			{
				printf("Wire a: %i\n", wires["a"]);

				int x = 0;
				std::cin >> x;

				return 0;
			}

			if (hasVar(c.var1) && hasVar(c.var2))
			{
				unsigned short var1 = getVar(c.var1);
				unsigned short var2 = getVar(c.var2);
				std::string dest = c.dest;

				switch (c.op)
				{
				case op::SET:
					wires[dest] = var1;
					break;
				case op::AND:
					wires[dest] = var1 & var2;
					break;
				case op::OR:
					wires[dest] = var1 | var2;
					break;
				case op::LSHIFT:
					wires[dest] = var1 << var2;
					break;
				case op::RSHIFT:
					wires[dest] = var1 >> var2;
					break;
				case op::NOT:
					wires[dest] = ~var1;
					break;
				}
			}
		}
	}


	// dump
	
	printf("----MAP DUMP----\n");

	for (auto itter = wires.begin(); itter != wires.end(); itter++)
	{
		printf("Wire: %s  Value: %i\n", itter->first.c_str(), itter->second);
	}

	printf("----MAP DUMP----\n"); 

	int x = 0;
	std::cin >> x;

    return 0;
}


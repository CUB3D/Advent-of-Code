// Day-8.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>

struct data
{
	int codeChars;
	int charCount;
};

std::string parse(std::string input)
{
	std::stringstream  ss;

	for (size_t i = 0; i < input.length(); i++)
	{
		char c = input.c_str()[i];

		if (c == '\\')
		{
			c = input.c_str()[i + 1];

			if (c == 'x')
			{
				i++;

				std::string asciiCode = "";

				asciiCode += input.c_str()[i++ + 1];
				asciiCode += input.c_str()[i++ + 1];

				// convert the contents of asciiCode into a number
				int asciiValue = 0;

				std::stringstream sss;
				sss << std::hex << asciiCode;
				sss >> asciiValue;

				char asciiChar = (char)asciiValue;

				ss << asciiChar;
			}

			if (c == '\"')
			{
				ss << "\"";
				i++;
			}

			if (c == '\\')
			{
				ss << "\\";
				i++;
			}
		}
		else
		{
			ss << c;
		}
	}

	return ss.str();
}

int main()
{
	std::ifstream data("Data.txt");

	std::string input = "";

	int totalCode = 0;
	int totalLiteral = 0;

	while (std::getline(data, input))
	{
		int length = input.length();
		int chars = parse(input).length() - 2;

		totalCode += length;
		totalLiteral += chars;

		printf("Code chars: %i\n", length);
		printf("Literal chars: %i\n", chars);
	}

	printf("Code - literal: %i\n", (totalCode - totalLiteral));

	int x = 0;
	std::cin >> x;

    return 0;
}


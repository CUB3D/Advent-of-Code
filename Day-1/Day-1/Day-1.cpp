// Day-1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <string>
#include <iostream>



int main()
{
	std::ifstream file("Data.txt");

	std::string data = "";
	std::getline(file, data);
	std::cout << "Read " << data.length() << " characters of data" << std::endl;

	const char* dataChar = data.c_str();

	int value = 0;
	int firstBasementValue = 0;

	for (int i = 0; i < data.length(); i++)
	{
		char c = dataChar[i];

		if (c == '(')
		{
			value++;
		}
		else
		{
			value--;
		}

		if (value == -1 && firstBasementValue == 0)
		{
			firstBasementValue = i + 1;
		}
	}

	std::cout << "Answer: " << value << std::endl;
	std::cout << "First basement value: " << firstBasementValue << std::endl;

	int x = 0;
	std::cin >> x;


    return 0;
}


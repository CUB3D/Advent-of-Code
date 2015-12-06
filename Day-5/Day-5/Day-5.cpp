// Day-5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>

bool hasDissalowed(std::string str)
{
	if (str.find("ab") != std::string::npos || str.find("cd") != std::string::npos || str.find("pq") != std::string::npos || str.find("xy") != std::string::npos) // if any naughtys are found
	{
		return true;
	}

	return false;
}

bool checkForRepeating(std::string str)
{
	for (int i = 0; i < str.length() - 1; i++)
	{
		char c = str.c_str()[i];

		if (c == str.c_str()[i + 1])
		{
			return true;
		}
	}

	return false;
}

int getVowelCount(std::string str)
{
	int vowels = 0;

	for (int i = 0; i < str.length(); i++)
	{
		char c = str.c_str()[i];

		if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
		{
			vowels++;
		}
	}

	return vowels;
}

int main()
{
	std::ifstream data("Data.txt");

	std::string input = "";

	int niceCount = 0;

	while (std::getline(data, input))
	{
		bool contains3Vowels = (getVowelCount(input) >= 3);
		bool containsARepeatingChar = checkForRepeating(input);
		bool hasDissalowedChars = hasDissalowed(input);

		bool isNice = contains3Vowels && containsARepeatingChar && !hasDissalowedChars;

		if (isNice)
		{
			niceCount++;
		}

		//std::cout << "Vowels: " << (contains3Vowels ? "true" : "false") << std::endl;
		//std::cout << "Repeating char: " << (containsARepeatingChar ? "true" : "false") << std::endl;
		//std::cout << "Has dissalowed: " << (hasDissalowedChars ? "true" : "false") << std::endl;

		std::cout << "Nice: " << (isNice ? "nice" : "naughty") << std::endl;
	}

	std::cout << "Number of nice strings: " << niceCount << std::endl;

	int x = 0;
	std::cin >> x;

    return 0;
}


// Day-5.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

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

void part_1(std::ifstream& data)
{
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
}

bool getHasRepeatingWithSpace(std::string str)
{
	for (int i = 0; i < str.length() - 2; i++)
	{
		char c = str.c_str()[i];

		//std::cout << "Checking " << c << std::endl;


		if (c == str.c_str()[i + 2])
		{
			return true;
		}
	}

	return false;
}

std::string setChar(std::string str, int pos, char rep)
{
	std::string s = "";

	for (int i = 0; i < str.length(); i++)
	{
		if (i == pos)
		{
			s += rep;
		}
		else
		{
			s += str.c_str()[i];
		}
	}

	return s;
}

bool getHasDoublePair(std::string str)
{
	for (int i = 0; i < str.length(); i++)
	{
		std::string pairA = "";

		pairA += (str.c_str()[i]);
		pairA += (str.c_str()[i + 1]);

		std::string mod = str;

		int numberOfMatchesThisPair = 0;

		for (int ii = 0; ii < mod.length() - 1; ii++)
		{
			char c = mod.c_str()[ii];
			char c1 = mod.c_str()[ii + 1];

			if (c == pairA.c_str()[0] && c1 == pairA.c_str()[1])
			{
				numberOfMatchesThisPair++;

				mod = setChar(mod, ii, '*');
				mod = setChar(mod, ii + 1, '*');
			}
		}

		if (numberOfMatchesThisPair >= 2)
		{
			return true;
		}
	}

	return false;
}

void part_2(std::ifstream& data)
{
	std::string input = "";

	int niceCount = 0;

	while (std::getline(data, input))
	{
		bool hasRepeatingWithSpace = getHasRepeatingWithSpace(input);
		bool hasDoublePair = getHasDoublePair(input);

		//std::cout << "Has repeating: " << (hasRepeatingWithSpace ? "true" : "false") << std::endl;
		//std::cout << "Has pair: " << (hasDoublePair ? "true" : "false") << std::endl;

		bool isNice = hasRepeatingWithSpace && hasDoublePair;

		if (isNice)
		{
			niceCount++;
		}

		std::cout << "Nice: " << (isNice ? "nice" : "naughty") << std::endl;
	}

	std::cout << "Number of nice strings: " << niceCount << std::endl;
}


int main()
{
	std::ifstream data("Data.txt");

	//part_1(data);

	part_2(data);

	int x = 0;
	std::cin >> x;

    return 0;
}


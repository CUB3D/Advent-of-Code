// Day-2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <algorithm>

struct present
{
	int length = 0;
	int width = 0;
	int height = 0;
};

present splitByX(std::string input)
{
	std::vector<std::string> data;

	std::string s;

	for (int i = 0; i < input.length(); i++)
	{
		if (input.c_str()[i] != 'x')
		{
			s += input.c_str()[i];
		}
		else
		{
			data.push_back(s);
			s = "";
		}
	}

	data.push_back(s);
	s = "";

	present p;

	std::stringstream(data[0]) >> p.length;
	std::stringstream(data[1]) >> p.width;
	std::stringstream(data[2]) >> p.height;

	return p;
}

int calcSlack(present pres)
{
	int areaA = pres.length * pres.width; // base and top
	int areaB = pres.length * pres.height; // sides
	int areaC = pres.width * pres.height; // front and back

	int smallestArea = std::min(std::min(areaA, areaB), areaC);

	return smallestArea;
}

int main()
{
	std::ifstream presentData("Data.txt");

	int totalFeet = 0;

	std::string input = "";

	while (std::getline(presentData, input))
	{
		present pres = splitByX(input);

		int area = (2 * pres.length * pres.width) + (2 * pres.width * pres.height) + (2 * pres.height * pres.length);
		int slack = calcSlack(pres);

		int totalArea = area + slack;

		totalFeet += totalArea;
	}


	std::cout << "Total feet: " << totalFeet << std::endl;

	int x = 0;

	std::cin >> x;

    return 0;
}


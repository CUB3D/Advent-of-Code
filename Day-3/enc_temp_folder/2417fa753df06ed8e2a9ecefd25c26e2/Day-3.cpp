// Day-3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

struct point
{
	int x, y;

	int value;
};

std::vector<point> locationToVists;

int x, y;

void addCurLocation()
{
	std::cout << "Santa is at (" << x << ", " << y << ")" << std::endl;

	bool exists = false;

	for (auto& a : locationToVists)
	{
		if (a.x == x && a.y == y) // has already visited
		{
			a.value++;
			exists = true;
			break; // exit (mainly for speed)
		}
	}

	if (!exists)
	{
		point p;

		p.x = x;
		p.y = y;
		p.value = 1;

		locationToVists.push_back(p);
	}
}

void move(const char instruction)
{
	if (instruction == '>')
	{
		// east (x + 1)
		x++;
	}

	if (instruction == '<')
	{
		// west (x - 1)
		x--;
	}

	if (instruction == '^')
	{
		// north (y + 1)
		y++;
	}

	if (instruction == 'v')
	{
		// south (y - 1)
		y--;
	}
}

int main()
{
	std::ifstream data("Data.txt");

	std::string input = "";

	addCurLocation(); // add start point

	while (std::getline(data, input))
	{
		for (int i = 0; i < input.length(); i++)
		{
			char c = input.c_str()[i];

			move(c);

			addCurLocation();
		}
	}

	int housesVisited = 0;

	for (auto a : locationToVists)
	{
		std::cout << "House at (" << a.x << ", " << a.y << ") had " << a.value << " visits" << std::endl;
		housesVisited++;
	}

	std::cout << "Houses visited total: " << housesVisited << std::endl;

	// pause
	int x = 0;
	std::cin >> x;

    return 0;
}


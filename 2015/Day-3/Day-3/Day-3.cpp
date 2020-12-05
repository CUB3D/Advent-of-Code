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
int x_r, y_r;


void addCurLocation(bool robo)
{
	if (robo)
	{
		std::cout << "Robo-santa is at (" << x_r << ", " << y_r << ")" << std::endl;

		bool exists = false;

		for (auto& a : locationToVists)
		{
			if (a.x == x_r && a.y == y_r) // has already visited
			{
				a.value++;
				exists = true;
				break; // exit (mainly for speed)
			}
		}

		if (!exists)
		{
			point p;

			p.x = x_r;
			p.y = y_r;
			p.value = 1;

			locationToVists.push_back(p);
		}
	}
	else
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
}

void move(const char instruction, bool robo)
{
	if (instruction == '>')
	{
		// east (x + 1)
		robo ? x_r++ : x++;
	}

	if (instruction == '<')
	{
		// west (x - 1)
		robo ? x_r-- : x--;
	}

	if (instruction == '^')
	{
		// north (y + 1)
		robo ? y_r++ : y++;
	}

	if (instruction == 'v')
	{
		// south (y - 1)
		robo ? y_r-- : y--;
	}
}

int main()
{
	std::ifstream data("Data.txt");

	std::string input = "";

	addCurLocation(false); // add start point (santa)
	addCurLocation(true); // add start point (robo)

	while (std::getline(data, input))
	{
		for (int i = 0; i < input.length(); i++)
		{
			char c = input.c_str()[i];

			move(c, false);

			addCurLocation(false);

			i++; // robo-santa

			c = input.c_str()[i];

			move(c, true);

			addCurLocation(true);
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


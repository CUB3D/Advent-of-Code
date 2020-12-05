// Day-6.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>

int width = 1000;
int height = 1000;

int map[1000][1000];

std::vector<std::string> split(std::string input, char delim)
{
	std::vector<std::string> strs;

	std::string s = "";

	for (int i = 0; i < input.length(); i++)
	{
		char c = input[i];

		if (c == delim)
		{
			strs.push_back(s);
			s = "";
			continue;
		}

		s += c;
	}

	strs.push_back(s);

	return strs;
}

int integer(std::string s)
{
	std::stringstream ss;

	ss << s;

	int result = 0;

	ss >> result;

	return result;
}

std::string string(int i)
{
	std::stringstream ss;

	ss << i;

	return ss.str();
}

enum Mode
{
	M_TOGGLE,
	M_TURN_ON,
	M_TURN_OFF
};

struct Point
{
	int x, y;
};

struct Instruction
{
	Mode mode;
	Point start;
	Point end;
};

void modArray(Instruction i)
{
	for (int x = i.start.x; x <= i.end.x; x++)
	{
		for (int y = i.start.y; y <= i.end.y; y++)
		{
			if (i.mode == M_TURN_ON)
			{
				map[x][y] += 1;
			}

			if (i.mode == M_TURN_OFF)
			{
				map[x][y] -= 1;

				map[x][y] = (int)fmax(0, map[x][y]);
			}

			if (i.mode == M_TOGGLE)
			{
				map[x][y] += 2;
			}
		}
	}
}

void dump()
{
	std::cout << "----DUMP BEGIN----" << std::endl;

	std::ofstream dump("Dump.txt");

	for (int y = 0; y < height; y++)
	{
		for (int x = 0; x < width; x++)
		{
			dump << string(map[x][y]);
		}

		dump << "\n";

		if (y % 100 == 0) // every 10 %
		{
			std::cout << (y / 10) << "%" << std::endl;
		}
	}

	dump.flush();
	dump.close();

	std::cout << "----DUMP END----" << std::endl;
}

int main()
{
	for (int x = 0; x < width; x++)
	{
		for (int y = 0; y < height; y++)
		{
			map[x][y] = 0;
		}
	}

	std::ifstream data("Data.txt");

	std::string input = "";

	while ((std::getline(data, input)))
	{
		std::vector<std::string> spl = split(input, ' ');

		Instruction inst;

		int i = 0;

		if (spl[i++] == "turn")
		{
			if (spl[i++] == "on")
			{
				inst.mode = M_TURN_ON;
			}
			else
			{
				inst.mode = M_TURN_OFF;
			}
		}
		else
		{
			inst.mode = M_TOGGLE;
		}

		//std::cout << "Mode: " << inst.mode << std::endl;

		std::vector<std::string> startPoint = split(spl[i++], ',');

		inst.start.x = integer(startPoint[0]);
		inst.start.y = integer(startPoint[1]);

		//std::cout << "Start X: " << inst.start.x << ", Y: " << inst.start.y << std::endl;

		i++; // skip through, never changes

		std::vector<std::string> endPoint = split(spl[i++], ',');

		inst.end.x = integer(endPoint[0]);
		inst.end.y = integer(endPoint[1]);

		//std::cout << "End X: " << inst.end.x << ", Y: " << inst.end.y << std::endl;

		std::cout << "Start X: " << inst.start.x << ", Y: " << inst.start.y << ", End X: " << inst.end.x << ", Y: " << inst.end.y << std::endl;

		modArray(inst);
	}

	dump();

	int lit = 0;

	for (int x = 0; x < width; x++)
	{
		for (int y = 0; y < height; y++)
		{
			lit += map[x][y];
		}
	}

	std::cout << "Total brightness: " << lit << std::endl;

	int x = 0;
	std::cin >> x;

	return 0;
}


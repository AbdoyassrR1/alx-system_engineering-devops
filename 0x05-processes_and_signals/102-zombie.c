#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 * Return: 0
 *
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates zombies
 * Return: 0
 */

int main(void)
{
	int c;
	pid_t child_pid;

	for (c = 0; c < 5; c++)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
		}
		else
			exit(0);
	}
	infinite_while();
	return (0);
}

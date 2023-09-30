#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies proccess.
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int count;
	pid_t pidme;

	count = 0;
	while (count < 5)
	{
		pidme = fork();
		if (pidme)
			printf("Zombie process created, PID: %i\n", pidme);
		else
			exit(0);
		count++;
	}
	sleep(100);
	return (0);
}

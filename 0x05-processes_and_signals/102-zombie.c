#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop for hanging
 *
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
		sleep(1);

	return (0);
}

/**
 * main - 5 zombie processes.
 *
 * Return: 0 (Success)
 */
int main(void)
{
	int i;
	pid_t zombie;

	for (i = 0; i < 5; i++)
	{
		zombie = fork();
		if (!zombie)
			return (0);
		else if (zombie < 0)
		{
			perror("Fork error");
			exit(EXIT_FAILURE);
		}
		printf("Zombie process created, PID: %d\n", zombie);
	}
	infinite_while();
	return (0);
}

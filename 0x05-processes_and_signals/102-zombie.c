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
 * main - 5 zombie_procss processes.
 *
 * Return: 0 (Success)
 */
int main(void)
{
	int i = 0;
	pid_t zombie_procss;

	for (; i < 5; i++)
	{
		zombie_procss = fork();
		if (!zombie_procss)
			return (0);
		else if (zombie_procss < 0)
		{
			perror("Fork error");
			exit(EXIT_FAILURE);
		}
		printf("Zombie process created, PID: %d\n", zombie_procss);
	}
	infinite_while();
	return (0);
}

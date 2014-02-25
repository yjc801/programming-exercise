#include <stdio.h>
#include <stdlib.h>

typedef struct Node{
	int val;
	struct Node *next;  	
}Node;

int findCycle(Node *head){
	Node *chaser;
	Node *runner;
	chaser = head;
	runner = head->next->next;
	while (runner && runner->next){
		if (runner == chaser) return 1;
		chaser = chaser->next;
		runner = runner->next->next;
	}
	return 0;
}

Node *returnNode(Node *head){
	if (head == NULL) return NULL;
	Node *chaser;
	Node *runner;
	chaser = head;
	runner = head;
	while (runner && runner->next){
		chaser = chaser->next;
		runner = runner->next->next;
		if (runner == chaser){
			chaser = head;
			while (chaser != runner){
				chaser = chaser->next;
				runner = runner->next;
			}
			return chaser;
		}
	}
	free(chaser);
	free(runner);
	return NULL;
}

int main(int argc, char const *argv[]){
	Node *head = (Node *)malloc(sizeof(Node));
	head->val = 1;
	head->next = (Node *)malloc(sizeof(Node));
	head->next->val = 2;
	head->next->next = (Node *)malloc(sizeof(Node));
	head->next->next->val = 3;
	head->next->next->next = (Node *)malloc(sizeof(Node));
	head->next->next->next->val = 4;
	head->next->next->next->next = head->next;
	
	Node *node;
	if (findCycle){
		node = returnNode(head);
		printf("%d\n",node->val);
	}

	// Fix
	Node *prev = node;
	while (prev->next != node){
		prev = prev->next;
	}
	prev->next = NULL;

	printf("%d\n", (findCycle(head)));

	return 0;
}
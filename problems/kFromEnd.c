#include <stdlib.h>
#include <stdio.h>

typedef struct Node{
	int val;
	struct Node *next;
}Node;

int kFromEnd(Node *head, int k){
	if (head == NULL) return 0;
	Node *chaser = head;
	Node *runner = head;
	for(; k != 0; k--){
		runner = runner->next;
	}
	while (runner){
		runner = runner->next;
		chaser = chaser->next;
	}
	return chaser->val;
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
	head->next->next->next->next = NULL;
	
	printf("%d\n", kFromEnd(head,3));

	return 0;
}

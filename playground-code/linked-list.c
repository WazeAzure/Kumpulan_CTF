#include <stdio.h>
#include <stdlib.h>

typedef struct Node* Next;
typedef struct {
	int val;
	Next next_node;
} Node;

int main(){
	Node head;
	head.val = 1;
	Node a1;
	a1.val = 2;
	Node a2;
	a2.val = 3;

	head.next_node = a1;
	a1.next_node = a2;

	Node* current = &head;
	while(current != null){
		printf("%d\n", (*current).val);
	}

	return 0;
}

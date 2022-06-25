#include <unistd.h>
#include <arpa/inet.h>
#include <stdio.h> 
#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 

void function(int socket_desc) 
{ 
	char buffer[80]; 
	int i; 
	for (;;)
	{ 
		bzero(buffer, sizeof(buffer)); 
		printf("YOU   : "); 
		i = 0; 
		while ((buffer[i++] = getchar()) != '\n'); 
		write(socket_desc, buffer, sizeof(buffer)); 
		bzero(buffer, sizeof(buffer)); 
		read(socket_desc, buffer, sizeof(buffer)); 
		printf("Server: %s", buffer); 
		if ((strncmp(buffer, "exit", 4)) == 0)
		{ 
			printf("\nClient left the chat...\n"); 
			printf("--SEE YOU SOON-- \n\n"); 
			break; 
		} 
		
	} 
}

int main() 
{ 
	int socket_desc, new_socket; 
	struct sockaddr_in server, client; 

	//create socket 
	socket_desc = socket(AF_INET, SOCK_STREAM, 0); 
	if (socket_desc == -1)
	{ 
		printf("Failed to create socket.\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully created.\n"); 
	bzero(&server, sizeof(server)); 

	// assign IP 
	printf("ENTER SERVER IP ADDRESS\n=> ");
	char serverip[20];
	scanf("%s", serverip);
	server.sin_family = AF_INET;  
	server.sin_addr.s_addr = inet_addr(serverip); 
	server.sin_port = htons(8888); 

	// connect client to server 
	if (connect(socket_desc, (struct sockaddr*)&server, sizeof(server)) != 0)
	{ 
		printf("Failed to connect to server.\n"); 
		exit(0); 
	} 
	else
	{
		printf("Connection is established. Waiting for a response...\n");
		printf("--WELCOME TO CHAT APP-- \n\n");
		printf("Press [CTRL + C] to quit chat\n\n----CHAT---\n"); 
	}
	
	//client-server chat function
	function(socket_desc); 

	// close socket 
	close(socket_desc);
 
}

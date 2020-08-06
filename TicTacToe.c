//Tic Tac Toe in c
#include<stdio.h>
#include<stdbool.h>

//global variable
	int i,j,brd[3][3],position;
	//User=97=A ||user=98=B 
	int user;
	//game is still on
	bool play=true;

//Game Board
void board()
{
	for(i=0;i<3;i++)
		for(j=0;j<3;j++)
			brd[i][j]=9;
}

//display board
void display()
{
	printf("\n");
	for(i=0;i<3;i++)
		{
			for(j=0;j<3;j++)
			{
				if(brd[i][j]==9)
					printf("|_|");
				else if(brd[i][j]==1)
					printf(" X ");
				else if(brd[i][j]==0)
					printf(" O ");
			}
			printf("\n");
		}
}

//switch user
void switch_user()
{
	if(user==65)
		user=66;
	else
		user=65;
}

//check row
int row()
{
	int a=0,b=0;
		for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
					{
						if(brd[i][j]==1)
							a++;
						else if(brd[i][j]==0)
							b++;
					}
				if(a==3)
					return 65;
				else if(b==3)
					return 66;
			}				
}

//check Diagonal
int diagonal()
{
	int a=0,b=0;
		for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
					if(brd[j][i]==1)
						a++;
					else if(brd[i][j]==0)
						b++;
				if(a==3)
					return 65;
				else if(b==3)
					return 66;
			}				
}

//check column
int column()
{
	int a=0,b=0;
	for(i=0;i<3;i++)
			{
				for(j=0;j<3;j++)
					{
						if(brd[j][i]==1)
							a++;
						else if(brd[j][i]==0)
							b++;
					}
				if(a==3)
					return 65;
				else if(b==3)
					return 66;
			}				
}

//check win
void win()
{
	int rst,flag=0;
	//right diagonal check
	rst=diagonal();
	//left diagonal check
	rst=diagonal();
	//column check
	rst=column();
	//row check
	rst=row();
	if(rst==65|| rst==66)
		{
			display();
			printf("\n%c's Win.",rst);
			play=false;
		}
	//else tie
	for(i=0;i<3;i++)
		for(j=0;j<3;j++)
			if(brd[i][j]==9)
				flag=1;
	if(flag==0 && (rst==65 || rst==66))
	{
		display();
		printf("\nIt's a Tie.");
		play=false;
	}
}

//inserting the input in the array
void insert()
{
	if(position==1)
		{
			if(user==65)
				brd[0][0]=1;
			else
				brd[0][0]=0;
		}
	else if(position==2)
		{
			if(user==65)
				brd[0][1]=1;
			else
				brd[0][1]=0;
		}
	else if(position==3)
		{
			if(user==65)
				brd[0][2]=1;
			else
				brd[0][2]=0;
		}
	else if(position==4)
		{
			if(user==65)
				brd[1][0]=1;
			else
				brd[1][0]=0;
		}
	else if(position==5)
		{
			if(user==65)
				brd[1][1]=1;
			else
				brd[1][1]=0;
		}
	else if(position==6)
		{
			if(user==65)
				brd[1][2]=1;
			else
				brd[1][2]=0;
		}
	else if(position==7)
		{
			if(user==65)
				brd[2][0]=1;
			else
				brd[2][0]=0;
		}
	else if(position==8)
		{
			if(user==65)
				brd[2][1]=1;
			else
				brd[2][1]=0;
		}
	else if(position==9)
		{
			if(user==65)
				brd[2][2]=1;
			else
				brd[2][2]=0;
		}
}

//play game
void game()
{
	user=65;
	board();
	//display();
	while(play!=false)
	{
		display();
		printf("\nIt's %c's turn.",user);
		printf("\nEnter your choice: ");
		scanf("%d", &position);
		insert();
		win();
		switch_user();
	}
}

void main()
{
	game();
}

#include "contact.h"

void menu()
{
	printf("*******************************************************\n");
	printf("**************1.add                 2.del**************\n");
	printf("**************3.search              4.modify***********\n");
	printf("**************5.show                6.sort*************\n");
	printf("**************           0.exit          **************\n");
	printf("*******************************************************\n");


}

int main()
{
	int input = 0;
	struct contact con;//con就是通讯录，里面包含data指针，size,capacipy
	//int size = 0;
	//struct peoinfo con[MAX];//存放一千个人信息

	initcontact(&con);
	do
	{
		menu();
		printf("请选择\n");
		scanf("%d", &input);
		switch (input)
		{
		case exit://0,在枚举中起始位置从零开始，exit与0相对应。
			printf("退出");
			break;
		case add:
			addcontact(&con);//增加一个人信息
			break;
		case del:
			delcontact(&con);
			break;
		case search:
			searchcontact(&con);
			break;
		case modify:
			modifycontact(&con);
			break;
		case show:
			showcontact(&con);
			break;
		case sort:
			//	sortcontact(&con);
			break;
		default:
			printf("选择错误\n");
			break;
		}
	} while (input);
	return 0;
}
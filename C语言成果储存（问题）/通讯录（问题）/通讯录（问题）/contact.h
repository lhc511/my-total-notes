#define _CRT_SECURE_NO_WARNINGS 1


#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//#define MAX 200

#define DEFAULT_SIZE 3

#define MAX_NAME 20
#define MAX_SEX 5
#define MAX_TELE 12
#define MAX_ADDR 30

enum option
{
	exit,//0,在枚举中起始位置从零开始，exit与0相对应。
	add,//1
	del,//2
	search,//3
	modify,//4
	show,//5
	sort//6             枚举中与test.c中的菜单选项相对应
};

typedef struct peoinfo
{
	char name[MAX_NAME];
	int age;
	char sex[MAX_SEX];
	char tele[MAX_TELE];
	char addr[MAX_ADDR];
}peoinfo;

typedef struct contact
{
	struct peoinfo* data;//存放一个信息
	int capacity;//当前通讯录最大容量
	int size;//记录当前已有元素个数。
}contact;

//函数声明
void initcontact(struct contact* ps);
void addcontact(struct contact* ps);
void showcontact(const struct contact* ps);//因为不会修改对象只显示所以加const.
void delcontact(struct contact* ps);
void modifycontact(struct contact* ps);
void searchcontact(struct contact* ps);//查找指定联系人

////void sortcontact(struct contact* ps);

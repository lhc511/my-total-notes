#include "contact.h"

void initcontact(struct contact* ps)
{
	ps->data = (struct peoinfo*)malloc(DEFAULT_SIZE * sizeof(peoinfo));
	if (ps->data == NULL);
	{
		return 0;
	}
	ps->size = 0;
	ps->capacity = DEFAULT_SIZE;

	//memset(ps->data, 0, sizeof(ps->data));//把data这块空间全部设置为0.
	//ps->size = 0;//设置通讯录最初有0个元素
}



static int findname(struct contact* ps, char name[MAX_NAME])
{
	int i = 0;
	for (i = 0; i < ps->size; i++)
	{
		if (0 == strcmp(ps->data[i].name, name))//等于零时内容相同
			return i;
	}
	return -1;
}

void checkc(struct contact* ps)
{
	if (ps->size == ps->capacity)
	{
		struct peoinfo* ptr = realloc(ps->data, (ps->capacity + 2) * sizeof(struct peoinfo));//realloc(源空间大小，新设置空间大小)            其返回类型为void*
		if (ptr != NULL)//增容成功
		{
			ps->data = ptr;
			ps->capacity += 2;
			printf("增容成功。");
		}
		else
		{
			printf("增加失败");
		}
	}
}

void addcontact(struct contact* ps)
{
	checkc(ps);//检测当前通讯录容量

	printf("请输入名字\n");
	scanf("%s", ps->data[ps->size].name);//指向data数组中的元素（结构体）（size为第几个联系人），在通过接头体访问name（结构体内的信息）

	printf("请输入年龄\n");
	scanf("%d", &(ps->data[ps->size].age));

	printf("请输入性别\n");
	scanf("%s", ps->data[ps->size].sex);
	printf("请输入电话\n");
	scanf("%s", ps->data[ps->size].tele);
	printf("请输入地址\n");
	scanf("%s", ps->data[ps->size].addr);

	ps->size++;
	printf("添加成功\n");

}

//void addcontact(struct contact* ps)
//{
//	if (ps->size == MAX)
//	{
//		printf("通讯录已满\n");
//	}
//	else
//	{
//		printf("请输入名字\n");
//		scanf("%s",ps->data[ps->size].name);//指向data数组中的元素（结构体）（size为第几个联系人），在通过接头体访问name（结构体内的信息）
//
//		printf("请输入年龄\n");
//		scanf("%d",&(ps->data[ps->size].age));
//
//		printf("请输入性别\n");
//		scanf("%s",ps->data[ps->size].sex);
//		printf("请输入电话\n");
//		scanf("%s",ps->data[ps->size].tele);
//		printf("请输入地址\n");
//		scanf("%s",ps->data[ps->size].addr);
//
//		ps->size++;
//		printf("添加成功\n");
//	}
//}

void showcontact(const struct contact* ps)
{
	if (ps->size == 0)
	{
		printf("通讯录为空\n");
	}
	else
	{
		int i = 0;
		printf("%-20s\t%-4s\t%-5s\t%-12s\t%-20s\n", "名字", "年龄", "性别", "电话", "地址");
		for (i = 0; i < ps->size; i++)
		{
			printf("%-20s\t%-4d\t%-5s\t%-12s\t%-20s\n\n",
				ps->data[i].name,
				ps->data[i].age,
				ps->data[i].sex,
				ps->data[i].tele,
				ps->data[i].addr);
		}
	}
}

void delcontact(struct contact* ps)//删除联系人
{
	char name[MAX_NAME];
	printf("请输入要删徐的联系人");
	scanf("%s", name);
	//1、查找删除掉人在什么位置
	//找到了返回名字元素下标，没找到返回-1。

	int pos = findname(ps, name);
	if (pos == -1)
		printf("要删除的人不存在\n");
	else
	{
		int j = 0;
		for (j = pos; j < ps->size - 1; j++)
		{
			ps->data[j] = ps->data[j + 1];
		}
		ps->size--;
		printf("删除成功\n");
	}
}

void searchcontact(struct contact* ps)
{
	char name[MAX_NAME];
	printf("请输入查找人的名字");
	scanf("%s", name);
	int pos = findname(ps, name);
	if (pos == -1)
	{
		printf("要查找的人不存在\n");
	}
	else
	{
		printf("%-20s\t%-4s\t%-5s\t%-12s\t%-20s\n", "名字", "年龄", "性别", "电话", "地址");
		printf("%-20s\t%-4d\t%-5s\t%-12s\t%-20s\n",
			ps->data[pos].name,
			ps->data[pos].age,
			ps->data[pos].sex,
			ps->data[pos].tele,
			ps->data[pos].addr);
	}
}

void modifycontact(struct contact* ps)
{
	char name[MAX_NAME];
	printf("请输入要修改人的名字");
	scanf("%s", name);

	int pos = findname(ps, name);

	if (pos == -1)
		printf("要修改的人不存在\n");
	else

	{
		printf("请输入名字\n");
		scanf("%s", ps->data[pos].name);//指向data数组中的元素（结构体）（size为第几个联系人），在通过接头体访问name（结构体内的信息）

		printf("请输入年龄\n");
		scanf("%d", &(ps->data[pos].age));

		printf("请输入性别\n");
		scanf("%s", ps->data[pos].sex);
		printf("请输入电话\n");
		scanf("%s", ps->data[pos].tele);
		printf("请输入地址\n");
		scanf("%s", ps->data[pos].addr);

		printf("修改成功\n");
	}
}

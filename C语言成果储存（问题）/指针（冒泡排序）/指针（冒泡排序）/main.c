#define _CRT_SECURE_NO_WARNINGS 1
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

//void buble_sort(int arr[10],int sz)
//{
//	int i = 0;
//	for (i == 0; i < sz-1; i++)
//	{
//		int j = 0;
//		for (j = 0; j <sz-1-i ; j++)
//		{
//			if (arr[j] > arr[j + 1])
//			{
//				int tmp = arr[j];
//				arr[j] = arr[j + 1];
//				arr[j + 1] = tmp;
//			}
//		}
//	}
//}

struct stu
{
	char name[20];
	int age;
};


int cmp_int(const void* e1, const void* e2)//比较两个整型值
{
	return (*(int*)e1 - *(int*)e2);////////////////////////////////////////////
}

void test1()
{
	int arr[10] = { 9,8,7,6,5,4,3,2,1,0 };
	int sz = sizeof(arr) / sizeof(arr[0]);
	qsort(arr, sz, sizeof(arr[0]), cmp_int);
	//排序数组arr, 有sz个元素，元素所占字节大小， 比较两个元素大小的函数
	int i = 0;
	for (i = 0; i < sz; i++)
	{
		printf("%d ", arr[i]);

	}
	printf("\n\n");
}

int cmp_float(const void* e1, const void* e2)//比较两个浮点值
{
	if (*(float*)e1 == *(float*)e2)                           //方法2：return (int)(*(float*)e1 - *(float*)e2);
		return 0;
	else if (*(float*)e1 < *(float*)e2)
		return -1;
	else
		return 1;
}


void test2()
{
	float f[] = { 9.0,8.0,7.0,6.0,5.0,4.0 };
	int sz = sizeof(f) / sizeof(f[0]);
	qsort(f, sz, sizeof(f[0]), cmp_float);
	int i = 0;
	for (i = 0; i < sz; i++)
	{
		printf("%f ", f[i]);
	}
	printf("\n");
}

int cmp_stu_by_age(const void* e1, const void* e2)
{
	return ((struct stu*)e1)->age - ((struct stu*)e2)->age;
}

int cmp_stu_by_name(const void* e1, const void* e2)
{
	//比较名字就是比较字符串
	//比较字符串不可以直接用<>=来比较，用strcmp比较。
	return strcmp(((struct stu*)e1)->name, ((struct stu*)e2)->name);
}

void test3()
{
	struct stu s[3] = { {"zhang",20},{"li",30},{"wang",10} };
	int sz = sizeof(s) / sizeof(s[0]);
	qsort(s, sz, sizeof(s[0]), cmp_stu_by_name);
}

void swap(char* buf1, char* buf2, int width)
{
	int i = 0;
	for (i = 0; i < width; i++)
	{
		char tmp = *buf1;
		*buf1 = *buf2;
		*buf2 =tmp ;
		buf1++;
		buf2++;
	}
}

void buble_sort(void* base, int sz, int width, int(*cmp)(void* e1, void* e2))
{
	int i = 0;
	for (i == 0; i < sz - 1; i++)
	{
		int j = 0;
		for (j = 0; j < sz - 1 - i; j++)
		{
			if (cmp((char*)base + j * width, (char*)base + (j + 1) * width) > 0)///////////////////////////////////////////////////
			{
				swap((char*)base + j * width, (char*)base + (j + 1) * width, width);
			}
		}
	}
}



void test4()
{
	int arr[10] = { 9,8,7,6,5,4,3,2,1,0 };
	int sz = sizeof(arr) / sizeof(arr[0]);
	buble_sort(arr, sz, sizeof(arr[0]), cmp_int);//使用该函数的人知道自己使用的是什么数据

}

void test5()
{
	struct stu s[3] = { {"zhang",20},{"li",30},{"wang",10} };
	int sz = sizeof(s) / sizeof(s[0]);
	buble_sort(s, sz, sizeof(s[0]),cmp_stu_by_age );//使用该函数的人知道自己使用的是什么数据
}

int main()
{
	/*test1();
	test2();
	test3();*/
	test4();
	test5();
	return 0;
}

//void qsort(void *base,//目标数组起始位置
//			size_t num,//数组元素个数
//			size_t width,//一个数组元素所占字节大小
//			int(*cmp)(const void *e1,const void *e2)//
//                       //要比较的两个元素的地址//
//);
#include<stdio.h>
int* add(int *,int *);
int* sub(int *,int *);
static int a,b;
void main(){
    int *aa,*bb;
    printf("Enter a,b");
    scanf("%d%d",&a,&b);
    aa=add(&a,&b);
    printf("Sum: %d",*aa);
    bb=sub(&a,&b);
    printf("Diff: %d",*bb);
}
int* add(int *p,int *q){
    int *r;
    *r=*p+*q;
    return r;
}
int* sub(int *p,int *q){
    int *r;
    *r=*p-*q;
    return r;
}
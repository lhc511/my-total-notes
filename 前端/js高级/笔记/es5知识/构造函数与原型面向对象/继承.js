//父类:公共属性和方法
function Person() {
    this.name = "why"
}

Person.prototype.eating = function() {
    console.log(this.name + " eating~")
}

// 子类:特有属性和方法
function Student() {
    this.sno = 111
    this.friends=[]
}

// 将Student的原型对象指向新创建的Person对象
Student.prototype = new Person()//实现继承，必须在·构造函数创建后写

Student.prototype. studying = function() {
    console.log(this.name + " studying~")
}
//
var stu = new Student()
// console. log(stu.name)
// console. log(stu.eating())


//原型链实现继承的弊端:
//1.打印stu对象,继承的属性是看不到的，只能打印原本构造函数中可枚举的属性
// 直接打印对象 (console.log(dog)) 默认只显示自有属性，不会递归遍历原型链
// console.log(stu)     //{sno: 111}
// console.log(stu.name) //why

// 2.创建出来两个stu的对象，原本会互相影响，因为指向了同一个Student.prototype(new Person())原型对象，但现在不会影响了
// var stu1 = new Student()
// var stu2 = new Student()
//
// stu1.friends.push("kobe")//现在会在student对象中直接添加friends列表，因此不会影响
// //但是回因此导致无法继承父级属性
//
// console.log(stu1)//Student{sno: 111, friends: Array(1)}
// console.log(stu2)//Student{sno: 111, friends: Array(0)}
// console.log(stu1.friends)
// console.log(stu2.friends)

// stu1.name = "kobe"
// console.log(stu2.name)
// //直接给student中添加属性，并没有在对象原型(person对象)中修改name属性，因此不会产生影响
// console.log(stu1)//Student{sno: 111, friends: Array(0), name: 'kobe'}

// /1 3.第三个弊端:在前面实现类的过程中都没有传递参数
//因为name属性是继承来的，建立stu对象无法将参数传输给原型对象(person对象)中的name属性
var stu3 = new Student("lilei", 112)
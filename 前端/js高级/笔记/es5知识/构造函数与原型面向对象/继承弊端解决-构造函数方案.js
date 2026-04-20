//父类:公共属性和方法
function Person(name,age,friends) {
    //this指向Student
    this.name = name
    this.age = age
    this.friends = friends
}

Person.prototype.eating = function() {
    console.log(this.name + " eating~")
}
// 子类:特有属性和方法
function Student(name, age, friends, sno) {
    //1,继承传参/打印/对象数据污染/问题解决，如果不写对应属性则返回undefined
    //将Person绑定为Student的this
    Person.call(this,name,age,friends)

    this.sno = 111
}

//相当于创建了一个Person对象，在查找数据数通过__proto__属性向上(原型对象Person.prototype)查找
var p = new Person()
Student.prototype = p

Student.prototype.studying = function() {
    console.log(this.name + " studying~")
}

const stu=new Student('a',12,'aaa',10)
const stu2=new Student('b',112,'abb',100)
console.log(stu.name)


//强调:借用构造函数也是有弊端:
//·1.第一个弊端 :· Person函数至少被调用了两次
//2.第二个弊端:stu的原型对象上会多出一些属性,但是这些属性是没有存在的必要
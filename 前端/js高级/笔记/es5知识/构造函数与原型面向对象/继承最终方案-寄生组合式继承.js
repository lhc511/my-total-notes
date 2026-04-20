//继承工具函数
function inheritPrototype(SubType, SuperType) {
    SubType.prototype = Object.create(SuperType.prototype)
    Object.defineProperty(SubType.prototype, "constructor", {
        enumerable: false,
        configurable: true,
        writable: true,
        value: SubType
    })
}

function Person(name, age, friends) {
    this.name = name
    this.age = age
    this.friends = friends
}

Person.prototype.running = function() {
    console.log("running~")
}

Person.prototype.eating = function() {
    console.log("eating~")
}

function Student(name, age, friends, sno, score) {
    Person.call(this, name, age, friends)
    this.sno = sno
    this.score = score
}
// //创建返回一个空对象{}并赋值给Student的原型对象，同时让这个对象的__proto__属性指向Person.prototype
// Student.prototype = Object.create(Person.prototype)
// //constructor指向错误解决方案
// Object.defineProperty(Student.prototype, "constructor",{
//     enumerable: false,
//     configurable: true,
//     writable: true,
//     value: Student
// })

inheritPrototype(Student,Person)

Student.prototype.studying = function() {
    console. log("studying~")
}

var stu = new Student("why", 18, ["kobe"], 111, 100)
console. log(stu)//Student{name: 'why', age: 18, friends: Array(1), sno: 111, score: 100}

//此处stu.constructor指向Person:原因是Student的原型对象在上方被修改为一个 指向了Person类原型对象的 空对象{}
//而Student原本运行对象中的constructor属性因为销毁，只剩一个空对象，在原型链查找过程中便指向其父类的原型对象中的constructor属性，因此指向person
// 解决方案在上方，即在 Student原型对象 中定义一个新的constructor属性并让其指向自身构造函数Student
console. log(stu.constructor)//Person(name, age, friends) {this.name = name,this.age = age,this.friends = friends}
stu.studying()
stu.running()
stu.eating()
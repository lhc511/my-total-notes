
// 我们每个对象中都有一个 [[prototype]]/__proto__,这个属性可以称之为对象的原型(隐式原型)
// function foo() {
//     console.log("foo~,函数体代码")
// }
// //、foo就是一个普通的函数
// // foo()
//
// //、换一种方式来调用foo函数 : 通过new关键字去调用一个函数,那么这个函数就是一个构造函数了
// var f1 = new foo
// console.log(f1)
//
// //创建一个构造函数
// function Person(name, age, height, address) {
//     this.name = name
//     this.age = age
//     this.height = height
//     this.address = address
//
//     this.eating = function () {
//         console.log(this.name + "在吃东西~")
//
//     }
//
//     this.running = function () {
//         console.log(this.name + "在跑步")
//
//     }
// }
// var p1 =new Person("张三",18,1.88,"广州市")
// console.log(p1)

//原型
//***********************对象原型理解***************************
// 原型是什么
// var obj = { name: "why" } // [[prototype]]
// var info = {} // [[prototype]]
//
// //早期的ECMA是没有规范如何去查看 [[prototype]]
//
// //给对象中提供了一个属性,可以让我们查看一下这个原型对象(浏览器提供)
// //_proto __
// console.log(obj. __proto__ ) // {}
// console. log(info.__proto__ ) // {}
//
// var obj = {name: "why", __proto__: {} }
// //ES5之后提供的Object.getPrototypeOf
// console.log(Object.getPrototypeOf(obj))

//2.原型有什么用呢?
// var obj = {name: "why", __proto__: {} }
// // 当我们从一个对象中获取某一个属性时,它会触发·[[get]] 操作
// //1. 在当前对象中去查找对应的属性,·如果找到就直接使用
// // 2 .· 如果没有找到,那么会沿着它的原型去查找 [[prototype]]
// console.log(obj.age)

//***********************函数原型理解******************************
// function foo() {
// }
//
// //函数也是一个对象
// //·console.log(foo .__proto__ )//函数作为对象来说,它也是有[[prototype]]·隐式原型
//
// //、函数：它因为是一个函数,所以它还会多出来一个显示原型属性:prototype
// console.log(foo.prototype)//{}
//
// var f1 = new foo()
// var f2 = new foo()
//
// console.log(f1.__proto__===foo.prototype)//true
// console.log(f2.__proto__===foo.prototype)//true

// function Person() {
//
// }
//
// var p1 = new Person()
// var p2 = new Person()
//
// // 都是为true
// // console.log(p1 .__proto__===Person. prototype)
// // console.log(p2 .__proto__===Person.prototype)
//
// // p1.name .= "why"
// // p1 .__ proto __. name = "kobe"
//
// Person.prototype.name = "james"
// console.log(p1.name)

function foo() {
}
//、foo.prototype这个对象中有一个constructor属性
// console. log(foo.prototype)
// console.log(Object.getOwnPropertyDescriptors(foo.prototype))

// Object.defineProperty(foo.prototype, "constructor", {
// enumerable: true,
// configurable: true,
// writable: true,
// ~. value:"哈哈哈哈"

// console. log(foo.prototype)

// prototype.constructor=构造函数本身
// console.log(foo.prototype.constructor) // [Function: foo]
// console.log(foo.prototype.constructor.name)
// console. log(foo.prototype.constructor.prototype.constructor.prototype.constructor)

// 2.我们也可以添加自己的属性
// foo. prototype.name = "why"
// foo.prototype.age = 18
// foo.prototype.height = 18
// foo. prototype. eating = function() {}
// var f1 = new foo()
// console.log(f1.name, fl.age)

//、3.直接修改整个prototype对象,此处创建了一个新的prototype对象并让函数指向新对象，原先的由于根目录无法找到会被销毁
foo.prototype = {
    //由于自己创建的函数没有constructor属性所以此处要手动添加，下面的有更接近原先的方式
    //此处的枚举是true，可遍历，而原函数是false不可遍历
    // constructor: foo,
    name: "why",
    age: 18,
    height: 1.88
}
var f1 = new foo()
console.log(f1.name, f1.age, f1.height)

// 真实开发中我们可以通过object.defineProperty方式添加constructor
Object.defineProperty(foo.prototype, "constructor", {
    enumerable: false,
    configurable: true,
    writable: true,
    value: foo
})

function Person(name, age, height, address) {
    this.name = name
    this.age = age
    this.height = height
    this.address = address
}

Person.prototype.eating = function() {
    console.log(this.name +"在吃东西~")//this只与调用位置有关
}

Person.prototype.running = function() {
    console.log(this.name + "在跑步~")
}
var p1 = new Person("why",18,1.88,"北京市")
var p2 =new Person("kobe",20,1.98,"洛杉矶市")

p1.eating()
p2.eating()

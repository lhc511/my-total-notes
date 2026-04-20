//定义类
// class Person {//相当于function Person(){}
// }
// //类的表达式
// // var Animal = class {}
//
// // 研究一下类的特点
// console. log(Person.prototype)//{} person类的原型对象
// console. log(Person.prototype.__proto__)//{}全局对象   对象的__proto__指向全局对象
// console. log(Person.prototype.constructor)//class Person {}指回类
// console. log(typeof Person)//function
//
// var p = new Person()
// //不用管这个识别错误，软件有问题
// console.log(p.__proto__===Person.prototype)// true


// 类的声明-构造函数/构造方法
// class Person
// {
//     // 类的构造方法
//     // 注意:一个类只能有一个构造函数
//     //-1.在内存中创建一个对象 moni ·= {}
//     //2.将类的原型prototype赋值给创建出来的对象 moni .__ proto __= Person.prototype
//     //3.将对象赋值给函数的this:new绑定 this =moni
//     // 4.执行函数体中的代码
//     //-5.自动返回创建出来的对象
//     constructor(name, age)
//     {
//         this.name = name
//         this.age = age
//     }
// }
// var p1 = new Person("why", 18)
// var p2 = new Person("kobe", 30)
// console.log(p1,p2)

//方法的定义******************************************
// var names = ["abc", "cba", "nba"]
// class Person {
//     //js中定义的属性不能写在constructor外面
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//         this._address='广州市'
//     }
//
//     //以下函数直接被放到Person的原型对象当中，可被直接调用
//     //普通的实例方法
//     //创建出来的对象进行访问
//     // var p .= new Person ()
//     // p.eating()
//     eating() {
//         console.log(this.name + " eating~")
//     }
//
//     running() {
//         console.log(this.name + " running~")
//     }
//
//     // 类的访问器方法  可以在赋值和读取时做拦截并做一些其他操作
//     get address() {
//         return this._address
//     }
//     set address(newAddress) {
//         this._address = newAddress
//     }
//
//     //类的静态方法(类方法)
//     // Person. createPerson()
//     // static createPerson(){
//     static randomPerson(){
//         var nameIndex = Math. floor (Math.random() * names.length)
//         var name = names [nameIndex]
//         var age = Math. floor(Math. random() * 100)
//         return new Person(name, age)
//     }
// }
//
// var p = new Person("why", 18)
// p.eating()
// p.running()
//
// //console.log(Object.getOwnPropertyDescriptors(Person.prototype))
//
// for (var i = 0; i < 50; i++) {
//     console.log(Person.randomPerson())
// }

//class实现继承
// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }
//
//     running() {
//         console.log(this.name + " running~")
//     }
//
//     eating() {
//         console.log(this.name + "eating~")
//     }
//
//     personMethod() {
//         console.log("处理逻辑1")
//         console.log("处理逻辑2")
//         console.log("处理逻辑3")
//     }
//
//
//     static staticMethod() {
//         console.log("PersonStaticMethod")
//     }
// }
//
//
// class Student extends Person {
//     //JS引擎在解析子类的时候就有要求,如果我们有实现继承
//     //、那么子类的构造方法中,在使用this之前
//     constructor (name, age, sno) {
//         super ()
//         this.sno = sno
//     }
//
//     studying() {
//         console. log(this.name +" studying~")
//     }
//
//     //-类对父类的方法的重写
//     running() {
//         console.log("student " + this.name + " running")
//     }
//
//     //-重写personMethod方法
//     personMethod() {
//         //复用父类中的处理逻辑
//         super .personMethod ()//直接执行父类继承函数中的所有代码
//
//         console.log("处理逻辑4")
//         console.log("处理逻辑5")
//         console.log("处理逻辑6")
//     }
//
//     //-重写静态方法
//     static staticMethod() {
//         super.staticMethod()
//         console.log("StudentStaticMethod")
//     }
// }
//
// var stu = new Student("why", 18, 111)
// console. log(stu)
//
// console. log(Object.getOwnPropertyDescriptors(stu .__proto__))
// console. log(Object.getOwnPropertyDescriptors(stu .__proto__.__proto__))
// stu.eating()

//一些内部转换
//在浏览器不支持es6新规时会做如下转换-babel转换
//案例一 class Person{}的转换
// function _classCallCheck(instance, Constructor) {
//     console.log(instance)
//     console.log(Constructor)
//     //检擦this指向是不是其构造函数
//     if (!(instance instanceof Constructor)) {
//         throw new TypeError("Cannot call a class as a function");
//     }else{
//         console.log("iascvb")
//     }
// }
//
//这里的Person变量和构造函数名Person是同一个地址，都指向Person构造函数
// var Person = function Person() {
        //类本身的构造函数引用"指指向构造函数自身的标识符或内存地址
//     _classCallCheck(this, Person);
// }
// console.log(Person)// ƒ Person() {_classCallCheck(this, Person);}
//
// const a=new Person()
// // Person{}
// // ƒ Person() {_classCallCheck(this, Person);}
//
// console.log(a)//Person {}
// console.log("+++++++++++++++++++++++++++++++++++++++++++")
// // Person()//直接调用是window，严格模式下是undefined
// Person()
// // Window {window: Window, self: Window, document: document, name: '', location: Location, …}
// // ƒ Person() {_classCallCheck(this, Person);}

//案例二
// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }
//
//     eating() {
//         console.log(this.name + " eating~")
//     }
// }
//转换后得到js代码
// "use strict";
//
// function _classCallCheck(instance, Constructor) {
//     if (!(instance instanceof Constructor)) {
//         throw new TypeError("Cannot call a class as a function");//无法将一个类作为函数调用
//     }
// }
// function _defineProperties(target, props) {
//     for (var i = 0; i < props.length; i++) {
//         //descriptor是一个对像，里面有属性描述符
//         var descriptor = props[i];//得到数组中的对象
//         //给数组中的对象添加/修改属性
//         descriptor.enumerable = descriptor.enumerable || false;
//         descriptor.configurable = true;
//         if ("value" in descriptor) descriptor.writable = true;
            // target:Constructor.prototype 函数原型对象的键 进行配置
//         Object.defineProperty(target, descriptor.key, descriptor);
//     }
// }
//
// // Constructor
// // 表示类对应的构造函数。这是类的核心标识，所有属性和方法最终都会绑定到该构造函数或其原型上。
// // protoProps
// // 包含需要添加到原型链上的方法描述符数组（即实例方法）。这些方法通过 Object.defineProperty 挂载到 Constructor.prototype 上
// // staticProps
// // 包含需要直接绑定到构造函数本身的静态方法描述符数组。这些方法通过 Object.defineProperty 直接挂载到 Constructor 上
// function _createClass(Constructor, protoProps, staticProps) {
//     // 如果传来的参数有值 执行后面代码
//     //                                    传递函数的原型对象     下方传来的数组
//     if (protoProps) _defineProperties(Constructor.prototype, protoProps);
//     //                                传进来的函数地址
//     if (staticProps) _defineProperties(Constructor, staticProps);
//     return Constructor;
// }
//
// //、/*# __ PURE __* / 纯函数
// //·webpack·压缩 tree-shaking（以后再了解）
// //-这个函数没副作用
// //此处是一个立即执行函数，之所以用一个函数给他包起来是让其成为一个局部函数 防止其中的内容和全局变量造成影响
// var Person = /*# PURE _*/ (function () {//
//     function Person(name, age) {
//         _classCallCheck(this, Person);
//         this.name = name;
//         this.age = age;
//     }
//     //person只一个地址指向内存中的构造函数
//     _createClass(Person, [
//         {
//             key: "eating",
//             value: function eating() {
//                 console.log(this.name + " eating-");
//             }
//         }
//     ]);
//     return Person;
// })();

//案例三-继承
// class Person {
//     constructor(name, age) {
//         this.name = name
//         this.age = age
//     }
//
//     running() {
//         console.log(this.name + " running~")
//     }
// }
//
// class Student extends Person {
//     constructor(name, age, sno) {
//         super(name, age)
//         this.sno = sno
//     }
//     studying() {
//         console.log(this.name + " studying~")
//     }
// }
// 转换后代码
//太多了不搞了


//
// class HYArray  extends Array{
// // class HYArray {
// //    以下两个是自定义方法，原本的Array中是没有的
//     firstItem() {
//         return this[0]
//     }
//     lastItem() {
//         return this[this.length - 1]
//     }
// }
// var arr = new HYArray(1,2,3)
// console.log(arr.firstItem())
// console. log(arr.lastItem())


//方案一        有较多限制 了解就好
function mixinRunner(BaseClass) {
    class NewClass extends BaseClass {
        running() {
            console.log("running~")

        }
    }
    return NewClass
}

function mixinEater (BaseClass) {
    // return class Eater extends BaseClass {//由于Eater不在其他地方使用，所以可以省略，如下
    return class extends BaseClass {
        eating() {
            console.log("eating~")
        }
    }
}
//在JS中类只能有一个父类:单继承
class Person{}
class Student extends Person {
}
//以下两行均为实现多继承的方式
var NewStudent = mixinRunner(Student)//混入Runner类
var NewStudent1 = mixinEater(mixinRunner(Student))//混入Runner类和Eater类

var ns = new NewStudent()
var ns1 = new NewStudent1()
ns.running()
ns1.eating()
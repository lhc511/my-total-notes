


// var obj = {
//     name: "why",
//     age: 18
// }
// //创建一个空对象，将自身的原型对绑定到 obj对象 的同时 给自身(info)创建一个address属性,创建的属性要用属性描述符来操控
// var info = Object.create(obj, {
//     address: {
//         value: "北京市",
//         enumerable: true
//     }
// })
// //判断自身是否有这个属性
// console.log(info.hasOwnProperty("address"))//true
// console.log(info.hasOwnProperty("name"))//false
//
// //-in 操作符:不管在当前对象还是原型中返回的都是true
// console. log("address" in info)
// console. log("name" in info)
//
// for (var key in info) {
//     console.log(key)
// }

//instanceof
function createObject2(o) {
    function Fn(name) {}
    Fn.prototype = o
    var newObj = new Fn()//构造函数创建的对象，__proto__指向构造函数的对象原型
    return newObj
}

function inheritPrototype(SubType, SuperType) {
    SubType.prototype = Object.create(SuperType.prototype)
    Object.defineProperty(SubType.prototype, "constructor", {
        enumerable: false,
        configurable: true,
        writable: true,
        value: SubType
    })
}

function Person() {
}
function Student() {
}

inheritPrototype(Student, Person)
const stu=new Student()  //Student {}   一个Student类的空对象
console.log(stu)
//instanceof用于验证一个对象是否继承自指定的构造函数原型。如果对象在原型链中存在该构造函数的prototype(即原型对象)属性，则返回true；否则返回false
console. log(stu instanceof Student) // true
console. log(stu instanceof Person) // true
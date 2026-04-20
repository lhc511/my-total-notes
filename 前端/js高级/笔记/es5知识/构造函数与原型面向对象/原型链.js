//原型链的理解
// var obj = {name: "why", age: 18}
// //`[[get]]操作
// //·1.在当前的对象中查找属性
// // 2.如果没有找到,这个时候会去原型( __ proto __ )对象上查找
// obj.__proto__ = {
// }
// //原型链
// obj.__proto__.__proto__={
// }
// console.log(obj.address)


//什么是顶层原型
var obj = { name: "why" }
//console.log(obj.address)
//、到底是找到哪一层对象之后停止继续查找了呢?
//、字面对象obj的原型是[Object;null prototype]{}
// [object:null prototype] {}就是顶层的原型
// console. log(obj.__proto__ )
// obj. _proto __= > [Object: null prototype] {}
// console. log(obj .__proto__.__proto__ )


// Object.prototype
// console.log(obj .__proto__ )
// console.log(Object.prototype)
// console. log(obj .__proto__===Object.prototype)//true

// console.log(Object.prototype)
//此处指回object构造函数
// console.log(Object.prototype.constructor)//f Object() { [native code] }=>function Object()

// console.log(Object)  //Object本身也是一个构造函数，因此也有prototype属性，指向他的原型对象


console.log(Object.__proto__)//ƒ () { [native code] }
// Object.__proto__ 指向 Function.prototype，这是由于 Object 本身是一个内置构造函数，而所有函数（包括构造函数）的原型都继承自 Function.prototype
// ƒ Function() { [native code] }/ƒ () { [native code] } 表示这是一个由 JavaScript 引擎原生实现的函数对象
// [native code] 标明该函数是底层原生代码（非用户编写的 JavaScript）
// 此输出本质上就是 Function.prototype 的字符串表示。

// console.log(Object.__proto__===Function.prototype)//true


// console.log(Object.__proto__.__proto__)//里面有各种各样的函数功能(不可枚举)
// 即 Function.prototype.__proto__，指向 Object.prototype

// console.log(Object.__proto__.__proto__ === Object.prototype); // true
// Object.prototype 的特殊性
// 所有 JavaScript 对象的最终原型（包括函数）
// 其 __proto__ 为 null，是原型链终点

console.log(Object.prototype.constructor); // ƒ Object() { [native code] }，指回构造函数本身

// 在 JavaScript 中，全局内置对象 Object 和 构造函数 Object 本质是同一个实体，但在不同使用场景下表现出双重角色。以下是详细解析：
console.log(Function.prototype.__proto__===Object.prototype); //true Object指的是全局的内置对象Object，而Object.prototype是Object构造函数的原型对象
console.log(Object.__proto__===Function.prototype)// true Object.__proto__ === Function.prototype中，Object指的是Object构造函数（函数对象）。

// console.log(Object.__proto__.__proto__.__proto__)  //null
// console.log(Object.__proto__.__proto__.__proto__.__proto__)  //报错:Cannot read properties of null (reading '__proto__')

function Person() {}

// console.log(Person.__proto__)////Function.prototype，继承自
// console.log(Person.__proto__.__proto__ === Object.prototype); // true
// console.log(Person.__proto__.__proto__)//{}均为不可枚举属性
// console.log(Person.__proto__.__proto__.__proto__)//null
// function foo(num1, num2, num3) {
// // 类数组对象中(长的像是一个数组,本质上是一个对象):orgum
// console.log(arguments)//Arguments(5)[10, 20, 30, 40, 50, callee: ƒ, Symbol(Symbol.iterator): ƒ]
//
// // 常见的对arguments的操作是三个
// // 1.获取参数的长度
//     console.log(arguments.length)
//
// // 2.根据索引值获取某一个参数
//     console.log(arguments[2])
//     console.log(arguments[3])
//     console.log(arguments[4])
//
// // 3.callee获取当前arguments所在的函数
//     console.log(arguments.callee)
// // arguments.callee()   //此处会无限递归
// }
// foo(10, 20, 30, 40, 50)
//********************************************
// 伪数组方法及转换
// function foo(num1, num2) {
// // 1.自己遍历
//     var newArr = []
//     for (var i = 0; i < arguments.length; i++) {
//         newArr.push(arguments[i] * 10)
//
//         console.log(newArr)
//
//         //2.arguments转成array类型
//         //2.1.自己遍历arguments中所有的元素
//     }
//     //传递的arguments伪数组，再调用slice函数时将其中this指向arguments
//     //slice()方法用于从数组中提取一段元素，并返回一个新数组，以下两种方法效果一样
//     var newArr2 = Array.prototype.slice.call(arguments)//将伪数组转换为真数组
//     console.log(newArr2)
//     //前面的时隐式绑定，不论里面的值是什么都和结果无关
//     var newArr3 = [2,2,2,].slice.call(arguments)
//     console. log(newArr3)
//
//     //2.3.ES6的语法 效果同上
//     var newArr4 = Array. from(arguments)
//     console. log(newArr4)
//     var newArr5 = [ ... arguments]
//     console. log(newArr5)
// }
// foo(10, 20,30,40,50)

//slice内部实现原理
// Array.prototype.hyslice = function(start, end) {
//     var arr = this
//     var newArray = []
//     for (var i = start; i < end; i++) {
//         newArray.push(arr[i])
//     }
//     return newArray
// }
//
// var newArray = Array. prototype.hyslice.call(["aaaa", "bbb", "cccc"], 1, 3)
// console. log(newArray)  //["bbb","ccc"]
//.var .names = ["aaa", "bbb","ccc", ."ddd"]
// names.slice(1,3)
//******************************************************************
// 箭头函数中的arguments使用
// var foo = () => {
//     console.log(arguments)   //报错，arguments is not defined，浏览器没有arguments参数
// }
// foo()

//2.案例二:
function foo() {
    var name=1
    var bar = () =>{
        console.log(arguments)//Arguments[123, callee: ƒ, Symbol(Symbol.iterator): ƒ]
    }
    return bar
}
var fn = foo(123)//在foo函数中添加了一个参数 123
fn()

//3
// var foo = (num1, num2, ... args) => {
//     console.log(args)
// }
// foo(10, 20, 30, 40,50)
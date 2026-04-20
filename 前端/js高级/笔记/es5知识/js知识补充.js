// with语句：不推荐
// "use strict"
var message = "Hello World"
// console. log(message)

//with语句:可以形成自己的作用域
// var obj = {name: "why", age: 18, message: "obj message"}
//
// function foo() {
//     function bar() {
//         //with会形成一个作用域，message会先在with中传的参数(obj)中查找，若没有则查找其父作用域链
//         with (obj) {
//             console.log(message)
//             console.log('---------')
//         }
//     }
//     bar()
// }
// foo()

//严格模式
// 3.静默错误      //有错，但是不影响执行就不报错
// true.name = "abc"
// NaN = 123
// var obj = {}
// Object.defineProperty(obj, "name", {
//     writable: false,
//     value: "why"
// })
//
// console.log(obj.name)
// obj .name = "kobe"

"use strict"

//、在严格模式下,·自执行函数(默认绑定)会指向undefined
//、之前编写的代码中,自执行函数我们是没有使用过this直接去引用window
function foo() {
    console.log(this)
}
var obj = {
    name: "why",
    foo: foo
}
foo() //undefined

obj. foo()  //obj
var bar = obj. foo
bar()//undefined
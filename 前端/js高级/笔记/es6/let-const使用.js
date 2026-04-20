// var foo = "foo"
//
// let bar = "bar"
//
// // const·constant(常量/衡量)
// const name = "abc"
// // name = "cba"   报错
//
// //const本质上是传递的值不可以修改
// //但是如果传递的是一个引用类型(内存地址),可以通过引用找到对应的对象,去修改对象内部的属性,这个是可以的
// const obj = {
//     foo: "foo"
// }
// // obj = {}   报错

// let-const作用域提升
// □这些变量会被创建在包含他们的词法环境被实例化时,但是是不可以访问它们的,直到词法绑定被求值;
//块级作用域

// 块代码(block code)
// {
//     //·表达
//     var foo = "foo"
// }
// console.log(foo)
//、声明对象的字面量
// var obj = {
//     name: "why"
// }

// 在ES5中只有两个东西会形成作用域
// 1.全局作用域
//2.函数作用域
// function foo() {
//     var bar ="bar"
// }
// console.log(bar)

// function foo() {
//     function demo() {
//     }
// }

//ES6的代码块级作用域
// 对let/const/function/class声明的类型是有效，对var声明无效
// {
//     let foo = "why"
//     function demo () {
//         console.log("demo function")
//     }
//     class Person {}
//
// }
// // console.log(foo) // foo is not defined
// //、不同的浏览器有不同实现的(大部分浏览器为了兼容以前的代码,让function是没有块级作用域)，有些浏览器则块级作用域
// // demo ()
// var p = new Person() // Person is not defined

//·if语句的代码就是块级作用域
// if (true){
//var foo = "foo"
// let .bar .= "bar"

// console. log(foo)
// console. log(bar)

//switch语句的代码就是块级作用域
// var color = "red"
// switch (color) {
//     case "red":
//         var foo = "foo"
//         let bar = "bar"
// }
// console. log(foo)
// console. log(bar)

//、for语句的代码也是块级作用域
// for (var i .= 0; i .<. 10; i++){
// console. log("Hello World".+.i)
// console.log(i)

// for (let i = 0; i < 10; i++){}
// console. log(i)

const btns = document.getElementsByTagName('button')
// 使用 var i 声明循环变量：var 没有块级作用域，i 属于全局作用域或函数作用域，循环结束后 i 的值会固定在 btns.length（例如 i=5）。
// 当按钮点击事件触发时（循环结束后执行），所有 onclick 函数访问的都是全局的 i，导致每个按钮都输出最后一个 i 值（例如所有按钮都显示 “第5个按钮被点击”)
//此处由于i不受块作用域限制所以是全局变量，因此最后只会输出  第4个按钮被点击
// for (var i = 0; i < btns.length; i++){
//    btns[i].onclick = function() {
//        console.log("第" + i + "个按钮被点击")
//    }
// }

//解决方法1
// 形成闭包:btns[i].onclick作为全局对象指向匿名函数，匿名函数的父作用域链指向自执行函数的ao，ao中存储着 被当时的i赋值的变量n，所以n不会被销毁
//此处它在每次循环迭代时被立即调用，并创建一个新的函数作用域。
// for (var i = 0; i < btns. length; i++) {
//     (function (n) {//此处是一个闭包
//         btns[i].onclick = function () {
//             console.log("第" + n + "个按钮被点击")
//         }
//     })(i)
// }

//解决方法2
// let 隐式地为每次循环创建闭包，避免手动写自执行函数
//for循环中每一次的i访问的都是块级作用域中的i，剩下的与上面同一个道理，只是此处父作用域是for的块作用域
// for (let i = 0; i < btns.length; i++){
//    btns[i].onclick = function() {
//        console.log("第" + i + "个按钮被点击")
//    }
// }

// const names = ["abc", "cba", "nba"]
// //let相当于给每一个块级作用域给i赋值，彼此独立不相互影响，而var是全局变量会相互影响
// for (let i = 0; i < names. length; i++) {
//     console. log(names[i])
// }
// {
//     let i = 0
//     console. log(names[i])
// }
// {
//     let i = 1
//     console. log(names [i])
// }

//for ... of:ES6新增的遍历数组(对象)
// for (const item of names) {//此处能使用const原因是给item直接赋值而没有改变他的值
//     console.log(item)
// }


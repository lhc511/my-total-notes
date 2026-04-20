// 这个的案例可以给我们什么样的启示呢?
//1.函数在调用时,JavaScript会默认给this绑定一个值;
//2.this的绑定和定义的位置(编写的位置)没有关系;
//3.this的绑定和调用方式以及调用的位置有关系;
//4.this是在运行时被绑定的;

// //以下三个结果不相同
// function foo() {
//     console.log(this)
// }
// // 1.直接调用这个函数
// foo () //window
// // 2.创建一个对象,对象指向foo
// var obj = {
//     name: 'why',
//     foo: foo
// }
// obj.foo() //打出的时obj对象的内容
// // 3.apply调用
// foo.apply("abc") //String("abc")
//
// // 当函数被独立调用一般打出的时windows，催出三个函数都是独立调用
// function foo1() {
//     console. log(this)
// }
// function foo2() {
//     console. log(this)
//     foo1()
// }
// function foo3() {
//     console. log(this)
//     foo2()
// }
// foo3()
// *************************
//-3.案例三: bar是函数foo的地址，bar()相当于直接调用foo因此是window
// var obj = {
//     name: "why",
//     foo: function () {
//         console.log(this)
//     }
// }
// var bar = obj.foo
// bar() // window

//**********************
function foo() {
    function bar() {
        console.log(this)
    }
    return bar
}

var fn = foo()
fn() // window

var obj = {
    name: "why",
    eating: fn
}
obj.eating()//隐式绑定 ，此处有了obj这个调用主题，因此返回的是obj对象中的内容
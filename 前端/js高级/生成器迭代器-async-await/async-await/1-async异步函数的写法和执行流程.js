//await/async
// async 声明异步函数的基本写法
//写法1
// async function foo1() {
//
// }
//写法2
// const foo2 = async () => {
//
// }
//写法3
// class Foo {
//     async bar() {
//
//     }
// }

/////////执行流程///////////
async function foo() {
    console.log("foo function start~")

    console.log("内部的代码执行1")
    console.log("内部的代码执行2")
    console.log("内部的代码执行3")

    console.log("foo function end~")
}
console.log ("script start")
foo()
console. log("script end")
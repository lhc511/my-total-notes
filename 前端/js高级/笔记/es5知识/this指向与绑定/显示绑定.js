function foo() {
console.log("函数被调用了",this)
}

//-foo直接调用和call/apply调用的不同在于this绑定的不同
//foo直接调用指向的是全局对象(window)
// foo()

// var obj = {
//     name: "obj"
// }
// // call/apply是可以指定this的绑定对象
// foo.call(obj)  //指向obj
// foo.apply(obj)//指向obj
// foo.apply("aaaa")  //指向”aaaa“


//2.call和apply有什么区别?传参方式不一样
function sum(num1, num2, num3) {
    console.log(num1 + num2 + num3, this)
}

sum.call("call", 20, 30, 40)
sum.apply("apply", [20, 30, 40])
//3.call和apply在执行函数时,是可以明确的绑定this,这个绑定规则称之为显示绑定

// bind使用
function foo() {
    console.log(this)
}
// foo.call("aaa")
// foo.call("aaa")
// foo.call("aaa")
// foo.call("aaa")
// 默认绑定和显示绑定bind冲突:优先级(显示绑定)
var newFoo = foo.bind("aaa")

newFoo()//aaa
newFoo()//aaa
newFoo()//aaa
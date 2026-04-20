// //call函数实现
//                 thisARG是被绑定的对象
// Function. prototype.hycall = function(thisARG,...args) {
// //、在这里可以去执行调用的那个函数(foo)
// //问题:得可以获取到是哪一个函数执行了hycall
// //    获取需要被执行的函数
//
//     // 对thisARG转换成对象类型,存在转换成对象，没有则为window
//     thisARG=thisARG?Object(thisARG):window
//     //需要被执行的函数，此处相当于隐式调用 this指向的是调用他的 对象
//     thisARG.fn=this
//     //执行函数
//     return thisARG.fn(...args)
// }
// function foo() {
//     console.log("foo函数被执行",this)
// }
//
// function sum(num1, num2) {
//     console.log('sum函数被执行',this,num1,num2)
//     return num1+num2
// }
//
// // 系统的函数的call方法
// // foo. call()
// // const result=sum.call({},20,30)
// // console.log('系统调用的结果',result)
// //·自己实现的函数的hycall方法
// // 默认进行隐式绑定
// // foo. hycall({})
// const result=sum.hycall('abc',20,30)
// console.log(result)

//******************************************************************************
// Function. prototype.hyapply = function(thisArg, argArray) {
// //·1.获取到要执行的函数
//     var fn = this  //this指向现在正执行的函数
//
// //2.处理绑定的thisArg，绑定对象非空并非未定义
//     thisArg = (thisArg !== null && thisArg !== undefined) ? Object(thisArg) : window
//
// //3.执行函数
//     thisArg.fn = fn //此处进行隐式绑定
//     var result
//
//     //if(!argArray){//·argArray是没有值(没有传参数)
//     //result =thisArg.fn()  //直接执行
//     //}else {// 有传参数
//     //result = thisArg.fn( ... argArray)      //将传递的参数展开传参再执行
//     //}
//     //argArray = argArray ? argArray: []
//
//     argArray = argArray || []  //若argArray非空则为argArray，反之为[]空数组
//     result = thisArg.fn(...argArray)//展开运算传参
//
//     delete thisArg.fn
//
// // 4.返回结果
//     return result
// }
// function sum(num1, num2) {
//     console.log("sum被调用", this, num1, num2)
//     return num1 + num2
// }
//
// function foo(num) {
//     return [num,this]
// }
//
// function bar () {
//     console.log("bar函数被执行",this)
// }
// // 系统调用
// // vor result .= sum.apply("abc", 20)
// // console.log(result)
//
// // 自己实现的调用
// // var result = sum.hyapply("abc", [20, 30])
// // console. Log(result)
//
// var result2 = foo.hyapply("abc", [20])
// console.log(result2)
//
// // edge case
// bar.hyapply(0)

//******************************************************
// bind函数实现
Function.prototype.hybind = function(thisArg, ... argArray){
    var fn = this

    //2.绑定this
    thisArg = (thisArg !== null && thisArg !== undefined) ? Object(thisArg): window

    function proxyFn( ... args) {
    //3.将函数放到thisArg中进行调用
        thisArg.fn = fn
    //特殊:对两个传入的参数进行合并
        var finalArgs = [...argArray, ...args]
        var result = thisArg.fn(...finalArgs)
        delete thisArg.fn

    //4、返回结果
        return result
    }

return proxyFn
}

function foo() {
    console.log("foo被执行", this)
}

function sum(num1, num2, num3, num4) {
    console.log(num1, num2, num3, num4)
}
// 系统的bind使用
// var bar = foo.bind("abc")
//bar ()

// var newSum =sum.bind("aaa", 10, 20, 30, 40)
// newSum()

// var newSum = sum.bind("aaa")
// newSum(10,20,30,40)

// var newSum = sum.bind("aaa", 10)
// newSum(20, 30, 40)

// 使用自己定义的bind
// var bar = foo.hybind("abc")
// var result = bar ()
// console.log(result)

var newSum = sum.hybind("abc", 10, 20)
var result = newSum(30, 40)
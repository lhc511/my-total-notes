//两个数组方法对比
// var names = ["abc", "cba", "nba", "dna"]

//slice只要给它传入一个start/end,·那么对于同一个数组来说,它会给我们返回确定的值
//·slice函数本身它是不会修改原来的数组
// slice -> this
//slice函数本身就是一个纯函数
// var newNames1 = names.slice(0, 3)
// console.log(newNames1)
// console. log(names)

// ["abc", "cba", "nba", "dna"]
//splice在执行时,有修改掉调用的数组对象本身,修改的这个操作就是产生的副作用
//splice不是一个纯函数
// var newNames2 = names.splice(2)//从第二个开始截取，包括第二个
// console.log(newNames2)//["nba", "dna"]
// console. log(names)//["abc", "cba"]

//柯里化
//、简化柯里化的代码
// var sum2 = x => y => z => {
//     return x + y + z
// }
// console.log(sum2(10)(20)(30))
//
// var sum3 = x => y => z => x + y + Z
// console.log(sum3(10)(20)(30))

//单一职责原则
// function add(x, y, z) {
//     x =x + 2
//     y =y* 2
//     z=z*z
//     return x + y + z
// }
//将每一层函数都进行了单一职责划分
// console.log(add(10, 20,30))
// function sum(x) {
//     x = x + 2
//     return function (y) {
//         y = y * 2
//         return function (z){
//             z=z*z
//             return x+y+z
//         }
//     }
// }
//
// console.log(sum(10)(20)(30))

//柯里化函数复用******************************************
//假如在程序中,我们经常需要把5和另外一个数字进行相加
// console.log(sum(5, 10))
// console.log(sum(5, 14))
// console.log(sum(5, 1100))
// console.log(sum(5, 555))

// function makeAdder(count) {
//     count=count*count
//     return function (num) {
//         return count + num
//     }
// }
// // var result =makeAdder(5)(10)
// // console.log(result)
// var adder5 = makeAdder (5)  //此处相当于对第一层函数做了逻辑复用
// adder5(10)
// adder5(14)
// adder5(1100)
// adder5(555)

//案例二
// function log(date, type, message) {
//console.log('[${date.getHours()}:${date.getMinutes()}][${type}]: [${message}]')
//}
//log(new Date(),"DEBUG","查找到轮播图的bug")
//log(new Date(),"DEBUG","查询菜单的bug")
//log(new Date(),"DEBUG","查询数据的bug")

//柯里化的优化
// var log = date => type => message => {
//     console.log('[${date.getHours()}:${date.getMinutes()}][${type}]: [${message} ]')
// }
// // 如果我现在打印的都是当前时间
// var nowLog = log(new Date())
// nowLog("DEBUG")("查找到轮播图的bug")
// nowLog("FETURE")("新增了添加用户的功能")

// //柯里化函数实现
// function add1(x,y,z) {
//     console.log(x + y + z)
//     return x + y + z
// }
// function add2(x,y,z) {
//     x = x + 2
//     y = y * 2
//     z = z * z
//     return x + y + z
// }
//
// function makeAdder(count) {
//     count = count * count
//     return function (num) {
//         return count + num
//     }
// }
//
// function log(date, type, message) {
//     console.log('[${date.getHours()}:${date.getMinutes()}][${type}]: [${message} ]')
// }
//
// // 柯里化函数的实现hyCurrying
// function hyCurrying(fn) {//将函数传入hyCurrying函数后自动实现函数柯里化
//     // 函数名.length  可以得到函数的参数个数
//     // console.log(fn.length)
//     //当使用展开运算符传参的时候会已数组形式存储参数，比如此处的args就是一个数组
//     console.log(this)
//     //下面在执行时是对第二层函数进行绑定
//     function curried(...args){  //柯里化后的调用方式传递的第一层参数(第一个括号内的参数)
//         // console.log(args)//[10, 20, 30]
//         //判断当前已经接收的参数的个数,可以参数本身需要接受的参数是否已经一致了
//
//         // window.curryAdd.call(10,20,30)
//         // console.log(this)//Number{10}
//         // fn(...args)   //无法执行，因为绑定的 对象{10} 没有方法。//报错:NaN
//
//         // window.curryAdd(10,20,30)
//         // console.log(this)//window
//         // fn(...args)   //60
//
//
//         if (args.length>=fn.length){
//             // fn(...args)
//             //两种写法   fn一定是传入的目标函数，均对传入的目标函数进行显式绑定，原因见下方
//             // fn.apply(this,args) //此处的this是curried的this
//             return fn.call(this,...args) //将fn函数的this指向和当前函数的this指向绑定一致
//         }else{
//             //没有达到个数时返回一个新函数继续接受参数
//             return function curried2(...args2){
//                 //接受参数后递归检查函数参数的的个数是否达到
//                 return curried.apply(this,[...args,...args2])
//             }
//         }
//     }
//     return curried
// }
//
// var curryAdd = hyCurrying(add1)
// // add1(10, 20, 30)   //原本调用方法
//
// // 柯里化后传参方式     此处执行的是函数中第二层curried函数
// // 由于函数默认调用是window.函数名 进行隐式绑定调用，因此在call/apply换绑后的绑定之并未有函数调用方法 可能会导致函数失效
// // 因此要在 自动柯里化函数 中的将传入的参数进行显式绑定
// curryAdd(10,20,30)//柯里化后调用方法1
// // window.curryAdd.call(10,20,30)//函数绑定其他值   此时this指向10，因为call默认绑定第一个位置参数，后面的是传递的函数参数(只有两个)
// // curryAdd(10,20)(30)//柯里化后调用方法2
// curryAdd(10)(20)(30)//柯里化后调用方法3

//组合函数 案例一
// function double(num) {
//     return num * 2
// }
//
// function square(num) {
//     return num ** 2
// }
//
// var count = 10
// var result = square(double(count))
// console.log(result)
//
// var num = 100
// square(double(num))
//
// function composeFn(m, n) {
//     return function (count) {
//         return n(m(count))
//     }
// }
// var newFn = composeFn(double, square)
// console.log(newFn(10))
//案例二  通用组合函数

function hyCompose(...fns){
    const length=fns.length//此处是函数的个数
    console.log(length)
    //判断是否为函数类型
    for (let i =0;i<length;i++){
        if (typeof fns[i]!=='function'){
            throw new TypeError("请添加函数类型参数")
        }
    }

    return function compose(...args){
        let index=0
        // 在length拥有值的情况下执行前面(将参数传递给函数并调用),若没有则执行后面，即返回参数
        let result =length? fns[index].apply(this,args):args
        while (++index<length){
            result=fns[index].call(this,result)
        }
        return result
    }
}
function double(m) {
    return m * 2
}
function square(n) {
    return n ** 2
}

var newFn = hyCompose(double, square)
console.log(newFn(10))

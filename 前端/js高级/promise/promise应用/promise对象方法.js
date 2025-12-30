//-Promise有哪些对象方法
// console.log(Object.getOwnPropertyDescriptors(Promise.prototype))


// 大概执行过程
// class Person {
//     constructor(executor) {
//         const resolve = () => {
//             this.callback
//         }
//
//         const reject = () => {
//         }
//
//         executor(resolve, reject)
//
//         then(callback)
//         {
//             this.callback = callback
//
//         }
//     }
// }
// new Person((resolve, reject) => {//该对象传入的方法就是executor会立即执行
//     resolve()
// })


// const promise = new Promise((resolve, reject) => {//该对象传入的方法就是executor
//     resolve()
// })
// 1.同一个Promise可以被多次调用then方法
//·当我们的resolve方法被回调时,所有的then方法传入的回调函数都会被调用
// promise.then(res => {
//     console.log("res1:", res)
// })
// promise.then(res => {
//     console.log("res2:", res)
// })
// promise.then(res => {
//     console.log("res3:", res)
// })

//-2.then方法传入的“回调函数:可以有返回值
//then方法本身也是有返回值的,它的返回值是Promise
//、1>如果我们返回的是一个普通值,那么这个普通的值被作为一个新的Promise的resolve值
// promise. then(res => {
//     return "aaaaaa"
//     //此处若无返回则默认为undefined
//     // return undefined // new Promise(resolve => resolve(undefined))
//
//     // 此处相当于以下代码(即返回了一个新的promise对象)
//     // return new Promise((resolve) => {
//     //     resolve("aaaaaa")
//     // })
//
// }).then(res => {      //此处的then时是新promise对象来调用的
//     console.log(res+':res')
// })


// promise. then(res => {
//     //此处相当于返回了一个promise对象的同时执行了内部的resolve函数并将返回的普定值作为resolve的参数
//     return "aaaaaa"
// }).then(res => {
//     console.log(res+':res')
// })
//第一个then函数后面的写法
// new Promise((resolve) => {
//         resolve("aaaaaa")
//     }).then(res => {
//     console.log(res+':res')
// })

//-1> 如果我们返回的是一个普通值(数值/字符串/普通对象/undefined),那么这个普通的值被作为一个新的Promise的resolve值
//·2>如果我们返回的是一个Promise
// promise.then(res => {
//     return new Promise((resolve, reject) => {
//         setTimeout(() => {
//             resolve(111111)
//         }, 3000)
//     })
// }).then (res=> {
//     console.log("res:", res)
// })

//-3>如果返回的是一个对象,并且该对象实现了thenable
const promise = new Promise((resolve, reject) => {//该对象传入的方法就是executor
    resolve()//此处是用来判断成功与失败状态的
})
// new Promise(resolve => resolve(obj.then))
promise.then(res => {
    return {
        then: function (resolve,rejected) {
            resolve(22222222)
        }
    }
//    返回一个新的promise对象
// new Promise((resolve) => {
//     resolve({return中返回的对象})//若有then则自动执行对象中的then方法
        //then方法中的resolve/rejected状态确定以后将其中参数传给新promise对象调用的then方法的参数
// }).then(res => {
//     console.log(res + ':res')
// })

}).then (res=> {
    console.log("res:", res)
})

// const promise = new Promise((resolve, reject) => {
// resolve ()
// // reject("rejected status")
//     // throw new Error("rejected status")//用抛出错误的方法会将所有错误信息都打印
// })

// promise.then(undefined, (err) => {
//     console.log("err:", err)
//     console.log('---------------------')
// })

//·2.通过catch方法来传入错误(拒绝)捕获的回调函数(另一种写法)
// promise.catch(err => {
//     console.log("err:", err)
// })

// catch的特殊性
// promise.then(res => {
//     return new Promise((resolve, reject) => {
//         reject("then rejected status")
//     })
//     // throw new Error("error message")
// //    这里的catch会默认优先捕获原对象的异常，若原对象没有异常，则会捕获then中创建的新promise对象的异常
// }).catch(err => {//此处虽然由then中新创建的对象调用catch 但是在内部处理时会让该catch指向原先的promise对象
//     console.log("err:", err)//err: rejected status
// })

//***************************************************************************
// const promise = new Promise((resolve, reject) => {
//     // reject (11111)
//     resolve (11111)
// })
//
// // 由于以下两个函数是独立调用互不影响，因此reject拒绝处理在then中无法处理那么就会报错
// promise.then(res=> {
// }) . then (res => {
//     throw new Error("then error message")
// }). catch(err => {
//     console.log("err:", err)//会从上往下的优先级去捕获异常，此处原对象和第一个then返回的promise对象都没异常，所以捕获第二个then
// })

// promise.catch(err=>{})

//4.catch方法的返回值
const promise = new Promise((resolve, reject) => {
    reject("111111")
})

//catch方法的返回值和then方法的返回值是一样的
promise.then(res => {
    console.log("res:", res)
}).catch(err => {
    console.log("err:", err)//err: 111111
    return "catch return value"//像此处一样返回一个普通值  会返回new Promise(resolve => resolve(x))，执行resolve
//    所以会执行then函数，除非在上面的catch中抛出异常或在返回的promise对象中用reject函数才会执行下方的catch函数
}) . then (res => {
    console.log("res result:", res)//res result: catch return value
}) . catch(err => {
    console.log("err result:", err)
})
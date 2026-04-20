//此对象中传递的参数函数会直接自执行
//完全等价于下面的代码
//·注意:Promise状态-旦确定下来,那么就是不可更改的(锁定)
// new Promise((resolve, reject) => {
//     // pending状态:待定/悬而未决的
//     console.log(" -------- ")
//     resolve()// 处于fulfilled状态(已敲定/兑现状态)
//     console.log("++++++++++++")
//     reject()//处于rejected状态(已拒绝状态) 此行代码无效 因为前面状态已确定
// }).then (res => {
//     console.log("res:", res)
// }, err => {
//     console.log("err:", err)
// })


/*
    *resolve(参数)
    *普通的值或者对象
    *传入一个Promise那么当前的promise状态会由传入的promise决定
    * 传入一个对象,并且这个对象有实现then方法(并且这个对象是实现了thenable接口(即这个对象有then方法))
    * 那么也会执行该then方法,并且又该then方法决定后续状态
*/

// const newPromise = new Promise((resolve, reject) =>{
//     //在此决定下方对then和catch(then的第二个参数)的回调
//     // resolve("aaaaaa")
//     reject("err message")
// })
// new Promise((resolve, reject) => {
//     resolve(newPromise)
// }).then (res => {
//     console.log("res:", res)
// }, err => {
//     console.log("err:", err)
// })

//2.传入一个对象,这个对象有then方法，则会自动执行then方法，并且会自动传入resolve, reject两个参数
// new Promise的executor中立即调用resolve(obj)，obj是一个thenable对象。
// 由于obj具有then方法，Promise会尝试获取这个对象的最终状态。规范中，这个过程称为“展开（unwrapping）”。
// 按照规范，会调用obj.then方法，并传入两个函数：一个用于解决（resolve），一个用于拒绝（reject）。
// 注意：这里传入的resolve和reject是Promise内部提供的，用于决定这个新Promise的状态。
// 在obj.then方法中，我们调用了reject(“reject message”)。这意味着这个thenable对象最终被拒绝（rejected），理由为"reject message"。
// 因此，最初创建的Promise的状态将被这个thenable对象的结果决定，即被拒绝（rejected），拒绝理由是"reject message"。
// 然后，我们在这个Promise上调用then方法，提供了两个回调：onFulfilled（成功）和onRejected（失败）。
// 由于Promise被拒绝，所以会执行onRejected回调，即打印错误信息。

new Promise((resolve, reject) => {
// pending -> fulfilled
//  初始化一个Promise
    const obj = {  //引擎调用obj.then(resolveFn, rejectFn)：
        then: function (resolve, reject) {//在这个函数内部决定promise对象的状态
            // resolve ("resolve message")
            reject("reject message")
        }
    }
    // 当resolve()参数是thenable对象（含then方法的对象）时
    // Promise会调用该对象的then方法，并等待其状态确定，并且会自动传入resolve, reject两个参数
    resolve(obj)//// 传入具有then方法的对象  同时确定该Promise的状态
}) . then (res => {
    console.log("res:", res)
}, err => {
    console.log("err:", err)
})


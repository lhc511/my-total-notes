// 在JavaScript Promise中，executor函数是用户自定义的函数，它作为参数传递给Promise构造函数。其主要作用如下：
// 封装异步操作：executor函数内部通常包含异步操作（如setTimeout、AJAX请求等）。
// 控制状态转换：通过调用其参数resolve和reject，将Promise的状态从pending转变为fulfilled或rejected。
// 同步执行：当创建Promise实例时，executor函数会被立即同步执行。
// 原理：
// executor函数接收两个函数参数：resolve和reject，它们由Promise内部提供。
// 在executor函数中，用户启动异步任务，并在任务完成时调用resolve（成功）或reject（失败）。
// 如果在executor函数中抛出异常（同步错误），Promise会自动捕获并将其视为reject。

const PROMISE_STATUS_PENDING = 'pending'
const PROMISE_STATUS_FULFILLED = 'fulfilled'
const PROMISE_STATUS_REJECTED = 'rejected'

class HYPromise {
    // 在 JavaScript 类的构造函数中使用 executor 函数是一种异步控制设计模式，主要实现对异步操作的封装和状态管理。
    // constructor(executor)是类的构造函数，在创建类的实例时会自动调用。它接收一个参数executor，这个参数是一个函数（我们通常称之为执行器函数）。
    constructor(executor) {//此处的executor就是从下面创建的对象中传递来的函数
        this.status = PROMISE_STATUS_PENDING
        this.value = undefined
        this.reason = undefined
        const resolve = (value) => {
            // 由于在下方创建的new HYPromise对象中在执行resolve函数时最底下的then函数还没有传递函数参数所以会在调用函数时报错，reject函数同理
            //此处设置setTimeout函数会将其中的代码添加到宏任务当中，在所有主线程的代码执行完毕之后才会执行(this已经传完函数参数)便能够规避报错
            // setTimeout(()=> {
            if (this.status === PROMISE_STATUS_PENDING) {
                this.status = PROMISE_STATUS_FULFILLED//将状态赋值
                 //此处queueMicrotask中的代码会在最后执行，这是一种机制后面讲
                 queueMicrotask(()=> {//此种方法也可以规避错误也更推荐
                     this.value = value
                     console.log("resolve被调用")
                     this.onFulfilled(this.value)
                 })
            }
        }
        const reject = (reason) => {
            //若前面的函数先执行则this.statu已改变，就不会执行此处的代码
            if (this.status === PROMISE_STATUS_PENDING) {
                this.status = PROMISE_STATUS_REJECTED
                 queueMicrotask(()=> {
                     this.reason = reason
                     console.log("reject被调用")
                     this.onRejected(this.reason)
                 })
            }
        }
         // 执行传入的回调函数executor(即下方创建对象new HYPromise时传进来的函数)，并传入resolve和reject作为参数
        executor(resolve, reject)//此函数的作用是将传递的参数作为一个选项供以后在创建对象时使用

    }

    then(onFulfilled,onRejected){
        this. onFulfilled = onFulfilled
        this.onRejected = onRejected
    }
}

const promise = new HYPromise((resolve, reject) => {//传入一个函数，一整个函数的引用在类中为executor
    console.log('状态pending')
    resolve(111)
    reject(222)
})

//调用then方法此处只会实行一次因为在执行下面的时候会将上方的执行的值覆盖掉
console. log(" ------ ")
promise.then(res => {
    console.log('res:'+res)
}, err => {
    console.log('err:'+err)
})

//调用then方法
promise.then(res => {
    console.log("res2:", res)
}, err => {
    console.log("err2:", err)
})
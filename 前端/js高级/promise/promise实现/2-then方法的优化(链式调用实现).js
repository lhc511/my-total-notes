//执行流程:创建一个new HYPromise对象赋值给promise变量，将对象中写一个函数作为参数传给类中的constructor
//并在构造函数constructor中立即执行(即执行传递过来的函数参数)，executor(作为参数传递的)函数内部:执行resolve函数(在构造函数中已初始化定义好)
//并且resolve已经作为参数传递给对象中的方法(executor)。执行到 queueMicrotask(()=> { 会跳过此处(这是一种代码执行机制，最后执行此处)，继续执行主线程中的代码，即后面promise对象调用的then方法
//then方法将其中的两个函数参数传递给类中定义的onFulfilled,onRejected参数，然后根据目前的status进行条件判断此时为pending(不执行函数)，因此将一个新定义的函数添加到对应数组(包含传来的函数)，添加完毕后then函数
//执行完毕，再执行原先的微队列。在执行微队列先判断状态是不是'pending'，若不是则不执行，若是则继续，将自身的状态赋值给，定义的状态status属性，
//然后遍历执行数组中的函数(即刚定义的新函数)，先执行下方then函数中传递的参数函数，若函数中由return则该 函数执行的结果 即是return返回值/若无则undefined
//将传递的参数函数的结果赋值给一个局部变量value，再由resolve函数接收参数并执行resolve函数，由于then方法中直接返回promise对象，所以相当于是再新返回的promise对象中执行了resolve函数
// 之后不断重复以上过程

const PROMISE_STATUS_PENDING = 'pending'
const PROMISE_STATUS_FULFILLED = 'fulfilled'
const PROMISE_STATUS_REJECTED = 'rejected'

// 工具函数
function execFunctionWithCatchError(execFn, value, resolve, reject) {
    try {
        const result = execFn(value)
        resolve(result)
    } catch (err) {
        reject(err)
    }
}

class HYPromise {
    // 在 JavaScript 类的构造函数中使用 executor 函数是一种异步控制设计模式，主要实现对异步操作的封装和状态管理。
    // constructor(executor)是类的构造函数，在创建类的实例时会自动调用。它接收一个参数executor，这个参数是一个函数（我们通常称之为执行器函数）。
    constructor(executor) {//此处的executor就是从下面创建的对象中传递来的函数
        this.status = PROMISE_STATUS_PENDING
        this.value = undefined
        this.reason = undefined
        this.onFulfilledFns=[]
        this.onRejectedFns=[]

        const resolve = (value) => {
            // 由于在下方创建的new HYPromise对象中在执行resolve函数时最底下的then函数还没有传递函数参数所以会在调用函数时报错，reject函数同理
            //此处设置setTimeout函数会将其中的代码添加到宏任务当中，在所有主线程的代码执行完毕之后才会执行(this已经传完函数参数)便能够规避报错
            // setTimeout(()=> {
            if (this.status === PROMISE_STATUS_PENDING) {
                 //此处queueMicrotask中的代码会在最后执行，这是一种机制后面讲
                 queueMicrotask(()=> {//此种方法也可以规避错误也更推荐
                     if (this.status !== PROMISE_STATUS_PENDING) return
                     this.status = PROMISE_STATUS_FULFILLED//将状态赋值
                     this.value = value
                     //对数组中的所有函数进行遍历实行
                     this.onFulfilledFns.forEach(fn => {//fn是后面所有then方法传回的函数，then方法传回的第 1 个参数
                         fn(this.value)//此处的fn和下面then中的onFulfilled参数代表的是一个函数

                     })
                 })
            }
        }

        const reject = (reason) => {
            //若前面的函数先执行则this.statu已改变，就不会执行此处的代码
            if (this.status === PROMISE_STATUS_PENDING) {

                //若将此代码放在上方，则赋值后满足条件then中会执行函数，而此时queueMicrotask中的this.reason还未被赋值并传递，所以后面打印出来的值时undefined
                // this.status = PROMISE_STATUS_REJECTED

                 queueMicrotask(()=> {
                     if (this.status !== PROMISE_STATUS_PENDING) return
                     this.status = PROMISE_STATUS_REJECTED
                     this.reason = reason
                     //对数组中的所有函数进行遍历实行
                     this.onRejectedFns.forEach(fn => {//fn是后面所有then方法传回的函数，then方法传回的第二个参数
                         fn(this.reason)//执行传回的函数
                     })
                 })
            }
        }

        try {
            // 执行传入的回调函数executor(即下方创建对象new HYPromise时传进来的函数)，并传入resolve和reject作为参数
            executor(resolve, reject)//此函数的作用是将传递的参数作为一个选项供以后在创建对象时使用
        }catch (err){
            reject(err)
        }

    }

    then(onFulfilled,onRejected){
        //直接返回一个新的HYPromise对象(此对象中的函数也会立即执行，即传入的判断条件)
        return new HYPromise((resolve, reject) => {
            //、1.如果在then调用的时候,状态已经确定下来并且onFulfilled有值
            //非pending状态下的会执行函数
            if (this.status === PROMISE_STATUS_FULFILLED && onFulfilled) {
                try {

                    //在此处能直接得到值是因为 一个对象只有一个this.value属性，对同一个对象调用该属性时可以拿到先前的赋值
                    const value =onFulfilled(this.value)
                    resolve(value)
                }catch (err){
                    reject(err)
                }
                // execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
            }

            if (this.status === PROMISE_STATUS_REJECTED && onFulfilled) {
                try {
                    const reason = onRejected(this.reason)
                    //除抛出错误外失败状态返回值一般也会传给下一个promise对象的resolve函数，并通过传参到then中的正确状态函数(第一个参数)，
                    resolve(reason)//所以调用resolve函数
                }catch (err){
                    reject(err)
                }
                // execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
            }

            if (this.status === PROMISE_STATUS_PENDING) {
                //此状态不执行函数，只定义函数并将该函数添加到对应数组函数
                this.onFulfilledFns.push(()=>{//在对应数组中实际存放的函数 也不执行，该函数会在上方resolve的微队列中执行
                    try {
                        //this.value是一个参数共函数内部使用，而onFulfilled(this.value)本身就是一个返回值二者的值无联系(下面也一样)
                        const value=onFulfilled(this.value)//此处的函数执行结果就是then函数中的参数函数的返回值
                        console.log(value)
                        resolve(value)//将返回值传递给resolve，进行再次的轮回
                    }catch (err){
                        reject(err)
                    }
                    // execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)

                })
                this.onRejectedFns.push(()=>{
                    try {
                        const reason=onRejected(this.reason)
                        resolve(reason)
                    }catch (err){
                        reject(err)
                    }
                    // execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
                })
            }
        })
    }
}

const promise = new HYPromise((resolve, reject) => {//传入一个函数，一整个函数的引用在类中为executor
    console.log('状态pending')
    resolve(111)
    // reject(222)
    // throw new Error("executor error message")
})

// 调用then方法多次调用  //
//在此函数作为参数本身并不执行，此处的函数会在传递到上面的类方法只执行
promise.then(res => {
    console.log("res1:", res)
    return 'aaaa'
    // throw new Error('错误')
}, err => {
    console.log("err1:", err)
    return 'bbbbbbb'
}) . then (res => {
console. log("res2:", res)
}, err => {
    console.log("err2:", err)
})
//执行流程:创建一个new HYPromise对象赋值给promise变量，将对象中写一个函数作为参数传给类中的constructor
//并在构造函数constructor中立即执行(即执行传递过来的函数参数)，executor(作为参数传递的)函数内部:执行resolve函数(在构造函数中已初始化定义好)
//并且resolve已经作为参数传递给对象中的方法(executor)：在执行resolve先判断状态是不是'pending'，若不是则不执行，若是则继续，将自身的状态赋值给
//定义的状态status属性，执行到 queueMicrotask(()=> { 会跳过此处(这是一种代码执行机制，最后执行此处)，继续执行主线程中的代码，即后面promise对象调用的then方法
//此时还是pending状态，所以会将函数添加到对应数组中，最后执行微队列queueMicrotask中的代码，遍历执行数组中的函数

//在执行setTimeout中的函数时该对象的status已经设置为fulfilled，所以满足then方法中判断的第一个条件直接执行函数，而同一个promise对象调用then方法中
//共享一个this.value属性，因此可以直接拿到值并传递(最初的)，value来源于promise对象中的executor参数中resolve函数传递的value




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
                     this.onFulfilledFns.forEach(fn => {//fn是后面所有then方法传回的函数
                         fn(this.value)
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
                     this.onRejectedFns.forEach(fn => {//fn是后面所有then方法传回的函数
                         fn(this.reason)
                     })
                 })
            }
        }
        // 执行传入的回调函数executor(即下方创建对象new HYPromise时传进来的函数)，并传入resolve和reject作为参数
        executor(resolve, reject)//此函数的作用是将传递的参数作为一个选项供以后在创建对象时使用
    }

    then(onFulfilled,onRejected){
        //、1.如果在then调用的时候,状态已经确定下来并且onFulfilled有值
        //若此处不做判断那么经过setTimout函数延迟执行的then方法会因为无法及时加入对应方法数组而被忽略
        if (this. status === PROMISE_STATUS_FULFILLED && onFulfilled) {
            //在此处能直接得到值是因为 一个对象只有一个this.value属性，对同一个对象调用该属性时可以拿到先前的赋值
            onFulfilled(this.value)
        }

        if (this. status === PROMISE_STATUS_REJECTED && onFulfilled) {
            onRejected(this.reason)
        }

        if (this. status === PROMISE_STATUS_PENDING) {
            this.onFulfilledFns.push(onFulfilled)
            this.onRejectedFns.push(onRejected)
        }

    }
}

// 在重复调用then时，因为调用者是同一个对象，该对象的状态第一次调用已经确定，所以可以直接调用，不用添加到数组里
const promise = new HYPromise((resolve, reject) => {//传入一个函数，一整个函数的引用在类中为executor
    console.log('状态pending')
    //在这当中状态依旧时pending，所以以下两行代码都会执行
    resolve(111)
    reject(222)//所以此处函数中的微任务也会加入代码执行队列，导致即使前方resolve执行此处的reject依旧执行
    // 解决方法 在queueMicrotask中加入if (this.status !== PROMISE_STATUS_PENDING) return进行判断
    // 由与resolve的微任务队列在前所以会将this.status赋值为fulfilled，因此当执行到reject的微任务队列就会因为不满足条件而退出
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

// const promise = new Promise((resolve, reject) => {
//     resolve("aaaaa")
// })

console.log(promise.status)//pending  执行此处还没有进入微队列所以依旧是pending状态

// 在此处若类中定义的then方法中无判断立即执行则无法执行settimeout中的then方法，因为此处设置了一秒延时
//类中定义的数组onFulfilledFns没有及时将该then加入到列表中，所以无法遍历执行
setTimeout(() => {
    console.log(promise.status)//fulfilled  此处上方的then方法执行完后也进入了微队列，将状态设置成

    promise.then(res => {
        //res3: 111 拿到111是因为前两个then函数已经对对象的value属性赋值，同一个promise对象共用一个value赋值
        console.log("res3:", res)
    }, err => {
    console.log("err3:", err)
})
}, 1000)

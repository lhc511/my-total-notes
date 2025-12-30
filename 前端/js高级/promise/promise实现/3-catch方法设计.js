// promise对象中执行reject函数，遇到微队列返回执行下面的他then函数，由于调用的then函数没传参所以默认undefined，
//类的内部方法为没有传参的onRejected赋值一个抛出错误函数，返回一个新promise对象同时执行executor函数，此时依旧是pending状态，
//给对应数组添加onRejected和onFulfilled函数，添加完后返回微队列去改变状态执行添加的函数(此处为抛出错误函数)，
// fn中的参数this.reason也会传参给抛错函数中的err参数，由于最终结果是抛出错误，所以会被捕获并执行try-catch中的函数，
///------注意 executor是所有函数的其实-----/ 即reject函数。相当于在新的promise对象中执行reject函数，同理err在从传递给reject，
//实现了reject参数在promise对象之间的传递。在执行reject遇到微队列调用catch方法，传入方法中的函数到类方法中的catch中
//再访去执行then方法，进行轮回


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
    constructor(executor) {//此处的executor就是从下面创建的对象中传递来的函数
        this.status = PROMISE_STATUS_PENDING
        this.value = undefined
        this.reason = undefined
        this.onFulfilledFns=[]
        this.onRejectedFns=[]

        const resolve = (value) => {
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
        // 判断onRejected是否有值，如果没有传入参数则抛出错误，
        onRejected = onRejected || (err => { throw err })//并不执行只是定义并赋值一个函数
        //直接返回一个新的HYPromise对象(此对象中的函数也会立即执行，即传入的判断条件)

        return new HYPromise((resolve, reject) => {
            //、1.如果在then调用的时候,状态已经确定下来并且onFulfilled有值
            if (this.status === PROMISE_STATUS_FULFILLED && onFulfilled) {
                execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
            }
            if (this.status === PROMISE_STATUS_REJECTED && onFulfilled) {
                execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
            }
            if (this.status === PROMISE_STATUS_PENDING) {
                if(onFulfilled)this.onFulfilledFns.push(()=>{
                    execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
                })
                if (onRejected)this.onRejectedFns.push(()=>{
                    execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
                })
            }
        })
    }

    catch(onRejected){
        this.then(undefined,onRejected)
    }
}



const promise = new HYPromise((resolve, reject) => {//传入一个函数，一整个函数的引用在类中为executor
    console.log('状态pending')
    // resolve(111)
    reject(222)
    // throw new Error("executor error message")
})

promise.then(res=>{
    console.log("res:"+res)
})//如果then中有第二个参数则会执行第二个参数，下面的catch就不会执行
    .catch(err=>{//此处是then函数中新返回的对象进行调用catch函数，而新对象没做reject
    console.log("err:"+err)
})
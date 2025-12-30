
const PROMISE_STATUS_PENDING = 'pending'
const PROMISE_STATUS_FULFILLED = 'fulfilled'
const PROMISE_STATUS_REJECTED = 'rejected'

// 工具函数
function execFunctionWithCatchError(execFn, value, resolve, reject) {
    try {//除非抛错否则均执行resolve()       //若抛错则执行下面函数  其中传入的value对应err的值
        const result = execFn(value)      //err => { throw err }
        // console.log(result+'------------')
        resolve(result)//现promise对象的方法
    } catch (err) {
        // console.log(err+"eeeeeeeeeeeeeeeeeeeee")
        reject(err)//现promise对象的方法
    }
}

class HYPromise {
    constructor(executor) {//此处的executor就是从下面创建的对象中传递来的函数
        this.status = PROMISE_STATUS_PENDING
        this.value = undefined
        this.reason = undefined
        this.onFulfilledFns=[]
        this.onRejectedFns=[]

        const resolve = (value) => {//原对象调用的方法
            if (this.status === PROMISE_STATUS_PENDING) {
                 //此处queueMicrotask中的代码会在最后执行，这是一种机制后面讲
                 queueMicrotask(()=> {//此种方法也可以规避错误也更推荐
                     if (this.status !== PROMISE_STATUS_PENDING) return
                     this.status = PROMISE_STATUS_FULFILLED//将状态赋值
                     this.value = value
                     //对数组中的所有函数进行遍历实行
                     this.onFulfilledFns.forEach(fn => {
                         fn(this.value)
                         // fn()//this.value在此处并无实际意义
                     })
                 })
            }
        }

        const reject = (reason) => {  //原对象调用的方法
            //若前面的函数先执行则this.statu已改变，就不会执行此处的代码
            if (this.status === PROMISE_STATUS_PENDING) {
                 queueMicrotask(()=> {
                     if (this.status !== PROMISE_STATUS_PENDING) return
                     //此处的this指向调用then/catch等方法(依旧返回promise对象即promise对象调用promise对象)的promise对象
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
    //then直接返回一个新对象/在新对象当中
    then(onFulfilled,onRejected){
        // 判断onRejected是否有值，如果没有传入参数则抛出错误
        onRejected = onRejected || (err => { throw err })

        //*******没有此处第一种情况会中断函数
        const defaultOnFulfilled = value => { return value }
        onFulfilled = onFulfilled || defaultOnFulfilled
        //***************

        //直接返回一个新的HYPromise对象(此对象中的函数也会立即执行，即传入的判断条件)
        return new HYPromise((resolve, reject) => {
            //、1.如果在then调用的时候,状态已经确定下来并且onFulfilled有值
            if (this.status === PROMISE_STATUS_FULFILLED) {
                execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
            }
            if (this.status === PROMISE_STATUS_REJECTED) {
                execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
            }
            if (this.status === PROMISE_STATUS_PENDING) {
                if(onFulfilled)this.onFulfilledFns.push(()=>{//此处再函数当中执行另一个函数
                    execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
                })
                if (onRejected)this.onRejectedFns.push(()=>{
                    execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
                })
            }
        })
    }

    catch(onRejected){
        return this.then(undefined,onRejected)//返回一个promise对象
    }

    finally(onFinally){
        //此处将两个参数位置都填onFinally函数，指不管什么状态都会执行该函数
        this.then(() =>{
            onFinally()
        }, () => {
            onFinally()
        })
    }

    static resolve(value) {
        //返回了一个HYPromise对象的同时给里面传参executor，并将参数函数在类的内部执行，调用内部的resolve函数
        return new HYPromise((resolve) => resolve(value))
    }
    //reject函数同理
    static reject(reason) {
        return new HYPromise((resolve, reject) => reject(reason))
    }
}

HYPromise.resolve("Hello World").then(res => {
    console.log("res:", res)
})

HYPromise.reject("Error Message").catch(err => {
    console.log("err:", err)
})
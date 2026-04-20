
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
        this.onFulfilledFns = []
        this.onRejectedFns = []

        const resolve = (value) => {//原对象调用的方法
            if (this.status === PROMISE_STATUS_PENDING) {
                //此处queueMicrotask中的代码会在最后执行，这是一种机制后面讲
                queueMicrotask(() => {//此种方法也可以规避错误也更推荐
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
                queueMicrotask(() => {
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
        } catch (err) {
            reject(err)
        }

    }

    //then直接返回一个新对象/在新对象当中
    then(onFulfilled, onRejected) {
        // 判断onRejected是否有值，如果没有传入参数则抛出错误
        onRejected = onRejected || (err => {
            throw err
        })

        //*******没有此处第一种情况会中断函数
        const defaultOnFulfilled = value => {
            return value
        }
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
                if (onFulfilled) this.onFulfilledFns.push(() => {//此处再函数当中执行另一个函数
                    execFunctionWithCatchError(onFulfilled, this.value, resolve, reject)
                })
                if (onRejected) this.onRejectedFns.push(() => {
                    execFunctionWithCatchError(onRejected, this.reason, resolve, reject)
                })
            }
        })
    }

    catch(onRejected) {
        return this.then(undefined, onRejected)//返回一个promise对象
    }

    finally(onFinally) {
        //此处将两个参数位置都填onFinally函数，指不管什么状态都会执行该函数
        this.then(() => {
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

    static all(promises) {//传进来创建的promise对象，存放在一个数组中
        return new HYPromise((resolve, reject) => {//由于all也可以连续调用所以返回一个promise对象
            const values = []
            //在此处决定到底是用reject还是resolve状态并将两个函数的参数传递下去供下一个then/catch使用
            promises.forEach(promise => {//将传来的每一个promise对象调用then方法，再根据resolve/reject传递参数(即结果)添加到数组中
                promise.then(res => {
                    values.push(res)
                    // 判断是否传递完成
                    if (values.length === promises.length) {
                        resolve(values)//传递完成则将values[传递的值的数组]保存在该对象的this.value属性中
                    }
                }, err => {//若传递的对象是reject状态就会执行该代码(和resolve一样层层执行)
                    reject(err)
                })
            })
        })
    }

    //返回所有对象的状态和值，所以不管resolve还是reject都是
    static allSettled(promises) {
        return new HYPromise((resolve) => {
            const results = []
            promises.forEach(promise => {
                promise.then(res => {
                    results.push({status: PROMISE_STATUS_FULFILLED, value: res})
                    if (results.length === promises.length) {
                        resolve(results)//将此处存储的结果带给下一个对象
                    }
                }, err => {
                    results.push({status: PROMISE_STATUS_REJECTED, value: err})
                    if (results.length === promises.length)
                        resolve(results)
                })
            })
        })
    }


    // 在实现 Promise.race() 方法时，外部 Promise 状态锁定导致后续回调失效的核心原因在于 Promise 的状态机机制和不可变性原则。
    // 触发 resolve(res) 或 reject(err)
    // 外部 Promise 状态立即锁定（如变为 fulfilled）
    // 后续其他 Promise 完成时，其回调中的 resolve/reject 因状态已锁定而失效（规范要求忽略后续调用）

    // 此处promises.forEach遍历的 每一个对象都会执行传递的参数函数，但是在第一个promise对象执行后
    //return new HYPromise(返回的新对象)中的status会被第一个中的resolve函数的微队列中设置状态，在此
    //之后由于执行时不再是pending状态，所以都会被忽略，因此只返回一个

    //setTimeout会给每一个对象中的resolve/reject延迟执行时间，此处返回最先执行的
    static race(promises) {
        return new HYPromise((resolve, reject) => {
            promises.forEach(promise => {
                // 当有某一个对象中的resolve执行完后直接执行该对象的代码
                //以下两种写法一样
                // promise.then(res => {
                //     resolve(res)
                // }, err => {
                //     reject(err)
                // })
                promise.then(resolve, reject)
            })
        })
    }

    static any(promises) {
    // resolve必须等到有一个成功的结果
    // reject所有的都失败才执行reject
        const reasons = []
        return new HYPromise((resolve, reject) => {
            promises.forEach(promise => {
                promise.then(resolve, err => {
                    reasons.push(err)
                    if (reasons.length === promises.length) {
                        reject(new AggregateError(reasons))
                    }
                })
            })
        })
    }

}


// race函数 数组中传递的所有对象哪个块执行哪个
const p1 = new Promise((resolve,reject) => {
    setTimeout(() => {
        reject(1111)
    }, 1000)
})
const p2 = new Promise((resolve,reject) => {
    // setTimeout(() => { resolve(2222) }, 2000)
    setTimeout(() => { resolve(2222) }, 2000)
})
const p3 = new Promise((resolve,reject) => {
    setTimeout(() =>{ reject(3333) }, 3000)
})

// HYPromise.race([p1, p2, p3]).then(res => {
//     console.log(res)
// }).catch(err => {
//     console. log(err)
// })

HYPromise.any([p1, p2, p3]).then(res => {
    console.log(res)
}).catch(err => {
    console. log(err)
})


//创建HYPromise对象名叫promise，执行resolve函数，到微队列先执行下方的then方法，将函数参数传递给类中的then方法，
//then方法传回一个新的promise对象，执行新promise对象中的executor，由于是pending状态(微队列执行后才修改状态),
//所以将一个包含传来的参数函数的外层函数存到数组，再返回执行微队列先改变原对象的状态，因为此微队列是原promise对象的代码，
//再将原promise对象中调用的resolve方法中的参数赋值给this.value,最后遍历执行数组中的方法=>
//先执行一遍调用then方法传来的参数函数即onFulfilled或onRejected。将该函数return的返回值(若午返回默认为undefined)赋值给局部变量result
//最后再执行resolve方法，此resolve是新promise1对象(第一个then方法返回的方法)，遇到微队列再向主线程执行

//新promise对象(promise1)调用catch方法是，将目标函数作为参数传递给类中的catch方法然后再传递给then方法(返回一个新promise对象记作promise2)
//将传递函数分给promise1中的对应数组(隐式绑定)，undefined传给this.onFulfilledFns，目标函数参数传给this.onRejectedFns，
//再执行promise1的resolve中的微队列，遍历执行传入函数，即this.onFulfilledFns的函数，而此是该数组中函数的内层函数的execFn只是undefined，所以不做任何事情，也无法作为函数执行所以中断程序

//如果把第一个对象中的resolve函数的执行换成reject函数，就是执行reject的保存函数数组中的代码，即使没传函数也会被直设置为一个err => { throw err }箭头函数
//使this.onRejectedFns=[]始终有函数，在执行execFn(value)抛出错误[在抛出错误中抛出的值就是捕获的值]，被捕获后执行reject(此处是promise2对象的reject)函数
//因为第一个then方法调用返回了一个promise对象return new promise，在这个对象中执行的reject

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
                     this.onFulfilledFns.forEach(fn => {//fn是后面所有then方法传回的函数，then方法传回的第 1 个参数
                         // fn(this.value)//此处的fn是下方判断条件下传进数组的外层函数，里面还会执行一个内函数，内函数会执行then等传参的函数
                         fn()//this.value在此处并无实际意义
                         // fn()//this.value在此处并无实际意义
                     })
                 })
            }
        }

        const reject = (reason) => {  //原对象调用的方法
            //若前面的函数先执行则this.statu已改变，就不会执行此处的代码
            if (this.status === PROMISE_STATUS_PENDING) {

                //若将此代码放在上方，则赋值后满足条件then中会执行函数，而此时queueMicrotask中的this.reason还未被赋值并传递，所以后面打印出来的值时undefined
                // this.status = PROMISE_STATUS_REJECTED

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



}


const promise = new HYPromise((resolve, reject) => {//传入一个函数，一整个函数的引用在类中为executor
    console.log('状态pending')
    // resolve(111)
    reject(222)
    // throw new Error("executor error message")
})

//------第一种情况------------------
//此处的finally不执行(再第一个promise执行时是resolve状态)，若是reject状态则执行代码
promise.then(res=>{
    console.log("res:"+res)
    return 'aaaa'       //此处最终执行代码是resolve(value)  value是aaaa
//    在此处将catch中的函数传进去后在then中判断并将其添加到数组中后会返回去执行then创建promise对象的resolve微队列
    //而catch传递的onFulfilled的值是undefined，因此数组中在执行的函数是undefined，就此中断
}).catch(err=>{
    console.log("err2:"+err)
}).finally(()=>{
    console.log('FINALLY')
})

//-------------第二种情况
//此处不管是reject还是resolve状态都会执行finally函数
// promise.then(res=>{
//     console.log("res:"+res)
//     return 'aaaa'
// }).then(res=>{
//     console.log("res2:"+res)
// }).finally(()=>{
//     console.log('FINALLY')
// })
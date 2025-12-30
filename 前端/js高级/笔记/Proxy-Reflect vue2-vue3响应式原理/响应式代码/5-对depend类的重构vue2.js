// 保存当前需要收集的响应式函数
let activeReactiveFn = null

/*Depend优化:
 1>·depend方法
 2>·使用Set来保存依赖函数,而不是数组[]
*/
class Depend {
    constructor() {
        //set对象里面不会出现重复
        this.reactiveFns = new Set()
    }
    //
    // addDepend(reactiveFn) {
    //     this.reactiveFns.push(reactiveFn)
    // }

    depend () {
        if (activeReactiveFn) {
            this.reactiveFns.add(activeReactiveFn)
        }
    }

    notify() {
        this.reactiveFns.forEach(fn => {
            fn()
        })
    }
}

// *************************对obj的响应式**************************
// 对象的响应式  在独对象发生改变之后自动执行功能就是响应式

//添加监听函数
function watchFn(fn) {
    activeReactiveFn = fn
    fn()
    activeReactiveFn=null
}

const targetMap = new WeakMap()
function getDepend(target, key) {
    let map = targetMap.get(target)
    if (!map) {
        map = new Map()
        targetMap.set(target, map)
    }

    let depend = map.get(key)
    if (!depend) {
        depend = new Depend()
        map.set(key, depend)
    }
    return depend
}

//在reactive传入的对象中取出键后通过遍历的方式给每一个键进行拦截操作
function reactive(obj) {
    // {name: "why", age: 18}
    //、ES6之前,使用Object.defineProperty
    Object.keys(obj).forEach(key => {
        let value = obj [key]
        Object.defineProperty(obj, key, {
            get: function () {
                const depend = getDepend(obj, key)
                depend.depend()
                return value
            },
            set: function (newValue) {
                value = newValue
                const depend = getDepend(obj, key)
                depend.notify()
            }
        })
    })
    return obj
}

const obj = {
    name: "why",  // depend对象
    age: 18,       // depend对象
}

const objProxy = reactive(obj)

//对函数进行监听
// watchFn
// watchFn(() => {
//     console.log(objProxy.name, 'dojvhndaojv')//此处两次都会在依赖中添加同一个方法，使代码重复执行
//     console.log(objProxy.name, "+++++++")
       //用set对象来解决，因为set对象内没有重复代码
// })
// console. log("改变------------------------------------------------------obj的name值")
// console.log(objProxy.name)
// objProxy.age = 100
// objProxy.name = "james"
// objProxy.name = "curry"

//// *************************对info的响应式**************************
const info = {
    address: "广州市",
    height: 1.88
}

const infoProxy = reactive(info)

watchFn(() => {
    console.log(infoProxy.address)
})
infoProxy.address = "北京市"

/////////////////////////////////////
// const foo = reactive({
//     name: "foo"
// })
// watchFn(() => {
//     console.log(foo.name)
// })


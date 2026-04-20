class Depend {
    constructor() {
        this.reactiveFns = []
    }

    addDepend(reactiveFn) {
        this.reactiveFns.push(reactiveFn)
    }

    notify() {
        this.reactiveFns.forEach(fn => {
            fn()
        })
    }
}

//添加监听函数
let activeReactiveFn = null
function watchFn(fn) {
   // depend.addDepend(fn)
    activeReactiveFn = fn
    //在此处执行函数的过程中若log则跳到代理对象中的get捕获器

    fn()//监听的函数在内部有改变属性的操作时也会触发捕获器，过程中将方法添加到对象属性的依赖中

    //因为捕获器触发后全局变量中的函数已经被添加到depend类的列表中了所以清除
    activeReactiveFn=null
}


///////////////////////////////////////////////////////////////////////////
//·封装一个获取depend函数
const targetMap = new WeakMap()
//                原对象   , 键
//根据对象中不同的属性创建相应的依赖(depend对象)
function getDepend(target, key) {
    //targetMap{target,Map对象{key,depend对象{}}}
    //根据target对象获取map的过程
    let map = targetMap.get(target)//拿出原对象的值  即map对象
    if (!map) {
        map = new Map()//创建一个map对象 (下面将 原对象 与 新map对象 相关联)
        targetMap.set(target, map)     //给 原对象的 值 设置为创建的map对象
    }
    //根据key获取depend对象
    let depend = map.get(key) //从上方创建的map对象中痛过key获取depend对象
    if (!depend) {  //如果没有对象
        depend = new Depend() //创建一个depend对象
        map.set(key, depend)//  在map对象中将键的值设置为 depend 对象
    }
    return depend  //返回拿出来的对象
}

// 对象的响应式  在独对象发生改变之后自动执行功能就是响应式
const obj = {
    //有捕获器的属性
    // _name: "why",  // depend对象
    //无捕获器的属性
    name: "why",  // depend对象
    age: 18,       // depend对象
    // get name() {
    //     //在代理对象有receiver参数后，此处this指向代理对象，因此this._name会触发代理对象的get函数
    //     return this._name
    // },
    // set name(newValue) {
    //     this._name = newValue
    // }
}

// 监听对象的属性变量:Proxy(vue3)/Object.defineProperty(vue2)
const objProxy = new Proxy(obj, {
    get: function (target, key, receiver) {

        // 根据target和key获取对应depend对象
        const depend=getDepend(target,key)
        //此处只有给对象的属性添加依赖，无执行方法
        depend.addDepend(activeReactiveFn)
        return Reflect.get(target, key, receiver)
    },
    set: function (target, key, newValue, receiver) {
        Reflect.set(target, key, newValue, receiver)
        //自动执行的代码 此处不会做区分会全部收集在一个属性当中，而不同的属性可能要做不同的操作，因此错误
        // depend.notify()
        const depend = getDepend(target, key)//找到对象属性的全部依赖方法
        depend.notify()//执行方法
    }
})

//对函数进行监听
watchFn(function () {
    console.log("你好啊,李银河")
    console.log("Hello World")
    console.log(objProxy.name) // 此处会执行代理对象中的get捕获器，并将该函数添加到该对象属性的依赖当中
})

watchFn(function () {
    console.log(objProxy.name,'casdvvdsdv')
})

watchFn(function() {
    console.log(objProxy.age, "age 发生变化是需要执行的 ---- 1")//此处触发get捕获器，添加方法到age的依赖中
})
watchFn(function() {
    console.log(objProxy.age, "age 发生变化是需要执行的 ---- 2")
})
watchFn(function() {
    //此处两个属性都会触发get捕获器，所以不管对哪个属性做操作(目前只有设置值的操作)都会触发该方法，将两个都打印
    console.log(objProxy.name, "新函数")
    console.log(objProxy.age, "新函数")
})


console. log("改变------------------------------------------------------obj的name值")
// console.log(objProxy.name)
objProxy.age = 100
// objProxy.name = "james"
// objProxy.name = "curry"
//


// const info = {
//     address: "广州市"
// }
// watchFn(function() {
//     console.log(info.address, "监听address变化+++++++++1")
// })
// watchFn(function() {
//     console.log(info.address, "监听address变化+++++++++2")
// })

// 数据结构大概思路
// //对每一个对象的属性的监听都要分类，不同属性发生改变时只调用对应方法
// //obj对象
// // name: depend
// // age: depend
// const objMap = new Map ()
// objMap.set("name", "nameDepend")
// objMap.set("age", "ageDepend")
// console.log(objMap)//{'name' => 'nameDepend', 'age' => 'ageDepend'}
// //info对象
// // address: depend
// // name: depend
// const infoMap = new Map()
// infoMap.set("address", "addressDepend")
// const targetMap = new WeakMap()
// targetMap.set(obj, objMap)
// targetMap.set(info, infoMap)
// // obj.name
// // const depend = targetMap.get(obj).get("name")
// // depend.notify()
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

// 定义类对象
const depend = new Depend()
//添加监听函数
function watchFn(fn) {
   depend.addDepend(fn)
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
        return Reflect.get(target, key, receiver)
    },
    set: function (target, key, newValue, receiver) {
        Reflect.set(target, key, newValue, receiver)
        //自动执行的代码
        depend.notify()
    }
})

//对函数进行监听
watchFn(function () {
    const newName = objProxy.name
    console.log("你好啊,李银河")
    console.log("Hello World")
    console.log(objProxy.name) // 10017
})

watchFn(function () {
    console.log(objProxy.name,'casdvvdsdv')
})

objProxy.name = "kobe"
// console.log(objProxy.name)
//当原对象有getset捕获器
// console.log(objProxy.name===obj._name) //true
// 当没有捕获器时
console.log(objProxy.name===obj.name) //true

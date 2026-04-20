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
    name: "why",  // depend对象
    age: 18       // depend对象
}

//对函数进行监听
watchFn(function () {
    const newName = obj.name
    console.log("你好啊,李银河")
    console.log("Hello World")
    console.log(obj.name) // 10017
})

watchFn(function () {
    console.log(obj.name,'casdvvdsdv')
})

obj.name = "kobe"
// 当修改了属性之后自动执行以下代码
depend.notify()

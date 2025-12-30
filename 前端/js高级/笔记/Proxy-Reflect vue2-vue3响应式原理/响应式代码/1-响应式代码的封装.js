// 封装一个响应式的函数
let reactiveFns = []
function watchFn(fn) {
    reactiveFns.push(fn)
}
// 对象的响应式  在独对象发生改变之后自动执行功能就是响应式
const obj = {
    _name: "why",
    age: 18,
}

watchFn(function foo() {
    const newName = obj.name
    console.log("你好啊,李银河")
    console.log("Hello World")
    console.log(obj.name) // 10017
})

watchFn(function demo() {
    console.log(obj.name,'casdvvdsdv')
})

//对函数进行监听
function foo(){
    const newName = obj.name
    console.log("你好啊,李银河")
    console. log("Hello World")
    console. log(obj.name) // 100行
}

function bar() {
    console.log("普通的其他函数")
    console.log("这个函数不需要有任何响应式")
}
// 当修改了属性之后自动执行以下代码
obj.name = "kobe"
reactiveFns.forEach(fn => {
    fn()
})

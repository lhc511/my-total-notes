import { name, age, foo } from './foo.js'

console. log(name)


//、import函数返回的结果是一个Promise对象
//此处在下载和解析文件时都交给了浏览器，js的主线程不受影响，继续执行代码
import("./foo.js") .then(res => {
    console.log("res:", res)
    console.log(res.age)//18  可以通过对象去访问
})
//在导入时必须把导入的代码的文件解析完之后才会执行后续的代码
console.log("后续的代码都是不会运行的~")
//·ES11新增的特性
//·meta属性本身也是一个对象 :· {·url :· ”当前模块所在的路径”·}
console. log(import.meta)
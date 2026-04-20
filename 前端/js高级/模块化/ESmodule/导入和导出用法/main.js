//导入方式一：普通导入
//      变量，变量，函数， 类
// import {name,age,foo,Person} from "./foo.js" //在webpack环境下不用加.js，因为webpack会自动加上
// import {fName,fAge,fFoo,} from "./foo.js" //在webpack环境下不用加.js，因为webpack会自动加上

//·2.导入方式二 :· 起别名
// import {name as fName, age as fAge, foo as fFoo} from './foo.js'
//
// console.log(fName)
// console.log(fAge)
// console.log(fFoo)

//·3.导入方式三 :· 将导出的所有内容放到一个标识符中
import * as foo from './foo.js'

console. log(foo.name)
console. log(foo.age)
foo. foo()

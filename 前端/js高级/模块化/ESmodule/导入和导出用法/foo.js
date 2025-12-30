//第一种导出方式:export 声明语句 导出后面的内容
// export const name = "why"
// export const age = 18
//
// export function foo () {
//     console.log("foo function")
// }
// export class Person {}

const name ="why"
const age = 18
function foo () {
    console.log("foo function")
}
//、2.第二种 :· export·导出·和·声明分开
export {//此处的大括号不是对象，而是本身的语法，内部将要导出的内容列出来
    // name:name, 此种写法错误
    name,
    age,
    foo
}

//·3.第三种方式:第二种导出时起别名，运用较少
//并且在起冲突时一般不会在这里起别名，而是会在导入的时候起别名
// export {
//     name as fName,
//     age as fAge,
//     foo as fFoo
// }
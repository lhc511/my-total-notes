// ES6之前拼接字符串和其他标识符
// const name = "why"
// const age = 18
// const height = 1.88
// // console. log ("my name is " + name + ", age is " + age + ", height is " + height)
//
// //、ES6提供模板字符串
// const message = `my name is ${name}, age is ${age}, height is ${height}`
// console. log(message)
//
// const info = 'age double is ${age * 2}'
// console. log(info)
//
// function doubleAge () {
//     return age * 2
// }
// const info2 = `double age is ${doubleAge()}`
// console.log(info2)

//用法2
//第一个参数依然是模块字符串中整个字符串,只是被切成多块,放到了一个数组中
// 第二个参数是第一个${}中的内容
function foo(m, n) {
    console. log(m, n, '---')
}

// foo("Hello", "World")

//、另外调用函数的方式:标签模块字符串

foo`Hello World` //m的参数为['Hello World']

const name = "why"
const age = 18
// ['Hello', 'Wo', 'rld'] why ---
//其中的${}会将模板字符串切割并放在一个数组中，并且函数第一个参数传递的永远是完整的字符串(不论何种形式)
foo`Hello${name}Wo${age}rld`

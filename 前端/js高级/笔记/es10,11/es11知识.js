// ES11Ż#0 max_safe_integer
// const maxInt = Number. MAX_SAFE_INTEGER   //此处意思为能够正确显示的最大数字，超出后可能无法正确显示
// console. log(maxInt) // 9007199254740991
// console. log(maxInt +1)//9007199254740992
// console.log(maxInt + 2)//9007199254740992 此处显示错误
//
// //-ES11之后:BigInt   数字后面跟一个 n 将普通数字转化为大数字
// const bigInt = 900719925474099100n
// console. log(bigInt + 10n)
//
// const num = 100
// console.log(bigInt + BigInt(num))//将数字转化为大数字类型再相加
//
// const smallNum = Number(bigInt)
// console. log(smallNum)//转换会普通数字后不一定正确


//-ES11:空值合并运算 ·??
// const foo = undefined
// // const bar = foo | | "default导出 value"  //0，空字符串 也会被看作false
// const bar = foo ?? "defualt value"//只将undefined和null判做false，0，空字符串 可正常获取
// console. log(bar)//


// 可选链 optional chain
// const info = {
//     name: "why",
//     friend: {
//         name: "lilei",
//         girlFriend: {
//             name: "hmm"
//         }
//     }
// }
// console.log(info. friend.girlFriend.name)

// console.log(info. friend.girlFriend.name)
//旧方法
// if (info && info. friend && info. friend.girlFriend) {
//     console.log(info.friend.girlFriend.name)
// }

//-ES11提供了可选链(Optional Chainling) 新方法
//一般情况下 值不存在会直接报错，但是在加入了可选择链(?)后当通过对应属性访问的值不存在会直接返回undefined并继续执行
// console.log(info.friend ?. girlFriend ?. name)
//
// console.log('其他的代码逻辑')


//·在浏览器下
// console. log(window)
// console. log(this)

//、在node下
// console. log(global)

//-ES11
console. log(globalThis)//可以获取当前环境的全局对象

// Object.values
// const obj = {
//     name: "why",
//     age: 18
// }
// console.log(Object.keys(obj))//['name', 'age']
// console.log(Object.values(obj))//['why', 18]
//
// //用的少
// console. log(Object.values(["abc","cba", "nba"]))//['abc', 'cba', 'nba']
// console. log(Object.values("abc"))//['a','b','c']

//Object.entries(obj)
// const obj = {
//     name: "why",
//     age: 18
// }
// console.log(Object.entries(obj))//[['name', 'why'],['age', 18]]
//
// const objEntries = Object.entries(obj)
// objEntries. forEach(item => {
//     console.log(item[0], item[1])
// })
// console.log(Object.entries(["abc","cba", "nba"]))//[ [ '0' , 'abc' ], [ '1', 'cba' ], [ '2', 'nba' ] ]
// console. log(Object.entries("abc"))//[ [ '0', 'a' ], [ '1', 'b' ], [ '2 , c' ] ]

//padStart，PadEnd
// const message = "Hello World"
// //先将message向前添加 * 到共十五个字符(若第二个参数没写则默认是空格)，，然后再向后添加 - 扩展到共20个字符
// const newMessage = message.padStart(15, "*").padEnd(20, "-")//****Hello World-----
// console. log(newMessage)

//案例
// const cardNumber = "321324234242342342341312"
// const lastFourCard = cardNumber.slice(-4)
// console.log(lastFourCard)
// console.log(cardNumber)
// const finalCard = lastFourCard.padStart(cardNumber.length, "*")//将finalCard填充到cardNumber原本的位数
// console. log(finalCard)
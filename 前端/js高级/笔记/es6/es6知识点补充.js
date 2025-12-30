// 三种自变量增强写法
// var name = "why"
// var age = 18
// //对象本身并没有作用域，所以箭头函数直接指向window
// var obj = {
// //property·shorthand(属性的简写)
//     //    原本写法
//     //     name:name,
//     //     age:age
//     name,
//     age,
//
// //method shorthand(方法的简写)
//     foo: function () {
//         console.log(this)
//     },
//     //此处为上面方法的简写，不能代替下面的箭头函数，因为箭头函数this指向父作用域
//     bar() {
//         console.log(this)
//     },
//
//     baz: () => {
//         console.log(this)
//     },
//
//     //3.computed·property name(计算属性名)
//     [name + 123]: 'hehehehe'
// }
// obj.baz()//Window {window: Window, self: Window, document: document, name: 'why', location: Location, …}
// //隐式绑定，指向对象
// obj.bar()//{name: 'why', age: 18, foo: ƒ, bar: ƒ, baz: ƒ}
// obj.foo()//{name: 'why', age: 18, foo: ƒ, bar: ƒ, baz: ƒ}


// 数组结构
// var names = ["abc", "cba", "nba"]
// var item1 = names[0]
// var item2 = names [1]
// var item3 =names[2]

// // 对数组的结构:[]
// var [item1, item2, item3]=names
// console.log(item1, item2, item3)
//
// //解构后面的元素
// var [, , itemz] = names
// console.log(itemz)
//
// //、解构出一个元素,后面的元素放到一个新数组中   与函数传参的 剩余参数 类似
// var [itemx, ... newNames] = names
// console.log(itemx, newNames)
//
// //~解构的默认值
// var [itema, itemb, itemc, itemd = "aaa"] = names
// console. log(itemd)

//对象结构
// var obj = {
//     name: "why",
//     age: 18,
//     height: 1.88
// }
//
// // 对象的解构:{}  获取其中的值。可以打乱顺序
// var { name, age, height } = obj
// console. log(name, age, height)
//
// var { age } = obj
// console. log(age)
//
// //给属性name命名为newName
// var { name: newName } = obj
// console.log (newName)
// //取新名字的同时 给出默认值
// var { address: newAddress = "N" } = obj
// console.log(newAddress)
//
// function foo(info) {
//     console.log(info.name, info.age)
// }
// foo(obj)
//
// function bar({name, age}) {
//     console.log(name, age)
// }
// bar(obj)

// 对象参数和默认值以及解构
// function printInfo({name, age} ={name: "why", age: 18}) {
//     console.log(name, age)
// }
// printInfo({name: "kobe", age: 40})
//
// // 另外一种写法
// function printInfol({name="why",age=18}={}) {
//     console.log(name, age)
// }
// printInfol()

// 有默认值的形参最好放到最后,若未放最后则徐三个参数全写，即第一种写法。
// function bar(x, y, z = 30) {
//     console.log(x, y, z)
// }
// // bar(10, 20)
// bar(undefined, 10, 20)
// bar( 10, 20)

// 4.有默认值的函数的length属性，从默认值开始包括默认值都不计算在内
// function baz(x, y, z, m, n = 30) {
//     console. log(x, y, z, m, n)
// }
// console. log(baz. length)//4
//剩余参数
// function foo( m, n, ... args) {//剩余参数是真数组
//     console.log(m, n)
//     console. log(args)
//     console. log(arguments) //[20, 30, 40, 50, 60]打印出所有参数  伪数组
// }
//
// foo(20,30,40, 50,60)
// rest paramaters必须放到最后

// 展开运算符
// const names = ["abc", "cba", "nba"]
// const name = "why"
// const info = {name: "why", age: 18}
// //1.函数调用时
// function foo(x, y, z) {
//     console.log(x, y, z)
// }
// // foo. apply (null, names) //apply传递的是一个数组
// foo( ... names)
// foo( ... name) //会将字符串拆开逐个传递
//
// // 2.构造数组时
// const newNames = [ ... names, ... name]
// console. log(newNames)
//
// // 3.ES2018(ES9)，对象展开
// const obj = { ... info, address: "/N" }
// console. log(obj)//{name: 'why', age: 18, address: '/N'}

//展开运算符其实是浅拷贝
// const info = {
//     name: "why",
//     friend: { name: "kobe"}
// }
//
// const obj = { ... info, name: "coderwhy" }
// // console.log(obj)
// obj.friend.name = "james"   //此处改变info也会改变
// console.log(info.friend.name)


// Symbol就是为了解决上面的问题,用来生成一个独一无二的值。
// Symbol值是通过Symbol函数来生成的,生成后可以作为属性名;
// □也就是在ES6中,对象的属性名可以使用字符串,也可以使用Symbol值

//·ES6中Symbol的使用
// const s1 = Symbol()
// const s2 = Symbol()
// console.log(s1)//Symbol()
// console. log(s1 === s2)
// //·ES2019(ES10)中,Symbol还有一个描述(description)
// const s3 = Symbol("aaa")
// console. log(s3.description)

//·3.Symbol值作为key
//-3.1.在定义对象字面量时使用
// const obj = {
//     [s1]: "abc",
//     [s2]: "cba"
// }
//
// //-3.2.新增属性
// obj [s3] = "nba"
//
// //3.3.Object.defineProperty方式
// const s4 = Symbol()
// Object.defineProperty(obj, s4,{
//     enumerable: true,
//     configurable: true,
//     writable: true,
//     value: "mba"
// })
// console.log(obj[s1], obj[s2], obj[s3], obj[s4])
//·注意:不能通过.语法获取
// console. log(obj.sl)

// 4.使用Symbol作为key的属性名,在遍历/Object.keys等中是获取不到这些Symbol值
//需要0bject.getOwnPropertySymbols来获取所有Symbol的key
// console.log(Object.keys(obj))//[]
// console.log(Object.getOwnPropertyNames(obj))//[]
// console.log(Object.getOwnPropertySymbols(obj))//[Symbol(), Symbol(), Symbol(aaa), Symbol()]
// const sKeys = Object.getOwnPropertySymbols(obj)
// for (const sKey of sKeys) {
//     console. log(obj [sKey]) //abc，cba，nba，mba
// }

// 5.Symbol.for(key) 可以使两个对象相等/Symbol.keyFor(symbol) (了解)
// const sa = Symbol.for("aaa")
// const sb = Symbol.for("aaa")
// console. log(sa === sb)   //true
//
// const key = Symbol.keyFor(sa)  //传入一个symbol对象啊返回key值
// console. log(key) //aaa
// const sc = Symbol.for(key)
// console.log(sa === sc)//true

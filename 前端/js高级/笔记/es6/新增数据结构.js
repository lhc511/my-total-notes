// set结构
// 10, 20, 40, 333
//1.创建Set结构 set结构中的元素不能重复
// const set = new Set()
// set.add(10)
// set.add(20)
// set.add(40)
// set.add(333)
// set.add(10) //此处无法添加
//
// //此处可以添加，因为此处添加的两个对象实际在内存中存储在不同的位置，是两个独立的对象
// // set.add({})
// // set.add({})
//
// const obj = {}//这里不能添加，obj指向同一个对象
// set.add(obj)
// set.add(obj)
//
// console. log(set)//{10, 20, 40, 333, {}}

// 3.对数组去重(去除重复的元素)
// const arr = [33, 10, 26, 30, 33, 26]
//方法一
// const newArr = []
// for (const item of arr) {
//     // indexOf()方法返回元素的索引（从0开始），如果元素不存在则返回-1
//     if (newArr.indexOf(item) === -1) {
//         newArr.push(item)
//     }
// }
// console.log(newArr)//[33, 10, 26, 30]
//方法二
//Array.from() 是 JavaScript 中用于将类数组对象或可迭代对象转换为真正数组

// const arrSet = new Set(arr)  //也可以直接传递数组 new Set([])
// const newArr = Array.from(arrSet)
// const newArr =[ ... arrSet]
// console.log(newArr)

//4.size属性  获取set中的数据个数
// console.log(arrSet.size) //4

// 5.Set的方法
// add
// arrSet.add(100)
// console. log(arrSet)
//
// // delete
// arrSet.delete(33)
// console.log(arrSet)
//
// // has   判断是否有该属性
// console.log(arrSet.has(100))//true
//
// // clear
// arrSet.clear()
// console.log(arrSet)//删除所有set中的属性

////-6.对Set进行遍历
// arrSet. forEach(item => {
//     console.log(item)
// })

// for(const item of arrSet){  //和python中的for in类似
//     console.log(item)
// }

//弱引用
// 弱因引用就是 依旧可通过对象去访问属性，但是GC(垃圾回收机制)不认可这种引用，依旧会对引用对象所在的内存空间进行回收
//强引用则是不会回收
//区别二:对对象是一个弱引用
// const  weakSet=new WeakSet()  //只能存放对象
//
// let obj = {
//     name: "why"
// }
// //weakSet.add(obj)
//
// const set = new Set()
// //·建立的是强引用
// set.add(obj)   //给set结构中添加的都是obj的地址(引用)
//
// //、建立的是弱引用
// weakSet.add(obj)
//
// //应用案例
// //、3.WeakSet的应用场景
// const personSet = new WeakSet()
// class Person {
//     constructor() {//除了设置属性还有别的进行初始化操作
//         personSet.add(this) //将绑定的对象传到弱引用对象结构中
//     }
//     running() {
//         if (!personSet.has(this)) {//对绑定的对象进行过滤
//             throw new Error("不能通过非构造方法创建出来的对象调用running方法")
//         }
//         console.log("running~", this)
//     }
// }
// const p = new Person()
// //此处对p对象进行了一次引用，在构造函数中personSet对p也进行了一次引用，但是由于弱引用所以不算
// //所以在清除时只要赋值p=null，不用在对personSet的数据额外清除
// p.running()
// p.running. call ({name: "why"})


// const obj1 = { name: "why" }
// const obj2 = { name: "kobe" }

// 当对象被用作属性名时，JavaScript会调用该对象的toString()方法来获取字符串表示。
// 所有JavaScript对象都继承自Object.prototype，其默认toString()方法返回"[object Object]
// const info = {
//     [obj1]: "aaa",
//     [obj2]: "bbb"
// }
// console. log(info)//{[object Object]: 'bbb'}
// 只存在一个数据的原因：
// []计算属性名会将里面的变量计算并转换成字符串形式，而obj1和obj2计算后的结果都是'[object Object]'，
//所以此处并不是对象作为key值，而是用的对象转换后的字符串形式作为key，而转换后二者是相等的导致后面覆盖前面，所以只有一个

//2.Map就是允许我们对象类型来作为key的
// const map = new Map ()
// map.set(obj1, "aaa")
// map.set(obj2, "bbb")
// map.set(1, "vcc")//基本数据类型也可以
//
// console. log (map)//Map(2) { { name: 'why' } => 'aaa', { name: 'kobe' } =>'bbb',1 => 'vcc' }
// //map传入数组的语法 :大数组中的每一个小数组存放键和值
// const map2 = new Map([[obj1,"aaa"], [obj2, "bbb"], [2, "ddd"]])
// console. log(map2)
//
// //-3.常见的属性和方法
// console.log(map2.size) //3 键值对的个数
//
// // set
// map2.set("why", "eee")   //'why' => 'eee'设置键值对
// console.log(map2)
//
// // get (key)
// console.log(map2.get("why"))   //eee 拿到值
//
// // has (key)
// console. log(map2.has("why"))  //true 判断是否存在
//
// // delete(key)
// map2.delete("why")
// console.log(map2)
// // clear  清空
// map2.clear()
// console. log(map2)
//
// // 4.遍历map
// // 一般forEach(当前元素，索引(可选)，目标数组(可选))
// map2.forEach((item, key) => {
//     console.log(item, key)
// })
//
// for (const item of map2){//此处item得到的是数每一个数组
//     console.log(item[0], item[1])
// }


// weakmap无法遍历
// const obj = {name: "obj1"}
// //·1.WeakMap和Map的区别二:  弱引用obj赋值为null回将直接删除，而强引用因为map.set()将obj作为键也有一次引用，共两次引用，所以赋null后无法直接删除
// const map = new Map()
// map.set(obj, "aaa")
//
// const weakMap = new WeakMap()
// weakMap.set(obj, "aaa")
//
// //2.区别一:不能使用基本数据类型
// // weakMap.set(1, "ccc")
//
// //3.常见方法
// // get方法获取值
// console.log(weakMap.get(obj))
//
// //-has方法
// console. log(weakMap.has(obj))
//
// //delete方法
// console.log(weakMap.delete(obj))
// // WeakMap { <items unknown> }
// console. log (weakMap)

//4.应用场景(vue3响应式原理)
const obj1 = {
    name: "why",
    age: 18
}
function obj1NameFn1() {
    console.log("objlNameFn1被执行")
}
function obj1NameFn2() {
    console.log("obj1NameFn2被执行")
}
function obj1AgeFn1() {
    console.log("obj1AgeFn1")
}
function obj1AgeFn2() {
    console.log("obj1AgeFn2")
}
const obj2 = {
    name: "kobe",
    height: 1.88,
    address: "广州市"
}

function obj2NameFn1() {
    console.log("obj1NameFn1被执行")
}
function obj2NameFn2() {
    console.log("objlNameFn2被执行")
}
//·1.创建WeakMap
const weakMap = new WeakMap()

// 2.收集依赖结构
//2.1.对obj1收集的数据结构
const obj1Map = new Map()  //创建一个Map对象
obj1Map.set("name",[obj1NameFn1, obj1NameFn2]) //在这个对象内将name属性与两个函数关联起来
obj1Map.set("age", [obj1AgeFn1, obj1AgeFn2])//在这个对象内将age属性与两个函数关联起来
weakMap.set(obj1, obj1Map)//将对象与Map对象关联

//~2.2.对obj2收集的数据结构
const obj2Map = new Map()
obj2Map.set("name", [obj2NameFn1, obj2NameFn2])
weakMap.set(obj2, obj2Map)

//-3.如果obj1.name发生了改变
// Proxy/Object.defineProperty
obj1.name = "james"
const targetMap = weakMap.get(obj1)
const fns = targetMap.get("name")
fns.forEach(item => item())
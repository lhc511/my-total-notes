"use strict"
// name和age虽然没有使用属性描述符来定义,但是它们也是具备对应的特性的
// value: 赋值的value
// configurable: true
// enumerable: true
// writable: true
// var obj = {
//     name: "why",
//     age: 18,
// }

// 数据属性描述符
//此处已经说明该属性不可修改，删除等操作
// configurable，enumerable，writable默认值是false
// Object.defineProperty(obj, "address", {
//     // 很多配置
//     value:'北京市',
//     //该属性不可删除修改/也不可以重新定义属性描述符
//     configurable: false,
//     // 该属性是配置对应的属性(address)是否是可以枚举,并且可以通过打印对象obj时显示
//     enumerable: true,
//     // 该特性是属性是否是可以赋值(写入值)
//     writable: false
// })
// delete obj.name
// console.log(obj.name)  //undefined
// delete obj.address
// console.log(obj.address) //北京市

// 由于上方configurable   此处无法生效   报错：Cannot redefine property: address
// Object.defineProperty(obj, "address", {
//     value: "广州市",
//     configurable: true
// })


// 测试enumerable的作用   true可以从以下方式得到，false则得不到，但是可以通过 . 直接访问
// console. log(obj)
// for (var key in obj) {
//     console.log(key)
// }
// console.log(Object.keys(obj))

// 测试Writable的作用  其属性值为false所以报错无法赋值
// obj.address="上海市"
// console.log(obj.address)//Cannot assign to read only property 'address' of object '#<Object>'

//存储属性描述符
// var obj = {
//     name: "why",
//     age: 18,
//     _address:"北极"    //加下滑线表示隐藏值
// }
//
// Object.defineProperty(obj, "address",{
//     enumerable: true,
//     configurable: true,
//     //value，writable和get，set不能同时存在，只能存在一组
//     //value，writable叫数据属性描述符，get，set叫存储属性描述符
//     // value:"北京市",
//     // writable: true,
//
//     //获取值
//     get: function() {
//         foo()  //拦截函数，每一次输出都会调用该函数
//         return this._address
//     },
//     //设置值
//     set: function (value) {
//         this._address=value
//     }
// })
//
// console. log(obj.address)
//
// obj.address ="上海市"
// console. log(obj.address)
//
// function foo() {
//     console.log("获取了一次address的值")
// }

//同时设定多个值
// var obj = {
// //、私有属性(js里面是没有严格意义的私有属性)
//     _age: 18,
//     _eating: function () {
//     },

    // ********在下方属性设置函数的写法*********
    // age: {
    //     configurable: true,
    //     enumerable: true,
    //     get: function () {
    //         return this._age
    //     },
    //     set: function (value) {
    //         this._age = value
    //     }
    // }
    //**********在原对象中的写法************
    // set age(value) {            //将configurable，enumerable属性默认赋值为true,
    //     this._age = value
    // },
    // get age() {
    //     return this._age
    // }
// }

//同时给多个属性设置配置
// Object.defineProperties(obj, {
//     name: {
//         configurable: true,
//         enumerable: true,
//         writable: true,
//         value: "why"
//     },
//     age: {
//         configurable: false,
//         enumerable: false,
//         get: function () {
//             return this._age
//         },
//         set: function (value) {
//             this._age = value
//         }
//     }
// })
//
//
//
// // 获取某一个特性属性的属性描述符
// console. log(Object.getOwnPropertyDescriptor(obj, "name"))//{ value: 'why', writable: true, enumerable: true, configurable: true }
// //、获取对象的所有属性描述符
// console.log(Object.getOwnPropertyDescriptors(obj))

var obj = {
name: 'why' ,
age: 18

}

//禁止对象继续添加新的属性
Object.preventExtensions(obj)

obj.height =1.88
obj.address ="广州市"

console. log(obj)

// 禁止该对象 配置(configurable)和删除里面的属性
for(var key in obj) {
    Object.defineProperty(obj, key, {
        configurable: false,
        enumerable: true,
        writable: true,
        value: obj[key]
    })
}

Object.seal(obj)
delete obj.name
console. log(obj.name)

// 3.让属性不可以修改(writable:false)
Object. freeze(obj)
obj.name = "kobe"
console.log(obj.name)
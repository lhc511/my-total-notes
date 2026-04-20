//基本使用 get/set捕获器
// const obj = {
//     name: "why",
//     age: 18
// }
// //receiver只有get和set有
// //第一个参数：代理目标 第二个，重写执行的操作
// const objProxy = new Proxy(obj, {
//     //-获取值时的捕获器 target:代理的原对象(此处是target)  key:键
//     get: function (target, key) {
//         console.log(`监听到对象的${key}属性被访问了`,target)
//         return target[key]
//     },
//     //设置值时的捕获器  前两个一样，第三个是新设置的参数
//     set:function (target,key,newValue){
//         console.log(`监听到对象的${key}属性被设置了`,target)
//         target[key]=newValue
//     },
//     //、监听in的捕获器
//     has: function(target, key) {
//         console.log(`监听到对象的${key}属性in操作`, target)
//         return key in target
//     },
//     //、监听delete的捕获器
//     deleteProperty: function(target, key) {
//         console.log(`监听到对象的${key}属性delete操作`, target)
//         delete target[key]
//     },
// }) //创建一个代理对象
//
// //结果与原输出一样
// // console.log(objProxy.name)
// // console.log(objProxy.age)
// //
// // //代理对象会自动将代理对象的操作同步到原对象中
// // objProxy.name = "kobe"
// // objProxy.age = 30
// //
// // console.log(obj.name)
// // console. log(obj.age)
//
// // 其他捕获器
// // in操作符  触发in捕获器，判断属性是否存在
// console. log("name" in objProxy)
//
// // delete操作
// delete objProxy.name

// proxy对函数对象的监听   new/apply
function foo() {
}
const fooProxy = new Proxy(foo, {
    apply: function (target, thisArg, argArray) {
        console.log("对foo函数进行了apply调用")
        return target.apply(thisArg, argArray)
    },
    construct: function (target, argArray, newTarget) {
        console.log("对foo函数进行了new调用")
        return new target(...argArray)
    }
})

fooProxy. apply({},["abc","cba"])//绑定时监听
new fooProxy("abc", "cba")//new调用时触发
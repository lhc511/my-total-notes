// 方式一
const obj = {
    name: "why",
    age: 18
}
// Object.defineProperty(obj, "name", {
//     get: function () {
//         console.log("监听到obj对象的name属性被访问了")
//     },
//     set: function () {
//         console.log("监听到obj对象的name属性被设置值")
//     }
// })

//遍历每一个键值对并设置监听

// 原理:
// 在 JavaScript 中，使用 Object.defineProperty() 设置 set 函数后
// 执行 value = newValue 能改变对象属性值的原因在于 属性描述符的底层实现机制。
// let internalValue; // 隐藏的内部存储位置
// Object.defineProperty(obj, 'prop', {
//   set(newVal) {
//     internalValue = newVal; // 值存储在内部变量
//     console.log('属性已更新');
//   },
//   get() {
//     return internalValue; // 从内部变量读取
//   }
// });
// 此时 obj.prop 不再直接存储在对象上，而是由描述符的 get/set 控制一个隐藏的内部存储位置

Object.keys(obj).forEach(key => {
    // let value=obj[key]   //此处定义的属性值实际隐藏的内部存储位置(任意取名)
    let b=obj[key]
    Object.defineProperty(obj, key, {
        get: function () {//返回要得到的值
            // console.log(`监听到obj对象的${key}属性被访问了`)
            // return value
            return b
        },
        //在此处要进行赋值才能真正改变,传入的值就是设置的值
        set: function (newValue) {
            console.log(`监听到obj对象的${key}属性被设置值`)
            // 在 set 函数中执行的 value = newValue 实际上是在修改这个内部存储的值，而非直接操作对象属性
            // value=newValue //访问的外层变量
            b =newValue //访问的外层变量
        }
    })
})



// console.log(obj.name)
obj.name = "kobe"
console.log(obj.name)
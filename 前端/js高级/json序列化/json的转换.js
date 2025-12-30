const obj = {
    name: "why",
    age: 18,
    friends: {
        name: "kobe"
    },
    hobbies: ["篮球", "足球"]
}

//·将对象数据存储localStorage
//此处将obj转化成字符串存储时会变成[object object]，无法得到对象真正存储的数据
localStorage.setItem("obj", obj)
console.log(localStorage.getItem("obj"))

//·将obj转成JSON格式的字符串，就能正常使用了
const objString =JSON.stringify(obj)
console. log(objString)

const jsonString = localStorage.getItem("obj")
//·将JSON格式的字符串转回对象
const info = JSON.parse(jsonString)
console. log(info)
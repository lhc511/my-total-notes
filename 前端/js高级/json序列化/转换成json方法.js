const obj= {
    name: "why",
    age: 18,
    friends: {
        name: "kobe"
    },
    hobbies: ["篮球", "足球"],
    //toJSON属性的值会直接作为所有JSON.stringify返回结果(不论参数是什么)
    toJSON:function (){
        return '1231242'
    }
}
//·需求 :· 将上面的对象转成JSON字符串
//·1.直接转化
// const jsonString1 =JSON.stringify(obj)
// console. log(jsonString1)

//·2.stringify第二个参数replacer
//·2.1.、传入数组:设定哪些是需要转换，即筛选
// const jsonString2 =JSON.stringify(obj, ["name", 'age',"friends"])
// console.log(jsonString2)

//·2.2 .· 传入回调函数:对传入的数据进行一定程度上的操作
// const jsonString3 = JSON.stringify(obj, (key, value)=> {
//     if(key==='age'){
//         // 将age属性的值加一然后返回json格式的对象
//         return value+1//{"name":"why","age":19,"friends":{"name":"kobe"},"hobbies":["篮球","足球"]}
//     }
//     //此处默认返回将原对象json转换后的值
//     return value//{"name":"why","age":18,"friends":{"name":"kobe"},"hobbies":["篮球","足球"]}
// })
// console.log(jsonString3)

//、3.stringify第三参数·space
//每一个数据前面的空格数，并且在打印每组数据后会换行打印另一组数据
//如果田其他字符就会变成相应的字符，数量也一致
const jsonString4 = JSON.stringify(obj, null,2)
console. log(jsonString4)
//打印的数据格式如下
// {
//   "name": "why",
//   "age": 18,
//   "friends": {
//     "name": "kobe"
//   },
//   "hobbies": [
//     "篮球",
//     "足球"
//   ]
// }


const name = "why"
const age = 18
const foo='foo value'

//·1.默认导出的方式一:
export {
    name,age,
    foo as default  //将foo作为默认导出的值
}

//、2.默认导出的方式二 :· 常见
export default foo

//默认导出只能有一个
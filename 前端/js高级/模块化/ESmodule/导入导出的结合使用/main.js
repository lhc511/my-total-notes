//从utils中导入函数，utils中的index文件中包含文件的工具函数，所有函数都会导入index.js文件

//效果相同
// import { add, sub, priceFormat, timeFormat } from './utils/index.js'
import { add, sub, priceFormat, timeFormat } from './utils'

console.log(add(10,20))
console.log(sub(10, 20))
console.log(priceFormat())
console. log(timeFormat())
import { name, age } from './foo.js'
// name='aaa'//会报错，导入的文件内部无法修改导出文件的值
console. log(name, age)
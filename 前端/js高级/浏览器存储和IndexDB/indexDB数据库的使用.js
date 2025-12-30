//·打开数据库(和数据库建立连接)，若没有就在indexdb中创建一个叫做why的数据库
const dbRequest =indexedDB.open("why")
dbRequest.onerror = function(err) {
    console.log("打开数据库失败~")
}
//数据库打开成功后会执行下面的函数
let db=null
//event是打开数据库这个事件，里面有很多属性
dbRequest.onsuccess = function(event) {
    // console.log('event:'+event)//得到一个事件对象object Event
    // console.log(event)
    // event.target.result：返回打开的数据库实例（IDBDatabase对象）
    //target的属性值IDBOpenDBRequest 即打开的数据库
    // console.log(event.target)
    //拿到的是一个object IDBDatabase对象，里面存储的打开的目标数据库

    db = event.target.result

    // console.log(db)
}
//·第一次打开/或者版本发生更新
dbRequest.onupgradeneeded = function (event) {
    const db = event.target.result
//、创建一些存储对象,keyPath是主键，对应mysql中的primary key，users对应对应库中的表名
//    可以看作在mysql中创建一个叫users，主键叫id的表
    db.createObjectStore("users", {keyPath: "id"})
}

class User {
    constructor(id, name, age) {
        this.id = id
        this.name = name
        this.age = age
    }
}

const users = [
    new User(100, "why", 18),
    new User(101, "kobe", 40),
    new User(102, "james", 30),
]

//获取btns,监听点击
const btns = document. querySelectorAll("button")
for (let i = 0; i < btns.length; i++) {
    btns[i].onclick = function () {
        // console.log(db)

        //第一个参数是数据库中存储的哪些表，第二个是对表的权限
        const transaction = db.transaction(["users"], "readwrite")
        // console.log(transaction)//IDBTransaction
        //objectStore在传递的表中选择要操作的表
        const store = transaction.objectStore("users")
        // console.log(store)//IDBObjectStore 数据库中的核心数据容器，相当于传统数据库的"表"
        switch (i) {
            case 0:
                console.log("点击了新增")
                for (const user of users) {
                    const request = store.add(user)
                    console.log(request)//IDBRequest
                    // request.onsuccess的含义与作用
// 触发时机：当某个特定操作（如打开数据库、读取数据、写入数据等）成功完成时触发
                    request.onsuccess = function () {
                        console.log(`${user.name}插入成功`)
                    }
                }
                // transaction.oncomplete的含义与作用
// 触发时机：当事务（Transaction）中所有操作全部完成且已提交到数据库时触发
                transaction.oncomplete = function () {
                    console.log("添加操作全部完成")
                }
                break

            case 1:
                console.log("点击了查询")
                //·1.查询方式一
                // const request = store.get(102)
                // request.onsuccess = function (event) {
                //     console.log(event.target.result)
                // }

                //·2.查询方式二:
                //对目标对象(表)创建一个游标，这个游标一开始指着第零个数据
                const request = store.openCursor()

                request.onsuccess = function (event) {//步骤4
                    //此时result=null是因为控制台捕获对象的浅层状态，来得及给值进行渲染(indexDB的异步执行机制)
                    // console.log(event)                 //步骤5
                    // console.log(event.target)          //步骤6
                    const cursor = event.target.result    //步骤7
                    // console.log(cursor) //返回一个对象IDBCursorWithValue，{id: 101, name: 'kobe', age: 40}
                    if (cursor) {//当cursor为null时，说明数据遍历完成·
                        // console.log(cursor.key, cursor.value)

                        //此处正常的原因是直接访问的就是使用中的数据，即直接获取值，就不担心值被修改
                        console.log("延迟打印:", event.target.result !== null);
                        console.log("延迟打印:", event.target.result);//正常

                        //而此处是null的原因是因为log对与对象的打印是通过引用来找实际值，即地址（动态引进机制）
                        // 而在调用continue后会将对应的游标的值释放，修改了该内存的地址的内容，即改为null
                        console.log("ll", event.target);//result:null
                        // 在 IndexedDB 游标操作中，当添加 event.target.result.continue() 后控制台打印显示 null。
                        // 但实际使用时数据正常，这是由 IndexedDB 游标的工作机制决定的：游标生命周期特性
                        // 调用 cursor.continue() 会立即结束当前游标对象的生命周期：调用 continue() 后，当前游标会被释放，变为null
                        // 下一次 onsuccess 事件会携带新的游标实例（或遍历结束时为 null）
                        cursor.continue()//在执行一次这个函数，同时把游标指向下一个数据

                        //在此处将continue延迟执行后就能正常看见对象中result的值了
                        // setTimeout(function () {
                        //     cursor.continue()
                        // }, 100000)

                        //在此处打印result一定是null，因为continue已经执行过了
                        console.log(event.target)


                    } else {
                        console.log("查询完成")
                    }
                }
                break
            case 2:
                console.log("点击了删除")
                const deleteRequest = store.openCursor()
                deleteRequest.onsuccess = function (event) {
                    const cursor = event.target.result
                    if (cursor) {
                        if (cursor.key === 101) {
                            cursor.delete()
                        } else {
                            cursor.continue()
                        }
                    } else {
                        console.log("查询完成")
                    }
                }
                break
            case 3:
                console.log("点击了修改")
                const updateRequest = store.openCursor()
                updateRequest.onsuccess = function (event) {
                    console.log('aa')
                    const cursor = event.target.result
                    if (cursor) {
                        if (cursor.key === 101) {
                            // 修改完点indexDB中的左上角的刷新数据库
                            const value = cursor.value;
                            value.name = "curry"
                            cursor.update(value)
                        } else {
                            cursor.continue()
                        }
                    } else {
                        console.log("查询完成")
                    }

                }
            break
        }
    }
}


//查询方式二的异步与事件循环的执行步骤
// 步骤 1：调用 store.openCursor() 立即返回一个 IDBRequest 对象
//     此时请求处于 pending 状态，request.result = null
//     实际游标操作被放入 IndexedDB 异步任务队列
// 步骤 2-3：同步打印日志
//          此时 request 对象显示 result: null（尚未获取数据）
// 步骤 4：同步注册 onsuccess 回调函数
//     回调函数不会立即执行，仅注册到请求对象
//     此时 JavaScript 主线程继续向下执行（无阻塞）
// 步骤 5-6：
//     console.log(event) 打印时，浏览器控制台对对象的输出是动态引用
//     初始展开可能显示 result: null（引擎尚未填充属性）
//     但实际内存中 event.target.result 已被赋值
// 步骤 7：
//     const cursor = event.target.result 同步读取内存中的游标对象
//     此时值必定有效（事件触发时 IndexedDB 已完成数据填充）

// 当执行 console.log(event.target) 时，控制台捕获对象的浅层状态
// 数据可能尚未被浏览器控制台渲染引擎处理

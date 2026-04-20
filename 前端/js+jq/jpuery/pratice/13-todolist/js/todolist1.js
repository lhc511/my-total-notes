$(function (){
    load()
    $('#title').on('keydown',function (event){
        if (event.keyCode===13){//因为回车键的asc码是13
            //将已有的数据拿出，若没有则跳到存储数据
            let local=getData()
            // console.log(local)
            local.push( {title:$(this).val(),done:false} )

            // 存储数据
            saveData(local)
            load()
        }
    })
    //读取本地存储数据
    function getData(){
        //拿到键对应的值  机json格式的字符串
        let data=localStorage.getItem('todolist')
        // localStorage.removeItem('username')
        //将json格式的字符串转换为对象格式
        if (data!==null){
            return JSON.parse(data)
        }else {
            return []
        }
    }
    function getDoneData(){
        //拿到键对应的值  机json格式的字符串
        let data=localStorage.getItem('doneList')
        // localStorage.removeItem('username')
        //将json格式的字符串转换为对象格式
        if (data!==null){
            return JSON.parse(data)
        }else {
            return []
        }
    }
    //保存本地存储数据
    function saveData(data){
        // 在这里一定要将对象转换为字符串格式来保存   前者为键，后者为值
        localStorage.setItem('todolist',JSON.stringify(data))
    }
    function
    saveDatUL(data){
        // 在这里一定要将对象转换为字符串格式来保存   前者为键，后者为值
        localStorage.setItem('doneList',JSON.stringify(data))
    }
    // todolist删除操作
    $('ol').on('click','a',function (){
        let data=getData()
        let index=$(this).attr('id')
        data.splice(index,1)
        saveData(data)
        load()
    })
    $('ul').on('click','a',function (){
        let doneData=getDoneData()
        let index=$(this).attr('id')
        doneData.splice(index,1)
        saveDatUL(doneData)
        load()
    })
    //渲染加载数据
    function load(){
        //拿到了装了很多对象的列表
        let data=getData()
        // console.log(data)
        let doneData=getDoneData()
        //将原先的元素清空
        $('ol').empty()
        //每一次都会向目标元素中添加所有的数据，因此要清空
        $.each(data,function(i,n){
            $('ol').prepend('<li><input type="checkbox" id="'+i+'"> <p>'+n.title+'</p> <a href="javascript:;" id="'+i+'"></a> </li>')
        })
        $('ul').empty()
        $.each(doneData,function(i,n){
          $('ul').prepend('<li><input type="checkbox" checked id="'+i+'"> <p>'+n.title+'</p> <a href="javascript:;" id="'+i+'"></a> </li>')
        })
    }
    //////////////////////////////////////////////////////////////////////
    //将未做事件转换到已做
    $('ol').on('change','input',function (){
        let data=getData()
        let index=$(this).attr('id')
        let doneData=getDoneData()         //拿出已做事件
        doneData.push(data[index])
        saveDatUL(doneData)
        data.splice(index,1)  //原数据删除
        saveData(data)
        load()
    })

    //将已做事件转换到未作
    $('ul').on('change','input',function (){
        let data=getData()
        let index=$(this).attr('id')
        let doneData=getDoneData()         //拿出已做事件
        data.push(doneData[index])
        saveData(data)
        doneData.splice(index,1)
        saveDatUL(doneData)
        load()
    })
})
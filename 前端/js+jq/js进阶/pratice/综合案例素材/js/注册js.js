window.addEventListener('load',function (){
    //验证码的重新发送
    let flag=true
    $('.code').on('click',function (){
        if (flag){
            flag=false
            let count=3
            $(this).text('请'+count+'秒后再尝试')
            let timer=setInterval(function (){
                // console.log(this)
                count--
                $('.code').text('请'+count+'秒后再尝试')
                if (count===0){
                    clearInterval(timer)
                    $('.code').text('发送验证码')
                    flag=true
                }
            }, 1000)
        }
    })

    //检查是否有按键按下


    //6-10位用户名
    let username=document.querySelector('[name=username]')
    // console.log(username)
    // console.log($('div[data-prop="username"]>input'))
    // $('div[data-prop="username"]>input').eq(0).on('change',function (){
    //     console.log(this)
    //     alert('aa')
    // })
    function one(){
        let reg=/^[0-9a-zA-Z-_]{6,10}$/
        let fit=reg.test($(username).val())
        // if (!fit||$(this).val()===''){
        if (!fit){
            $(username).next().html('输入不合法,请输入6~10位')
            return false
        }else {
            $(this).next().html('')
            return true
        }
    }
    $(username).on('change',one)

    //电话号码11位数字
    const phone=document.querySelector('[name=phone]')
    $(phone).on('change',function (){
        let reg=/^[0-9]{11}$/
        // let fit=reg.test($(this).val())
        if (!reg.test($(phone).val())){
            $(this).next().html('输入不合法,请输入正确的11位手机号码')
        }else {
            $(this).next().html('')
        }
    })

    //6位数字验证码
    const code=document.querySelector('[name=code]')
    function two(){
        let reg=/^[0-9]{6}$/
        // let fit=reg.test($(this).val())
        // if (!fit||$(this).val()===''){
        if (!reg.test($(code).val())){
            $(code).next().html('输入不合法,6 位数字')
            return false
        }else {
            $(code).next().html('')
            return true
        }

    }
    $(code).on('change',two)
    //六到二十位字母数字符号的组合密码

    //密码确认

    // if (!(two()&&one())){}

    const queren = document.querySelector('.icon-queren')
    queren.addEventListener('click', function () {
      // 切换类  原来有的就删掉，原来没有就添加
      this.classList.toggle('icon-queren2')
    })

     const form = document.querySelector('form')
    $(form).on('submit', function (e) {
        // e.preventDefault()
      // 判断是否勾选我同意模块 ，如果有 icon-queren2说明就勾选了，否则没勾选
        if (!queren.classList.contains('icon-queren2')) {
            alert('请勾选同意协议')
            // 阻止提交
            e.preventDefault()
        }
        // e.preventDefault()

        // 依次判断上面的每个框框 是否通过，只要有一个没有通过的就阻止
        // console.log(verifyName())
        // console.log(one())
        //

        if (!one()) e.preventDefault()
        // if (!two()) e.preventDefault()
    })
})
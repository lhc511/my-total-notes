window.addEventListener('load',function (){
    const headCheck=$('.cart-thead>.t-checkbox>.checkall')
    const allCheckBox=$('.cart-item .p-checkbox .j-checkbox')
    const cartItems=$('.cart-item-list .cart-item')
    headCheck.change(function (){
        // console.log($(this).prop('checked'))
        allCheckBox.prop('checked',$(this).prop('checked'))
        allCheckBox.change()
        total()
    })

    allCheckBox.change(function (){
        if ($(this).prop('checked')){
          $(this).parent().parent().addClass('check-cart-item')

        }else if($(this).prop('checked')===false) {
            $(this).parent().parent().removeClass('check-cart-item')
        }
        if ($('.j-checkbox:checked').length>=$('.j-checkbox').length)
            {headCheck.prop('checked',true)}
        else {headCheck.prop('checked',false)}
        total()
    })
    //////////////////////////////////////////////////////////////
    function perSum(obj,value){
        $(obj).siblings('input').val(value)
        let pPrice=$(obj).parent().parent().siblings('.p-price')
        let pSum=$(obj).parent().parent().siblings('.p-sum')
        let valueSum=Number(pPrice.text().substr(1))*value
        // console.log(valueSum)
        valueSum=valueSum.toFixed(2)
        pSum.text('￥'+valueSum)
        total()
    }

    function total(){
        let a=0
        for (let i=0;i<$('.p-sum').length;i++){
            let num = Number($('.j-checkbox:checked').parent().siblings('.p-sum').eq(i).text().substr(1))
            a=(a+num)
        }
        $('.price-sum em').html(a.toFixed(2))
    }

    total()


    $('.decrement').click(function (){
        // console.log(typeof ($(this).siblings('input').val())) //string 1
        let value=Number($(this).siblings('input').val())-1
        if(value>=1){
            perSum(this,value)
        }
    })

    $('.increment').click(function (){
        let value=Number($(this).siblings('input').val())+1
        if(Number(value)<99) {
            perSum(this,value)
        }
    })

    $('.itxt').change(function(){
        let value=Number($('.itxt').val())
        perSum(this,value)
    })

    /////////////////////////////////////////////


    //删除模块
    $('.p-action').click(function (){
        $(this).parent().remove()
        total()
    })

    //清除选中商品
    $('.remove-batch').click(function (){
        $('.j-checkbox:checked').parent().parent().remove()
        total()
    })

    //清空购物车
    $('.clear-all').click(function (){
        $('.cart-item').remove()

    })
})
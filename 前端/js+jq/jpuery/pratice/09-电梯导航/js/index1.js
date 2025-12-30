window.addEventListener('load',function (){
    $(function (){
        const tools=$('.fixedtool>ul li')
        const floors=$('.floor>.w')
        const startTop=$('.recom-hd').offset().top//如果在滚动函数里面设置就会一直改变

        let flag=true
        $(window).scroll(function (){
            if ($(document).scrollTop()>=startTop){
                $('.fixedtool').fadeIn()
            }else {
                $('.fixedtool').fadeOut()
            }
            // for (let i=0;i<tools.length;i++){
            //     if ($(document).scrollTop()>=floors.eq(i).offset().top){
            //        tools.eq(i).addClass('current').siblings().removeClass('current')
            //     }
            // }

            $.each(floors,function(i,ele){
                if (flag===true){
                    if ($(window).scrollTop()>=$(ele).offset().top){
                        tools.eq(i).addClass('current').siblings().removeClass('current')
                    }
                }
            })
        })

        $.each(tools,function(i,ele){
                $(ele).click(function (){
                    flag=false
                    $(this).addClass('current').siblings().removeClass('current')
                    $('body,html').stop().animate({
                        scrollTop:floors.eq(i).offset().top
                    },function ()
                    {flag=true})
                })

            })
    })
})
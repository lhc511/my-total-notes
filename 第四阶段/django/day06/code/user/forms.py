from django import forms

class MyRegForm(forms.Form):
    username=forms.CharField(label='用户名')
    password=forms.CharField(label='密码',required=False)
    password2=forms.CharField(label='重复密码')
    # age=forms.IntegerField(label="年龄")

    #对username进行验证
    def clean_username(self):#下划线后面的名字要和上面的属性名一模一样
        # 限定username必须>=6个字符
        uname=self.cleaned_data['username']
        if len(uname)<6:
            raise  forms.ValidationError("用户名太短")
        return uname
    def clean(self):
        pwd1=self.cleaned_data['password']
        pwd2=self.cleaned_data['password2']
        if pwd1!=pwd2:
            raise forms.ValidationError("两次密码不一致")
        return self.cleaned_data


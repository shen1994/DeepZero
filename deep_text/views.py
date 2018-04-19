from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import TextChat

# Create your views here.

def text_chat(request):
    text_show_num = 5
    if request.method == 'POST':
        
        need_to_submit = request.POST["question"]
        answer = text_chat_interface(need_to_submit)
        
        try:
            new_text = TextChat()
            user = User.objects.get(username="shen1995")
            new_text.user = user
            new_text.question = need_to_submit
            new_text.answer = answer
            new_text.save()
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    else:
        user = User.objects.get(username="shen1995")
        new_text = TextChat.objects.filter(user=user)
        if not new_text.exists():
            new_sentence = TextChat()
            new_sentence.user = user
            new_sentence.question = "你好,机器人!"
            new_sentence.answer = "讨厌，人家好害羞!"
            new_sentence.save()
            sentences = list(TextChat.objects.all())
            return render(request, "text/text_chat.html", { \
                            "sentences":sentences})
        count = 0
        is_over = False
        for new_text_single in new_text:
            count += 1
            if count >= text_show_num:
                is_over = True
                break
            
        if is_over:
            sentences = list(TextChat.objects.all()[0:text_show_num])
            for i in range(int(text_show_num / 2)):
                sentences_temp = sentences[i]
                sentences[i] = sentences[text_show_num - i - 1]
                sentences[text_show_num - i - 1] = sentences_temp  
            return render(request, "text/text_chat.html", { \
                        "sentences":sentences})
        else:
            sentences = list(TextChat.objects.all()[0:count])
            for i in range(int(count / 2)):
                sentences_temp = sentences[i]
                sentences[i] = sentences[count - i - 1]
                sentences[count - i - 1] = sentences_temp 
            return render(request, "text/text_chat.html", { \
                        "sentences":sentences})

def text_chat_interface(question):
    '''
    @params[in]: question,用户从界面输入,类型str
    @params[out]: answer,模型处理后的返回值,类型str
    '''
    answer = "就是讨厌你"
    return answer
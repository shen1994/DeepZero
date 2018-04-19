from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

import base64
import io
from PIL import Image

from .models import ImageImage
from .models import ImageRetrieval

# Create your views here.

def image_retrieval(request):
    if request.method == 'POST':
        need_to_submit = request.POST["img"]
        try:
            new_image = ImageImage()
            
            # 这里使用超级用户
            #new_image.user = request.user
            user = User.objects.get(username="shen1995")
            new_image.user = user
            
            new_image.title = "system_image_" + user.username
            new_image.url = "空"
            new_image.description = "空"
            new_image.image = need_to_submit
            new_image.save()
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    return render(request, "image/image_retrieval.html")
    
def image_result(request):
    images = ['' for i in range(10)]
    if request.method == 'POST':
        try:
            need_to_submit = request.POST["img"]
            need_trans = need_to_submit.replace("data:image/png;base64,", "")
            image_data = base64.b64decode(str(need_trans))
            fresh_image = Image.open(io.BytesIO(image_data))
            fresh_image = fresh_image.convert("RGB")
            fresh_image.format = "JPEG"
            
            image_retrieval_interface(fresh_image, images)            
                
            user = User.objects.get(username="shen1995")
            new_image = ImageRetrieval.objects.filter(user=user)
            if new_image.exists():
                for part_new_image in new_image:
                    part_new_image.delete()

            new_image = ImageRetrieval()
            new_image.user = user
            new_image.title = "空#空#空#空#空#空#空#空#空#空#"
            for i in range(10):
                new_image.address += images[i]
                new_image.address += "#"
            new_image.status = True
            new_image.save()               
           
            return HttpResponse("1")
        except:
            return HttpResponse("0")
    else:
        
        user = User.objects.get(username="shen1995")
        new_image = ImageRetrieval.objects.filter(user=user)
        if not new_image.exists():
            for i in range(10):
                images[i] = "image_library/image_show.jpg"
        else:
            count = 0
            long_address = new_image[0].address
            for i in range(10):
                while(long_address[count] != '#'):
                    images[i] += long_address[count]
                    count += 1
                count += 1                
            
        return render(request, 'image/image_result.html',{
                        'images_top': images[0:5],
                        'images_bottom': images[5:10],
                    })
        
def image_retrieval_interface(input_image, output_images):
    '''
    @params[in]:input_image为输入剪裁图片
    @params[out]:output_images为输出图片的路径,设置为10张,必须填满
    '''     
    for i in range(10):
        output_images[i] = "image_library/image_show.jpg"    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# DeepZero
django+python3环境下开发的web接口

## 1. 效果展示  
![image](https://github.com/shen1994/README_FILE/raw/master/images/menu.jpg)
![image](https://github.com/shen1994/README_FILE/raw/master/images/blog_submit.jpg)
![image](https://github.com/shen1994/README_FILE/raw/master/images/image_retrieval.jpg)
![image](https://github.com/shen1994/README_FILE/raw/master/images/text_chat.jpg)

## 2.model载入数据库,并且保证localhost:8000/home/menu/运行一次  
`cd DeepZero-master`  
`python manage.py makemigrations home`  
`python manage.py makemigrations account`  
`python manage.py makemigrations deep_image`  
`python manage.py makemigrations deep_text`  
`python manage.py makemigrations deep_vedio`  
`python manage.py migrate`  
`python manage.py runserver 0.0.0.0:8000`  

## 3.创建超级用户，用于发布信息  
`python manage.py createsuperuser`

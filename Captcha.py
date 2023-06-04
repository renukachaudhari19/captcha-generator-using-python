#!/usr/bin/env python
# coding: utf-8

# In[1]:


from captcha.image import ImageCaptcha
import string 
import random
N = 7
res = ''.join(random.choices(string.ascii_uppercase + string.digits,k = N))
str1=str(res)
image = ImageCaptcha(width=300,height=300)
captcha_text=str1
data = image.generate(captcha_text)
image.write(captcha_text , 'CAPTCHA_1.png')
from PIL import Image
Image.open('CAPTCHA_1.png')


# In[3]:


pip install captcha


# In[ ]:





# In[ ]:





# In[ ]:





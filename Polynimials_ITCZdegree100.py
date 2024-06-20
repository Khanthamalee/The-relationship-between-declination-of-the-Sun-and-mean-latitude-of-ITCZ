#!/usr/bin/env python
# coding: utf-8

# # Import Libraries in Python

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl


# # 1.อ่านไฟล์ที่บันทึกค่า ITCZdegree ที่ได้จากการคำนวน

# In[2]:


fileadd = pd.read_excel("samping.xlsx")
fileadd


# # 1.1 สร้าง subset ของแต่ละคอลัมภ์ให้ง่ายต่อการเรียกใช้งาน

# In[3]:


fileadd_subset=fileadd[['Order','date_order','date','formpixel','ITCZdegree','declination']]
fileadd_subset


# # 1.2 สร้างกราฟเพื่อวิเคราะห์ข้อมูล

# In[4]:


s = fileadd_subset['declination']
t = fileadd_subset['ITCZdegree']
plt.scatter(s,t)
plt.show()
#Data can split data to create 2 graphs.


# # 2. เปิดไฟล์ที่เราได้คัดเลือกจากกราฟด้านล่าง

# In[5]:


ITCZdown = pd.read_excel("ITCZdown.xlsx")
ITCZdown


# # 2.1 สร้าง subset ของแต่ละคอลัมภ์ ITCZdownให้ง่ายต่อการเรียกใช้งาน

# In[6]:


ITCZdown_subset=ITCZdown[['Order','date_order','date','formpixel','ITCZdegree','declination']]
ITCZdown_subset


# # 2.2 Polinomials regression ITCZdown

# In[7]:


k = ITCZdown_subset['declination']
m = ITCZdown_subset['ITCZdegree']
plt.scatter(k,m)
myModel = np.poly1d(np.polyfit(k,m,100))
myline = np.linspace(-18,23,2000)
plt.scatter(myline,myModel(myline))
plt.show()
from sklearn.metrics import r2_score
print(r2_score(m,myModel(k)))
print('error =', 100 -r2_score(m,myModel(k))*100 )


# # 3. เปิดไฟล์ที่เราได้คัดเลือกจากกราฟด้านบน

# In[8]:


ITCZup = pd.read_excel("ITCZup.xlsx")
ITCZup


# # 3.1 สร้าง subset ของแต่ละคอลัมภ์ของ ITCZup ให้ง่ายต่อการเรียกใช้งาน

# In[9]:


ITCZup_subset=ITCZup[['Order','date_order','date','formpixel','ITCZdegree','declination']]
ITCZup_subset


# # 3.2 Polinomials regression ITCZdown

# In[10]:


o = ITCZup_subset['declination']
p = ITCZup_subset['ITCZdegree']
plt.scatter(o,p)
myModel = np.poly1d(np.polyfit(o,p,45))
myline = np.linspace(-12,20,2000)
plt.scatter(myline,myModel(myline))
plt.show()
from sklearn.metrics import r2_score
print(r2_score(p,myModel(o)))
print('error =', 100 -r2_score(p,myModel(o))*100 )


# In[11]:


from sklearn.metrics import r2_score
print(r2_score(p,myModel(o)))
print('error =', 100 -r2_score(p,myModel(o))*100 )


# In[ ]:





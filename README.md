# Import Libraries in Python


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
```

# 1.อ่านไฟล์ที่บันทึกค่า ITCZdegree ที่ได้จากการคำนวน


```python
fileadd = pd.read_excel("samping.xlsx")
fileadd
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>time</th>
      <th>ITCZ1MIN</th>
      <th>ITCZ1MAX</th>
      <th>ITCZ2MIN</th>
      <th>ITCZ2MAN</th>
      <th>ITCZ3MIN</th>
      <th>ITCZ3MAX</th>
      <th>ITCZaverage</th>
      <th>ITCZdegree</th>
      <th>declination</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>00:00:00</td>
      <td>563</td>
      <td>629</td>
      <td>563</td>
      <td>629</td>
      <td>564</td>
      <td>630</td>
      <td>596.333333</td>
      <td>-14.351067</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>2007-01-01</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>06:00:00</td>
      <td>537</td>
      <td>638</td>
      <td>536</td>
      <td>638</td>
      <td>535</td>
      <td>638</td>
      <td>587.000000</td>
      <td>-13.279600</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>18:00:00</td>
      <td>533</td>
      <td>614</td>
      <td>534</td>
      <td>613</td>
      <td>533</td>
      <td>614</td>
      <td>573.500000</td>
      <td>-11.729800</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>00:00:00</td>
      <td>517</td>
      <td>650</td>
      <td>516</td>
      <td>650</td>
      <td>516</td>
      <td>650</td>
      <td>583.166667</td>
      <td>-12.839533</td>
      <td>16.563839</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>1900-01-01 06:00:00</td>
      <td>496</td>
      <td>636</td>
      <td>496</td>
      <td>634</td>
      <td>495</td>
      <td>635</td>
      <td>565.333333</td>
      <td>-10.792267</td>
      <td>16.563839</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2936</th>
      <td>325</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 00:00:00</td>
      <td>449</td>
      <td>484</td>
      <td>449</td>
      <td>481</td>
      <td>449</td>
      <td>481</td>
      <td>465.500000</td>
      <td>12.477350</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>2937</th>
      <td>326</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 06:00:00</td>
      <td>440</td>
      <td>478</td>
      <td>440</td>
      <td>477</td>
      <td>440</td>
      <td>477</td>
      <td>458.666667</td>
      <td>13.067067</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>2938</th>
      <td>327</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 12:00:00</td>
      <td>440</td>
      <td>475</td>
      <td>440</td>
      <td>475</td>
      <td>440</td>
      <td>475</td>
      <td>457.500000</td>
      <td>13.167750</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>2939</th>
      <td>328</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 18:00:00</td>
      <td>438</td>
      <td>490</td>
      <td>439</td>
      <td>490</td>
      <td>439</td>
      <td>490</td>
      <td>464.333333</td>
      <td>12.578033</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
    <tr>
      <th>2940</th>
      <td>329</td>
      <td>3459</td>
      <td>2016-10-24</td>
      <td>33</td>
      <td>1903-11-09 00:00:00</td>
      <td>440</td>
      <td>492</td>
      <td>438</td>
      <td>495</td>
      <td>438</td>
      <td>495</td>
      <td>466.333333</td>
      <td>12.405433</td>
      <td>-12.612016</td>
      <td>NaN</td>
      <td>NaT</td>
    </tr>
  </tbody>
</table>
<p>2941 rows × 16 columns</p>
</div>



# 1.1 สร้าง subset ของแต่ละคอลัมภ์ให้ง่ายต่อการเรียกใช้งาน


```python
fileadd_subset=fileadd[['Order','date_order','date','formpixel','ITCZdegree','declination']]
fileadd_subset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>ITCZdegree</th>
      <th>declination</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-14.351067</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-13.279600</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-11.729800</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>-12.839533</td>
      <td>16.563839</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>-10.792267</td>
      <td>16.563839</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2936</th>
      <td>325</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>12.477350</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>2937</th>
      <td>326</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>13.067067</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>2938</th>
      <td>327</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>13.167750</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>2939</th>
      <td>328</td>
      <td>3458</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>12.578033</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>2940</th>
      <td>329</td>
      <td>3459</td>
      <td>2016-10-24</td>
      <td>33</td>
      <td>12.405433</td>
      <td>-12.612016</td>
    </tr>
  </tbody>
</table>
<p>2941 rows × 6 columns</p>
</div>



# 1.2 สร้างกราฟเพื่อวิเคราะห์ข้อมูล


```python
s = fileadd_subset['declination']
t = fileadd_subset['ITCZdegree']
plt.scatter(s,t)
plt.show()
#Data can split data to create 2 graphs.
```


    
![png](output_7_0.png)
    


# 2. เปิดไฟล์ที่เราได้คัดเลือกจากกราฟด้านล่าง


```python
ITCZdown = pd.read_excel("ITCZdown.xlsx")
ITCZdown
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>time</th>
      <th>ITCZ1MIN</th>
      <th>ITCZ1MAX</th>
      <th>ITCZ2MIN</th>
      <th>ITCZ2MAN</th>
      <th>ITCZ3MIN</th>
      <th>ITCZ3MAX</th>
      <th>ITCZaverage</th>
      <th>ITCZdegree</th>
      <th>declination</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>00:00:00</td>
      <td>563</td>
      <td>629</td>
      <td>563</td>
      <td>629</td>
      <td>564</td>
      <td>630</td>
      <td>596.333333</td>
      <td>-14.351067</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>39083.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>06:00:00</td>
      <td>537</td>
      <td>638</td>
      <td>536</td>
      <td>638</td>
      <td>535</td>
      <td>638</td>
      <td>587.000000</td>
      <td>-13.279600</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>18:00:00</td>
      <td>533</td>
      <td>614</td>
      <td>534</td>
      <td>613</td>
      <td>533</td>
      <td>614</td>
      <td>573.500000</td>
      <td>-11.729800</td>
      <td>16.274926</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>00:00:00</td>
      <td>517</td>
      <td>650</td>
      <td>516</td>
      <td>650</td>
      <td>516</td>
      <td>650</td>
      <td>583.166667</td>
      <td>-12.839533</td>
      <td>16.563839</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>1900-01-01 06:00:00</td>
      <td>496</td>
      <td>636</td>
      <td>496</td>
      <td>634</td>
      <td>495</td>
      <td>635</td>
      <td>565.333333</td>
      <td>-10.792267</td>
      <td>16.563839</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2089</th>
      <td>485</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>1903-01-03 00:00:00</td>
      <td>515</td>
      <td>644</td>
      <td>514</td>
      <td>644</td>
      <td>514</td>
      <td>644</td>
      <td>579.166667</td>
      <td>-11.828500</td>
      <td>-6.861150</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2090</th>
      <td>486</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>1903-01-03 06:00:00</td>
      <td>513</td>
      <td>645</td>
      <td>513</td>
      <td>645</td>
      <td>513</td>
      <td>645</td>
      <td>579.000000</td>
      <td>-11.809600</td>
      <td>-6.861150</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2091</th>
      <td>487</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>1903-01-03 12:00:00</td>
      <td>547</td>
      <td>662</td>
      <td>546</td>
      <td>661</td>
      <td>546</td>
      <td>661</td>
      <td>603.833333</td>
      <td>-14.625700</td>
      <td>-6.861150</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2092</th>
      <td>488</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>1903-01-03 18:00:00</td>
      <td>529</td>
      <td>683</td>
      <td>529</td>
      <td>681</td>
      <td>529</td>
      <td>681</td>
      <td>605.333333</td>
      <td>-14.795800</td>
      <td>-6.861150</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2093</th>
      <td>489</td>
      <td>157</td>
      <td>2013-10-10</td>
      <td>40</td>
      <td>1903-01-04 00:00:00</td>
      <td>605</td>
      <td>676</td>
      <td>605</td>
      <td>676</td>
      <td>605</td>
      <td>676</td>
      <td>640.500000</td>
      <td>-18.783700</td>
      <td>-7.237889</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>2094 rows × 16 columns</p>
</div>



# 2.1 สร้าง subset ของแต่ละคอลัมภ์ ITCZdownให้ง่ายต่อการเรียกใช้งาน


```python
ITCZdown_subset=ITCZdown[['Order','date_order','date','formpixel','ITCZdegree','declination']]
ITCZdown_subset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>ITCZdegree</th>
      <th>declination</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-14.351067</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-13.279600</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2007-05-07</td>
      <td>52</td>
      <td>-11.729800</td>
      <td>16.274926</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>-12.839533</td>
      <td>16.563839</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>2</td>
      <td>2007-05-08</td>
      <td>52</td>
      <td>-10.792267</td>
      <td>16.563839</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2089</th>
      <td>485</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>-11.828500</td>
      <td>-6.861150</td>
    </tr>
    <tr>
      <th>2090</th>
      <td>486</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>-11.809600</td>
      <td>-6.861150</td>
    </tr>
    <tr>
      <th>2091</th>
      <td>487</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>-14.625700</td>
      <td>-6.861150</td>
    </tr>
    <tr>
      <th>2092</th>
      <td>488</td>
      <td>156</td>
      <td>2013-10-09</td>
      <td>40</td>
      <td>-14.795800</td>
      <td>-6.861150</td>
    </tr>
    <tr>
      <th>2093</th>
      <td>489</td>
      <td>157</td>
      <td>2013-10-10</td>
      <td>40</td>
      <td>-18.783700</td>
      <td>-7.237889</td>
    </tr>
  </tbody>
</table>
<p>2094 rows × 6 columns</p>
</div>



# 2.2 Polinomials regression ITCZdown


```python
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

```

    C:\Users\ADMIN\Jupyter Notebook\lib\site-packages\IPython\core\interactiveshell.py:3369: RankWarning: Polyfit may be poorly conditioned
      exec(code_obj, self.user_global_ns, self.user_ns)
    


    
![png](output_13_1.png)
    


    0.628562604817532
    error = 37.1437395182468
    

# 3. เปิดไฟล์ที่เราได้คัดเลือกจากกราฟด้านบน


```python
ITCZup = pd.read_excel("ITCZup.xlsx")
ITCZup
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>time</th>
      <th>ITCZ1MIN</th>
      <th>ITCZ1MAX</th>
      <th>ITCZ2MIN</th>
      <th>ITCZ2MAN</th>
      <th>ITCZ3MIN</th>
      <th>ITCZ3MAX</th>
      <th>ITCZaverage</th>
      <th>ITCZdegree</th>
      <th>declination</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>1903-01-05 06:00:00</td>
      <td>342</td>
      <td>414</td>
      <td>342</td>
      <td>415</td>
      <td>342</td>
      <td>415</td>
      <td>378.333333</td>
      <td>19.687333</td>
      <td>23.053028</td>
      <td>NaN</td>
      <td>41640.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>1903-01-05 12:00:00</td>
      <td>350</td>
      <td>428</td>
      <td>351</td>
      <td>428</td>
      <td>351</td>
      <td>428</td>
      <td>389.333333</td>
      <td>18.728133</td>
      <td>23.053028</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>1903-01-05 18:00:00</td>
      <td>348</td>
      <td>439</td>
      <td>348</td>
      <td>437</td>
      <td>348</td>
      <td>437</td>
      <td>392.833333</td>
      <td>18.422933</td>
      <td>23.053028</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>37</td>
      <td>2014-06-12</td>
      <td>38</td>
      <td>1903-01-06 00:00:00</td>
      <td>356</td>
      <td>435</td>
      <td>356</td>
      <td>435</td>
      <td>356</td>
      <td>435</td>
      <td>395.500000</td>
      <td>18.190400</td>
      <td>23.129774</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>37</td>
      <td>2014-06-12</td>
      <td>38</td>
      <td>1903-01-06 06:00:00</td>
      <td>339</td>
      <td>424</td>
      <td>340</td>
      <td>424</td>
      <td>340</td>
      <td>424</td>
      <td>381.833333</td>
      <td>19.382133</td>
      <td>23.129774</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>840</th>
      <td>325</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 00:00:00</td>
      <td>449</td>
      <td>484</td>
      <td>449</td>
      <td>481</td>
      <td>449</td>
      <td>481</td>
      <td>465.500000</td>
      <td>12.477350</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>841</th>
      <td>326</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 06:00:00</td>
      <td>440</td>
      <td>478</td>
      <td>440</td>
      <td>477</td>
      <td>440</td>
      <td>477</td>
      <td>458.666667</td>
      <td>13.067067</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>842</th>
      <td>327</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 12:00:00</td>
      <td>440</td>
      <td>475</td>
      <td>440</td>
      <td>475</td>
      <td>440</td>
      <td>475</td>
      <td>457.500000</td>
      <td>13.167750</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>843</th>
      <td>328</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>1903-11-08 18:00:00</td>
      <td>438</td>
      <td>490</td>
      <td>439</td>
      <td>490</td>
      <td>439</td>
      <td>490</td>
      <td>464.333333</td>
      <td>12.578033</td>
      <td>-12.273420</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>844</th>
      <td>329</td>
      <td>171</td>
      <td>2016-10-24</td>
      <td>33</td>
      <td>1903-11-09 00:00:00</td>
      <td>440</td>
      <td>492</td>
      <td>438</td>
      <td>495</td>
      <td>438</td>
      <td>495</td>
      <td>466.333333</td>
      <td>12.405433</td>
      <td>-12.612016</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>845 rows × 16 columns</p>
</div>



# 3.1 สร้าง subset ของแต่ละคอลัมภ์ของ ITCZup ให้ง่ายต่อการเรียกใช้งาน


```python
ITCZup_subset=ITCZup[['Order','date_order','date','formpixel','ITCZdegree','declination']]
ITCZup_subset
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Order</th>
      <th>date_order</th>
      <th>date</th>
      <th>formpixel</th>
      <th>ITCZdegree</th>
      <th>declination</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>19.687333</td>
      <td>23.053028</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>18.728133</td>
      <td>23.053028</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>36</td>
      <td>2014-06-11</td>
      <td>38</td>
      <td>18.422933</td>
      <td>23.053028</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5</td>
      <td>37</td>
      <td>2014-06-12</td>
      <td>38</td>
      <td>18.190400</td>
      <td>23.129774</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>37</td>
      <td>2014-06-12</td>
      <td>38</td>
      <td>19.382133</td>
      <td>23.129774</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>840</th>
      <td>325</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>12.477350</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>841</th>
      <td>326</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>13.067067</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>842</th>
      <td>327</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>13.167750</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>843</th>
      <td>328</td>
      <td>170</td>
      <td>2016-10-23</td>
      <td>33</td>
      <td>12.578033</td>
      <td>-12.273420</td>
    </tr>
    <tr>
      <th>844</th>
      <td>329</td>
      <td>171</td>
      <td>2016-10-24</td>
      <td>33</td>
      <td>12.405433</td>
      <td>-12.612016</td>
    </tr>
  </tbody>
</table>
<p>845 rows × 6 columns</p>
</div>



# 3.2 Polinomials regression ITCZup


```python
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
```

    C:\Users\ADMIN\Jupyter Notebook\lib\site-packages\IPython\core\interactiveshell.py:3369: RankWarning: Polyfit may be poorly conditioned
      exec(code_obj, self.user_global_ns, self.user_ns)
    


    
![png](output_19_1.png)
    


    0.6735952793117158
    error = 32.640472068828416
    


```python
from sklearn.metrics import r2_score
print(r2_score(p,myModel(o)))
print('error =', 100 -r2_score(p,myModel(o))*100 )
```

    0.6735952793117158
    error = 32.640472068828416
    


```python

```

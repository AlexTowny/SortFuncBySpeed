#!/usr/bin/env python
# coding: utf-8

# # FuncFucker3000

# *Simple way to compare fast of your functions*

# In[ ]:


get_ipython().system(u'pip3 install sympy')


# In[1]:


import sympy as su


# In[2]:


def fac(k):
    ans = 1.0
    for i in range(1,k):
        ans *= i
    return ans


# Enter your functions expressions.
# One line - one expression.

# In[3]:


n = su.symbols('n')


# In[8]:


expr_arr = ["pow(1/3,n)","17","su.log(n,2)","su.sqrt(n)","n","pow(n,3)","pow(3/2,n)","pow(n,2)","su.factorial(n)"]


# In[9]:


def compr(i1, i2):
    limit_expr = su.limit(eval(expr_arr[i1])/eval(expr_arr[i2]), n, su.oo)
    return limit_expr==su.oo


# In[10]:


def bubble_sort(exprs):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(exprs) - 1):
            if compr(i, i+1):
                exprs[i], exprs[i + 1] = exprs[i + 1], exprs[i]
                swapped = True
    return exprs

print(bubble_sort(expr_arr))


# In[ ]:





# In[ ]:





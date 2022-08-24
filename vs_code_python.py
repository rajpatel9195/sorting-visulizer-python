
import matplotlib.pyplot as plt
import numpy as np

amount = 25

lst = np.random.randint(0,500,amount)
x = np.arange(0,amount,1)
n=len(lst)
c = ["gray"] *n
for i in range(n):
    for j in range(0,n-i-1):
      
        
        ################grren and red color #####################
        c[j]='green'
        c[j+1]='red'
        #####################################
        plt.bar(x,lst,color= c)
        plt.pause(0.5)
        plt.clf()
        ##############for number above bar#########
        for i in range(len(x)):
            plt.text(i,lst[i],lst[i],ha="center",va='bottom')
            
        #########sorting logic#####################    
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j] 
        ##########finishing green color in last ######### 
        c[j]='gray'
        c[j+1]='green'       
        
plt.show()       

        

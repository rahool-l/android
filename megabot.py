U
    Qu�^e  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZdZe	ed� ze
dd	�Ze�� Zej W nJ   eed
��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX z&e
dd	�Ze
dd	�Ze�� Zej W nJ   eed��Ze
dd�Ze�e� ej e
dd	�Ze�� Zej Y nX zd dlZW nF ek
�rp   e	d� e�d� e	d� e�d� d dlZeZY nX dd� Zdd� Zedk�r�e�  dS )�    N�cleara�                                           
[1;34;40m                  \             /            
[1;34;40m                   \___________/    won data 
[1;33;40m                   /           \             
[1;33;40m                  /   @     @   \            
[1;32;40m                 ||             ||          
[1;34;40m                  \   \_ __ _/  /            
[1;30;40m                   \___________/                        
a�    
[1;34;40m                  \             /            
[1;34;40m                   \___________/    not data 
[1;33;40m                   /           \             
[1;33;40m                  /   @     @   \            
[1;32;40m                 ||    _ _ _    ||           
[1;32;40m                  \   /     \   /            
[1;30;40m                   \___________/             
  zG[1;36;40m
___________________________________________________________
a�  [1;36;40m
             **                  **                 M
               **               **                  E 
                ** *********** **                   G
                 ***************                    A
                ******************
              **** @ ****** @ *****
             ***********************                R
            *************************               U
           ***************************              N  
                                        
        ****    ******************     ****         2  
       ******  ********************   ******          
       ******  *********************  ******        0     
       ******  *********************  ******         
       ******  *********************  ******        2     
       ******  *********************  ******          
       ******  *********************  ******        0  
       ******  *********************  ******            
       ******  *********************  ******              
       ******  *********************  ******              
       ******  *********************  ******              
       ******    *****************    ******           
        ****       *************       ****        R  
                                                   J 
                ******       *****                      
               ********     ********                     
               ********     ********                    
               ********     ********               S     
               ********     ********               T    
               ********     ********               U      
               ********     ********               D      
               ********     ********               I      
                ******       ******                O      
__________________________________________________________

[1;35;40m             [Be Cool] mod by RJ studio 2020
� zfile_auth.txt�rz![1;0;40mPaste Your Auth here :- �wzfile_url.txtzPaste Your URL here :- zwaiting.......zpip3 install requestsz%s Requests installed.c            	      C   s&  t �d� ttd� dtdd�} t}ttd��}d}t||�D ]�}t �d� tt� d}t	j
|| d�}t|�}|d	kr�tt� n*|d
kr�tt� ntt� td� tt� |d7 }tdt|�ddd� td�D ]@}|d d }tdtt|��d dd� t�d� tj�d� q�q>t �d� t�  d S )Nr   �
zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionz[1;36;40mEnter Amount - r   )Zheadersz<Response [204]>z<Response [200]>zC
[1;31;40m [retry] Check Again your internet connection... [retry]�   z
[1;0;40m
zWait For Next requestr   )�end�   �d   z[1;36;40m
>>> [+]z% g      �?z[Fzfiglet FINISHED)�os�system�print�name�	file_auth�	file_url1�int�input�range�requests�get�str�no_data�won_data�line�time�sleep�sys�stdout�write�again)	�headZurl�sZrr�sizeZrjZrequest�jZrrr� r$   �/storage/emulated/0/mega.py�maint   s>    

 �




r&   c                  C   sJ   t d�} | dks| dkr t�  n&| dks0| dkr8t�  ntd� | �  d S )Nz*[1;0;40m
Do Restart Algorithm :  (y/n) - �y�Y�n�Nz[1;30;40mReEnter)r   r&   �quitr   )r   r$   r$   r%   r   �   s    r   �__main__)r   Zurllibr   r   r   r   r   r   r   r   �open�f�readr   �closer   r   Zwrr   r   r   �ImportErrorZauthr&   r   �__name__r$   r$   r$   r%   �<module>   s^   
'














'

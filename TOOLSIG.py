U
    !�^Z  �                
   @   sZ  d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ e�d� e�ddd�Ze	e� e	edd�� e	ed	d
�� e	edd�� e	edd�� e
edd��Ze �e�jZe�dee�e�de��d��dd����Zee��dd�Zee��dd�Zee��dd�Zee��dd�Ze	edd�� e
d�Zeed��e �e�j� e	edd
�� dS )�    N)�colored�clearzTOOLS IGzABIN XD.5TXZ01zYOUTUBE: BENJAMIN IDZwhitez)GITHUB: https://github.com/Abinayanafaiq/ZredzInstagram: abinayanafaiq_Zyellowz2==================================================Zgreenz
URL POST: Zbluez'display\_url'\:\ \'(.*?)'z_sharedData = (.*)</�   �;� �[�]�"�'zCONTOH : /sdcard/FOTO.pngzPATH:�wbz"IMAGE TERSIMPAN DI FOLDER TERSEBUT)Zrequests�reZjson�osZvar_animateZ	termcolorr   �systemZbanner�print�inputZurl�get�text�b�findall�str�loads�search�group�replace�r�Z�j�h�y�g�open�writeZcontent� r"   r"   �/sdcard/ig.py�<module>   s(    
,
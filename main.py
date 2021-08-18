# -*- coding: UTF-8 -*-

import os
import tqdm
    
def split_txt_each_line(file, save_file, key_words, num_split, num_save):
    '''
    file(str)：原始文件路径（a/b/c.txt）
    save_file(str)：保存文件路径(a/b/d.txt)
    key_words(str)：按什么字符开刀
    num_split(int)：切几刀
    num_save(int)：保存哪一段
    '''
    with open(file, 'r', errors='ignore') as f:
        for line in f:
            line_split = line.split(key_words, num_split)
            f = open(save_file, 'a')
            if num_save == num_split + 1:   # 保存最后一段，防止产生双重换行
                f.write(line_split[num_save-1])
            else:
                f.write(line_split[num_save-1] + '\n')
    print('done')
    

if __name__ == '__main__':
    print("hello world!")
    
    
    # 测试split_txt_each_line
    line_list = []
    file = '/Users/yijie/Code/python-txt/text.txt'
    save_file = '/Users/yijie/Code/python-txt/text_new.txt'
    split_txt_each_line(file=file, save_file=save_file, key_words="你好：", num_split=2, num_save=3)
    
    
    
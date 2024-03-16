from io import StringIO
from pathlib import Path
import streamlit as st
import time
from detect import *
import os
import sys
import argparse
from PIL import Image


def get_subdirs(b='.'):
    '''
        Returns all sub-directories in a specific Path
    '''
    result = []
    for d in os.listdir(b):
        bd = os.path.join(b, d)
        if os.path.isdir(bd):
            result.append(bd)
    return result


def get_detection_folder():
    '''
        Returns the latest folder in a runs\detect
    '''
    return max(get_subdirs(os.path.join('runs', 'detect')), key=os.path.getmtime)


if __name__ == '__main__':

    st.title('YOLOv9 Streamlit App')

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', nargs='+', type=str,
                        default='D:/yolov9/runs/train/exp3\weights/best.pt', help='model.pt path(s)')
    parser.add_argument('--source', type=str,
                        default=ROOT / 'data/images', help='source')

    opt = parser.parse_args()
    print(opt)

    source = ("图片检测")



    uploaded_file = st.sidebar.file_uploader(
        "上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file is not None:
        is_valid = True
        with st.spinner(text='资源加载中...'):
            st.sidebar.image(uploaded_file)
            picture = Image.open(uploaded_file)
            picture = picture.convert('RGB')
            # 现在你可以保存为JPEG了
            picture.save(f'data/images/{uploaded_file.name}', 'JPEG')

            opt.source = f'data/images/{uploaded_file.name}'
    else:
        is_valid = False


    if is_valid:
        print('valid')
        if st.button('开始检测'):

            res(opt)


            with st.spinner(text='Preparing Images'):
                for img in os.listdir(get_detection_folder()):
                    st.image(str(Path(f'{get_detection_folder()}') / img))

                st.balloons()

                st.balloons()

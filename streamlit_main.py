import streamlit as st
import torch
from torch import nn
import torchvision.transforms as transforms
import os, json

st.title('FashinMNIST')

img.file = st.file_unloader('이미지를 업로드 하세요' , 

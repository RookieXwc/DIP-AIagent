# installation

```shell
conda create -n agent python=3.8
conda activate agent

conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cpuonly -c pytorch

pip install -r requirements.txt

conda install -c conda-forge ffmpeg
```



1.参考https://github.com/XiaoXinYo/Easy-Ernie，得到自己百度文心一言对话模型的API，填到main\_loop.py的34、35行

2.连接梯子，从[microsoft/git-base-coco at main (huggingface.co)](https://huggingface.co/microsoft/git-base-coco/tree/main)下载git-base-coco模型，放到项目目录下。如果没有梯子，可以从百度网盘下载。链接：https://pan.baidu.com/s/1WwXuAfq-frCnAPNaFKEpDQ，提取码：wurp 

3.运行main\_loop.py
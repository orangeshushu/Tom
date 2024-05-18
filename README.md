# TOM

## Installation

Docker environment (recommended)
<details><summary> <b>Expand</b> </summary>

``` shell
pip install -r .
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

</details>


## Inference

<div align="center">
    <a href="./">
        <img src="./figure/horses_prediction.jpg" width="49%"/>
    </a>
</div>

``` shell
# inference demo
python detect_dual.py --source 'sample.jpg' 
```

## Weights

Please download the weights from the below link:
https://mailmissouri-my.sharepoint.com/:u:/g/personal/jx993_umsystem_edu/EW25OTrOcd5OjAOhQuIYIDkBKUGueGmW-rk6uznFM4AEjA?e=ejdlVc
And put it in the path:
runs/train/tongue3/weights/best.pt
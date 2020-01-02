# FogKiller

Single Image Haze Removal Using Dark Channel Prior

## References

- http://kaiminghe.com/publications/cvpr09.pdf

- http://kaiminghe.com/publications/eccv10guidedfilter.pdf

- https://arxiv.org/abs/1505.00996

## How to Use 

- Make sure you are using [Python 3](http://python.org/) and install dependencies:

```shell
  python setup.py install
```

- Run Python code in shell:

```shell
  python dehaze.py -i inputImagePath
  python dehaze.py -i inputImagePath -o outputImagePath
  # example
  python dehaze.py -i ./image/1.bmp
  python dehaze.py -i ./image/1.bmp -o ./output/output.jpg
```

- Run in Windows:

```shell
cd ./App

# install dependencies
npm install

# serve with hot reload at localhost:9080
npm run dev

# build electron application for production
npm run build
```

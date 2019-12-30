# DSN

Developer knowledge transfer network analysis
Assignment of Complex Network Analysis, take facebookresearch's fastText project as an example, construct knowledge flow network betweeen contributors, apply social network analysis menthod (centrality metrics, community detection, influenctial maximization et.al) to find interesting things.

## Data Preparation

1. get commit log

``` Shell
$ cd data
$ git clone https://github.com/PaddlePaddle/Paddle.git
$ git log --name-only --pretty="STARTOFTHECOMMIT:%H;%an;%ae;%at" > log
```

2. get knowledge transfer edges

```Shell
$ python src/data_process.py data/log data/edge
```


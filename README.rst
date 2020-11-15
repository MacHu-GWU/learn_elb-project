
AWS Elastic Beanstalk 学习笔记
==============================================================================

.. contents::
    :depth: 1
    :local:


初步理解 ELB 是如何工作的
------------------------------------------------------------------------------

建议参照 e (https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) 这篇文档, 完整的走一遍流程, 部署一个网站. 这个 Repo 里已经有一个 ``flask-example`` 的文件夹了, 请先 cd 到这个文件件里, 将它作为实验的 Workspace. 请参考 ``flask-example/README.rst`` 中的信息.

**概念 Workspace (工作目录)**:

工作目录即为一个文件夹. 你部署的时候会根据 ``.ebignore`` 和 ``.gitignore`` 中的规则, 将整个项目打包上传到 S3. 而且在你用 ``eb init`` 命令初始化时, 你需要先进入 Workspace Dir 里面. 通常情况下, 你的整个 Git Repository 的目录就是你的 EB Workspace 目录.

**概念 Initialization (初始化)**:

如果你目前默认的 AWS profile 就是你想要使用的, 那么你可以直接用 ``eb init``, 否则需要用 ``eb init --profile ${your_aws_profile_name}`` 来指定你想要用的 AWS profile. 显然这个 AWS Profile 要能够:

- 创建 S3 Bucket, S3 PutObject
- 创建 CloudFormation

总之这个的权限要求的还是比较高的, 建议使用你平时主力开发的权限.

执行完 ``eb init`` 命令后, 你会发现在 Workspace 下多了一个 ``.elasticbeanstalk`` 的目录, 里面有个 ``config.yml`` 里面记录了你所使用的 AWS Profile, 你所指定的 EB Platform (我们在用 Python, 当然是 Python 的 Platform 了), 连接 EC2 的 SSH Key Pair, Application Name 用在 EB Console 中的 Application 等信息. **所以本质上** ``eb init`` **就是帮你创建了这个** ``config.yml`` 文件而已.

注意, 这里的 Application 是一个专有名词, 指 EB Console 中的 Application. 每一个 Application 代表一个应用的抽象概念. 而 Environment 则是一个实际的 Web Server 服务器, 背后有 EC2, Load Balancer 等等.


Quick Links
------------------------------------------------------------------------------

- Flask Tutorial: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
- EB Cli Reference: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-getting-started.html

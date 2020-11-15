此文件夹按照官方文档 Deploying a flask application to Elastic Beanstalk https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html, 成功部署了一个 Web app. 简单了解了 EB 是如何工作的.

里面比较关键的命令有:

.. code-block:: bash

    $ eb init -p python-3.6 flask-example --region us-east-1 --profile eq_sanhe``
    $ eb create flask-env
    $ eb deploy flask-env

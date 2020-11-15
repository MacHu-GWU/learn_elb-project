# -*- coding: utf-8 -*-

from learn_elb.webapp.app import create_app

# EB looks for an 'application' callable by default,
# please keep the variable name as it is
application = create_app()

# THE CODE BELOW IS FOR TESTING ON LOCAL ONLY, please DON't enable it in production!
# if __name__ == "__main__":
#     import learn_elb.webapp.config as config
#     application.debug = True
#     application.run(port=config.PORT)

# -*- coding: utf-8 -*-

from learn_elb.webapp.app import create_app
import learn_elb.webapp.config as config

# EB looks for an 'application' callable by default,
# please keep the variable name as it is
application = create_app()

# if __name__ == "__main__":
#     application.debug = True
#     application.run(port=config.PORT)

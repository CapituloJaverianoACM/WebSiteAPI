from distutils.core import setup

setup(name='acm_web_site',
      version='2.0',
      packages=['acm_web_site',
                'acm_web_site.settings',
                'web_site',
                'web_site.migrations',
                ],
      scripts=['acm_web_site/manage.py']
)

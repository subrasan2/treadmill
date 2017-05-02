"""Treadmill module."""


import os
import pkgutil
import treadmill

__path__ = pkgutil.extend_path(__path__, __name__)


def deploy_path_join(obj):
    deploy_path = treadmill.TREADMILL_DEPLOY_PACKAGE
    if os.path.exists('deploy') and os.listdir('deploy'):
        deploy_path = os.path.join('deploy/')
    return os.path.realpath(deploy_path + obj)


def __root_join(*path):
    """Joins path with location of the current file."""
    mydir = os.path.dirname(os.path.realpath(__file__))
    return os.path.realpath(os.path.join(mydir, *path))


# Global pointing to root of the source distribution.
#
# TODO: how will it work if packaged as single zip file?
if os.name == 'nt':
    _TREADMILL_SCRIPT = 'treadmill.cmd'
else:
    _TREADMILL_SCRIPT = 'treadmill'

VIRTUAL_ENV = os.environ.get('VIRTUAL_ENV')

if VIRTUAL_ENV:
    TREADMILL_BIN = os.path.join(VIRTUAL_ENV, 'bin', _TREADMILL_SCRIPT)
    TREADMILL = os.path.join(treadmill.__path__[0], '../')
else:
    TREADMILL_BIN = os.path.join('/bin', _TREADMILL_SCRIPT)
    TREADMILL = __root_join('..')

if not os.environ.get('TREADMILL_EXE_WHITELIST', None):
    os.environ['TREADMILL_EXE_WHITELIST'] = \
        os.path.join(TREADMILL, 'etc/linux.exe.config')

TREADMILL_LDAP = os.environ.get('TREADMILL_LDAP')
TREADMILL_DEPLOY_PACKAGE = os.path.join(treadmill.__path__[0], '../deploy/')
os.environ['ANSIBLE_CONFIG'] = deploy_path_join('ansible.cfg')

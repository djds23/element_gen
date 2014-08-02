from distutils.core import setup, Command

class PyTest(Command):
    user_options=[]
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, 'runtest.py'])
        raise SystemExit(errno)

setup(
    cmd = {'test':PyTest},
    name='element_gen',
    version='0.1',
    author='Dean Rex Silfen',
    packages=['element_gen','element_gen.tests'],
    license='LICENSE',
    description='Create slideshows from Twitter users!'
)

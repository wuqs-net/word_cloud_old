import io
from setuptools import setup
from setuptools.extension import Extension
import versioneer

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(
    author="CS489 - Group 12",
    name='wordcloud_cs489_old',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url='https://github.com/wuqs-net/word_cloud_old',
    description='A little word cloud generator',
    long_description=readme,
    long_description_content_type='text/markdown; charset=UTF-8',
    license='MIT',
    install_requires=['numpy>=1.6.1', 'pillow', 'matplotlib'],
    ext_modules=[Extension("wordcloud.query_integral_image",
                           ["wordcloud/query_integral_image.c"])],
    entry_points={'console_scripts': ['wordcloud_cli=wordcloud.__main__:main']},
    packages=['wordcloud'],
    package_data={'wordcloud': ['stopwords', 'DroidSansMono.ttf']}
)

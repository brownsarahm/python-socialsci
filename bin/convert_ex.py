import os
import sys
import frontmatter


top_ex_dir = '../exercises/'
# iterate over files in _exercises folder

learner_dir = os.path('../../python-socialsci-files')
os.mkdir(learner_dir)
os.mkdir(os.path.join(learner_dir,'code'))
os.mkdir(os.path.join(learner_dir,'data'))

for ex_file in os.path.list(top_ex_dir):
    post = frontmatter.load('tests/hello-world.markdown')
    ex = post.content

    # replace ~~~ with ''
    ex.replace()

    # comment non code?

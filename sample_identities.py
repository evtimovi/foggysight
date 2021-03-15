"""
A module for subsampling identities from the VGG Face 2 dataset,
available at http://www.robots.ox.ac.uk/~vgg/data/vgg_face2/
"""
import os
import numpy as np
import random

from absl import app, flags

VGG_BASE = "/data/vggface"

FLAGS = flags.FLAGS

flags.DEFINE_string('image_directory',
                    os.path.join(VGG_BASE, 'test'),
                    'Top level directory for images')
flags.DEFINE_string('output_file',
                    'sampled_identities.txt',
                    'Directory to output processed images')
flags.DEFINE_integer('seed',
                    3003202021,
                    'Random seed to use for the random generators')
flags.DEFINE_integer('num_id',
                    20,
                    'Number of identities to sample')
flags.DEFINE_integer('num_im',
                    50,
                    'Number of pictures per identity')

def sample_identities(argv=None):
    identities = os.listdir(FLAGS.image_directory)

    np.random.seed(FLAGS.seed)
    random.seed(FLAGS.seed)

    with open(FLAGS.output_file, "w") as f:
        f.write("{} {}\n".format(FLAGS.num_id, FLAGS.num_im))
        identities = np.random.choice(identities, FLAGS.num_id)
        for identity in identities:
            images = os.listdir(os.path.join(FLAGS.image_directory, identity))
            images = np.random.choice(images, FLAGS.num_im)
            f.write(identity + "\n")
            f.write("\n".join(images))
            f.write("\n")

if __name__ == '__main__':
    app.run(sample_identities)

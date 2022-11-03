import math
import tensorflow as tf


def probability_word(word_frequency, sampling_factor=0.00005):
    '''p(word) = (min(1, math.sqrt(word_frequency / sampling_factor) /
            (word_frequency / sampling_factor)))'''

    if word_frequency == 0:
        probability = 0
    else:
        probability = (min(1, math.sqrt(
            word_frequency/sampling_factor) / (word_frequency / sampling_factor)))

    return probability


print(probability_word(word_frequency=10))


def frequency_rank(rank):
    '''frequency(rank) ~ 1/(rank * (log(rank) + gamma) + 1/2 - 1/(12*rank))
    gamma => Euler-Mascheroni constant = 0.5772156649015328606065120900824024310421'''
    gamma = 0.5772156649015328606065120900824024310421

    f_rank = 1/(rank * (math.log(rank) + gamma) + 1/2 - 1/(12*rank))

    return f_rank


print(frequency_rank(1))


sampling_table = tf.keras.preprocessing.sequence.make_sampling_table(size=10)
print(sampling_table)

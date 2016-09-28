#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def sigmoid(x1, x2, a = 1.0):
    y = 1.0 / (1.0 + np.exp(- (x1 - x2)))
    return y


def mapping(data, f = sigmoid):
    map = []
    for i in range(len(data)):
        x = []
        for j in range(len(data)):
            x.append(int(255 * f(data[i], data[j])))
        map.append(x)

    map = np.array(map)
    return map


if __name__ == '__main__':
    import random
    import cv2
    import matplotlib.pyplot as plt
    # 一様乱数
    data = []
    for i in range(1000):
        data.append(random.random())
    plt.plot(data)
    plt.savefig("uniform.png")
    plt.clf()
    m = mapping(data)
    cv2.imwrite('sample_uniform.jpg',m)
    # ホワイトノイズ
    data = []
    for i in range(1000):
        data.append(np.random.randn())
        plt.plot(data)
    plt.savefig("white.png")
    plt.clf()
    m = mapping(data)
    cv2.imwrite('sample_white.jpg',m)
    # ポワソン分布
    data = []
    for i in range(1000):
        data.append(np.random.poisson())
        plt.plot(data)
    plt.savefig("poisson.png")
    plt.clf()
    m = mapping(data)
    cv2.imwrite('sample_poisson.jpg',m)
    # 三角波
    data = []
    for i in range(1000):
        data.append(np.sin(2.0 * np.pi * i / 50.0))
        plt.plot(data)
    plt.savefig("sin.png")
    plt.clf()
    m = mapping(data)
    cv2.imwrite('sample_sin.jpg',m)

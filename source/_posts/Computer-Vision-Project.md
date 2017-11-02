---
title: Project - Computer Vision
date: 2017-10-17 19:48:50
tags:
- Computer Vision
- Deep Learning
- CS348
- Coursework
- English
categories: Research
thumbnail: /assets/rain-princess.jpg
---
# 2017.10.17
In course CS348, Computer Vision, our coursework is to write a paper and submit it to a conference.

My Partners are Siqi Liu and Mengyao Cao. After discussion, we decided our draft topic as:

A Painting AI based on Cascaded Refinment Network

The PPT illustrates our scheme:

<iframe src="../files/Computer Vision.pdf" style="width:718px; height:700px;" frameborder="0"></iframe>

<a href="../files/Computer Vision.pdf">Download File</a>

The final topic will be confirm in tomorrow's class.

Wish our project a brilliant success!

# 2017.10.25
This time, I read a paper named **A Neural Algorithm of Artistic Style**.

This paper is about generating a picture with given real picture and a Painting. The generated picture will have both the feature of
the painting and the initial picture.

For example, this is the painting used:
![rain-princess](/assets/rain-princess.jpg)

Then, the Algorithm will produce a picture like this:

![dome-afremov](/assets/dome-afremov.png)

It is so amazing!!

### The paper
The method of the paper is:

>Use the VGG-19 network to process the initial picture, noted by $\mathbf{p}$, and the painting, noted by $\mathbf{a}$, then at each layer, the nerwork will have some feature maps corresponding to $\mathbf{p}$ and $\mathbf{a}$.

>Input a noise picture $\mathbf{x}$ to the network, also, $\mathbf{x}$ will also have some featuremaps at every layers.

>Define a loss function between $\mathbf{x}$ and $\mathbf{p}$, called content loss. And a loss function between $\mathbf{x}$ and $\mathbf{a}$, called style loss.Then, the author define a compound loss function:

$$L_{total}(\mathbf{p}, \mathbf{a}, \mathbf{x})=\alpha L_{content}(\mathbf{x}, \mathbf{p}) + \beta L_{style}(\mathbf{x}, \mathbf{a})$$

>Using the optimization method to maximize the $L_{total}$, and with this process, fix the noise picture $\mathbf{x}$. Then, the noise picture will become the finally result.

We can actually change the ratio between $\alpha$ and $\beta$ to change the ratio of content and style.

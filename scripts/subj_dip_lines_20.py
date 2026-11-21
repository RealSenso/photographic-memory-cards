"""DIP Topic 20 (CNNs) statements, line by line."""

SUBJECT = "DIP"

FIX = {
    3191: {"statement": r"""<b>Convolution layer.</b>"""
        r"""<span class="ln">Each output unit sees only a $K\times K$ patch of the input</span>"""
        r"""<span class="ln">and all positions share the same $F$ filters.</span>"""
        r"""<span class="ln">For input size $H$, padding $P$ and stride $S$ the output size is</span>"""
        r"""<span class="ln in">$H'=\big\lfloor\frac{H-K+2P}{S}\big\rfloor+1$,</span>"""
        r"""<span class="ln">and the layer has $K^2C_{\rm in}F+F$ parameters, independent of the image size.</span>"""
        r"""<span class="ln">(Implemented as cross-correlation, without flipping the kernel.)</span>"""},
    3192: {"statement": r"""<b>Receptive field.</b>"""
        r"""<span class="ln">The input region influencing one unit grows as</span>"""
        r"""<span class="ln in">$\mathrm{RF}_l=\mathrm{RF}_{l-1}+(K_l-1)\prod_{i\lt l}S_i$.</span>"""
        r"""<span class="ln">$L$ stacked $3\times3$ stride-1 convolutions give $(2L+1)\times(2L+1)$;</span>"""
        r"""<span class="ln">two of them match one $5\times5$ with $2\cdot9C^2$ rather than $25C^2$ weights.</span>"""
        r"""<span class="ln">Pooling (e.g. $2\times2$, stride 2) halves the spatial size and adds slight translation invariance.</span>"""},
    3193: {"statement": r"""<b>Activations and gradient flow.</b>"""
        r"""<span class="ln">Without a nonlinearity, stacked convolutions collapse to one linear map.</span>"""
        r"""<span class="ln">$\mathrm{ReLU}(x)=\max(0,x)$ has gradient 1 for $x\gt0$ and does not saturate;</span>"""
        r"""<span class="ln">the sigmoid has $\sigma'=\sigma(1-\sigma)\le\tfrac14$,</span>"""
        r"""<span class="ln in">so gradients shrink by at least $4$ per layer.</span>"""
        r"""<span class="ln">For a layer with input $a_{l-1}$ and output $z_l=W_la_{l-1}$,</span>"""
        r"""<span class="ln in">backpropagation gives $\partial L/\partial W_l=\delta_l\,a_{l-1}^T$, where $\delta_l=\partial L/\partial z_l$.</span>"""},
    3194: {"statement": r"""<b>From LeNet to ResNet.</b>"""
        r"""<span class="ln">LeNet-5 (1998) set the pattern conv, pooling, fully-connected.</span>"""
        r"""<span class="ln">AlexNet (2012) used ReLU, dropout and GPUs;</span>"""
        r"""<span class="ln">VGG (2014) showed depth with only $3\times3$ filters;</span>"""
        r"""<span class="ln">GoogLeNet (2014) used parallel branches and $1\times1$ convolutions $C_{\rm in}\to C_{\rm out}$ to cut parameters;</span>"""
        r"""<span class="ln">ResNet (2015) added identity skip connections, making 50–152 layers trainable.</span>"""},
    3195: {"statement": r"""<b>Residual block.</b>"""
        r"""<span class="ln">Instead of learning $H(x)$, learn $F(x)=H(x)-x$</span>"""
        r"""<span class="ln in">and output $y=F(x,\{W_i\})+x$.</span>"""
        r"""<span class="ln">Then $\partial y/\partial x=\partial F/\partial x+I$,</span>"""
        r"""<span class="ln in">so the gradient has a direct path through $+I$ and does not vanish with depth.</span>"""
        r"""<span class="ln">The shortcut is the identity if shapes match, otherwise a $1\times1$ projection;</span>"""
        r"""<span class="ln">bottleneck blocks ($1\times1$, $3\times3$, $1\times1$) keep deep nets cheap.</span>"""},
    3196: {"statement": r"""<b>Example (ResNet-style stem, with biases).</b>"""
        r"""<span class="ln">Input $224\times224\times3$, kernel $7\times7$, stride $2$, padding $3$, $F=64$:</span>"""
        r"""<span class="ln in">$H'=\lfloor(224-7+2\cdot3)/2\rfloor+1=\lfloor223/2\rfloor+1=112$,</span>"""
        r"""<span class="ln in">giving a $112\times112\times64$ map,</span>"""
        r"""<span class="ln in">with $7\cdot7\cdot3\cdot64+64=9\,408+64=9\,472$ parameters.</span>"""},
}

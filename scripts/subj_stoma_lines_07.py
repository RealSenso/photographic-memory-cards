"""StoMA Topic 07 statements, line by line (one hypothesis or conclusion per line; the source on its own small line)."""

SUBJECT = "StoMA"

FIX = {
    30701: {"statement": r"""<b>Joint CDF.</b>"""
        r"""<span class="ln">For random variables $X,Y$ on the same space,</span>"""
        r"""<span class="ln in">$F_{X,Y}(x,y)=\mathbb P(X\le x,\,Y\le y)$.</span>"""
        r"""<span class="ln">It is non-decreasing in each variable, right-continuous,</span>"""
        r"""<span class="ln">tends to $0$ as either argument $\to-\infty$ and to $1$ as both $\to\infty$,</span>"""
        r"""<span class="ln">and for $a\lt b$, $c\lt d$:</span>"""
        r"""<span class="ln in">$\mathbb P(a\lt X\le b,\,c\lt Y\le d)=F_{X,Y}(b,d)-F_{X,Y}(a,d)-F_{X,Y}(b,c)+F_{X,Y}(a,c)\ge0$.</span>"""
        r"""<span class="src">Ross 6.1; Grimmett 4.5</span>"""},
    30702: {"statement": r"""<b>Joint density.</b>"""
        r"""<span class="ln">$X,Y$ are jointly continuous if there is $f_{X,Y}\ge0$ with</span>"""
        r"""<span class="ln in">$\mathbb P((X,Y)\in A)=\iint_Af_{X,Y}(x,y)\,dx\,dy$ for all (Borel) sets $A\subset\mathbb R^2$;</span>"""
        r"""<span class="ln">then $f_{X,Y}(x,y)=\dfrac{\partial^2F_{X,Y}(x,y)}{\partial x\,\partial y}$ where it exists,</span>"""
        r"""<span class="ln">and $\iint f_{X,Y}=1$.</span>"""
        r"""<span class="src">Ross 6.1; Grimmett 4.5</span>"""},
    30703: {"statement": r"""<b>Marginal distributions.</b>"""
        r"""<span class="ln">If $(X,Y)$ has joint density $f_{X,Y}$, then</span>"""
        r"""<span class="ln in">$X$ has density $f_X(x)=\int_{-\infty}^\infty f_{X,Y}(x,y)\,dy$,</span>"""
        r"""<span class="ln in">and likewise $f_Y(y)=\int f_{X,Y}(x,y)\,dx$;</span>"""
        r"""<span class="ln">in the discrete case $p_X(x)=\sum_yp_{X,Y}(x,y)$.</span>"""
        r"""<span class="ln">If the support depends on $x$, the limits of the inner integral are those of the section at $x$.</span>"""
        r"""<span class="src">Ross 6.1; Grimmett 3.6, 4.5</span>"""},
    30704: {"statement": r"""<b>Conditional density.</b>"""
        r"""<span class="ln">If $f_X(x)\gt 0$, the conditional density of $Y$ given $X=x$ is</span>"""
        r"""<span class="ln in">$f_{Y\mid X}(y\mid x)=\dfrac{f_{X,Y}(x,y)}{f_X(x)}$.</span>"""
        r"""<span class="ln">For each such $x$, $f_{Y\mid X}(\cdot\mid x)$ is a density:</span>"""
        r"""<span class="ln in">$\int f_{Y\mid X}(y\mid x)\,dy=1$,</span>"""
        r"""<span class="ln in">and $f_{X,Y}(x,y)=f_X(x)f_{Y\mid X}(y\mid x)$.</span>"""
        r"""<span class="src">Ross 6.5; Grimmett 4.6</span>"""},
    30705: {"statement": r"""<b>Independence via densities.</b>"""
        r"""<span class="ln">Jointly continuous $X,Y$ are independent iff</span>"""
        r"""<span class="ln in">$f_{X,Y}(x,y)=f_X(x)f_Y(y)$ for all $(x,y)$.</span>"""
        r"""<span class="ln">This forces the support of $(X,Y)$ to be a product set $S_X\times S_Y$;</span>"""
        r"""<span class="ln in">a density like $4xy$ on the triangle $0\le x\le y\le1$ factorises as a formula,</span>"""
        r"""<span class="ln in">but the coupled support makes $X,Y$ dependent.</span>"""
        r"""<span class="src">Ross 6.2; Grimmett 4.5</span>"""},
    30706: {"statement": r"""<b>Uniform on a triangle.</b>"""
        r"""<span class="ln">Let $(X,Y)$ have density $f_{X,Y}=2$ on $T=\{0\le y\le x\le1\}$ and $0$ elsewhere.</span>"""
        r"""<span class="ln">Then</span>"""
        r"""<span class="ln in">$f_X(x)=\int_0^x2\,dy=2x$ on $[0,1]$,</span>"""
        r"""<span class="ln in">$f_Y(y)=\int_y^12\,dx=2(1-y)$ on $[0,1]$,</span>"""
        r"""<span class="ln in">and $f_{Y\mid X}(y\mid x)=\dfrac2{2x}=\dfrac1x\mathbf 1_{\{0\le y\le x\}}$, a uniform law on $[0,x]$.</span>"""
        r"""<span class="ln">Since $f_{X,Y}\ne f_Xf_Y$, $X,Y$ are dependent.</span>"""
        r"""<span class="src">Ross 6.1</span>"""},
}

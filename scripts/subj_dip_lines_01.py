"""DIP Topic 01 statements, line by line (one setup, item or conclusion per line)."""

SUBJECT = "DIP"

FIX = {
    40101: {"statement": r"""<b>Pinhole camera model.</b>"""
        r"""<span class="ln">A pinhole camera has optical centre $C=(0,0,0)$ and an image plane at distance $f$ (the focal length) from $C$, perpendicular to the optical axis $Z$.</span>"""
        r"""<span class="ln">A scene point $(X,Y,Z)$ with $Z\gt 0$ is imaged at the point where the ray from $C$ through it meets the image plane:</span>"""
        r"""<span class="ln in">$x=f\,X/Z,\ y=f\,Y/Z$</span>"""
        r"""<span class="ln">(with the plane placed in front of $C$, to avoid the sign flip of the real inverted image).</span>"""
    },
    40102: {"statement": r"""<b>Camera (projection) matrix.</b>"""
        r"""<span class="ln">In homogeneous coordinates a pinhole camera is the $3\times4$ matrix $P=K[R\mid t]$,</span>"""
        r"""<span class="ln">with $R\in SO(3)$, $t\in\mathbb R^3$ the camera's pose and $K$ its $3\times3$ intrinsic matrix.</span>"""
        r"""<span class="ln">A world point $\mathbf X=(X,Y,Z,1)^\top$ is imaged at $\mathbf x=(\tilde u,\tilde v,\tilde w)^\top\sim P\mathbf X$,</span>"""
        r"""<span class="ln in">where $\sim$ means equality up to a nonzero scale;</span>"""
        r"""<span class="ln in">the pixel is $(u,v)=(\tilde u/\tilde w,\ \tilde v/\tilde w)$.</span>"""
    },
    40103: {"statement": r"""<b>Intrinsic calibration matrix.</b>"""
        r"""<span class="ln in">$K=\begin{pmatrix}\alpha_x&s&c_x\\0&\alpha_y&c_y\\0&0&1\end{pmatrix}$,</span>"""
        r"""<span class="ln">where $\alpha_x=f\,m_x$, $\alpha_y=f\,m_y$ are the focal length in pixels ($m_x,m_y$ pixels per unit length),</span>"""
        r"""<span class="ln">$(c_x,c_y)$ is the principal point in pixels</span>"""
        r"""<span class="ln">and $s$ is the skew (zero when sensor axes are orthogonal).</span>"""
        r"""<span class="ln">$K$ maps a point $(X,Y,Z)$ of the camera frame to the pixel</span>"""
        r"""<span class="ln in">$u=\alpha_xX/Z+c_x,\ v=\alpha_yY/Z+c_y$ (for $s=0$).</span>"""
    },
    40104: {"statement": r"""<b>Hierarchy of 2D planar transformations.</b>"""
        r"""<span class="ln">A homography is $\mathbf x'\sim H\mathbf x$ with $H\in\mathbb R^{3\times3}$ invertible, defined up to scale (8 degrees of freedom).</span>"""
        r"""<span class="ln">Subgroups:</span>"""
        r"""<span class="ln in">Euclidean $[R\mid t]$ (3 DOF, preserves lengths and angles);</span>"""
        r"""<span class="ln in">similarity $[sR\mid t]$ (4, preserves angles);</span>"""
        r"""<span class="ln in">affine, with last row $(0,0,1)$ (6, preserves parallelism);</span>"""
        r"""<span class="ln in">projective (8, preserves straight lines only).</span>"""
    },
    40105: {"statement": r"""<b>Inverse warping with bilinear interpolation.</b>"""
        r"""<span class="ln">Given a transformation $T$ and a source image $f$,</span>"""
        r"""<span class="ln">for every integer pixel $(x',y')$ of the output</span>"""
        r"""<span class="ln in">compute $(x,y)=T^{-1}(x',y')$,</span>"""
        r"""<span class="ln in">let $x_0=\lfloor x\rfloor$, $y_0=\lfloor y\rfloor$, $a=x-x_0$, $b=y-y_0$,</span>"""
        r"""<span class="ln in">and set the output $g(x',y')=(1-a)(1-b)f_{00}+a(1-b)f_{10}+(1-a)b\,f_{01}+ab\,f_{11}$,</span>"""
        r"""<span class="ln">with $f_{ij}=f(x_0+i,y_0+j)$ the four source pixels around $(x,y)$.</span>"""
    },
    40106: {"statement": r"""<b>Estimating a homography from four points (DLT).</b>"""
        r"""<span class="ln">Each correspondence $(x_i,y_i)\leftrightarrow(x_i',y_i')$ gives two linear equations in the entries $h$ of $H$</span>"""
        r"""<span class="ln in">(from $x_i'(h_{31}x_i+h_{32}y_i+h_{33})=h_{11}x_i+h_{12}y_i+h_{13}$ and the same for $y_i'$).</span>"""
        r"""<span class="ln">Four correspondences, no three collinear, give $A\in\mathbb R^{8\times9}$ and $Ah=0$;</span>"""
        r"""<span class="ln in">the solution with $\|h\|=1$ is the right singular vector of $A$ for its smallest singular value</span>"""
        r"""<span class="ln in">(equivalently the eigenvector of $A^\top A$ for its smallest eigenvalue).</span>"""
    },
}

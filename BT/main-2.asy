if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
defaultfilename="main-2";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);


import graph;

real left = -5;
real right = 5;

real delta = 0.15;

real lambda0(real x) { return sqrt(tanh(x)^2+delta**2)/2; }
real lambda1(real x) { return -sqrt(tanh(x)^2+delta**2)/2; }

xaxis("$x$",Arrow);
yaxis("$y$",Arrow);

draw(graph(lambda0,left,right,operator ..),blue);
draw(graph(lambda1,left,right,operator ..),blue);

real u = lambda0(2);
pair l1 = (1,u);

real u = lambda1(2);
pair l0 = (1,u);

label("$\lambda_1(x)$",l1+1.5*S);
label("$\lambda_0(x)$",l0+1.5*N);

real gauss(real x) {
real mu = -3.5;
real sigma = 0.09;
real gamma = 0.2;
return lambda0(mu) + gamma * 1.0/sqrt(2.*pi * sigma**2) * exp(-(x-mu)**2/(2.0*sigma**2));
}

draw(graph(gauss,-3.8,-3.2,500,operator --),orange);

real s = lambda0(-3.5) + 0.3;
pair s = (-3.5,s);

draw(s--(s+0.5*E),orange,Arrow,DotMargin);
dot(s,orange);
label("$p$",s+0.25*E+0.3N,orange);

pair s = (-3.5,0);
dot(s, orange);
label("$q$",s+0.25*N,orange);
size(345.0pt,0,keepAspect=true);
viewportsize=(345.0pt,0);

import graph;
size(0,150);

real left = -4;
real right = 4;

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

label("$\lambda_1(x)$",l1+S);
label("$\lambda_0(x)$",l0+N);

real gauss(real x) {
  real mu = -3.5;
  real sigma = 0.05;
  real gamma = 0.025;
  return lambda0(mu) + gamma * 1.0/sqrt(2.*pi * sigma**2) * exp(-(x-mu)**2/(2.0*sigma**2));
}

draw(graph(gauss,-3.65,-3.35,500,operator --),orange);

real s = lambda0(-3.5) + 0.1;
pair s = (-3.5,s);

draw(s--(s+0.25*E),orange,Arrow,DotMargin);
dot(s,orange);
label("$p$",(s+0.3*E));


real gauss2(real x) {
  real mu = 3.5;
  real sigma = 0.05;
  real gamma = 0.015;
  return lambda0(mu) + gamma * 1.0/sqrt(2.*pi * sigma**2) * exp(-(x-mu)**2/(2.0*sigma**2));
}

real gauss3(real x) {
  real mu = 3.5;
  real sigma = 0.05;
  real gamma = 0.010;
  return lambda1(mu) + gamma * 1.0/sqrt(2.*pi * sigma**2) * exp(-(x-mu)**2/(2.0*sigma**2));
}

draw(graph(gauss2,3.35,3.65,500,operator --),orange);
draw(graph(gauss3,3.35,3.65,500,operator --),orange);

real s = lambda0(3.5);
pair s = (3.5,s)+0.2*S;

label("?",s);

real s = lambda1(3.5);
pair s = (3.5,s)+0.2*N;

label("?",s);

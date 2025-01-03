pkg load control;

r = 10; % ohms
l = 500e-3; % H
c = 100e-6; % F
vi = 24; % V

A = [0 -1/l; 1/c, -1/(r*c)];
B = [vi/l; 0];
C = [0 1];
D = 0;

sys = ss(A,B,C,D)
G = tf(sys)

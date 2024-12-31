pkg load control;

% Pole placement methodology for plant stability
clc;

A = [0 1; 2 -1];
B = [1; 0];
C = [1 0];
D = 0;

sys = ss(A,B,C,D);
% unstable pole at 1
E = eig(A)

% move the pole to -1
P = [-1 -2]
K = place(A,B,P)

% calculate new closed loop A matrix (feeback state variables)
Acl = A - B*K;
Ecl = eig(Acl);

% create closed system loop object
sys_cl = ss(Acl,B,C,D);
step(sys_cl);
pause

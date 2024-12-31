pkg load control;


% system parameters
r = 1e3;
l1 = 1e-3;
l2 = 1e-3;
c = 400e-6;

% state space matrices
A = [0 1/l2 0; 1/c 0 1/c; 0 -1/l1 -r/l1]
B = [0; 1/c; 0]
C = [0 1 -r]
D = 0

% build state space model and transfer functions
sys = ss(A, B, C, D)
% note that the system is not stable

% check eigenvalues of A for poles
E = eig(A)

% A has a positive pole, so the system is unstable. Lets adjust the pole using pole placement
P = E;
% modify the unstable pole to be -1
P = [-1.5, -1.5, -10]
K = place(A, B, P);
Acl = A - B*K

% rebuild state space model using Acl
syscl = ss(Acl, B, C, D)

% calculate the gain matrix for the reference Kr in order to make the response 1
Kdc = dcgain(syscl)
Kr = 1/Kdc
syscl_scaled = ss(Acl, B*Kr, C, D)

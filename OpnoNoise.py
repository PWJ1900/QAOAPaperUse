import time

edges = [[3, 7], [8, 5], [4, 6], [4, 0], [6, 5], [6, 9], [2, 5], [2, 0], [1, 5], [0, 9]]
arr = [[0, 2], [2, 5], [5, 1], [5, 6], [6, 4], [6, 9], [5, 8], [3, 7]]
arr2 = []
for i in arr:
    arr2.append([i[0], i[1], 1])
for i in edges:
    if [i[0], i[1]] not in arr and [i[1], i[0]] not in arr:
        arr2.append([i[0], i[1], 0])
print(arr2)

nqubits = 10


from qiskit import QuantumCircuit
from qiskit import Aer

fs = []


def maxcut_obj(x):
    obj = 0
    for i, j, k in arr2:
        if x[i] != x[j]:
            obj -= 1
    return obj


def compute_expectation(counts):
    avg = 0
    sum_count = 0
    for bitstring, count in counts.items():
        obj = maxcut_obj(bitstring)
        avg += obj * count
        sum_count += count
    print(avg)
    fs.append(1)
    print(len(fs))
    return avg / sum_count


def create_qaoa_circ(theta):
    nqubits = 10
    p = len(theta) // 2  # number of alternating unitaries
    qc = QuantumCircuit(nqubits)
    beta = theta[:p]
    gamma = theta[p:]
    # initial_state
    for i in range(0, nqubits):
        qc.h(i)
    for irep in range(0, p):
        # problem unitary
        for pair in list(arr2):
            if pair[2] == 0:
                qc.cx(pair[0], pair[1])
            qc.rz(2 * gamma[irep], qubit=pair[1])
            qc.cx(pair[0], pair[1])
        # mixer unitary
        for i in range(0, nqubits):
            qc.rx(2 * beta[irep], i)
    qc.measure_all()
    return qc


def get_expectation(p, shots=512):
    backend = Aer.get_backend('qasm_simulator')
    backend.shots = shots
    def execute_circ(theta):
        qc = create_qaoa_circ(theta)
        counts = backend.run(qc, seed_simulator=10,
                             nshots=512).result().get_counts()
        return compute_expectation(counts)
    return execute_circ


from scipy.optimize import minimize

expectation = get_expectation(p=1)
print(expectation)

# 来一步步的向期望逼近
res = minimize(expectation,
               [1.0, 1.0],
               method='cobyla')
# method='BFGS')


from qiskit.visualization import plot_histogram

backend = Aer.get_backend('qasm_simulator')
backend.shots = 512
time_start = time.time()
qc_res = create_qaoa_circ(res.x)
qc_res.draw(output='mpl', style={'backgroundcolor': '#ffffff'}, with_layout=False)
time_end = time.time()
print(time_end - time_start)
print(qc_res)
counts = backend.run(qc_res, seed_simulator=10).result().get_counts()

a = 0
print(counts)


# 计算值


def defineSuce(key):
    a = []
    for i in key:
        a.append(i)
    for i in range(len(a)):
        if i < len(a) - 1 and a[i] == a[i + 1]:
            return False
    return True


for i in counts:
    a = counts[i] + a
print(a)
b = 0
for key, value in counts.items():
    if defineSuce(key):
        b += value / 1024
print(b)

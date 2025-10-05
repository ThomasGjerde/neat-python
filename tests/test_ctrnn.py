import neat
from neat.activations import sigmoid_activation


def test_basic():
    # Create a fully-connected network of two neurons with no external inputs.
    node1_inputs = [(1, 0.9), (2, 0.2)]
    node2_inputs = [(1, -0.2), (2, 0.9)]

    node_evals = {1: neat.ctrnn.CTRNNNodeEval(0.01, sigmoid_activation, sum, -2.75 / 5.0, 1.0, node1_inputs),
                  2: neat.ctrnn.CTRNNNodeEval(0.01, sigmoid_activation, sum, -1.75 / 5.0, 1.0, node2_inputs)}

    net = neat.ctrnn.CTRNN([], [1, 2], node_evals)

    init1 = 0.0
    init2 = 0.0

    net.set_node_value(1, init1)
    net.set_node_value(2, init2)

    times = [0.0]
    outputs = [[init1, init2]]
    for i in range(1250):
        output = net.advance([], 0.002, 0.002)
        times.append(net.time_seconds)
        outputs.append(output)

if __name__ == '__main__':
    test_basic()

"""test profiler track and sync `pt.trace.json` files functionality

---
id: 0.profiler
plugin:
  - wandb
var:
  - run0:
      :fn:find:
      - item
      - :wandb:runs
      - :item[config][id]: 0
  - count0:
      :fn:count_regex:
      - item
      - :wandb:runs[0][files]
      - .*pt.trace.json
assert:
  - :wandb:runs_len: 1
  - :wandb:runs[0][config]: { id: profiler_sync_trace_files }
  - :op:contains_regex:
      - :wandb:runs[0][files]
      - .*pt.trace.json
  - :count0: 1
  - :wandb:runs[0][exitcode]: 0
"""

import torch
from torch.nn.functional import log_softmax, max_pool2d, relu
import wandb


def test_profiler():
    """
    This test simulates a typical use-case for PyTorch Profiler: training performance.
    It generates random noise and trains a simple conv net on this noise
    using the torch profiler api.
    Doing so dumps a "pt.trace.json" file in the given logdir.
    This test then ensures that these trace files are sent to the backend.
    """

    def random_batch_generator():
        for i in range(10):
            # create 1-sized batches of 28x28 random noise (simulating images)
            yield i, (torch.randn((1, 1, 28, 28)), torch.randint(0, 10, (1,)))

    class Net(torch.nn.Module):
        def __init__(self):
            super(Net, self).__init__()
            self.conv1 = torch.nn.Conv2d(1, 32, 3, 1)
            self.conv2 = torch.nn.Conv2d(32, 64, 3, 1)
            self.fc1 = torch.nn.Linear(9216, 128)
            self.fc2 = torch.nn.Linear(128, 10)

        def forward(self, x):
            x = relu(self.conv1(x))
            x = relu(self.conv2(x))
            x = max_pool2d(x, 2)
            x = torch.flatten(x, 1)
            x = relu(self.fc1(x))
            x = self.fc2(x)
            output = log_softmax(x, dim=1)
            return output

    model = Net()
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
    model.train()

    def train(data):
        inputs, labels = data[0], data[1]
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    with wandb.init() as run:
        run.config.id = "profiler_sync_trace_files"
        with torch.profiler.profile(
            schedule=torch.profiler.schedule(wait=1, warmup=1, active=3, repeat=1),
            on_trace_ready=wandb.profiler.trace(),
            record_shapes=True,
            with_stack=True,
        ) as prof:
            for step, batch_data in random_batch_generator():
                if step >= (1 + 1 + 3) * 1:
                    break
                train(batch_data)
                prof.step()

    wandb.finish()


test_profiler()
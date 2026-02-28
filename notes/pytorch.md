**Pytorch**

**Tensors**
- A tensor is a multi-dimensional array used in PyTorch that supports GPU acceleration and automatic differentiation.
- It is similar to a NumPy array but integrates with autograd and CUDA.
- Three properties of tensors are: 
    - Shape: Size of each dimension
    - dtype: Datatype of the values in the tensor
    - device: where the tensor lives. Eg CPU or CUDA
- Tensors use CrossEntropyLoss and therefore have floating point inputs and int64(long) labels because internally indexing operations in CrossEntropyLoss require int64 labels

**GPU Basics**
- A GPU accelerates deep learning by parallelizing large matrix computations across thousands of cores.
- Since neural networks rely heavily on matrix multiplications, GPUs are optimised for thses tasks.
- Device Mismatch Error - If the input tensors and the model parameters are on diff sources
- GPUs help when:
    - Models are very large
    - Batch size is large
    - Heavy matrix operations


Dropout is a regularisation technique that is used to reduce overfitting in neural networks

**Autograd**
- Autograd is PyTorch’s automatic differentiation engine that computes gradients for tensors during backpropagation.
- torch.autograd is PyTorch’s automatic differentiation engine that powers neural network training
- What does Pytorch do?
    - Instead of manually deriving derivatives, PyTorch builds a computation graph during forward pass and automatically computes gradients during backward pass.
- How does it work?
    - During forward pass → PyTorch builds a computation graph.
    - When you call loss.backward() → gradients are computed using chain rule.
    - Gradients are stored in .grad attribute of parameters.


**Optimiser**
- An optimizer updates model parameters using computed gradients to minimize the loss function.
- optimizer.step() updates the model params using their stored gradients according to the optimization algo
- It doesn't compute backprop, just updates weights
- The learning rate controls the step size of parameter updates during optimization.
- If the learning rate is too high, then the loss may explode and convergence will be extremely unstable.
- If the learning rate is too low, then the convergence will be very slow 

**Dataset & DataLoader in PyTorch**
- A Dataset defines how to access and preprocess individual data samples.
- DataLoader wraps a Dataset and provides batching, shuffling, and parallel data loading.
- Key Parameters:
    - batch_size: Number of samples per batch
    - shuffle=True: shuffles every epoch
    - num_workers: Number of subprocesses for data loading.
**Mixed Precision**
- Mixed precision training uses both 16-bit and 32-bit floating-point numbers to reduce memory usage and speed up training while maintaining model accuracy.
- How does it speed up memory?
    - Float16 (FP16) uses half the memory of float32
    - GPUs (especially NVIDIA Tensor Cores) are optimized for FP16
    - Less memory → larger batch sizes possible
- Why not use Float16 entirely?
    - Because FP16 has lower precision, small numerical range and  rosk of underflow/overflow
- So we use FP16 for forward pass and FP32 for weight updates



Sources- ChatGPT, Pytorch Documentation(https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html, https://docs.pytorch.org/docs/stable/optim.html, https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html, )